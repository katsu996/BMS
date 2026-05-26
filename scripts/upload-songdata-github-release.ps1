#Requires -Version 5.1
<#
.SYNOPSIS
  Upload songdata.db to a GitHub Release via the REST API.

.DESCRIPTION
  Intended to run from any folder: copy this .ps1, the .bat, and a secrets file
  next to your songdata.db. Tag defaults to songdata-YYYY-MM-DD if omitted.

  Auth (later steps override earlier):
  1) upload-songdata-github-release.secrets.txt (same folder as this script)
  2) upload-songdata-github-release.local.ps1 (dot-sourced; see .example in repo)
  3) env GITHUB_TOKEN / GH_TOKEN and GITHUB_REPOSITORY
  4) -Token / -Repo

.PARAMETER Tag
  Release tag. If empty: songdata-<today yyyy-MM-dd>. Match SONGDATA_RELEASE_TAG in Actions.

.PARAMETER Repo
  owner/repo. Default: env GITHUB_REPOSITORY.

.PARAMETER Token
  PAT override (prefer secrets file or env).

.PARAMETER SongdataPath
  File to upload. Default: songdata.db next to this script, else repo data/songdata.db.

.PARAMETER AssetName
  Asset name on GitHub. Default: songdata.db

.PARAMETER TargetCommitish
  When creating a release for a new remote tag: branch or SHA. If empty, -DefaultBranch is used.

.PARAMETER DefaultBranch
  Used as target_commitish when creating a release if -TargetCommitish is empty. Default: main.
#>
param(
    [Parameter(Mandatory = $false, Position = 0)]
    [string] $Tag = "",

    [Parameter(Mandatory = $false)]
    [string] $Repo = "",

    [Parameter(Mandatory = $false)]
    [string] $Token = "",

    [Parameter(Mandatory = $false)]
    [string] $SongdataPath = "",

    [Parameter(Mandatory = $false)]
    [string] $AssetName = "songdata.db",

    [Parameter(Mandatory = $false)]
    [string] $TargetCommitish = "",

    [Parameter(Mandatory = $false)]
    [string] $DefaultBranch = "main"
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$secretsTxt = Join-Path $PSScriptRoot "upload-songdata-github-release.secrets.txt"
$localCfg = Join-Path $PSScriptRoot "upload-songdata-github-release.local.ps1"

function Import-SecretsTxtFile {
    param([string] $Path)
    if (-not (Test-Path -LiteralPath $Path)) {
        return
    }
    $lines = @(
        Get-Content -LiteralPath $Path -Encoding UTF8 |
        ForEach-Object { $_.Trim() } |
        Where-Object { $_ -and -not $_.StartsWith("#") }
    )
    if ($lines.Count -ge 1) {
        $env:GITHUB_TOKEN = $lines[0]
    }
    if ($lines.Count -ge 2) {
        $env:GITHUB_REPOSITORY = $lines[1]
    }
}

Import-SecretsTxtFile -Path $secretsTxt
if (Test-Path -LiteralPath $localCfg) {
    . $localCfg
}

if (-not $Tag -or $Tag.Trim() -eq "") {
    $Tag = "songdata-" + (Get-Date -Format "yyyy-MM-dd")
}
$Tag = $Tag.Trim()
Write-Host "Release tag: $Tag"

$apiRoot = "https://api.github.com"
$apiVersion = "2022-11-28"

function Get-RepoToken {
    param([string] $CmdLineToken)
    if ($CmdLineToken) {
        return $CmdLineToken
    }
    $t = $env:GITHUB_TOKEN
    if (-not $t) { $t = $env:GH_TOKEN }
    if (-not $t) {
        $msg = @"
Missing token.

Put your PAT in ONE of these (same folder as upload-songdata-github-release.ps1):
  1) $secretsTxt
     Line 1: token (required)
     Line 2: owner/repo (optional if GITHUB_REPOSITORY is already set)
     (Copy from upload-songdata-github-release.secrets.txt.example in the repo.)
  2) $localCfg
     (Copy from upload-songdata-github-release.local.ps1.example in the repo.)

Or set environment variable GITHUB_TOKEN / GH_TOKEN before running.
"@
        throw $msg.Trim()
    }
    return $t
}

function Get-ApiHeaders {
    param([string] $Token)
    return @{
        Authorization          = "Bearer $Token"
        Accept                 = "application/vnd.github+json"
        "X-GitHub-Api-Version" = $apiVersion
    }
}

function Get-UploadHeaders {
    param([string] $Token)
    return @{
        Authorization          = "Bearer $Token"
        Accept                 = "application/vnd.github+json"
        "X-GitHub-Api-Version" = $apiVersion
        "Content-Type"         = "application/octet-stream"
    }
}

function Invoke-GitHubGet {
    param(
        [string] $Uri,
        [hashtable] $Headers
    )
    return Invoke-RestMethod -Uri $Uri -Headers $Headers -Method Get
}

function Invoke-GitHubPostJson {
    param(
        [string] $Uri,
        [hashtable] $Headers,
        [hashtable] $Body
    )
    $json = $Body | ConvertTo-Json -Compress
    return Invoke-RestMethod -Uri $Uri -Headers $Headers -Method Post -Body $json -ContentType "application/json; charset=utf-8"
}

function Invoke-GitHubDelete {
    param(
        [string] $Uri,
        [hashtable] $Headers
    )
    Invoke-RestMethod -Uri $Uri -Headers $Headers -Method Delete | Out-Null
}

function Get-ReleaseByTag {
    param(
        [string] $Owner,
        [string] $Name,
        [string] $TagName,
        [hashtable] $Headers
    )
    $enc = [uri]::EscapeDataString($TagName)
    $uri = "$apiRoot/repos/$Owner/$Name/releases/tags/$enc"
    try {
        return Invoke-GitHubGet -Uri $uri -Headers $Headers
    }
    catch {
        $resp = $_.Exception.Response
        if ($null -ne $resp -and [int]$resp.StatusCode -eq 404) {
            return $null
        }
        throw
    }
}

function New-GitHubRelease {
    param(
        [string] $Owner,
        [string] $Name,
        [string] $TagName,
        [string] $Title,
        [string] $BodyText,
        [string] $Commitish,
        [hashtable] $Headers
    )
    $uri = "$apiRoot/repos/$Owner/$Name/releases"
    $payload = @{
        tag_name   = $TagName
        name       = $Title
        body       = $BodyText
        draft      = $false
        prerelease = $false
    }
    if ($Commitish) {
        $payload["target_commitish"] = $Commitish
    }
    return Invoke-GitHubPostJson -Uri $uri -Headers $Headers -Body $payload
}

function Get-ReleaseAssets {
    param(
        [string] $Owner,
        [string] $Name,
        [int] $ReleaseId,
        [hashtable] $Headers
    )
    $uri = "$apiRoot/repos/$Owner/$Name/releases/$ReleaseId/assets?per_page=100"
    $result = Invoke-GitHubGet -Uri $uri -Headers $Headers
    if ($null -eq $result) {
        return @()
    }
    if ($result -is [System.Array]) {
        return $result
    }
    return @($result)
}

function Remove-ReleaseAsset {
    param(
        [string] $Owner,
        [string] $Name,
        [int] $AssetId,
        [hashtable] $Headers
    )
    $uri = "$apiRoot/repos/$Owner/$Name/releases/assets/$AssetId"
    Invoke-GitHubDelete -Uri $uri -Headers $Headers
}

function Expand-UploadUri {
    param([string] $UploadUrlTemplate, [string] $Name)
    # Single-quoted pattern: in double quotes `$` breaks -replace on Windows PowerShell 5.1
    $base = $UploadUrlTemplate -replace '\{\?name,label\}$', ''
    return ($base + "?name=" + [uri]::EscapeDataString($Name))
}

function Send-ReleaseAsset {
    param(
        [string] $UploadUri,
        [string] $FilePath,
        [string] $Token
    )
    $uh = Get-UploadHeaders -Token $Token
    Invoke-RestMethod -Uri $UploadUri -Headers $uh -Method Post -InFile $FilePath | Out-Null
}

# --- main ---
$token = Get-RepoToken -CmdLineToken $Token
$headers = Get-ApiHeaders -Token $token

if (-not $Repo -or $Repo.Trim() -eq "") {
    $Repo = $env:GITHUB_REPOSITORY
}
if (-not $Repo -or $Repo.Trim() -eq "") {
    $msg = @"
Missing repository (owner/name).

Set line 2 in:
  $secretsTxt
or set in:
  $localCfg
or set environment variable GITHUB_REPOSITORY, or pass -Repo owner/name.
"@
    throw $msg.Trim()
}
$parts = $Repo.Trim().Split("/")
if ($parts.Length -ne 2 -or -not $parts[0] -or -not $parts[1]) {
    throw "Repo must be owner/name: $Repo"
}
$owner = $parts[0]
$name = $parts[1]

if (-not $SongdataPath) {
    $nextToScript = Join-Path $PSScriptRoot $AssetName
    if (Test-Path -LiteralPath $nextToScript -PathType Leaf) {
        $SongdataPath = $nextToScript
    }
    else {
        $repoRoot = Split-Path $PSScriptRoot -Parent
        $SongdataPath = Join-Path (Join-Path $repoRoot "data") $AssetName
    }
}

if (-not (Test-Path -LiteralPath $SongdataPath -PathType Leaf)) {
    throw "File not found: $SongdataPath (copy songdata.db next to the script, use -SongdataPath, or keep repo layout data/$AssetName)"
}

$release = Get-ReleaseByTag -Owner $owner -Name $name -TagName $Tag -Headers $headers
if ($null -eq $release) {
    Write-Host "No release for tag; creating: tag=$Tag"
    $title = "$AssetName ($Tag)"
    $notes = "Uploaded via upload-songdata-github-release.ps1"
    $commitish = $TargetCommitish
    if (-not $commitish) {
        $commitish = $DefaultBranch
    }
    $release = New-GitHubRelease -Owner $owner -Name $name -TagName $Tag -Title $title -BodyText $notes -Commitish $commitish -Headers $headers
}

$rid = [int]$release.id
$uploadTpl = [string]$release.upload_url
if (-not $uploadTpl) {
    throw "API response missing upload_url."
}

$assets = Get-ReleaseAssets -Owner $owner -Name $name -ReleaseId $rid -Headers $headers
foreach ($a in $assets) {
    if ($a.name -eq $AssetName) {
        Write-Host "Deleting existing asset: $AssetName (id=$($a.id))"
        Remove-ReleaseAsset -Owner $owner -Name $name -AssetId ([int]$a.id) -Headers $headers
    }
}

$uploadUri = Expand-UploadUri -UploadUrlTemplate $uploadTpl -Name $AssetName
Write-Host "Uploading: $SongdataPath -> $AssetName (release_id=$rid)"
Send-ReleaseAsset -UploadUri $uploadUri -FilePath $SongdataPath -Token $token

$dl = "https://github.com/$owner/$name/releases/download/$Tag/$AssetName"
Write-Host "Done. Public download URL example: $dl"
Write-Host "If Actions uses this file, set repository variable SONGDATA_RELEASE_TAG to: $Tag"

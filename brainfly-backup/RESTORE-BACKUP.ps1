$ErrorActionPreference = 'Stop'
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$out = Join-Path $here 'BrainFly-0241-SOURCE-LIGHT.zip'
$parts = Get-ChildItem $here -Filter 'BrainFly-0241-SOURCE-LIGHT.zip.b64.part*' | Sort-Object Name
if (-not $parts) { throw 'No backup parts found' }
$b64 = ($parts | ForEach-Object { Get-Content $_.FullName -Raw }) -join ''
[IO.File]::WriteAllBytes($out, [Convert]::FromBase64String($b64))
$sha=(Get-FileHash $out -Algorithm SHA256).Hash.ToLower()
Write-Host "restored: $out"
Write-Host "sha256:   $sha"
if ($sha -ne 'dc8ed23b1265273f29b83f9a585d09a7d6be40c4f590049db76d9422c580a5cf') { throw 'SHA256 mismatch' }

# Rebuild the print edition inside the pinned container (Windows, Docker Desktop). Run from anywhere.
$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
docker build -q -f "$Root\build\Dockerfile" -t mow-build "$Root"
docker run --rm -v "${Root}:/work" mow-build @args
$h = Join-Path $Root "final\The_Measure_of_the_Wound.pdf.sha256"; if (-not (Test-Path $h)) { $h = Join-Path $Root "The_Measure_of_the_Wound.pdf.sha256" }; Get-Content $h

$ErrorActionPreference = "Stop"

$runDirectory = Split-Path -Parent $MyInvocation.MyCommand.Path
Push-Location $runDirectory
try {
    python code\analyze_identifiability.py
    if ($LASTEXITCODE -ne 0) {
        throw "Analysis failed with exit code $LASTEXITCODE"
    }

    python -m pytest -q tests -p no:cacheprovider
    if ($LASTEXITCODE -ne 0) {
        throw "Tests failed with exit code $LASTEXITCODE"
    }
} finally {
    Pop-Location
}

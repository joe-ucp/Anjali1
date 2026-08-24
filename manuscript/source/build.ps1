$ErrorActionPreference = "Stop"

$sourceDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$runRoot = Resolve-Path (Join-Path $sourceDir "..\..")
$buildDir = Join-Path $runRoot "working\build"
$renderedDir = Join-Path $runRoot "manuscript\rendered"

New-Item -ItemType Directory -Force $buildDir | Out-Null
New-Item -ItemType Directory -Force $renderedDir | Out-Null

Push-Location $sourceDir
try {
    $outputDirectoryArgument = "-output-directory=$buildDir"
    pdflatex -interaction=nonstopmode -halt-on-error $outputDirectoryArgument manuscript.tex
    bibtex (Join-Path $buildDir "manuscript")
    pdflatex -interaction=nonstopmode -halt-on-error $outputDirectoryArgument manuscript.tex
    pdflatex -interaction=nonstopmode -halt-on-error $outputDirectoryArgument manuscript.tex
} finally {
    Pop-Location
}

$output = Join-Path $renderedDir "Bulk_Tissue_Nitrite_Source_Contributions_2026.pdf"
Copy-Item -LiteralPath (Join-Path $buildDir "manuscript.pdf") -Destination $output -Force
Write-Output $output

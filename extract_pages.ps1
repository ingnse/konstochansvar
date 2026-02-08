# PowerShell script to extract all pages from konstochansvar.se

$baseUrl = "https://konstochansvar.se"
$pagesDir = "pages"
$outputDir = "extracted_pages"

# Create output directory
New-Item -ItemType Directory -Force -Path $outputDir | Out-Null

# List of pages to extract
$pages = @(
    "pressrum",
    "organigram", 
    "vanligafragor",
    "kontakt",
    "roundaboutart",
    "ebf",
    "kidsclub",
    "laromedel",
    "statskyrkomuseum",
    "jagarlikgiltig",
    "engagemang",
    "lblistan"
)

Write-Host "Extracting pages from konstochansvar.se..." -ForegroundColor Green
Write-Host ""

foreach ($page in $pages) {
    $url = "$baseUrl/$page.html"
    $outputFile = "$outputDir\$page.html"
    
    try {
        Write-Host "Downloading: $page.html..." -ForegroundColor Yellow
        Invoke-WebRequest -Uri $url -OutFile $outputFile -UseBasicParsing -ErrorAction Stop
        Write-Host "  OK - Saved to: $outputFile" -ForegroundColor Green
    }
    catch {
        Write-Host "  FAILED - Could not download: $url" -ForegroundColor Red
        Write-Host "    Error: $($_.Exception.Message)" -ForegroundColor Red
    }
}

Write-Host ""
Write-Host "Extraction complete! Files saved to: $outputDir" -ForegroundColor Green


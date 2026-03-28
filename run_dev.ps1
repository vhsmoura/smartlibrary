<#
Run development server (PowerShell).
Usage: ./run_dev.ps1
This will prefer the virtualenv at .venv if present, set DEBUG=True and a fallback SECRET_KEY,
run migrations and start the Django development server.
#>
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$venvPy = Join-Path $ScriptDir ".venv\Scripts\python.exe"

# Set safe defaults for development
$env:DEBUG = 'True'
if (-not $env:SECRET_KEY) { $env:SECRET_KEY = 'dev-secret-key' }

Write-Host "Starting development server (DEBUG=$env:DEBUG)"

if (Test-Path $venvPy) {
    & $venvPy manage.py migrate
    & $venvPy manage.py runserver
} else {
    python manage.py migrate
    python manage.py runserver
}

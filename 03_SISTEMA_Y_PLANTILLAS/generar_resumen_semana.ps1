# Genera 03_SISTEMA_Y_PLANTILLAS/guiones_bundle.js con SOLO la semana en curso + vista previa de la siguiente
$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $PSScriptRoot
$dataPath = Join-Path $PSScriptRoot 'diario_data.json'
$data = Get-Content -Path $dataPath -Raw -Encoding UTF8 | ConvertFrom-Json

$semActual = [string]$data.semana_actual
$semPad = $semActual.PadLeft(2, '0')
$semFolder = Get-ChildItem -Path (Join-Path $root '02_CLASES_SEMANALES\PARCIAL_2') -Directory -Filter "SEMANA_${semPad}*" | Select-Object -First 1

$niveles = @{
  '8VO_EGB'  = '8VO EGB'
  '9NO_EGB'  = '9NO EGB'
  '10MO_EGB' = '10MO EGB'
  '1RO_BGU'  = '1RO BGU'
  '2DO_BGU'  = '2DO BGU'
  '3RO_BGU'  = '3RO BGU'
}

$guiones = @{}
if ($semFolder) {
  foreach ($nf in $niveles.Keys) {
    $file = Join-Path $semFolder.FullName "${nf}_SEMANA${semPad}.md"
    if (Test-Path $file) {
      $guiones[$niveles[$nf]] = Get-Content -Path $file -Raw -Encoding UTF8
    }
  }
}

$semSiguiente = [string]([int]$semActual + 1)
$payload = @{
  semana_actual    = $semActual
  semana_info      = $data.semanas.$semActual
  semana_siguiente = $data.semanas.$semSiguiente
  horario          = $data.horario
  registros_s3     = $data.semanas.'3'.registros
  guiones          = $guiones
}

$json = $payload | ConvertTo-Json -Depth 6 -Compress
$outPath = Join-Path $PSScriptRoot 'guiones_bundle.js'
[System.IO.File]::WriteAllText($outPath, "window.RESUMEN_DATA = $json;", [System.Text.UTF8Encoding]::new($false))
Write-Host "RESUMEN_DATA actualizado: Semana $semActual ($($guiones.Count) guiones)"

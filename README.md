### Descargar y convertir
```bash
python run_update.py
```

#### Configuración

```yml
paths:
  output: ./output # Destino del .dat
  data: ../foo     # Localización del .zip 

names:
  zip: GeoLite2-City-CSV.zip # Nombre con el que guardar el .zip descargado
  dat: GeoLiteCity.dat       # Nombre con el que guardar el .dat (convertido)

on_start:
  download_zip: true    # Ejecutar la descarga del zip 
                        # (si es true, se ejecuta antes de convertir)

  convert_to_dat: true  # Ejecutar la conversión de formato 
                        # (si es true, se ejecuta después de descargar)

max_mind:
  license-key: XXXXXYYYYZZZZ
  edition: GeoLite2-City-CSV
```
import subprocess
from sys import stderr, stdout
from pathlib import Path
from os import rename, getcwd, path


START_DOWNLOAD = False
START_CONVERT = True

CURRENT_DIR = Path(getcwd())

ZIP_NAME = 'GeoLite2-City-CSV.zip'


# Relative (to current dir) paths to 
DOWNLOAD_DIRNAME = './data'
OUTPUT_DIRNAME = './output'

DOWNLOAD_ABSPATH = CURRENT_DIR.joinpath(DOWNLOAD_DIRNAME)
OUTPUT_ABSPATH = CURRENT_DIR.joinpath(OUTPUT_DIRNAME)

if START_DOWNLOAD:
    # Download .zip
    download_output = subprocess.run(['composer', 'update', 'tronovav/geoip2-update'],
                                     capture_output=True,
                                     shell=True,
                                     cwd='./geoip2-update')
    print(download_output)
    # TODO: Rename .zip to GeoLite2-City-CSV.zip


# Convert format
if START_CONVERT:
    # python geolite2legacy.py -i GeoLite2-City-CSV.zip -o GeoLiteCity.dat -f geoname2fips.csv
    downloaded_zip_asbpath = CURRENT_DIR.joinpath(ZIP_NAME)
    print(downloaded_zip_asbpath)
    update_output = subprocess.run(['python', 'geolite2legacy.py',
                                    '-i', '../data/GeoLite2-City-CSV.zip',
                                    '-o', '../output/GeoLiteCity.dat',
                                    '-f', 'geoname2fips.csv'],
                                   cwd='./geolite2legacy')
    print(update_output)




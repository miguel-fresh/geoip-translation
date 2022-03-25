import subprocess
from sys import stderr, stdout
from pathlib import Path
from os import rename, getcwd, path


START_DOWNLOAD = False
START_CONVERT = False

CURRENT_DIR = getcwd()
DOWNLOAD_DIRNAME = './data'
DOWNLOAD_ABSPATH = path.join(CURRENT_DIR, DOWNLOAD_DIRNAME)
print(DOWNLOAD_ABSPATH)


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
    update_output = subprocess.run(['python', 'geolite2legacy.py',
                                    '-i', '../data/GeoLite2-City-CSV.zip',
                                    '-o', '../output/GeoLiteCity.dat',
                                    '-f', 'geoname2fips.csv'],
                                   cwd='./geolite2legacy')
    print(update_output)


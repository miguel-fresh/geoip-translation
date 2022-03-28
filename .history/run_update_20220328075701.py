from asyncio.subprocess import STDOUT
from fileinput import filename
from genericpath import exists
import subprocess
from pathlib import Path
from os import remove, rename, path
import yaml


def removeFileIfExists(file_path):
    if path.exists(file_path):
        remove(file_path)


# LEGACY
ZIP_LEGACY_NAME = 'GeoLite2-City-CSV.zip'

# Default values
ONSTART_DOWNLOAD = False
ONSTART_CONVERT = False

CURRENT_DIR = Path(__file__).parent.resolve()
CONFIG_FILENAME = 'config.yml'
CONFIG_ABSPATH = CURRENT_DIR.joinpath(CONFIG_FILENAME)

ZIP_NAME = 'GeoLite2-City-CSV.zip'
DAT_NAME = 'GeoLiteCity.dat'

DOWNLOAD_DIRNAME = './data'
OUTPUT_DIRNAME = './output'

LICENSE_KEY = ''
DB_EDITION = ''


# Get config from config.yml file
try:
    with open(CONFIG_ABSPATH) as cfg_file:

        documents = yaml.full_load(cfg_file)
        paths = documents['paths']
        names = documents['names']
        on_start = documents['on_start']
        max_mind = documents['max_mind']
        
        OUTPUT_DIRNAME = paths['output']
        DOWNLOAD_DIRNAME = paths['data']

        ZIP_NAME = names['zip']
        DAT_NAME = names['dat']

        ONSTART_DOWNLOAD = on_start['download_zip']
        ONSTART_CONVERT = on_start['convert_to_dat']

        LICENSE_KEY = max_mind['license-key']
        DB_EDITION = max_mind['edition']
except:
    print('No config.yml file found, using default values...')

# Setting paths
DOWNLOAD_ABSPATH = CURRENT_DIR.joinpath(DOWNLOAD_DIRNAME)
OUTPUT_ABSPATH = CURRENT_DIR.joinpath(OUTPUT_DIRNAME)

ZIP_ABSPATH = DOWNLOAD_ABSPATH.joinpath(ZIP_LEGACY_NAME)
DAT_ABSPATH = OUTPUT_ABSPATH.joinpath(DAT_NAME)





if ONSTART_DOWNLOAD:
    removeFileIfExists(ZIP_ABSPATH)

    print(f'Downloading {ZIP_LEGACY_NAME}...')
    # Download .zip
    download_output = subprocess.run(['php', 'download.php', 
        '--license-key', LICENSE_KEY,
        '--output-path', DOWNLOAD_ABSPATH,
        '--edition', DB_EDITION],
        cwd=CURRENT_DIR.joinpath('./geoip2-update'), stderr=STDOUT)

    # Rename zip if necessary
    if (ZIP_LEGACY_NAME != ZIP_NAME):
        rename(ZIP_ABSPATH, DOWNLOAD_ABSPATH.joinpath(ZIP_NAME))

# Convert format
if ONSTART_CONVERT:
    # python geolite2legacy.py -i GeoLite2-City-CSV.zip -o GeoLiteCity.dat -f geoname2fips.csv
    downloaded_zip_asbpath = CURRENT_DIR.joinpath(ZIP_LEGACY_NAME)
    print(downloaded_zip_asbpath)
    update_output = subprocess.run(['python', 'geolite2legacy.py',
                                    '-i', ZIP_ABSPATH,
                                    '-o', DAT_ABSPATH,
                                    '-f', 'geoname2fips.csv'],
                                   cwd='./geolite2legacy')

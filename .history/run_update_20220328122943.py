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


def checkExistence(path_to_check):
    if not path.exists(path_to_check):
        raise(Exception(f"No existe la ruta \'{path_to_check}\'"))
    return True

def good_msg(msg):
    return f"+ {msg}"

def bad_msg(msg):
    return f"- {msg}"

def neutral_msg(msg):
    return f"~ {msg}"


# LEGACY
ZIP_LEGACY_NAME = 'GeoLite2-City-CSV.zip'

# Default values
ONSTART_DOWNLOAD = False
ONSTART_CONVERT = True

CURRENT_DIR = Path(__file__).parent.resolve()
CONFIG_FILENAME = 'config.yml'
CONFIG_ABSPATH = CURRENT_DIR.joinpath(CONFIG_FILENAME)

ZIP_NAME = 'GeoLite2-City-CSV.zip'
DAT_NAME = 'GeoLiteCity.dat'

DOWNLOAD_DIRNAME = './data'
OUTPUT_DIRNAME = './output'

LICENSE_KEY = ''
DB_EDITION = 'GeoLite2-City-CSV'


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

        if ('license-key' in max_mind):
            LICENSE_KEY = max_mind['license-key']
            print(bad_msg('No se ha especificado una license-key para MaxMind :('))
        else:
            pass
        DB_EDITION = max_mind['edition'] if 'edition' in max_mind else DB_EDITION 
except:
    print(neutral_msg('No se encontró un archivo config.yml válido, usando valores por defecto...'))

if (not ONSTART_CONVERT and not ONSTART_DOWNLOAD):
    print(good_msg("No se especificó ninguna acción (download_zip, convert_to_dat). Saliendo..."))
    exit(0)

# Setting paths
DOWNLOAD_ABSPATH = CURRENT_DIR.joinpath(DOWNLOAD_DIRNAME)
OUTPUT_ABSPATH = CURRENT_DIR.joinpath(OUTPUT_DIRNAME)

ZIP_ABSPATH = DOWNLOAD_ABSPATH.joinpath(ZIP_LEGACY_NAME)
DAT_ABSPATH = OUTPUT_ABSPATH.joinpath(DAT_NAME)


# Download .zip 
if ONSTART_DOWNLOAD:
    # Check if download folder exists
    checkExistence(DOWNLOAD_ABSPATH)

    # Remove previous .zip file if exists
    removeFileIfExists(ZIP_ABSPATH)

    print(good_msg(f'Descargando {ZIP_LEGACY_NAME}...'))
    # Download .zip
    download_output = subprocess.run(['php', 'download.php',
                                      '--license-key', LICENSE_KEY,
                                      '--output-path', DOWNLOAD_ABSPATH,
                                      '--edition', DB_EDITION],
                                     cwd=CURRENT_DIR.joinpath('./geoip2-update'), stderr=STDOUT)

    # Rename .zip if necessary
    if (ZIP_LEGACY_NAME != ZIP_NAME):
        rename(ZIP_ABSPATH, DOWNLOAD_ABSPATH.joinpath(ZIP_NAME))

    # Check if download was successful
    if (download_output.returncode != 0):
        raise(Exception(bad_msg('Error en la descarga :(')))

    checkExistence(ZIP_ABSPATH)
    print(good_msg(f'Descarga exitosa :) -> {ZIP_ABSPATH}'))


# Convert format
if ONSTART_CONVERT:
    # Check if .zip exists
    checkExistence(ZIP_ABSPATH)

    # Check if output folder exists
    checkExistence(OUTPUT_ABSPATH)

    # python geolite2legacy.py -i GeoLite2-City-CSV.zip -o GeoLiteCity.dat -f geoname2fips.csv
    update_output = subprocess.run(['python', 'geolite2legacy.py',
                                    '-i', ZIP_ABSPATH,
                                    '-o', DAT_ABSPATH,
                                    '-f', 'geoname2fips.csv'],
                                   cwd='./geolite2legacy')

    # Check convertion was successful
    if update_output.returncode != 0:
        raise(Exception(bad_msg('Error en la conversión de formato :(')))
    print(good_msg(f'Conversión existosa :) -> {DAT_ABSPATH}'))


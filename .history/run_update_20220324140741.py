import subprocess
from sys import stderr, stdout
from pathlib import Path
from os import rename, getcwd

# download_process = subprocess.Popen(['echo', '"hello"'],
# return_code = subprocess.call(['composer', '--version'],
#                                     stdout=subprocess.PIPE,
#                                     stderr=subprocess.PIPE,
#                                     shell=True,
#                                     universal_newlines=True)
# print('Errors: ', stderr)
# print('Output: ', stdout)

CURRENT_DIR = os.getcwd()
DOWNLOAD_DIR = Path.joinpath()


# Download .zip
download_output = subprocess.run(['composer', 'update', 'tronovav/geoip2-update'],
                                 capture_output=True,
                                 shell=True,
                                 cwd='./geoip2-update')
print(download_output)

# Rename .zip to GeoLite2-City-CSV.zip
rename()

# Convert format



# python geolite2legacy.py -i GeoLite2-City-CSV.zip -o GeoLiteCity.dat -f geoname2fips.csv

update_output = subprocess.run(['python', 'geolite2legacy.py',
                                '-i', '../data/GeoLite2-City-CSV.zip',
                                '-o', '../output/GeoLiteCity.dat',
                                '-f', 'geoname2fips.csv'],
                                cwd='./geolite2legacy')

print(download_output)
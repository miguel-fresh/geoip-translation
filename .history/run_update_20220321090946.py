import subprocess
from sys import stdout

# download_process = subprocess.Popen(['echo', '"hello"'],
return_code = subprocess.call(['composer', 'update', 'tronovav/geoip2-update'],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE, shell=True)
print(stdout)                                    
print(return_code)

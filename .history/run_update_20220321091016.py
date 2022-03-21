import subprocess
from sys import stderr, stdout

# download_process = subprocess.Popen(['echo', '"hello"'],
return_code = subprocess.call(['composer', 'update', 'tronovav/geoip2-update'],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE,)
print(stdout, stderr)                                    
print(return_code)

import subprocess
from sys import stderr, stdout

# download_process = subprocess.Popen(['echo', '"hello"'],
return_code = subprocess.call(['composer', '--version'],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE,
                                    shell=True)
print(stdout, stderr)                                    
print(return_code)

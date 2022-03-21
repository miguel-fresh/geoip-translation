import subprocess
from sys import stderr, stdout

# download_process = subprocess.Popen(['echo', '"hello"'],
return_code = subprocess.Popen(['composer', '--version'],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE,
                                    shell=True,
                                    universal_newlines=True)
print('Errors: ', stderr)
print('Output: ', stdout)
print(return_code)

import subprocess
from sys import stderr, stdout

# download_process = subprocess.Popen(['echo', '"hello"'],
download_output = subprocess.run(['composer', '--version'], capture_output=True)
# return_code = subprocess.call(['composer', '--version'],
#                                     stdout=subprocess.PIPE,
#                                     stderr=subprocess.PIPE,
#                                     shell=True,
#                                     universal_newlines=True)
print('Errors: ', stderr)
print('Output: ', stdout)
print(return_code)

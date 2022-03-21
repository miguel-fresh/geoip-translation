import subprocess
from sys import stderr, stdout

# download_process = subprocess.Popen(['echo', '"hello"'],
# return_code = subprocess.call(['composer', '--version'],
#                                     stdout=subprocess.PIPE,
#                                     stderr=subprocess.PIPE,
#                                     shell=True,
#                                     universal_newlines=True)
# print('Errors: ', stderr)
# print('Output: ', stdout)

download_output = subprocess.run(['composer', '--version'],
                                 capture_output=True,
                                 shell=True)

print(download_output)

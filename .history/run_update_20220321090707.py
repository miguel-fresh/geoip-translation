import subprocess

download_process = subprocess.call(['composer', '--version'],
# download_process = subprocess.Popen(['echo', '"hello"'],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE),
                                  

stdout, stderr = download_process.communicate()
print(stdout, stderr)
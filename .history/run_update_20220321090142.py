import subprocess

# download_process = subprocess.Popen(['composer', 'update', 'tronovav/geoip2-update'],
download_process = subprocess.Popen(['echo', '"hello"'],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE)

stdout, stderr = download_process.communicate()
print(stdout, stderr)
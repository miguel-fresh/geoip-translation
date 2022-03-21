import subprocess

# download_process = subprocess.Popen(['composer', 'update', 'tronovav/geoip2-update'],
download_process = subprocess.Popen(['eco', 'hello'],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE)

stdout, stderr = download_process.communicate()
stdout, stderr
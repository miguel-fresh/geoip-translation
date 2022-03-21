import subprocess

download_process = subprocess.Popen(['composer', 'update', 'tronovav/geoip2-update'],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE)

stdut, stderr = download_process.communicate()
import subprocess

return_code = subprocess.call(['composer', '--version'],
# download_process = subprocess.Popen(['echo', '"hello"'],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE),
                                  


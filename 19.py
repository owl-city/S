import time
import subprocess

while True:
  subprocess.call(['sh', 'ss9.sh'])
  time.sleep(250)
  subprocess.call(['nohup', 'python3', '20.py'])
  subprocess.call(['nohup', 'python3', '17.py'])
  break
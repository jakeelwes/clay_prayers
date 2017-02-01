import subprocess, signal
import os

subprocess.call('python clay_local.py', shell=True)
subprocess.Popen('processing-java --sketch=clay --run', shell=True)

while True:
        try:
                subprocess.call('python clay_pi.py', shell=True)
        except ValueError:
                print "Nothing to worry"

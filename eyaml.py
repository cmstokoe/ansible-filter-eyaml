import os
import subprocess
import sys

def eyaml(arg):
    FNULL = open(os.devnull, 'w')
    cmd="eyaml decrypt -s \"" + arg + "\""
    output = subprocess.check_output(cmd, stderr=FNULL, shell=True)
    return output.rstrip();

class FilterModule(object):
     def filters(self):
         return {'eyaml': eyaml}

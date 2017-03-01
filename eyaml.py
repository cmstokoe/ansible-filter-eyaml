# usage
## The in-line encrypted variable can be referenced and automaticly de-crypted within your ansible plays/roles using the following Jinja2 instantiation {{ secret_variable | eyaml }}.
import os
import subprocess
import sys
import yaml

def eyaml(arg):
  path_to_script = os.path.dirname(os.path.realpath(__file__))
  with open(path_to_script + "/eyaml.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

    eyaml_private_key=cfg['eyaml_private_key']
    eyaml_public_key=cfg['eyaml_public_key']

  FNULL = open(os.devnull, 'w')
  cmd="eyaml decrypt --pkcs7-private-key=" + eyaml_private_key + " --pkcs7-public-key=" + eyaml_public_key + " -s \"" + arg + "\""
  output = subprocess.check_output(cmd, stderr=FNULL, shell=True)
  return output.rstrip();

class FilterModule(object):
   def filters(self):
       return {'eyaml': eyaml}

import json
import os
import re
import sys

env_file = sys.argv[1]
environment = "{}_".format(sys.argv[2])
secrets = json.loads(sys.argv[3])
for key, value in secrets.items():
    if not key.startswith(environment):
        continue

    if re.match(r'^[A-Z_]+=', value):
        print(f"Setting {key} ...")
        os.system(f"echo '{value}' >> {env_file}")

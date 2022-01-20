import json
import os
import re

env_file = ""

path = str(os.environ.get("GITHUB_WORKSPACE", "."))
env_file_name = str(os.environ.get("INPUT_FILE_NAME", ".env"))
environment = str(os.environ.get("INPUT_ENVIRONMENT", "STAGING"))
secrets = json.loads(str(os.environ.get("INPUT_SECRETS", "[]")))

for key, value in secrets.items():
    print(f"Setting {key} ...", end=' ')

    if not key.startswith("{}_".format(environment)):
        print(':o:')
        continue

    if re.match(r'^[A-Z_]+=', value):
        env_file += value + "\n"
        print(':heavy_check_mark:')
    else:
        print(':x:')

with open(os.path.join(path, env_file_name), "w") as text_file:
    text_file.write(env_file)

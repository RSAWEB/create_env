import json
import os
import re

env_file = ""

path = str(os.environ.get("GITHUB_WORKSPACE", "."))
env_file_name = str(os.environ.get("INPUT_FILE_NAME", ".env"))
environment = str(os.environ.get("INPUT_ENVIRONMENT", "STAGING"))
secrets = json.loads(str(os.environ.get("INPUT_SECRETS", "[]")))

for key, value in sorted(secrets.items()):
    print(f"Setting {key} ...", end=' ')

    if not key.startswith("{}_".format(environment)):
        print("\U00002b55")
        continue

    if re.match(r'^[A-Z_]+=', value):
        env_file += value + "\n"
        print("\U00002714")
    else:
        print("\U0000274c")

if not re.findall('^DEBUG=', env_file, re.MULTILINE):
    if environment == "PROD":
        env_file += "DEBUG=False"
    else:
        env_file += "DEBUG=True"

with open(os.path.join(path, env_file_name), "w") as text_file:
    text_file.write(env_file)

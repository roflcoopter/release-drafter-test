import json
import re

f = open("response.json")
releases = json.load(f)
f.close()

draft = releases[0]
latest_release = releases[1]

next_beta = 1

if latest_release["prerelease"]:
    print("Latest release is a beta")
    match = re.search(r"b(\d+)", latest_release["tag_name"])
    if match:
        next_beta = int(match.group(1)) + 1

print(f"Next beta number is {next_beta}")

tag_name = f"{draft['tag_name']}b{next_beta}"
print("::set-env name=RELEASE_ID::{}".format(draft["id"]))

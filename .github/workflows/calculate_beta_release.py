import json
import re
import os
import sys

f = open("response.json")
releases = json.load(f)
f.close()

draft = releases[0]
if not draft["draft"]:
    print("No draft found!")
    sys.exit(255)

latest_release = releases[1]

next_beta = 1

if latest_release["prerelease"]:
    print("Latest release is a beta")
    match = re.search(r"b(\d+)", latest_release["tag_name"])
    if match:
        print("Found match!")
        print(match.group(0))

        tag_search = re.match("(.*?)b", latest_release["tag_name"])
        if tag_search:
            print(tag_search.group(1))
            if tag_search.group(1) == draft["tag_name"]:
                print("Same version, incrementing beta number")
                next_beta = int(match.group(1)) + 1

print(f"Next beta number is {next_beta}")

tag_name = f"{draft['tag_name']}b{next_beta}"

print(f"New tag name: {tag_name}")

with open(str(os.getenv("GITHUB_ENV")), "a") as f:
    f.write(f'VISERON_RELEASE_ID={draft["id"]}\n')
    f.write(f"VISERON_TAG_NAME={tag_name}\n")

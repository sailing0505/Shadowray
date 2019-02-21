import os
from config.v2_repo import RELEASE_API
from config.version import *
from common.utils import parse_yes_or_no
from common.utils import download_file
import requests
import json
import platform

print("Shadowray:")
print("version: ", VERSION_ID)

s = None
while s is None:
    t = input("Do you want to download the v2ray-core automatically?(Y/N)\n")
    s = parse_yes_or_no(t)

if os.path.exists("v2ray") is False:
    os.mkdir("v2ray")

if s:
    r = json.loads(requests.get(RELEASE_API).text)
    print("Latest publish date of v2ray-core: " +r['published_at'])
    print("Latest version of v2ray-core: " + r['tag_name'])

    os = str(platform.system())
    arch = str(platform.architecture()[0])
    print("Platform: " + os + " " + arch)

    assets = r['assets']

    download_url = None
    for asset in assets:
        name = str(asset['name'])

        if name.endswith("zip") and name.find(os.lower()) != -1 and name.find(arch[0:2]) != -1:
            download_url = str(asset['browser_download_url'])
            break
    print(download_url)
    if download_url is None:
        print("Download failed,you can download by yourself.")
    else:
        download_file(download_url,"v2ray/" + download_url.split('/')[-1])
else:
    print("Please download the v2ray-core by yourself and put it into the 'v2ray' folder.")
import os
import requests
import urllib3

#TEST_URL = "192.168.1.139"
TEST_URL_ROBOTS = "www.google.com.au"

#Can I get this to return an error if not found
def curlforbots(url):
    result = os.popen(f"curl -v https://{url}/robots.txt").read()
    with open("robots.txt", "w") as f:
        print(result, file=f)
    print(result)


curlforbots(TEST_URL_ROBOTS)

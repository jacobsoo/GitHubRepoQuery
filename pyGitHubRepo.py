import os, sys
import urllib2
import json

def main(szUserName):
    # Assemble the GitHub URL to query
    github_url = "https://api.github.com/users/" + szUserName + "/repos"
    print("[INFO] Looking for repositories from @%s" % szUserName)
    response = urllib2.urlopen(github_url)
    json_obj = response.read()
    data = json.loads(json_obj)
    for item in data:
        print("       [+] https://github.com/%s" % item['full_name'])
    response.close()

if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print("[+] Usage: %s [Github_UserName]" % sys.argv[0])
        sys.exit(0)
    else:
        szUserName = sys.argv[1]
        main(szUserName)
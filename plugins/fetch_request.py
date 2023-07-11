from urllib.parse import urljoin
from colorama import Fore
import requests
import re

requests.packages.urllib3.disable_warnings()

user_agent_ = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
header = {"User-Agent": user_agent_}

def get_requests(domain):
    s = requests.Session()
    r = s.get(f"{domain}", verify=False, headers=header)
    content = r.content
    links = re.findall('(?:href=")(.*?)"', content.decode('utf-8'))
    duplicate_links = set(links)
    no_duplicates = []
    for page_links in links:
        page_links = urljoin(f"{domain}", page_links)
        if page_links not in duplicate_links:
            no_duplicates.append(page_links)
    return ("\n".join(map(str, no_duplicates)))

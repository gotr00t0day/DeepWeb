from colorama import Fore
from animation import load_animation
from bs4 import BeautifulSoup
import requests


def do_link_analysis(links: str):
    domains = []
    domains.append(links)
    dot_com_domains = []
    no_duplicates = []
    for domain_list in domains:
        domain_name = domain_list.split("/")
        for domain_names in domain_name:
            domain_names = domain_names.strip()
            if ".com" in domain_names:
                domain_names = domain_names.replace("https:", "")
                domain_names = domain_names.replace("www.", "")
                domain_names = domain_names.strip()
                domain_names = domain_names.split("#")[0]
                dot_com_domains.append(domain_names)
    for x in dot_com_domains:
        if x not in no_duplicates:
            no_duplicates.append(x)
    print("\n".join(map(str, no_duplicates)))
    print("\n")

    print(f"{Fore.WHITE}")

    load_animation("Getting url paths")

    # Split the path from the url
    path_no_duplicates = []
    path_links = []
    for domains_ in domains:
        split_domain = domains_.split("/")
        for i in split_domain:
            if "https:" in i:
                i = i.replace("https:", "")
                i = i.strip()
                if i in dot_com_domains:
                    pass
                else:
                    path_links.append(i)
    for x_paths in path_links:
        if x_paths not in path_no_duplicates:
            path_no_duplicates.append(f"/{x_paths}")
    print(f"{Fore.GREEN}")
    print("\n".join(map(str, path_no_duplicates)))

    print("\n")
    print(f"{Fore.WHITE}")
    load_animation("Gettting admin and login pages")
    print("\n")

    # Find admin and login pages
    pages = []
    for admin_login_pages in domains:
        with open("urls.txt", "w") as f:
            f.write(admin_login_pages)
        admin_login_pages2 = admin_login_pages.split(".com/")
        if "admin" in admin_login_pages2 or "login" in admin_login_pages2:
            pages.append(admin_login_pages)
        with open("urls.txt", "r") as fread:
            url_list = [x.strip() for x in fread.readlines()]
            url_list = set(url_list)
            for urls in url_list:
                try:
                    s = requests.Session()
                    r = s.get(urls)
                    soup = BeautifulSoup(r.content, 'html.parser', from_encoding="iso-8859-1")
                    for title in soup.find_all('title'):
                        print(f"{urls} - {title.get_text()}")
                        if "admin" in title.get_text() or "login" in title.get_text():
                            pages.append(urls)
                        else:
                            pass
                except requests.exceptions.ConnectionError:
                    pass
                forms = soup.find_all('form')
                username_types = ['text', 'email', 'username', 'password']
                for form in forms:
                    input_fields = form.find_all('input')
                    types = [input_field.get('type') for input_field in input_fields]
                    if 'password' in types and any(username_type in types for username_type in username_types):
                        pages.append(urls)
    if pages:
        for page_list in pages:
            print(f"{Fore.GREEN} {page_list}")
    if not pages:
        print(f"{Fore.RED} No Admin or Login pages found")


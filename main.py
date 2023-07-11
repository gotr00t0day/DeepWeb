from plugins import fetch_request, link_analysis
from colorama import Fore
import animation
import argparse


parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()

parser.add_argument('-t', '--target',
                   help="Target to scan",
                   metavar="https://www.domain.com")

group.add_argument('-s', '--save', action='store',
                   help='save output to a file',
                   metavar="output.txt")


args = parser.parse_args()

banner = f"""
{Fore.MAGENTA}

▓█████▄ ▓█████ ▓█████  ██▓███   █     █░▓█████  ▄▄▄▄
▒██▀ ██▌▓█   ▀ ▓█   ▀ ▓██░  ██▒▓█░ █ ░█░▓█   ▀ ▓█████▄
░██   █▌▒███   ▒███   ▓██░ ██▓▒▒█░ █ ░█ ▒███   ▒██▒ ▄██
░▓█▄   ▌▒▓█  ▄ ▒▓█  ▄ ▒██▄█▓▒ ▒░█░ █ ░█ ▒▓█  ▄ ▒██░█▀
░▒████▓ ░▒████▒░▒████▒▒██▒ ░  ░░░██▒██▓ ░▒████▒░▓█  ▀█▓
 ▒▒▓  ▒ ░░ ▒░ ░░░ ▒░ ░▒▓▒░ ░  ░░ ▓░▒ ▒  ░░ ▒░ ░░▒▓███▀▒
 ░ ▒  ▒  ░ ░  ░ ░ ░  ░░▒ ░       ▒ ░ ░   ░ ░  ░▒░▒   ░
 ░ ░  ░    ░      ░   ░░         ░   ░     ░    ░    ░
   ░       ░  ░   ░  ░             ░       ░  ░ ░
 ░                                                   ░

{Fore.CYAN}Author:  {Fore.WHITE} c0d3Ninja
{Fore.CYAN}Version: {Fore.WHITE} 0.1.3
"""

print(banner)

if args.target:
    target = args.target
    if "https://" in target:
        target = target.replace("https://", "")
    if "http://" in target:
        target = target.replace("http://", "")
    print(f"{Fore.WHITE}")
    animation.load_animation(f"Extracting Links from {target}")
    print("\n")
    links = fetch_request.get_requests(f"{args.target}")
    print(f"{Fore.GREEN}{links}")
    print(f"{Fore.WHITE}\n")
    animation.load_animation("Getting Domain names")
    print(f"{Fore.GREEN}\n")
    link_analysis.do_link_analysis(links)

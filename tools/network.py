import sys, socket, ipaddress, requests
from urllib.parse import urlparse
from time import sleep
from colorama import Fore

#Check if site is under CloudFlare protection

def isCloudFlare(link):
    parsed_uri = urlparse(link)
    domain = "{uri.netloc}".format(uri=parsed_uri)
    try:
        origin = socket.gethostbyname(domain)
        iprange = requests.get("https://www.cloudflare.com/ips-v4").text
        ipv4 = [row.rstrip() for row in iprange.splitlines()]
        for i in range(len(ipv4)):
            if ipaddress.ip_address(origin) in ipaddress.ip_network(ipv4[i]):
                print(
                    f"{Fore.RED}[!] {Fore.YELLOW}The site is protected by CloudFlare, attacks may not produce results.{Fore.RESET}"
                )
                sleep(1)
    except socket.gaierror:
        return False

#Is connected to internet?

def InternetConnectionCheck():
    try:
        requests.get("https://google.com", timeout=4)
    except:
        print(
            f"{Fore.RED}[!] {Fore.MAGENTA}Your device is not connected to the Internet{Fore.RESET}"
        )
        sys.exit(1)
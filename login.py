import requests,random
import re,sys,os
import time

D = '\033[90;1m'
G = '\033[97;1m'
R = '\033[91;1m'
W = '\033[92;1m'
Y = '\033[93;1m'
B = '\033[94;1m'
P = '\033[95;1m'
C = '\033[96;1m'
N = '\x1b[0m'
my_color = [
    B, C, R, W, G, Y, P, D
]
secdet = random.choice(my_color)
def danger(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.1)

url = "https://tbblab.shop/tbbcs/index.php"


logo = f"""                       
{R} █▀{B} █▀▀{W} █▀▀{P} █▀▄ {Y}█▀▀{C} ▀█▀
{R} ▄█ {B}██▄ {W}█▄▄{P} █▄▀ {Y}██▄ {C} █
                    \033[90;1m╔═══════════════════╗ 
                      \033[91;1mADNAN\033[94;1m ADIF \033[91;1mHISHAM
                    \033[90;1m╚═══════════════════╝
"""

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control": "max-age=0",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "https://tbblab.shop",
    "Referer": "https://tbblab.shop/tbbcs/index.php",
    "Sec-Ch-Ua": '"Chromium";v="136", "Microsoft Edge";v="136", "Not.A/Brand";v="99"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0",
    "Cookie": "PHPSESSID=027f20b8dbd43903b8e3dbebb0d68779"
}
os.system("clear")  
print(logo)
danger(f"{B}This Tool Is For Educational Purpose Only")
danger(f"{D}I Am Not Responsible For Any Misuse Of This Tool")
danger(f"{Y}This Tool Is Made By ADNAN ADIF HISHAM")
print(f"{R}This Tool api collect from Team Black Berry")
os.system("clear")
print(f"{D} {W} {R} {G} {Y} {B} {P} {C} {N}")

print(logo)
number = input(f"{G}Please Input Your Number: ")
msg = input(f"{B}Please Input Your Message: ")
payload = {
    "number": number,
    "message": msg,
}
response = requests.post(url, headers=headers, data=payload, allow_redirects=True)
print(f"{secdet}Used Number: {number} | {secdet}msg : {msg} | {W}Status Code: {response.status_code}")
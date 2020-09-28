import speedtest
import requests
from subprocess import PIPE, Popen

#Name Lastname
Name_LastName = str(input("Enter your first and last name: "))

#ping
res = Popen('ping -n 300 ya.ru | find "Пакетов" & ping -n 1 ya.ru | find "Минимальное"', shell=True, stdout=PIPE)
out = str(res.communicate()[0].decode("CP866"))


#Speedtest
test = speedtest.Speedtest()
download = test.download()
upload = test.upload()
download_mbs = round(download / (10 ** 6), 2)
upload_mbs = round(upload / (10 ** 6), 2)

#Result
Speed_test = (f" \n Download speed: {download_mbs} Mb/s \n Upload Speed : {upload_mbs} Mb/s")
ping_out = (f" \n Ping info: \n {out}")

#telegram
api_token = 'token'

requests.get('https://api.telegram.org/bot{}/sendMessage'.format(api_token), params=dict(
   chat_id='id',
   text=Name_LastName + Speed_test + ping_out
))

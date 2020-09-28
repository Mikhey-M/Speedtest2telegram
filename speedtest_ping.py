import speedtest
import requests
from subprocess import PIPE, Popen

#Name Lastname
Name_LastName = str(input("Введите Имя и Фамилию: "))

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
api_token = '1241957629:AAE18fewdITf4Zc-v46Grwp7k-P_lnq1pIc'

requests.get('https://api.telegram.org/bot{}/sendMessage'.format(api_token), params=dict(
   chat_id='-348050921',
   text=Name_LastName + Speed_test + ping_out
))
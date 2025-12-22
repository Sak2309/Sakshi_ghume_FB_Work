import time

for i in range(1,4):
    print(i)
    time.sleep(1)


res = time.localtime()
print(res)
print(res.tm_wday)

res = time.strptime('17-03-2025 10:05:06', '%d-%m-%Y %H:%M:%S')
print(res)

res = time.strftime('%d-%m-%Y %H:%M:%S')
print(res)
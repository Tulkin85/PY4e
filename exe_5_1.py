import time
print(time.strftime("%H:%M:%S", time.gmtime(time.time())))

cur_time = time.strftime("%Y-%m-%d", time.gmtime(time.time()))

print(cur_time)

old_time = '1970-09-09'

print(cur_time - old_time)

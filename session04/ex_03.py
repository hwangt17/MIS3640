import time

print(time.time())
date = int(time.time())
days = date // (60 * 60 * 24)
secday = date % (60 * 60 * 24)
hrs = secday // (60 * 60)
mins = secday // 60 - hrs * 60
secs = secday - hrs * 60 * 60 - mins * 60

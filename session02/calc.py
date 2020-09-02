print('1. How many secounds are there in 42 minutes 42 secounds?')
x = 42 * 60 + 42
print(str(x) + " seconds") 

print('2. How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile.')
y = 10 / 1.61
print(str(y) + " miles")

print('3. If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace (time per mile in minutes and seconds)? What is your average speed in miles per hour?')
SPM = x // y
MPMM = SPM // 60
MPMS = SPM % 60

print("The average pace is " + str(MPMM) + " minutes " + str(MPMS) + " seconds per mile")

H = x/3600.0
MPH = y / H

print("The average speed is " + str(MPH) + " miles per hour")
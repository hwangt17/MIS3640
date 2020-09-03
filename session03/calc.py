import math

print('1. What is the volume of a sphere with radius 5?')
r = 5 #radius of the sphere
sphere = (4/3) * math.pi * r ** 3 #volume of a sphere equation
print(f'The volume of the sphere is {sphere:.2f}m^3.')

print('2. Suppose the cover price of a book is $24.95, but bookstores get a 40 percent discount. Shipping costs $3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for 60 copies?')
cover = 24.95
discount = 0.4
first_copy = (cover * (1 - discount)) - 3
other_copy = (cover * (1-discount)) - 0.75
total_copy = first_copy + (59 * other_copy)
print(f'The total Wholesale cost for 60 copies is ${total_copy:.2f}.')

print('3. If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?')
easypace_sec = (8 * 60) + 15
tempo_sec = (7 * 60) + 12
total_run_sec = easypace_sec + (tempo_sec * 3) + easypace_sec
total_run_min = total_run_sec // 60
date_min = (6 * 60) + 52
return_date_in_min = date_min + total_run_min
return_date_hr = return_date_in_min // 60
return_date_min = return_date_in_min % 60
print(f'I will get home at {return_date_hr}:{return_date_min}am for breakfast.')

print('4. If my average grade rises from 82 to 89. What is the percentage of the increase?')
grade_1 = 82
grade_2 = 89
grade_inc = 89/82-1
print(f'{grade_inc:.1%} increase')

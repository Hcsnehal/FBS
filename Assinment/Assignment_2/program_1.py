# 1. Convert the time entered in hh,min and sec into seconds.

# 1 hour = 3600sec
# 1 min = 60 sec
# sec = sec

# formulae to calculate total seconds is
# total_sec = (hh * 3600) + (min * 60) + sec

hours = int(input("Enter hours :"))
min = int(input("enter a min :"))
sec = int(input('enter a seconds :'))

total_sec = (hours*3600)+(min*60) + sec
print(f'total seconds is {total_sec}')
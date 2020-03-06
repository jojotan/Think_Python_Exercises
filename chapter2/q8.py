# You look at the clock and it is exactly 2pm. You set an alarm to go off in 51 hours. 
# At what time does the alarm go off? 
# Write a Python program to solve the general version of the above problem. 
# Ask the user for the time now (in hours), and ask for the number of hours to wait. 
# Your program should output what the time will be on the clock when the alarm goes off.

time = int(input("Please input the time now (in hours): "))
wait_time= int(input("Please input the number of hours to wait: "))


n_days = wait_time // 24
after_time = wait_time % 24

if time + after_time < 24:
    alarm_time = time + after_time
    n_days = n_days
else:
    alarm_time = (time + after_time) -24
    n_days = n_days + 1

print("The alarm will goes off ", n_days, " days later, at ", alarm_time, ":00 clock")


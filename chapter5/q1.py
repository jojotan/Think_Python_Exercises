# Assume the days of the week are numbered 0,1,2,3,4,5,6 from Sunday to Saturday.
# Write a function which is given the day number, and it returns the day name (a string).

def num_to_name_day (num):
    week = ['Sunday', 'Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    for i in range(len(week)):
        while num == i:
            return week[i]

num = int(input("Please input the day number (from 0 to 6) : "))
print(num_to_name_day(num))
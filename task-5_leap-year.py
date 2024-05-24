#there is a number of a year
#is it a leap year? 
#YES - this us the leap year
#NO - this is not

# #%4=0 and not#%100=0 or #%400=0 - leap year

year = int(input('The number of the year: '))

if year%4 == 0 and year%100 != 0 or year%400 == 0:
    print('YES')
else:
    print('NO')



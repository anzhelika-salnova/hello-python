# every ticket consists of 6 digits 
# lucky ticket - the sum of 1, 2 & 3 digits equal the sum of 4, 5 & 6 digits

n = int(input('Enter the ticket number: '))

d1 = n//100000       # the first digit of the entered number 
d2 = (n//10000)%10   # the second digit of the entered number  
d3 = (n//1000)%10    # the third digit of the entered number
d4 = (n//100)%10     # the fourth digit of the entered number
d5 = (n//10)%10      # the fifth digit of the entered number
d6 = n%10            # the sixth digit of the entered number

if d1+d2+d3 == d4+d5+d6:
    print('yes')
else:
    print('no')
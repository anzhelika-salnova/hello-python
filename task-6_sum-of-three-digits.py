# n - three-digit number 
# res - sum of the three digits

n = int(input('Enter a three-digit number: '))

d1 = n//100       # the first digit of the entered number
d2 = (n//10)%10   # the second digit of the entered number
d3 = n%10         # the third digit of the entered number

res = d1+d2+d3 

print(res)
# n - three-digit number 
# sum - sum of the three digits

n = int(input('Enter a three-digit number: '))
sum = 0

while n>0:
    x = n % 10
    sum = sum + x
    n = n//10

print(sum)
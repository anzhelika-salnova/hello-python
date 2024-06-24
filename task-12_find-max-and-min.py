# n - the total quantity of numbers 
#find the maximum and minimum nuber

n = int(input())

first = int(input())
minim = first
maxim = first

for i in range(n-1):
    checked = int(input())
    if checked < minim:
        minim = checked
    elif checked > maxim:
        maxim = checked
        
print(minim, maxim)


# for i in range(5):
#     print("hello")
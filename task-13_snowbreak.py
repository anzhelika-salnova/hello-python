#Put the quantity of the days - N(1<=N<=1000)
#Put the temperature of the each day [-50:50]
#The biggest number of quantity days with temperature >0

n = int(input('Enter the number of checked days: '))

max_current = 0
max_global = 0

for i in range(n):
    value = int(input())
    if value > 0:
        max_current +=1 
        if max_current >= max_global:
            max_global = max_current

    else:
        max_current = 0

print('max_global', max_global)

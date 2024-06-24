# a>1 
#Fibonacci(n)=a?
#If A is NOT a Fibonacci - print -1

searched = int(input()) 

order_number = 2
tail = 0
head = 1
result = -1

while head < searched: 
    order_number += 1 
    previousHeadForNextTail = head 
    head = tail + head 
    tail = previousHeadForNextTail 
    if (head == searched): 
        result = order_number

print(result)

#0 1 1 2 3 5 8 13 21 34
#numbers of carriages - from 1 to X
# i - number in the ticket (depends on direction)
# j - number of the carriage

i = int(input('Ticket number: '))
j = int(input('The number on the carriage: '))

if i == j:
    print('not enough information')
else:
    print(i+j-1)

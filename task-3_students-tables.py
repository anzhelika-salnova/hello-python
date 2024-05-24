#3 new math classes
#gooing to buy some tables
#2 students for 1 table
#min amount of tables for buying?
# DO NOT USE IF OR WHILE

print('Number of students in the first math class:')
cs1 = int(input())
print('Number of students in the second math class:')
cs2 = int(input())
print('Number of students in the third math class:')
cs3 = int(input())

ct1 = cs1//2 + round(cs1%2,0)
ct2 = cs2//2 + round(cs2%2,0)
ct3 = cs3//2 + round(cs3%2,0)
#ct1/ct2/ct3 = abs(-cs1/-cs2/-cs3//2), abs == MODULUS

print(ct1 + ct2 + ct3)
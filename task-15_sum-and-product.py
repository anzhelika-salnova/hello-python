"""
There are two numbers (X and Y), and we know only sum of them (s) and product of them (multiply - m)
X,Y≤1000 and X,Y>0
Result: X, Y (P.S. X <= Y)
"""

#Vieta's theorem

from math import sqrt

s = 38
m = 297

d = s**2 - 4 * m

X = (s + sqrt(d))/2
Y = (s - sqrt(d))/2

print(int(X), int(Y))
"""
# There is a chocolate bar 
# The bar size = axb
# c - snaped off chocolate picies
# Result - 2 rectangles

"""

a = int(input('Pieces-length: '))
b = int(input('Pieces-width: '))
c = int(input('Pieces to snap off: '))

if c < a*b and (c%a==0 or c%b==0):
    print('yes')
else:
    print('no')
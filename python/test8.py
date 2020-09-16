x = int(input('Please insert your mark here:'))
if 100 >= x >= 90:
    print ('GRADE A*')
elif 90 > x >= 80:
    print ('GRADE A')
elif 80 > x >= 60:
    print ('GRADE B')
elif 60 > x >= 40:
    print ('GRADE C')
elif 40 > x >= 0:
    print ('UNGRADED')

else :
    print('Wrong print.')

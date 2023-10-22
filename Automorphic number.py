n=int(input('Enter the number:'))
n_square=pow(n,2)
length=len(str(n))
n1=pow(10,length)

if (n_square%n1)==n:
    print('It is an automorphic number')
else:
    print('It is not an automorphic number')
print('The square of the given number n is:',n_square)

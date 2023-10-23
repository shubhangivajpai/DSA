# armstrong number
#371
number=int(input('Enter the number'))
n1=number
digit=0
res=0

length=len(str(n1))
for i in range(length):
    digit=n1%10
    n1=n1//10
    res+=pow(digit,length)
if res==number:
    print('It is an Armstrong Number')
else:
    print('It is not an armstrong number')
    

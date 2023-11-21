num=int(input("Enter the number you want to check:"))
temp=num
reverse=0
while temp!=0:
    rem= temp%10
    reverse=reverse*10+rem
    temp=temp//10
if num==reverse:
    print(f"{num} is a palindrome")
else:
    print(f"{num} is not a palindrome")

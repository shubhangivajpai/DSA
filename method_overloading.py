# implementation of method overloading in python in python method
#overloading can not be implemented directly it can be implemented through default arguments
#and variable arguments 

class Calculator:
    def add(self,a,b,c=0):
        return a+b+c
calc=Calculator()
res1=calc.add(2,3)
res2=calc.add(2,3,4)
print(res1)
print(res2)

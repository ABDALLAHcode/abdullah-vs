num1=float(input('enter first num:'))

opy=input('enter opreation:')

num2=float(input('enter second num:'))

if opy == '+':
    print(num1 + num2)
elif opy == '-':
    print(num1-num2)
elif opy == '*':
    print(num1*num2)
elif opy == '**':
    print(num1**num2)
elif opy == '/':
    print(num1/num2)
elif opy == '//':
    print(num1//num2)
elif opy == '%':
    print(num1%num2)
else:
    print('enter value correct')

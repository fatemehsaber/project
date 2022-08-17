import math
types = input('''what type do you want to use ?
a)elementary
b)advanced
c)khast \n''')
countain = int (input('how many times do tou want to use the calculator ? '))
i1 = 0
i2 = 0
i3 = 0
if (types == 'a'):
    while (i1 < countain):
        num1 = float(input('enter your first number : '))
        print('''
        1)sum = +
        2)subtraction = -
        3)mul = *
        4)div = /
        5)mod = %
        6)int_div = //
        7)pow = **
        8)absolute value = abs
        9)logaritm = log
        10)radical = rad''')

        operator = input('enter your operator : ')
        if (operator == '+' or operator == '-' or operator == '*' or operator == '/'or operator == '//' or operator == '%' or operator == '**'):
            num2 = float(input('enter your seconed number : '))
        i1 += 1
        if (operator == '+'):
            print('sum is = ',num1 + num2)
        elif (operator == '-'):
            print('subtraction is = ',num1 - num2)
        elif (operator == '*'):
            print('mul is = ',num1 * num2)
        elif (operator == '/'):
            if(num2 != 0):
                print('div is = ',num1 / num2)
            else:
                print('error!')
        elif (operator == '%'):
            print('mod is = ',num1 % num2)
        elif (operator == '//'):
            if(num2 != 0):
                print('int_div is = ',num1 // num2)   
            else:
                print('error!')
        elif (operator == '**'):
            print('pow is = ',num1 ** num2)
        elif (operator == 'abs'):
            print('subtraction is = \n ',abs(num1))
        elif (operator == 'log'):
            print('logaritm is = ',math.log(num1))
        elif (operator == 'rad'):
            print('radical is = ',math.sqrt(num1))
elif (types == 'b'):
    while (i2 < countain):
        num1 = float(input('enter your first number : '))
        print('''
        1) sin
        2)cos
        3)tan
        4)fact
        5)max
        6)min
        7)bmm
        8)kmm
        9)radian
        10)degree
        11)ceil
        12)floor''')
        operator = input('enter your operator : ')
        if (operator == 'max' or operator == 'min'):
            num2 = float(input('enter your seconed number : '))
        i2 += 1
        if (operator == 'sin'):
            print('sin is = ',math.sin(num1))
        elif (operator == 'cos'):
            print('cos is = ',math.cos(num1))
        elif (operator == 'tan'):
            print('tan is = ',math.tan(num1))
        elif (operator == 'fact'):
            print('fact is = ',math.factorial(num1))
        elif (operator == 'max'):
            print('max is = ',max(num1,num2))
        elif (operator == 'min'):
            print('min is = ',min(num1,num2))
        elif (operator == 'radian'):
            print('radian is = ',math.radians(num1))
        elif (operator == 'degree'):
            print('degree is = ',math.degrees(num1))
        elif (operator == 'ceil'):
            print('ceil is = ',math.ceil(num1))
        elif (operator == 'floor'):
            print('floor is = ',math.floor(num1))
elif (types == 'c'):
    while (i3 < countain):
        num1 = int(input('enter your first number : '))
        print('''
        1)fact
        2)bmm
        3)kmm
        4)prime num = prime''')
        operator = input('enter your operator : ')
        if (operator == 'bmm' or operator == 'kmm'):
            num2 = int(input('enter your seconed number : '))
        i3 += 1
        if (operator == 'fact'):
            print('sin is = ',math.factorial(num1))
        elif (operator == 'bmm'):
            print('bmm is = ',math.gcd(num1,num2))
        elif (operator == 'kmm'):
            print('kmm is = \n ',math.lcm(num1,num2))
        elif (operator == 'prime'):
            accumulator = 0
            for i in range(1, num1+1):
                if num1%i == 0:
                    accumulator+=1
            if accumulator==2:
                    print('your number is prime')
            else:
                    print('your number is not prime')
           
     
else:
       
        print('error!')
  
        
        




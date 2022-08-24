from hashlib import sha1
import math

types = input('''what type do you want to use ?
a)elementary
b)advanced
c)khast
d)tabdil_mabna
e)BMI
f)temperature conversion
g)shapes \n''')

countain = int (input('how many times do tou want to use the calculator ? '))

i1 = 0
i2 = 0
i3 = 0
i4 = 0
i5 = 0
i6 = 0
i7 = 0

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
        9)logaritm2 = log2
        10)logaritm10 = log10
        11)logaritm = log
        12)radical = rad
        13)even or odd''')

        operator = input('enter your operator : ')

        if (operator == '+' or operator == '-' or operator == '*' or operator == '/'or operator == '//' or operator == '%'or operator == 'log' or operator == '**'):
            
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

        elif (operator == 'log2'):
            print('logaritm2 is = ',math.log2(num1))

        elif (operator == 'log10'):
            print('logaritm10 is = ',math.log10(num1))

        elif (operator == 'log'):
            print('logaritm is = ',math.log(num1,num2))

        elif (operator == 'rad'):

            print('radical is = ',math.sqrt(num1))

        elif (operator == 'even_odd'):
                
                if(num1%2==0):
                    print("your number is even")
                else:
                    print("your number is odd")

elif (types == 'b'):

    while (i2 < countain):

        num1 = float(input('enter your first number : '))
    
        print('''
        1) sin
        2)cos
        3)tan
        4)max
        5)min
        6)bmm
        7)kmm
        8)radian
        9)degree
        10)ceil
        11)floor
        12)atan
        ''')

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

        elif (operator == 'atan'):
            print('atan is = ',math.atan(num1))

elif (types == 'c'):

    while (i3 < countain):

        num1 = int(input('enter your first number : '))

        print('''
        1)fact
        2)bmm
        3)kmm
        4)prime num = prime
        5)exp''')

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
        elif (operator == 'exp'):
            print('exp is = ',math.exp(num1))

elif (types == 'd'):

    while (i4 < countain):
                 
                print('='*10,'convert','='*10,'\n''selec: ''\n''1)bin--->dec''\n''2)bin--->oct''\n''3)bin--->hex''\n''4)oct--->dec''\n''5)oct--->bin''\n''6)oct--->hex''\n''7)hex--->dec''\n''8)hex--->bin''\n''9)hex--->oct''\n''10)dec--->bin''\n''11)dec--->oct''\n''12)dec--->hex')
                select=int(input('select:'))
                if select==1:
                    number=0
                    bace=1
                    last=0
                    sums=0
                    number = int(input("Enter number: "))
                    while number:
                        last = int(number%10)
                        number = int(number/10)
                        last *= bace
                        sums += last
                        bace = bace*2
                    print('dec',(sums))
                        
                elif select==2:
                    number=0
                    bace=1
                    last=0
                    sums=0
                    number = int(input("Enter number: "))
                    while number:
                        last = int(number%10)
                        number = int(number/10)
                        last *= bace
                        sums += last
                        bace = bace*2
                    print(oct(sums))
                elif select==3:
                    number=0
                    bace=1
                    last=0
                    sums=0
                    number = int(input("Enter number: "))
                    while number:
                        last = int(number%10)
                        number = int(number/10)
                        last *= bace
                        sums += last
                        bace = bace*2
                    print(hex(sums))
                elif select==4:
                    number=0
                    bace=1
                    last=0
                    sums=0
                    number = int(input("Enter number: "))
                    while number:
                        last = int(number%10)
                        number = int(number/10)
                        last *= bace
                        sums += last
                        bace = bace*8
                    print(sums)
                elif select==5:
                    number=0
                    bace=1
                    last=0
                    sums=0
                    number = int(input("Enter number: "))
                    while number:
                        last = int(number%10)
                        number = int(number/10)
                        last *= bace
                        sums += last
                        bace = bace*8
                    print(bin(sums))
                elif select==6:
                    number=0
                    bace=1
                    last=0
                    sums=0
                    number = int(input("Enter number: "))
                    while number:
                        last = int(number%10)
                        number = int(number/10)
                        last *= bace
                        sums += last
                        bace = bace*8
                    print(hex(sums))
                elif select==7:
                    number=0
                    bace=1
                    last=0
                    sums=0
                    number = int(input("Enter number: "))
                    while number:
                        last = int(number%10)
                        number = int(number/10)
                        last *= bace
                        sums += last
                        bace = bace*16
                    print(sums)
                elif select==8:
                    number=0
                    bace=1
                    last=0
                    sums=0
                    number = int(input("Enter number: "))
                    while number:
                        last = int(number%10)
                        number = int(number/10)
                        last *= bace
                        sums += last
                        bace = bace*16
                    print(bin(sums))
                elif select==9:
                    number=0
                    bace=1
                    last=0
                    sums=0
                    number = int(input("Enter number: "))
                    while number:
                        last = int(number%10)
                        number = int(number/10)
                        last *= bace
                        sums += last
                        bace = bace*16
                    print(oct(sums))
                elif select==10:
                    number = int(input("Enter number: "))
                    print(bin(number))
                elif select==11:
                    number = int(input("Enter number: "))
                    print(oct(number))
                elif select==12:
                    number = int(input("Enter number: "))
                    print(hex(number))

        

elif (types == 'e'):

    while (i5 < countain):
        
        heigh = float(input('enter your heigh (m): '))
        weight = float(input('enter your weight (kg): '))
        age = int (input(' enter your age (24 be bala): '))
        i5 += 1

        BMI = weight // (heigh ** 2)


        print(BMI)
        if (BMI <= 15):
            print('your BMI is : ',BMI,'\n You are severely underweight.')
    
        elif(15 < BMI <=18.5):
            print('your BMI is : ',BMI,'\n You are underweight.')
   
        elif(18.5 < BMI <= 25):
            print('your BMI is : ',BMI,'\n You have a normal weight.')
    
        elif(25 < BMI <= 30):
            print('your BMI is : ',BMI,'\n You are overweight.')
    
        elif(30 < BMI <= 35):
            print('your BMI is : ',BMI,'\n You have normal obesity.')
    
        elif(35 < BMI <= 40):
            print('your BMI is : ',BMI,'\n You are severely obese.')
    
        elif(40> BMI):
            print('your BMI is : ',BMI,'\n You are very obese.')

    

        if (19 < age <=25):
            print('BMI monaseb sen shoma:22')
        elif(25 < age <= 35):
            print('BMI monaseb sen shoma:23')
        elif(35 < age <= 45):
            print('BMI monaseb sen shoma:24')
        elif(45 < age <= 55):
            print('BMI monaseb sen shoma:25')
        elif(55 < age <= 65):
            print('BMI monaseb sen shoma:26')
        elif(age > 65):
            print('BMI monaseb sen shoma:27')

elif (types == 'f'):

    while (i6 < countain):
        
            dama=float(input(' please enter dama : '))
            type_dama1 =input('''please enter your first temperatuur : 
1)celsius 
2)fahrenheit 
3)kelvin  
''' )

            type_temp2 =input('''please enter your second temperatuur : 
1)celsius 
2)fahrenheit 
3)kelvin  
''' )
            i6  += 1
            if type_dama1 =='1' and type_temp2 =='2':
               f = (dama * 1.8) + 32
               print('fahrenheit = ',f)

            elif type_dama1 == '2' and type_temp2 == '1':
                c = (dama - 32) / 1.8
                print('celsius = ',c)

            elif type_dama1 == '3' and type_temp2 == '1':
                c = dama - 273.15
                print('celsius = ',c)

            elif type_dama1 == '1' and type_temp2 == '3':
                k = dama + 273.15
                print('kelvin = ',k)

            elif type_dama1 == '2' and type_temp2 == '3':
                print('kelvin =',(dama + 459.67) / 1.8)


            elif type_dama1 == '3' and type_temp2 == '2':
                print('fahrenhit =',(dama * 1.8) - 459.67) 

            else:
                print('mojadad vared shavid')


elif (types == 'g'):

    while (i7 < countain):

        print('''
        a)circle
        b)cylinder
        c)triangle
        d)square
        e)rectanggle
        f)diamond
        g)trapezius
        h =parallelogram

        i)oval
        j) cube
        k)rectangular cube
        l)sphere
        m)elliptical sphere''')

        shape = input('enter your first shape : ')
        
        if(shape == 'a'):
            
            radius = float(input('enter of radius : '))
            
            C = 2 * math.pi *radius
            A = math.pi * radius ** 2

            print('area is :', A , 'environment is :' , C)

        elif(shape == 'b'):
            
            height = float(input('enter the height : '))

            radius = float(input('enter the radius : '))



            volume = (math.pi * height * radius ** 2)
            lateralArea = (2 * math.pi * radius * height)
            totalArea = ((2 * math.pi) * radius ** 2) + lateralArea

            print('lateralArea = %f  \n volume = %f \n totalArea = %f' %(lateralArea,volume,totalArea))

        elif(shape == 'c'):
            
            base = float(input('enter of base : '))
            height = float(input('enter of height : '))
            side1 = float(input('enter of side1 : '))
            side2 = float(input('enter of side2 : '))
            side3 = float(input('enter of side3 : '))
            
            C = 0.5 * base * height
            A = side2 + side1 + side3
            if (side1 * side1 == side2 * side2 + side3 * side3 or side2 * side2 == side1 * side1 + side3 * side3 or side3 * side3 == side2 * side2 + side1 * side1):
                 print('it is a right angle')
            else:
                print('it is not a right angle')
            print('area is :', A , 'environment is :' , C)
        
        elif(shape == 'd'):
            
            side = float(input('enter of side : '))
            
            C = side ** 2
            A = 4 * side

            print('area is :', A , 'environment is :' , C)
        elif(shape == 'e'):
            
            l = float(input('enter of length : '))
            w = float(input('enter of width : '))
            
            C = l * w
            A = 2 * l + 2 * w

            print('area is :', A , 'environment is :' , C)

        elif(shape == 'f'):
            
            b = float(input('enter of length : '))
            h = float(input('enter of width : '))
            
            C = b * h
            A = 4 * b

            print('area is :', A , 'environment is :' , C)
        
        elif(shape == 'g'):
            
            Base = float(input('enter of Base : '))
            base = float(input('enter of base : '))
            height = float(input('enter of height : '))
            side1 = float(input('enter of side1 : '))
            side2 = float(input('enter of side2 : '))
            side3 = float(input('enter of side3 : '))

            C = height*(Base + base) /2
            A = side1 + side2 + side3

            print('area is :', A , 'environment is :' , C)

        elif(shape == 'h'):
            
            b = float(input('enter of base : '))
            h = float(input('enter of height : '))
            side1 = float(input('enter of side1 : '))
            side2 = float(input('enter of side2 : '))
            side3 = float(input('enter of side3 : '))
            
            C = b * h
            A = side1 + side2 + side3

            print('area is :', A , 'environment is :' , C)

        elif(shape == 'i'):
            
            r1 = float(input('enter of radius : '))
            r2 = float(input('enter of radius : '))
            
            A = math.pi * r1 * r2

            print('area is :', A )
        
        elif(shape == 'j'):
            
            s = float(input('enter of side : '))
        
            C = 6 * s ** 2
            V = s ** 3

            print('area is :', C , 'volume is :' , V)

        elif(shape == 'k'):
            
            a = float(input('enter of side1 : '))
            b = float(input('enter of side2 : '))
            c = float(input('enter of side3 : '))

            A = 2 * a *c +2 *b *c + 2 * a *b
            V =a * b * c

            print('area is :', C , 'volume is :' , V)
        
        elif(shape == 'l'):
            
            r = float(input('enter of radius : '))
            
            C = 4 * math.pi * r ** 2
            V = (4/3) * math.pi * r ** 3

            print('area is :', C , 'volume is :' , V)

        elif(shape == 'm'):
            
            r1 = float(input('enter of radius1 : '))
            r2 = float(input('enter of radius2 : '))
            r3 = float(input('enter of radius3 : '))
            
            C = 4 * math.pi * r1 * r2
            V = (4/3) * math.pi * r1 * r2 * r3

            print('area is :', C , 'volume is :' , V)

else:
       
        print('error!')
  
        
        




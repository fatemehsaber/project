
import math

countain = int (input('\nhow many times do tou want to use the calculator ? \n\n'))

types = input('''\nwhat type do you want to use ?
a)elementary
b)advanced
c)khast
d)tabdil_mabna
e)BMI
f)temperature conversion
g)shapes \n\n''')



i1 = 0
i2 = 0
i3 = 0
i4 = 0
i5 = 0
i6 = 0
i7 = 0

if (types == 'a'):

    while (i1 < countain):

        print('''
        a)sum 
        b)subtraction 
        c)mul 
        d)div 
        e)mod 
        f)int_div 
        g)pow 
        h)absolute value 
        i)logaritm2
        j)logaritm10 
        k)logaritm 
        l)radical = rad
        m)even or odd''')

        operator = input('\nenter your operator : \n\n ')

        num1 = float(input('enter your first number : '))

        if (operator == 'a' or operator == 'b' or operator == 'c' or operator == 'd'or operator == 'f' or operator == 'e'or operator == 'k' or operator == 'g'):
            
            num2 = float(input('enter your seconed number : '))

        i1 += 1
        if (operator == 'a'):
            print('sum is = ',num1 + num2)

        elif (operator == 'b'):
            print('subtraction is = ',num1 - num2)

        elif (operator == 'c'):
            print('mul is = ',num1 * num2)

        elif (operator == 'd'):

            if(num2 != 0):
                print('div is = ',num1 / num2)
            else:
                print('error!')

        elif (operator == 'e'):
            print('mod is = ',num1 % num2)

        elif (operator == 'f'):

            if(num2 != 0):
                print('int_div is = ',num1 // num2)   
            else:
                print('error!')

        elif (operator == 'g'):
            print('pow is = ',num1 ** num2)

        elif (operator == 'h'):
            print('subtraction is = \n ',abs(num1))

        elif (operator == 'i'):
            print('logaritm2 is = ',math.log2(num1))

        elif (operator == 'j'):
            print('logaritm10 is = ',math.log10(num1))

        elif (operator == 'k'):
            print('logaritm is = ',math.log(num1,num2))

        elif (operator == 'l'):

            print('radical is = ',math.sqrt(num1))

        elif (operator == 'm'):
                
                if(num1%2==0):
                    print("your number is even")
                else:
                    print("your number is odd")

elif (types == 'b'):

    while (i2 < countain):

        print('''
        1) sin
        2)cos
        3)tan
        4)max
        5)min
        6)radian
        7)degree
        8)ceil
        9)floor
        10)atan
        ''')

        operator = input('enter your operator : ')

        num1 = float(input('enter your first number : '))

        if (operator == '4' or operator == '5'):
            num2 = float(input('enter your seconed number : '))

        i2 += 1

        if (operator == '1'):
            print('sin is = ',math.sin(num1))

        elif (operator == '2'):
            print('cos is = ',math.cos(num1))

        elif (operator == '3'):
            print('tan is = ',math.tan(num1))

        elif (operator == '4'):
            print('max is = ',max(num1,num2))

        elif (operator == '5'):
            print('min is = ',min(num1,num2))

        elif (operator == '6'):
            print('radian is = ',math.radians(num1))

        elif (operator == '7'):
            print('degree is = ',math.degrees(num1))

        elif (operator == '8'):
            print('ceil is = ',math.ceil(num1))

        elif (operator == '9'):
            print('floor is = ',math.floor(num1))

        elif (operator == '10'):
            print('atan is = ',math.atan(num1))

elif (types == 'c'):

    while (i3 < countain):

        print('''
        1)fact
        2)bmm
        3)kmm
        4)prime num = prime
        5)exp''')


        operator = input('enter your operator : ')

        num1 = int(input('enter your first number : '))

        if (operator == '2' or operator == '3'):
            num2 = int(input('enter your seconed number : '))

        i3 += 1

        if (operator == '1'):
            print('sin is = ',math.factorial(num1))

        elif (operator == '2'):
            print('bmm is = ',math.gcd(num1,num2))

        elif (operator == '3'):
            print('kmm is = \n ',math.lcm(num1,num2))

        elif (operator == '4'):

            accumulator = 0

            for i in range(1, num1+1):

                if num1%i == 0:
                    accumulator+=1

            if accumulator==2:
                    print('your number is prime')
            else:
                    print('your number is not prime')
        elif (operator == '5'):
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
            if radius < 0 :
                print('error!')
                break
            
            C = 2 * math.pi *radius
            A = math.pi * radius ** 2

            print('area is :', A , 'environment is :' , C)

        elif(shape == 'b'):
            
            height = float(input('enter the height : '))

            radius = float(input('enter the radius : '))

            if radius < 0 or height < 0 :
                print('error!')
                break



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

            if base < 0 or height < 0 or side1 < 0 or side2 < 0 or side3 < 0:
                print('error!')
                break
            
            C = 0.5 * base * height
            A = side2 + side1 + side3
            if (side1 * side1 == side2 * side2 + side3 * side3 or side2 * side2 == side1 * side1 + side3 * side3 or side3 * side3 == side2 * side2 + side1 * side1):
                 print('it is a right angle')
            else:
                print('it is not a right angle')
            print('area is :', A , 'environment is :' , C)
        
        elif(shape == 'd'):
            
            side = float(input('enter of side : '))
            if side < 0  :
                print('error!')
                break
            
            C = side ** 2
            A = 4 * side

            print('area is :', A , 'environment is :' , C)
        elif(shape == 'e'):
            
            l = float(input('enter of length : '))
            w = float(input('enter of width : '))
            if l < 0 or w < 0 :
                print('error!')
                break
            
            C = l * w
            A = 2 * l + 2 * w

            print('area is :', A , 'environment is :' , C)

        elif(shape == 'f'):
            
            b = float(input('enter of length : '))
            h = float(input('enter of width : '))
            if b < 0 or h< 0 :
                print('error!')
                break
            
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

            if Base< 0 or base < 0 or height < 0 or side1 < 0 or side2 < 0 or side3 < 0:
                print('error!')
                break

            C = height*(Base + base) /2
            A = side1 + side2 + side3

            print('area is :', A , 'environment is :' , C)

        elif(shape == 'h'):
            
            b = float(input('enter of base : '))
            h = float(input('enter of height : '))
            side1 = float(input('enter of side1 : '))
            side2 = float(input('enter of side2 : '))
            side3 = float(input('enter of side3 : '))

            if b < 0 or h < 0 or side1 < 0 or side2 < 0 or side3 < 0:
                print('error!')
                break
            
            C = b * h
            A = side1 + side2 + side3

            print('area is :', A , 'environment is :' , C)

        elif(shape == 'i'):
            
            r1 = float(input('enter of radius : '))
            r2 = float(input('enter of radius : '))
            
            if r2< 0 or r1< 0 :
                print('error!')
                break
            A = math.pi * r1 * r2

            print('area is :', A )
        
        elif(shape == 'j'):
            
            s = float(input('enter of side : '))

            if  s < 0:
                print('error!')
                break
        
            C = 6 * s ** 2
            V = s ** 3

            print('area is :', C , 'volume is :' , V)

        elif(shape == 'k'):
            
            a = float(input('enter of side1 : '))
            b = float(input('enter of side2 : '))
            c = float(input('enter of side3 : '))

            if a< 0 or b< 0 or c < 0:
                print('error!')
                break

            A = 2 * a *c +2 *b *c + 2 * a *b
            V =a * b * c

            print('area is :', C , 'volume is :' , V)
        
        elif(shape == 'l'):
            
            r = float(input('enter of radius : '))
            if r< 0 :
                print('error!')
                break
            
            C = 4 * math.pi * r ** 2
            V = (4/3) * math.pi * r ** 3

            print('area is :', C , 'volume is :' , V)

        elif(shape == 'm'):
            
            r1 = float(input('enter of radius1 : '))
            r2 = float(input('enter of radius2 : '))
            r3 = float(input('enter of radius3 : '))

            if r1< 0 or r2 < 0 or r3 < 0 :
                print('error!')
                break
            
            C = 4 * math.pi * r1 * r2
            V = (4/3) * math.pi * r1 * r2 * r3

            print('area is :', C , 'volume is :' , V)

else:
       
        print('error!')
  
        
        



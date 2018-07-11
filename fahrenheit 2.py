#Kyle Miller
#EMT 1111 - Logic and Problem Solving
#10/23/16


while True:
    Celsius = int(input("Enter a value in Celsius to calculate Fahrenheit: "))

    Fahrenheit = (9.0/5.0) * Celsius + 32

    print('%0.1f degree Celsius is equal to %0.1f degree Fahrenheit' %(Celsius,Fahrenheit))

    repeat = input("Would you like find another temperature? (y/n): ")
    if repeat == 'n':
            break
    

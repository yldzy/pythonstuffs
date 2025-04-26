checker = 0

convs = ["\nCONVERSIONS:", "Celsius to Kelvin", "Celsius to Fahrenheit", "Celsius to Rankine", "Kelvin to Celsius", "Kelvin to Fahrenheit", "Kelvin to Rankine", "Fahrenheit to Celsius", "Fahrenheit to Kelvin", "Fahrenheit to Rankine", "Rankine to Fahrenheit", "Rankine to Kelvin", "Rankine to Celsius"]
    
x = int(input("Input the temperature: "))

for i in range(len(convs)):
    
    if i > 0:
        print(i, end = '')
        print(" - ", end = '')
        
    print(convs[i], end = '')
    print()

y = int(input("\nChoose the number of your conversion: "))

while checker == 0:
    
    if y > 0 and y < 13:
        checker += 1
    
    else:
        y = int(input("\nInvalid input. Please try again: "))

if y == 1:
    a = x + 273.15
    b = 1

elif y == 2:
    a = (x * 9/5) + 32
    b = 2
    
elif y == 3:
    a = (x + 273.15) * 9/5
    b = 3
    
elif y == 4:
    a = x - 273.15
    b = 4
    
elif y == 5:
    a = (x * 9/5) - 459.67
    b = 5
    
elif y == 6:
    a = x * 9/5
    b = 6
    
elif y == 7:
    a = (x - 32) * 5/9
    b = 7
    
elif y == 8:
    a = (x + 459.67) * 5/9
    b = 8

elif y == 9:
    a = x + 459.67
    b = 9
    
elif y == 10:
    a = x - 459.67
    b = 10
    
elif y == 11:
    a = x * 5/9
    b = 11
    
elif y == 12:
    a = (x - 491.67) * 5/9
    b = 12
    
print("\nConverted ", x, " ", convs[b], ": ", a, sep = '')

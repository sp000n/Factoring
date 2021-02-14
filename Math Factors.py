# Factors the user entered numbers until no entry is given.
import sys

while True:
    
    print('What number do you need factored? (nothing to exit) ', end='')
    number=input()
    if number=='':
        sys.exit()
    number=int(number)    
    factorsLower=[]
    factorsUpper=[]
    
    i=0
    while i**2 <= number:
        i += 1
        if i**2 == number:
            factorsLower.append(i)
            break
        elif number % i == 0:
            factorsLower.append(i)
            factorsUpper.insert(0,int(number / i))
        elif number % i != 0:
            continue
    
    factors = factorsLower + factorsUpper
    if len(factors)==2:
        print(str(number) + ' is a prime number.')
    if len(factors)>2:
        print (str(number) + ' has ' + str(len(factors)) + ' factors: ', end='')
        print (factors)
    print()

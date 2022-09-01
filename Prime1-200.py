#Printing Prime numbers from 0 to 200 using for and range
for number in range(1,200):
    if number>1:
        for i in range(2,number):
            if (number%i)==0:
                break
        else:
            print(number)
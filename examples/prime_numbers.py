#we can write a python to find the prime number of a range of numbers
for primeNum in range (1, 101):
    count = 0
    for i in range(2, (primeNum//2 + 1)):
        if(primeNum % i == 0):
            count = count + 1
            break

    if (count == 0 and primeNum != 1):
        print(primeNum)
        
#example of a prime 
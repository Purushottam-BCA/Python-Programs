'''
PROBLEM :   Print integers 1 to N, but print “Fizz” if an integer is divisible by 3, 
            “Buzz” if an integer is divisible by 5, and “FizzBuzz” if an integer is 
            divisible by both 3 and 5.
'''

#----------Method-1------------

i=1
while(i<=100):
    if(i%3==0 and i%5==0):
        print("FizzBuzz")
    elif(i%3==0):
        print("Fizz")
    elif(i%5==0):
        print("Buzz")
    else:
        print(i)
    i+=1

#---------Method-2---------------

for i in range(1,101):
    output=""
    if(i%3==0):
        output="Fizz"
    if(i%5==0):
        output+="Buzz"
    print(output or i) 
 
#---------Method-3---------------

output=""
for i in range(1,101):
    output="Fizz" if i%3==0 else ""
    output+="Buzz" if i%5==0 else ""
    print(i) if output=="" else print(output)

#---------Method-4---------------

for i in range(1,101):
    print("Fizz" *(i%3<1) +"Buzz" *(i%5<1) or i) 
    

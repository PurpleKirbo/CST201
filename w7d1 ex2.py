#this is a example for loop

num = 5 

#the loop below has a start value of 0, a stop value of 5, (the Num variable) and a step value of 1
#the loop below will loop 5 times

for i in range(0, num, 1):
    print(i)

#the loop below has a start value of 0, a stop value of 5 (the num variable) and a step value of 2 
#the loop below will loop 3 times
print("\n\n")

for i in range(0, num, 2):
    print(i)


#Start and step in the range function are optional 
#if the start value is not given, it defaults to 0 
#if the step value is not given it defaults to 1
print("\n\n")
for j in range(num):
    print(j)


print("\n\n")
for w in range(10, num, -2):
    print(w)
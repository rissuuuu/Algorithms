print("Using recursion..................\n")
def Fibonacci(n):
    if n==0:
        return 0;
    elif n==1:
        return 1;
    else:
        return(Fibonacci(n-1)+Fibonacci(n-2))
for i in range(10):
    print((Fibonacci(i)))


print("\nWithout recursion...........")

a=0;
b=1;
count=0
num=int(input("Enter the number to generate a sequence"))
print(a)
print(b)
while(count<num-2):
    count+=1
    c=a+b;
    a=b
    b=c
    print(c);

def coin(a,inpt):
        b=[]
        i=0
        sum=0
        length=len(a)
        while(sum!=inpt):
            if(sum>inpt):
                b.remove(a[i])
                sum=sum-a[i]
                i+=1
            else:
                if(i==length):
                    print("Solution not found")
                    break
                b.append(a[i])
                sum = sum + a[i]
        print(b,sum)


a=[2,5,10,20,50,100,500]
inpt=int(input("Enter the coin to exchange:"))
a.sort(reverse=True)
coin(a,inpt)
import matplotlib.pyplot as plt

def totient(num):
    cappi=1
    divisibleprimes=[]
    for i in range(2,num+1):
        f=0
        for j in range(2,(i//2)+1):
            if i%j==0:
                f=1
                break
        if f==0 and num%i==0:
            divisibleprimes.append(i)
            cappi*=1-(1/i)
    
    return int(num*cappi), divisibleprimes
    


'''
number=int(input("Enter the number:"))

tot,nums=totient(number)
print(f"Totient({number})={tot}")

totnums=[]
for i in range(1,number):
    f=0
    for j in nums:
        if i%j==0:
            f=1
    if f==0:
        totnums.append(i)
print(totnums)

#the below code is in comments as the value below is same as totient(n)/2

sumoftotvals=0
for i in totnums:
    sumoftotvals+=i 

quot=sumoftotvals/number
print(quot)

print(tot/2)
'''

x=[]
y=[]
for i in range(3,500):
    x.append(i)
    tot,nums=totient(i)
    y.append(int(tot))

print(y)
plt.plot(x,y,linestyle="-")
plt.xlabel("Numbers----->")
#plt.ylabel("Summation of xi's coprime values/xi")
plt.ylabel("Euler's Totient")
plt.title("Pattern of Euler's Phi")

plt.show()

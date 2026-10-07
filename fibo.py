
# fibo Series

# firstNum=0
# secNum=1
# n=int(input("Enter Travese Number : "))
# for i in range(n):
#     print(firstNum ,end=" ")
#     print(secNum , end=" ")
#     next=firstNum+secNum
#     print(next ,end=" ")
#     firstNum=secNum
#     secNum=firstNum+secNum


n=5
f=0
s=1
print(f,end=" ")
    # f=s
print(s,end=" ")
for i in range(n):
    next=s+f
    print(next ,end=" ")
    f=s
    s=next
    

 

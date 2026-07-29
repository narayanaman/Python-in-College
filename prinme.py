# write a program to find prime number between 1 to 100

for i in range(2,100):
    prime=True
for j in range(2,i):
    if i%j==0:
        prime=False
        break
if prime=True:
    
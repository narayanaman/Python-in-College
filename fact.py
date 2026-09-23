# write a program of factorial using user input and also in function
def factorial(n):
  fact=1
  for i in range(1,n+1):
    fact *= i
  return fact

n=int(input("Enter Number :"))
print(factorial(n))
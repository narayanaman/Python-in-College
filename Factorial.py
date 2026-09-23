def fact():
  n=int(input("Enter Number :"))
  fact=1
  i=1

  for i in range(1,n+1):
    fact *= i
    i+= 1
    print(fact)


fact(5)


    
  

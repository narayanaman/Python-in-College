

s="Hello"
print(s)
# rev=reversed(s)
rev=s[::-1] #reverse
print(rev)
rev=s[::1]
print(rev)

# for i in range (0 ,len(s)):
#     print(i)
#     print(s[i])
# print(rev)
    

if s==rev:
    print("This is Palidrom")
else:
    print("This is not Palidrom")

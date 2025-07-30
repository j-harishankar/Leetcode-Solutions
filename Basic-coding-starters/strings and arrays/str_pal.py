#Check if a string is a palindrome (ignore spaces, punctuation).
#solved using two pointer method
def is_pal(strin):
    strin = ''.join(c.lower() for c in strin if c.isalnum())
    left = 0
    right = len(strin) - 1
    for i in range(len(strin)):
        while left!=right:
            if strin[left] != strin[right]:
                 return 0
                 break
            left+=1
            right-=1
    return 1
strin = input("Enter string")
k = is_pal(strin)
if k:
    print("pal")
else:
    print("no pal")
def reverse(strin):
    l = []
    s = ""
    for i in strin:
        if i!=" ":
            s+=i
        else:
            if s:
                l.append(s)
                s = ""
    if s:
        l.append(s)
        s = ""
    rev_word = []
    for i in range(len(l)-1,-1,-1):
        rev_word.append(l[i])
    return " ".join(rev_word)
print(reverse("i am hari and i am from tvm"))
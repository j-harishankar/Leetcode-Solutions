# Replace sequences of the same character with that 
# character followed by the number of times it appears consecutively


# i used list because since strings are immutable it creates multiple copies each time += is done 
# use list and join ""
def compress(arr):
    if not arr:
        print("")
        return
    left = 0
    count = 1
    l = []
    for i in range(1,len(arr)):
        if arr[left] == arr[i]:
            count+=1
        else:
            l.append(arr[left]+str(count))
            left = i 
            count = 1 
    l.append(arr[left]+str(count))
    return ''.join(l)

    print(l)
arr = "aaabbcccc"
print(compress(arr))
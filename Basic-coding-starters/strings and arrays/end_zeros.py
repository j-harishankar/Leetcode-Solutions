#Move all zeros to the end of the array.

def move_zeroes(arr):
    left = 0
    for i in range(len(arr)):
        if arr[i]!=0:
            arr[i],arr[left] = arr[left],arr[i]
            left+=1
            
    print(arr)
n = int(input("enter the arr size"))
arr = [int(input("enter the arr")) for i in range(n) ]
move_zeroes(arr)
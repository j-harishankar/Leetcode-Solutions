 #Find the second largest element in an array.
def second_largest(arr):
    arr.sort()
    print(arr[-2])
n = int(input("enter the arr size"))
arr = [int(input("enter the arr")) for i in range(n) ]
second_largest(arr)
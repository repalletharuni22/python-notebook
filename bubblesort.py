def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0,n-1-i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
my_list = list(map(int,input("give an array").split()))
sorted_list = bubble_sort(my_list)
print("sorted array is", sorted_list)
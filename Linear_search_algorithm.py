def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

list_of_fruits = ['apple','banana','mango']
fruit="mango"

result = linear_search(list_of_fruits,fruit)
if result != -1:
    print(result)
else:
    print("Not found")

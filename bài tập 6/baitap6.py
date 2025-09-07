import time

with open("data.txt", "w") as f:
    data = [int(line.strip()) for line in f]

def linear_search(arr,k):
    for i in range(1,1000001):
        if arr[i] == k:
            return i in range(len(arr))
    return -1
def binary_search(arr,k):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == k:
            return mid
        elif arr[mid] < k:
            left = mid + 1
        else:
            right = mid - 1

k = 999999
start = time.time()
ketqua = linear_search(data,k)
end = time.time()
print(f"tìm kiếm tuần tự mất: {end - start} giây") 

start = time.time()
binary_search(data,k)
end = time.time()
print(f"tìm kiếm nhị phân mất: {end - start} giây")

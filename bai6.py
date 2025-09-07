def binary_search(arr,k):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == k:
            return mid
        elif arr[mid] < k:
            left = mid + 1
        else:
            right = mid - 1

arr = [1,2,3,4,5,6,7,8,9]
ketqua = binary_search(arr,1)

if ketqua != -1:
    print(f"đã tìm thấy phần tử ở vị trí {ketqua}")
else:
    print("không tìm thấy phần tử")
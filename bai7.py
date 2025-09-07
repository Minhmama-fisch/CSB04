# def selection_sort(data):
#     n = len(data)
#     for i in range(n):
#         min_idx = i
#         for j in range(i + 1,n):
#             if data[j] < data[min_idx]:
#                 min_idx = j
#         data[i], data[min_idx] = data[min_idx], data[i]
#     return data

# arr = [1,2,3,4,5,6,7,8,9]
# ketqua = selection_sort(arr)
# print("mảng sau khi sắp xếp:", ketqua)

def bubble_sort(data):
    n = len(data)
    for i in range(n - 1):
        swapped = False
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True
        if not swapped:
            break
    return data 

arr = [64, 34, 25, 12, 22, 11, 90]
ketqua = bubble_sort(arr)
print("Mảng sau khi sắp xếp:", ketqua)
        
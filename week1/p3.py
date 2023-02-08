# 2 repeating numbers
# Input: arr = [4, 2, 4, 5, 2, 3, 1], N = 5
# Output: 4 2

# sort and seek
arr = [4, 2, 4, 5, 2, 3, 1]
arr.sort()
for i in range(len(arr)-1):
    if (arr[i] == arr[i+1]):
        print(arr[i], end=' ')
# hash table

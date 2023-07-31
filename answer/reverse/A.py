str  = input()

arr_str = list(str)
arr_reverse_str = []
reverse_str = ""

print(arr_str)

for i in range(len(arr_str)):
    arr_reverse_str.append(arr_str[len(arr_str) - i - 1])
    
for i in range(len(arr_str)):
    reverse_str += arr_reverse_str[i]

print(str, reverse_str)
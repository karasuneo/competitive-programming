slice = []

num1 = input()

slice.append(num1)

num = input().split()

slice.append(num[0])
slice.append(num[1])

str = input()

slice_int = map(int, slice)

print(sum(slice_int), str)

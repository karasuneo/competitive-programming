num = input().split()

if int(num[0]) * int(num[1]) % 2 == 0:
    print("Even")
elif int(num[0]) * int(num[1]) % 2 == 1:
    print("Odd")
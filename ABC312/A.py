S = input()
ANS = ["ACE", "BDF", "CEG", "DFA", "EGB", "FAC", "GBD"]

for a in ANS:
    print
    if S == a:
        print("Yes")
        exit(0)

print("No")

num=int(input())

print("dividers:")
print("|")
print("|")
print("V")
print()


for i in range(1,num+1):
    if num%i==0:
        print(i)
    else:
        continue

input()
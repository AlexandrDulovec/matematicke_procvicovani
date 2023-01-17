num=int(input())

if num!=1:
    for i in range(2,num):
        z=num%i
        if z==0:
            print("NENÍ PRVOČÍSLO")
            break

    if z!=0:
        print("JE PRVOČÍSLO")


if num==1:
    print("NENÍ PRVOČÍSLO")
input()
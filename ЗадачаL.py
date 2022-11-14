q = input()
count=0
m = False
for i in range(int(q)):
    nums = int(input())
    list = input().split(" ")
    for i2 in range(nums):
        if i2 != nums-1:
            if list[i2] > list[i2+1]:
                m = True
            elif m:
                count+=1
                m=False
        elif i2==nums-1 and list[len(list)-2]>list[len(list)-1]:
            count+=1
            print(count)
        else:
            print(count)
    m=False
    count=0
print("Кінець циклу")
            
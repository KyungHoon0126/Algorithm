# 방법 1
n = int(input())

try:
    print(list(map(int, input().split()))[0:n].index(int(input())) + 1)
except:
    print(-1)


# 방법 2
cnt = int(input())
data = list(map(int, input().split()))[0:cnt]
target = int(input())

left = 0
right = len(data) - 1
flag = True

while left <= right:
    flag = False
    mid = (left + right) // 2
    if data[mid] == target:
        print(mid + 1)
        flag = True
        break
    elif data[mid] > target:
        right = mid - 1
    else:
        left = mid + 1

if flag == False:
    print(-1)

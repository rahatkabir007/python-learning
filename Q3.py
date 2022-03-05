# import sys
#
# number = 3456
# count = 0
#
# for _ in iter(int, 1):
#     number//=10
#     count+=1
#     if number == 0:
#         break
#
# print(str(count))


num = int(input())
count = 0

while num > 0:
    num //= 10
    count += 1

print(count)


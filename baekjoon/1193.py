n = int(input())

num = 0
num_cnt = 0

while num_cnt < n:
    num += 1
    num_cnt += num
num_cnt -= num

if num % 2 == 0:
    i = n - num_cnt
    j = num - i + 1
else:
    i = num - (n - num_cnt) + 1
    j = n - num_cnt

print(f"{i}/{j}")

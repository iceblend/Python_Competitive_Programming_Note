n = int(input())

cnt = 1
cnt_six = 6
room_count = 1

while n > cnt:
    room_count += 1
    cnt += cnt_six
    cnt_six += 6
print(room_count)
import math
from collections import defaultdict

def calcTime(time_in, time_out):
    in_h, in_m = map(int, time_in.split(':'))
    out_h, out_m = map(int, time_out.split(':'))

    total_h = out_h - in_h
    total_m = out_m - in_m
    total_time = total_h * 60 + total_m
    return total_time


def calcFee(fees, total_time):
    base_time = fees[0]
    base_fee = fees[1]
    clock_time = fees[2]
    clock_fee = fees[3]
    resFee = 0

    total_time -= base_time
    resFee += base_fee

    if total_time > 0:
        tmp = math.ceil(total_time / clock_time)
        resFee += tmp * clock_fee

    return resFee



def solution(fees, records):
    cars = {}
    cars_count = defaultdict(int)

    for record in records:
        time, num, status = record.split()

        if status == "IN":
            cars[num] = time
        else:
            time_in = cars.pop(num)
            time_out = time
            total_time = calcTime(time_in, time_out)
            cars_count[num] += total_time

    for k in cars.keys():
        time_in = cars[k]
        time_out = '23:59'
        total_time = calcTime(time_in, time_out)
        cars_count[k] += total_time

    list_of_dictA = sorted(cars_count.items())
    cars_count = dict(list_of_dictA)

    answer = []
    for k in cars_count.keys():
        t = cars_count[k]
        total_fee = calcFee(fees, int(t))
        answer.append(total_fee)
    return answer


print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))

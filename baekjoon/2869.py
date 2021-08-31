# 달팽이는 올라가고 싶다
import math

a, b, v = map(int, input().split())
x = math.ceil((v - b) / (a - b))
print(x)
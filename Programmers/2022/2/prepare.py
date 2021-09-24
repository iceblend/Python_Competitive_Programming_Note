# Reference
# https://coding-grandpa.tistory.com/entry/Python%EC%9C%BC%EB%A1%9C-JSON-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EC%9D%BD%EA%B8%B0-%EC%8B%A4%EC%A0%84%ED%8E%B8
# https://programmers.co.kr/skill_check_assignments/67

import json # 파이썬 내부의 JSON Module

with open("json_example.json", "r", encoding="utf8") as f:
    contents = f.read() # string 타입
    json_data = json.loads(contents) #json_data는 dict 타입임

print(json_data) # 전체 JSON을 dict type으로 가져옴
print()
print(json_data["employees"]) # Employee 정보를 조회
print()
print(json_data["employees"][0]["firstName"]) # 첫 Employee의 이름을 출력 -> John


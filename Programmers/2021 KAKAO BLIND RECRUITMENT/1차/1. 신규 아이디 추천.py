def solution(new_id):

    # 1단계 : 대문자를 소문자로 치환
    new_id = new_id.lower()

    # 2단계 : 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거
    for c in new_id:
        if c.isalpha() or c == '-' or c == '_' or c == '.' or c.isdigit():
            continue
        else:
            new_id = new_id.replace(c, '')

    # 3단계 : 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환
    while '..' in new_id:
        new_id = new_id.replace('..', '.')

    # 4단계 : 마침표(.)가 처음이나 끝에 위치한다면 제거
    if new_id[0] == '.' and len(new_id) > 1:
        new_id = new_id[1:]
    if new_id[-1] == '.':
        new_id = new_id[:-1]

    # 5단계 : new_id가 빈 문자열이라면, new_id에 "a"를 대입
    if len(new_id) == 0:
        new_id += 'a'

    # 6단계 : 길이 맞추기 1
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]

    # 7단계 : 길이 맞추기 2
    if len(new_id) <= 3:
        new_id += new_id[-1] * (3 - len(new_id))

    return new_id


print(solution("...!@BaT#*..y.abcdefghijklm"))

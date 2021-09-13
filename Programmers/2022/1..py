def solution(id_list, report, k):
    user = {}
    userReport = [[] for _ in range(len(id_list))]
    reportScore = [0] * len(id_list)
    suspendScore = [0] * len(id_list)
    for i in range(len(id_list)):
        user[id_list[i]] = i


    for s in report:
        reportInfo = s.split()

        s_userIdx = user[reportInfo[0]]
        r_userIdx = user[reportInfo[1]]

        if r_userIdx not in userReport[s_userIdx]:
            userReport[s_userIdx].append(r_userIdx)
            reportScore[r_userIdx] += 1


    for i in range(len(reportScore)):
        if reportScore[i] >= k:
            for j in range(len(userReport)):
                if i in userReport[j]:
                    suspendScore[j] += 1

    return suspendScore
def solution(progresses, speeds):
    answer = []
    tmp = []

    for i in range(len(progresses)):
        ts = (100 - progresses[i])
        k = int(ts / speeds[i])
        if (ts / speeds[i]) > k:
            tmp.append(k+1)
        else:
            tmp.append(k)
    count = 1
    max_day = tmp[0]
    for s in range(1, len(tmp)):
        if tmp[s] <= max_day:
            count+=1
        else:
            answer.append(count)
            count=1
            max_day = tmp[s]
    answer.append(count)
    return answer
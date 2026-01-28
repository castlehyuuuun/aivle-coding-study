def solution(a, b):
    answer = 0
    ab = int(str(a) + str(b))
    ba = int(str(b) + str(a))
    
    if ab > ba:
        print(ab)
        answer += ab
    else:
        print(ba)
        answer += ba
    return answer
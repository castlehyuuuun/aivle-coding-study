from collections import deque
def solution(board, moves):
    answer = 0
    cols = [list(col) for col in zip(*board)]
    basket = []
    
    for m in moves:
        col = cols[m-1]
        for t in range(len(col)):
            if col[t] != 0:
                doll = col[t]
                col[t] = 0
                
                if basket and basket[-1] == doll:
                    basket.pop()
                    answer += 2
                else:
                    basket.append(doll)
                break
    
    return answer
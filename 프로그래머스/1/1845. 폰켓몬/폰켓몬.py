def solution(nums):
    answer = []
    nums.sort()

    for i in range(len(nums)):
        if nums[i] not in answer:
            answer.append(nums[i])
            if len(answer) == len(nums)//2:
                break
    return len(answer)
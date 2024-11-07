# https://school.programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    k = len(nums) // 2

    set_nums = set(nums)
    if len(set_nums) >= k:
        return k
    else:
        return len(set_nums)

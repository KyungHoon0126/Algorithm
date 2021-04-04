def solution(nums):
    cnt = len(nums) // 2
    pocketmons = list(set(nums))
    if len(pocketmons) < cnt:
      return len(pocketmons)
    return cnt

solution([3,3,3,2,2,2])
def max_independent_set(nums):
    n = len(nums)
    if n == 0:
        return []

    cache = [0] * (n + 1)
    cache[0] = 0
    cache[1] = max(nums[0], 0)
    for i in range(2, n + 1):
        cache[i] = max(cache[i - 1], cache[i - 2] + nums[i - 1])

    if all(num < 0 for num in nums):
        return []

    solution = []
    i = n
    while i >= 1:
        if cache[i] == cache[i - 1]:
            i -= 1
        else:
            solution.append(nums[i - 1])
            i -= 2

    return list(reversed(solution))

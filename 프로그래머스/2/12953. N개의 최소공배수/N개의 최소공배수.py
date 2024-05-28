def solution(arr):
    a = arr[0]
    lcm = arr[0]

    for num in range(1, len(arr)):
        b = arr[num]
        while b > 0:
            a, b = b, a % b
        lcm = (lcm * arr[num]) // a
        a = lcm

    return lcm
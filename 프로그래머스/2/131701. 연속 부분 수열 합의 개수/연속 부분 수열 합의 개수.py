def solution(elements):
    n = len(elements)
    sum_list = set()

    for i in range(n):
        temp = elements[i]
        sum_list.add(temp)
        for j in range(i + 1, i + n):
            temp += elements[j % n]
            sum_list.add(temp)

    return len(sum_list)


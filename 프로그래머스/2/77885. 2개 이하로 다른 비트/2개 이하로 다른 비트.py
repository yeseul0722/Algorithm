def solution(numbers):
    answer = []
    
    for n in numbers:
        bin_num = '0' + bin(n)[2:]
        idx = bin_num.rfind('0')
        bin_lst = list(bin_num)
        bin_lst[idx] = '1'
        
        if n % 2 == 1:
            bin_lst[idx + 1] = '0'
        
        answer.append(int(''.join(bin_lst), 2))
        
    return answer
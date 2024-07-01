def solution(phone_book):
    answer = True
    phone_book.sort()
    
    for num in range(len(phone_book) - 1):
        if phone_book[num] in phone_book[num + 1] and phone_book[num + 1].index(phone_book[num]) == 0:
            answer = False
            break
        
    return answer
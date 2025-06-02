from itertools import combinations

expr = list(input())
indices = []
stk = []
answers = set()

for i in range(len(expr)):
    if expr[i] == '(':
        stk.append(i)
    elif expr[i] == ')':
        indices.append((stk.pop(), i))

for i in range(len(indices)):
    for comb in combinations(indices, i+1):
        temp = expr[:]
        for idx in comb:
            temp[idx[0]] = temp[idx[1]] = ""
        answers.add("".join(temp))      

for item in sorted(list(answers)):
    print(item)
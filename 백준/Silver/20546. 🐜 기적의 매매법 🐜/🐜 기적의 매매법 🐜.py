import sys
input = sys.stdin.readline


def bnp(seed):
    stock = 0
    for i in stocks:
        if seed >= i:
            stock += seed // i
            seed %= i

    return stocks[-1] * stock + seed


def timing(seed):
    stock = 0
    for i in range(3, n):
        if stocks[i - 3] < stocks[i - 2] < stocks[i - 1] < stocks[i]:
            if stock:
                seed += stock * stocks[i]
                stock = 0
            continue
        if stocks[i - 3] > stocks[i - 2] > stocks[i - 1] > stocks[i]:
            if seed >= stocks[i]:
                stock += seed // stocks[i]
                seed %= stocks[i]

    return stock * stocks[-1] + seed


seed = int(input())
stocks = list(map(int, input().split()))
n = len(stocks)

bnp = bnp(seed)
timing = timing(seed)

if bnp > timing:
    print('BNP')
elif timing > bnp:
    print('TIMING')
else:
    print('SAMESAME')
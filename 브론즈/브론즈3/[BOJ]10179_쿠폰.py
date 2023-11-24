N = int(input())
for i in range(N):
    price = float(input())
    print(f'${round(price * 0.8, 2):.2f}')
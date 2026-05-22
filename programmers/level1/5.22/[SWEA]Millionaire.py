T = int(input())
for t in range(T):
    day = int(input())
    prices = list(map(int,input().split()))

    max_price = 0
    total = 0

    for price in reversed(prices):
        if price> max_price:
            max_price = price
    
        else:
            total += max_price - price

    print(f"#{t+1} {total}")d
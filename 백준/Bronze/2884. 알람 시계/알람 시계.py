[H, M] = list(map(int, input().split()))

D = H * 60 + M

D -= 45

if D < 0:
    D += 24 * 60

print(f"{D // 60} {D % 60}")
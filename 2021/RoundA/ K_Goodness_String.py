t = int(input())

def solve(test_case):
    n,k = list(map(int,input().split()))
    word = input()
    goodness = 0
    if n%2 == 0:
        left = word[n//2:]
    else:
        left = word[n//2+1:]
    right = word[:n//2]

    for i in range(n//2):
        if right[i] != left[ n//2 -i -1 ]:
            goodness += 1
    print(f"Case #{test_case}: {abs(goodness-k)}")

for val in range(1,t+1):
    solve(val)
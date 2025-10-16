N = int(input())
for _ in range(N):
    a, b = input().split()
    rev_a = int(str(a)[::-1])
    rev_b = int(str(b)[::-1])
    s = rev_a + rev_b
    rev_s = int(str(s)[::-1])
    print(rev_s)  
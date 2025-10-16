N = int(input())
for _ in range(N):
    a_str, b_str = input().split()
    a = int(a_str)
    b = int(b_str)
    last_digit = pow(a, b, 10)  
    print(last_digit)

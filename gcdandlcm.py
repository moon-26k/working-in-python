T = int(input())
for _ in range(T):
    line = input()
    parts = line.split()  
    X = int(parts[0])
    Y = int(parts[1])
    a = X
    b = Y
    while b != 0:
        temp = b
        b = a % b
        a = temp
    gcd = a
    lcm = (X * Y) // gcd
    print(gcd, lcm)

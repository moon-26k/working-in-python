N = int(input())
for i in range(N):
    num = 1  
    line = ""  
    for j in range(i + 1):
        line = line + str(num) + " " 
        num = num * (i - j) // (j + 1)
    print(line)

N = int(input())
for i in range(1, N + 1):  
    line = ""  
    for j in range(i):
        line = line + "#"
    print(line)

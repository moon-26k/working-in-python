N = int(input())
stones = N
round_number = 1  
while True:
    if stones <= round_number:
        print("Ramesh")
        break
    stones = stones - round_number  
    suresh_stones = round_number * 2
    if stones <= suresh_stones:
        print("Suresh")
        break
    stones = stones - suresh_stones  
    round_number = round_number + 1

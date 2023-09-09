def maxPresentations(sT, sE):
    #[1, 1, 2, 3]
    #[2, 3, 3, 4]
    
    #1) brute force each possible
    next_available = float('infinity')
    attendable = 0
    for i in range(len(sT)):
        start_time = sT[i]
        end_time = sE[i]
        
        if start_time < next_available:
            attendable += 1
            next_available = end_time
    return attendable

print(maxPresentations([6,1,2,3],[8,9,4,7]))
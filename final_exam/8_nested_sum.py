def nested_sum(l):
    t = 0
    for n in l:
        if isinstance(n, list):
            n = nested_sum(n)
        
        t += n
    
    return t

print(nested_sum([4, 3, [2, 5, [1, 6]]]))
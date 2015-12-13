
def problema_de_josephus(n, m):
    i = 1
    count = 0
    while i <= n:
        i += m + 2
        count += 1
    print(count)
    return count

problema_de_josephus(50, 3)
    
    

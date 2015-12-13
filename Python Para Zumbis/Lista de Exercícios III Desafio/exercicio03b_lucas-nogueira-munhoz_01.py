n = int(input('N: '))
result = 0
i = 0

while result < n:
    result = i * ( i + 1 ) * ( i + 2 )
    i += 1
if result == n:
    print("%d eh Triangular!" %n)
else:
    print("%d nao eh Triangular!" %n)
        

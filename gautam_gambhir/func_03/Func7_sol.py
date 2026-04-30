def factoriyal(n):
    if n == 0:
        return 1
    else:
        return n * factoriyal(n-1)
    

print(factoriyal(5))

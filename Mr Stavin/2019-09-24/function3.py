# #fibonacci sequence using cache
def fibonacci1(n, _cache={}):
    if n in _cache:
        return _cache[n]
    elif n > 1:
        return _cache.setdefault(n, fibonacci1(n-1) + fibonacci1(n-2))
    return n

# factorial sequence using cache
def factorial1(n, _cache={}):
    if n in _cache:
        return _cache[n]
    elif n > 1:
        return _cache.setdefault(n, n*factorial1(n-1))
    return n


#fibonacci sequence using iteration
def fibonacci2(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

# factorial sequence using iteration
def factorial2(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num

print(factorial1(500) == factorial2(500))

print(fibonacci1(500) == fibonacci2(500))

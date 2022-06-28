def seed_serie(n, k):
    if n <= 0 or k <= 0:
        return None
    if n == 1:
        return 1
    return n * seed_serie(n-k, k)

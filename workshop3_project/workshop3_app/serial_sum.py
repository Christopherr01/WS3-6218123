def serial_sum(n, m=None):
    if m is None:
        return sum(range(1, n + 1))
    else:
        return sum(range(n, m + 1))

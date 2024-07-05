def zigzag(a, b, c):
    if a < b and b > c:
        return True
    elif a > b and b < c:
        return True
    else:
        return False

def fract(n):
    if n < 1:
        return 0
    return n + fract(n-1)



if __name__ == '__main__':
    print(fract(4))
def staircase(n):
    for i in range(n):
        print((n-1-i)*' ', end="")
        print((i+1)*'#')


if __name__ == '__main__':
    num = 5

    staircase(num)

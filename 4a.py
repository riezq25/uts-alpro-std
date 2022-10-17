def printDownwardTriangle(n):
    for i in range(n, 0, -1):
        print(i * "X")


def rightChevron():
    for i in range(4):
        for j in range(4):
            if i == j:
                for k in range(9):
                    print('z', end='')
            else:
                print(" ", end="")
        print()
    for i in range(4):
        for j in range(4):
            if i + j == 3:
                for k in range(9):
                    print('z', end='')
            else:
                print(" ", end="")
        print()

if __name__ == '__main__':
    print('Fungsi M1:')
    printDownwardTriangle(8)
    print('\nFungsi M2:')
    rightChevron()

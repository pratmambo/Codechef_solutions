for i in range(int(input())):
    bit = 1
    nibble = 0
    byte = 0
    n = int(input())
    while True:
        n -= 2
        if n > 0:
            nibble = bit
            bit = 0
        else:
            break
        n -= 8
        if n > 0:
            byte = nibble
            nibble = 0
        else:
            break
        n -= 16
        if n > 0:
            bit = byte * 2
            byte = 0
        else:
            break
    print(bit, end=' ')
    print(nibble, end=' ')
    print(byte)

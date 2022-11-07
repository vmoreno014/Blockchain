import hashlib, itertools

def main():
    MSG_LEN = 12
    START = ord('a')
    FINAL = ord('z')

    assert isinstance(MSG_LEN, int) and MSG_LEN > 0
    assert isinstance(START, int) and isinstance(FINAL, int)
    assert 0 <= START < FINAL < 256

    message = bytearray([START] * MSG_LEN)
    lowesthash = None

    for trials in itertools.count():
        hash = hashlib.sha256(message).hexdigest()
        if lowesthash is None or hash < lowesthash:
            lowesthash = hash
            print(f'Trial #{trials}: sha512({message.decode()}) = {hash[ : 50]}...')

        i = MSG_LEN - 1
        while i >= 0 and message[i] == FINAL:
            message[i] = START
            i -= 1
        if i < 0:
            break
        message[i] += 1

    print(f'Lowest hash: {lowesthash}')

if __name__ == '__main__':
    main()
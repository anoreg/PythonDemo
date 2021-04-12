alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def _encrypt(msg: str, shift: int) -> str:
    # HINT: How do you get the index of an item in a list:
    # https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list
    # 🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛
    cipher: str = ''
    for cr in msg:
        index: int = alphabet.index(cr) + shift
        cipher += alphabet[_get_encrypt_index(index)]
    print(f"The encoded text is {cipher}")
    return cipher


def _decrypt(msg: str, shift: int) -> str:
    plain: str = ""
    for cr in msg:
        index: int = alphabet.index(cr) - shift
        plain += alphabet[_get_decrypt_index(index)]
    print(f"The decoded text is {plain}")
    return plain


global recursion
recursion: int = 0


def _get_encrypt_index(index: int) -> int:
    global recursion
    recursion += 1
    diff: int = (len(alphabet) - 1) - index  # index is zero based
    return index if diff >= 0 else _get_encrypt_index(abs(diff) - 1)


def _get_decrypt_index(index: int) -> int:
    return index if index >= 0 else _get_decrypt_index(len(alphabet) + index)


def caesar(text: str, shift: int, direct: str) -> str:
    result: str = ""
    shift = shift % len(alphabet)
    print(f'shift {shift}')
    if direct == "decode":
        shift *= -1
    for letter in text:
        if letter in alphabet:
            index = alphabet.index(letter.strip())
            new_index = index + shift
            result += alphabet[_get_caesar_index(new_index, direct)]
        else:
            result += letter
    global recursion
    print(f'recur {recursion}')
    recursion = 0
    print(f'The {direct} text is {result}')
    return result


def _get_caesar_index(index: int, direct: str) -> int:
    return _get_encrypt_index(index) if direct == 'encode' else _get_decrypt_index(index)


caesar(text=text, shift=shift, direct=direction)

import random
alphabet = " АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"  
alphabet_map = {char: idx for idx, char in enumerate(alphabet)}
reverse_map = {idx: char for idx, char in enumerate(alphabet)}

def caesar_encrypt(text, shift=2):
    encrypted_text = ""
    for char in text.upper():
        if char in alphabet_map:
            original_index = alphabet_map[char]
            new_index = (original_index + shift) % len(alphabet)
            encrypted_text += reverse_map[new_index]
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(text, shift=2):
    decrypted_text = ""
    for char in text.upper():
        if char in alphabet_map:
            encrypted_index = alphabet_map[char]
            original_index = (encrypted_index - shift) % len(alphabet)
            decrypted_text += reverse_map[original_index]
        else:
            decrypted_text += char
    return decrypted_text


original_text = input("Введите текст для шифрования: ")
shift = int(input("Введите сдвиг: ") or 2)

encrypted_text = caesar_encrypt(original_text, shift)
decrypted_text = caesar_decrypt(encrypted_text, shift)

print("Оригинальный текст:", original_text)
print("Зашифрованный текст:", encrypted_text)
print("Дешифрованный текст:", decrypted_text)

def shuffle_blocks(text, block_size, iterations=1):
    blocks = [text[i:i+block_size] for i in range(0, len(text), block_size)]
    for _ in range(iterations):
        random.shuffle(blocks)
    return ''.join(blocks)


text = input("Введите текст для шифрования блоками: ")
block_size = int(input("Введите размер блока: "))
iterations = int(input("Введите количество итераций перемешивания: "))

shuffled_text = shuffle_blocks(text, block_size, iterations)
print("Зашифрованный текст блоками:", shuffled_text)

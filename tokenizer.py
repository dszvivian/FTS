



# Character Level Encoder
def encode(text):
    return [ord(char) for char in text]

def decode(encoded_array:list):
    return ''.join(chr(index) for index in encoded_array)

if __name__ == "__main__":
    print(decode(encode("HEllo World")))
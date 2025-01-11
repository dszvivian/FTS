









# Character Level Encoder/decoder
def encode(text):
    return [ord(char) for char in text]

def decode(encoded_array:list):
    return ''.join(chr(index) for index in encoded_array)

def encode(text,unicode_format):
    return list(text.encode(unicode_format))

if __name__ == "__main__":
    text = "Hello World"
    print(f"utf-8 = {(encode(text,'utf-8'))}")
    print(f"utf-16 = {(encode(text,'utf-16'))}")
    print(f"utf-32 = {(encode(text,'utf-32'))}")
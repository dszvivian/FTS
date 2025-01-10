

class Character_Level_Tokenizer:
    # TODO: Add many more cases other than alphabets
    def __init__(self):
        chars = [ chr(i) for i in range(ord('a'),ord('z')+1) ]
        self.chars = sorted(chars)
        self.charstoindex = {char:index for index,char in enumerate(chars)}
        self.indextochar = {index:char for index,char in enumerate(chars)}

    def encode(self,text):
        return [self.charstoindex.get(char,"?") for char in text.lower()]
    
    def decode(self,encoded_array:list):
        return ''.join(self.indextochar.get(index,"?") for index in encoded_array)

if __name__ == "__main__":
    cle = Character_Level_Tokenizer()
    print(cle.decode(cle.encode("Hello WOrld")))
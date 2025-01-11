

class BPE:

    def __init__(self,training_text:str):
        self.training_text = training_text
        self.utf8_encoded =  list(training_text.encode('utf-8'))

        self.common_pairs = self.find_common_pairs()

    def find_common_pairs(self):
        pairs = {}
        for b1,b2 in zip(self.utf8_encoded,self.utf8_encoded[1:]):
            if (b1,b2) in pairs:
                pairs[(b1,b2)] += 1
            else:
                pairs[(b1,b2)] = 1
        return sorted(pairs.items(),key=lambda item:item[1],reverse=True)
    
    def merge(self,pair,value):
        pass



    def encode(self,text):
        return 

    def decode(self,encoded_array:list[int]):
        pass





# Character Level Encoder/decoder
def encode(text):
    return [ord(char) for char in text]

def decode(encoded_array:list):
    return ''.join(chr(index) for index in encoded_array)

def encode(text,unicode_format):
    return list(text.encode(unicode_format))

if __name__ == "__main__":
    bpe = BPE("Helllo Worldo ")

    print(bpe.find_common_pairs())
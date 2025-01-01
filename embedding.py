from DatasetLoader import DatasetLoader


class Embedding:

    def __init__(self,dataset:DatasetLoader):
        print('abcd')
        self.documents =  dataset.documents 

        self.words = set( word for document in self.documents for word in document['content'].split())
        self.words = {index:word for index,word in enumerate(self.words)}

        self.chunks =  self.split_documents_calculate_tfidf()


    def tfidf(document):
        pass      

    def tf(self,document):
        tf = [0 for _ in range(len(self.words))]
        
        total_words_in_document = len(document)

        for index in range(len(self.words)):
            word = self.words[index]            
            occurrences = find_occurrences(word,document)
            tf[index] = occurrences / total_words_in_document

        return tf
            

    def idf(document):
        pass


    def split_documents_calculate_tfidf(self):
        chunks = {}

        for document in self.documents:

            chunks[document['file_path']] = {}
            
            lines = document['content'].split('\n')

            for line_number,content in enumerate(lines):
                chunks[document['file_path']][line_number] = content

        return chunks



# todo: create & move to a suitable util file
# todo: Implemented Brute Forced Method --> Optimize it
def find_occurrences(word:str, document:list[str]):
    counter = 0 
    for element in document:
        if element == word:
            counter += 1
    return counter

    


if __name__ == "__main__":

    embedding = Embedding(dataset=DatasetLoader("../personal_notes"))
    print(embedding.chunks)
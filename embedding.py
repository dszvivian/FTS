from math import log

from DatasetLoader import DatasetLoader


class Embedding:

    def __init__(self,dataset:DatasetLoader):
        self.documents =  dataset.documents 

        self.words = set( word for document in self.documents for word in document['content'].split())
        self.words = {index:word for index,word in enumerate(self.words)}

        self.idf = self.calculate_idf()
        self.chunks =  self.split_documents_calculate_tfidf()


    def calculate_tfidf(self,document):
        tf = self.calculate_tf(document)
        return multiply_arrays(tf, self.idf)      

    def calculate_tf(self,document):
        tf = [0 for _ in range(len(self.words))]

        total_words_in_document = len(document)

        for index in range(len(self.words)):
            word = self.words[index]            
            occurrences = find_occurrences(word,document)
            tf[index] = occurrences / total_words_in_document

        return tf
            

    def calculate_idf(self):
        idf = [0 for _ in range(len(self.words))]

        for index in range(len(self.words)):
            total_documents =  len(self.documents)
            number_of_document_term_has_occured = 0

            for document in self.documents:
                if self.words[index] in document['content']:
                    number_of_document_term_has_occured += 1

            idf[index] = log(total_documents / number_of_document_term_has_occured)            
        return idf

    def split_documents_calculate_tfidf(self):
        chunks = {}

        for document in self.documents:
            chunks[document['file_path']] = {}            
            lines = document['content'].split('\n')

            for line_number,content in enumerate(lines):
                document_words = content.split(" ")
                tfidf = self.calculate_tfidf(document_words)
                chunks[document['file_path']][line_number] = {'content': content,'tfidf': tfidf }

        return chunks



#TODO: create & move to a suitable util file
#TODO: Implemented Brute Forced Method --> Optimize it
def find_occurrences(word:str, document:list[str]):
    counter = 0 
    for element in document:
        if element == word:
            counter += 1
    return counter


def multiply_arrays(arr1,arr2):
    for index in range(len(arr1)):
        arr1[index] *= arr2[index]
    return arr1

if __name__ == "__main__":
    embedding = Embedding(dataset=DatasetLoader("../personal_notes"))
    print(embedding.chunks)
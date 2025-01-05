import time
from math import sqrt,cos

from DatasetLoader import DatasetLoader
from embedding import Embedding
from utils.timelogger import time_logger

class Search(Embedding):

    def __init__(self,query,dataset:DatasetLoader):
        self.query = query
        super().__init__(dataset)
        
        self.query_tfidf = self.calculate_tfidf(self.query)

    @time_logger
    def brute_force(self):
        
        start_time = time.perf_counter()

        for document in self.dataset.documents:
            if self.query in document["content"]:
                print(f"found in {document['file_path']}")

        print(time.perf_counter() - start_time)

    # TODO: give good variable names which are less confusing
    def top_k_results(self):

        file_name = ""
        line_number = -1
        similiarity = 0

        for file in self.chunks:
            for document_index in self.chunks[file]:
                document_similiarity = cosine_similiarity(self.query_tfidf,self.chunks[file][document_index]['tfidf'])

                if document_similiarity >= similiarity:
                    file_name = file
                    line_number = document_index
                    similiarity = document_similiarity

        return (file_name,similiarity,line_number)

                


# TODO: Move these functions into util 

def cosine_similiarity(vec1:list,vec2:list):

    if ((magnitude_of_vector(vec1)*magnitude_of_vector(vec2)) == 0):
        return 0 

    return  dot_product(vec1,vec2) / (magnitude_of_vector(vec1)*magnitude_of_vector(vec2))


def multiply_arrays(arr1,arr2):
    result = []
    for index in range(len(arr1)):
        result.append(arr1[index] * arr2[index])
    return result

def dot_product(vec1:list,vec2:list):
    return sum(multiply_arrays(vec1,vec2))

def magnitude_of_vector(vec:list):
    return sqrt(sum(multiply_arrays(vec,vec)))
    


if __name__ == "__main__":
    search = Search("""https://github.com/elsamuko/Shirt-without-Stripes """.split(" "), DatasetLoader('../personal_notes'))

    (file_name,similiarity,document_index) = search.top_k_results()

    print(f"file_name={file_name} line_number={document_index} similiarity={similiarity}")
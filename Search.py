import time

from DatasetLoader import DatasetLoader
from utils.timelogger import time_logger

class Search:

    def __init__(self,query,dataset:DatasetLoader):
        self.query = query
        self.documents =  dataset.documents 

        self.words = set( word for document in self.documents for word in document['content'].split()) # finding unique words from the corpus
        self.words = {index:word for index,word in enumerate(self.words)}  # assign unique number to each index

    @time_logger
    def brute_force(self):
        
        start_time = time.perf_counter()

        for document in self.dataset.documents:
            if self.query in document["content"]:
                print(f"found in {document['file_path']}")

        print(time.perf_counter() - start_time)


if __name__ == "__main__":
    print(Search("Synthetic ",dataset=DatasetLoader("../personal_notes")).words)
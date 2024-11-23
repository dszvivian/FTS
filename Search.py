import time

from DatasetLoader import DatasetLoader
from utils.timelogger import time_logger

class Search:

    def __init__(self,query,dataset:DatasetLoader):
        self.query = query
        self.dataset =  dataset        

    @time_logger
    def brute_force(self):
        
        start_time = time.perf_counter()

        for document in self.dataset.documents:
            if self.query in document["content"]:
                print(f"found in {document['file_path']}")

        print(time.perf_counter() - start_time)


if __name__ == "__main__":
    Search("Synthetic ",dataset=DatasetLoader("../personal _notes")).brute_force()
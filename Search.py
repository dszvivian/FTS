import time

from DatasetLoader import DatasetLoader
from embedding import Embedding
from utils.timelogger import time_logger

class Search(Embedding):

    def __init__(self,query,dataset:DatasetLoader):
        self.query = query
        super().__init__(dataset)
        self.query_tfidf = self.calculate_tfidf(self.query)


    def cosine_similiarity(self):
        pass

    @time_logger
    def brute_force(self):
        
        start_time = time.perf_counter()

        for document in self.dataset.documents:
            if self.query in document["content"]:
                print(f"found in {document['file_path']}")

        print(time.perf_counter() - start_time)


if __name__ == "__main__":
    print(Search("Synthetic ",dataset=DatasetLoader("../personal_notes")).chunks)
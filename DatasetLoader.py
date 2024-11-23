import os 


class DatasetLoader:

    def __init__(self,path):
        self.path = path

        self.documents = []
        self.load_documents()

        print(self.documents)

    
    def load_documents(self):
        if os.path.isfile(self.path):
            self.documents.append(self.extract_contents_from_file(self.path))
        else:
            for filename in os.listdir(self.path):
                file_path = os.path.join(self.path, filename)

                if os.path.isfile(file_path):
                    self.documents.append(self.extract_contents_from_file(file_path))

    @staticmethod
    def extract_contents_from_file(file_path):
        contents = {}
        with open(file_path,"r",encoding="utf-8") as file:
            content = file.read()
            contents['file_path'] = file_path
            contents["content"] = content
            return contents


if __name__ == "__main__":
    
    documents = DatasetLoader(path="..\personal _notes")



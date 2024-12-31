def textpreprocessing_pipeline(text:str):
    return toLower(text)

def toLower(text:str):
    return text.lower()

def remove_stop_words(text:str):
    NotImplementedError("Stop Words Yet to be Removed") #TODO:implement nltk stopword removal

def stemmer(text:str):
    NotImplementedError("Stemmer Yet to be Implemented") #TODO:implement nltk stemmer
# Full Text Search Engine

- [ ] First Work on Correctness of Result
- [ ] Make Search Fast
- [ ] Make Sure to take a Very large Dataset, Before Implementing the Algorithms  
So that You the Get the importance of these Algorithms(ie: Wikipidea dataset)
- [ ] Do Proper DataPreprocessing


## RoadMap

- [x] Loading all the Documents(ie: In a Efficient way)
- [x] Buid a Time Recording Method to Record the Timing it took to find that word
- [x] Try Brute Force method(Looping through all the documents and searching for that word)
- [x] Use Regex to Faster Search
- [x] Build a Index for quick calculations
    - [x] Building a Tokenizer(ie: Assignes a value For Each Word)
    - [ ] Adding additional Filters
        - [x] converting the text to Lowercase
        - [ ] Dropping common words in a sentence(ie: Maybe)
        - [ ] Stemming(ie: Running -> run)
- [x] Using the Same Tokenizer for the input Query


Diffrent Ways to Tokenize:

- [x] TF-IDF from Scratch



# Occurences where i wrote Brute Force Code:

in Embeddings.py Optimize these Functions

- [ ] Util Functions:
    - [ ] Find Occurences 
    - [ ]  Multiplying Two Arrays
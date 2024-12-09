- [ ] find unique words
- [ ] Give a Unique Number to each word(ie: Use a Set) ( ie: Creating a Corpus)
    - [ ] Easiest Way: for loop Enumerate and assign default index
- [ ] Using TF-IDF method:
    - [ ] Calculate Term Frequency for that specific chunk of words against the Whole Corpus.
    - [ ] Calculate Inverse Document Filtering against the whole corpus
    - [ ] Calculate TF-IDF
    - [ ] Convert query to vector form against the Corpus
    - [ ] Find Cosine Similiarity for all the Documents against the query,  
    and return top K documents with highest Similiarity.



**Process:**


Term Frequency:

- Create a Corpus(ie: List of Unique words)
- TF = ( Counts Of Term in Document / Total Number of Words in that Document)

Calculating Inverse Document Filtering:

- Document Frequency = ( Number of Occurrences of Term in Document / Total Number of Document)
- IDF = (Number of Documents / df)
- IDF value might explore for very common words like "is","was" etc.. So we Use Log
- IDF = log(Number of Documents / df)

Calculating TF-IDF = TF * IDF   and Create a matrix

- Multiply the Query against the matrix and return the top k matching rows


References:

- [David Oniani: TF-IDF from Scratch](https://www.youtube.com/watch?v=otgVLfBabKk)
- https://towardsdatascience.com/tf-idf-for-document-ranking-from-scratch-in-python-on-real-world-dataset-796d339a4089


# # NLP (Natural Language Processing)
# # =================================

# """
# >> a field of artificial intelligence (AI) that enables computers to understand, interpret, and
#    generate human language 

# >> which convert our language into machine knowing language (text message to machine knowing)

# """

# # Preprocessing steps (optional)
# # ==============================

# """
# >> remove unwanted space
# >> convert the character into ASCII code
# >> expand the short form
# >> remove unwanted like(%, $, @, #, etc.) (special character)

# """

# # Must Implement Steps : 
# # =====================

# """
# <<<<<<< HEAD
# # universities are amazing places for studying and learning new things.
# =======
# >> universities are amazing places for studying and learning new things.
# >>>>>>> d2a6df3517b1cdda6afe518f7d16ad920bced32b

# >> remove the stop words 
#    eg : are, for, and, the, is, etc.

# >> convert all the text into lower case

# >> stemming and lemmatization
#    to find the root word(remove the tail part of the word)
#    eg : amazing -> amaze
#         studying -> study   
#         leaving -> leave

# >> tokenization
#    to split the text into smaller parts (words or sentences)

#    eg : "vinay is a good boy"      # split the words using white space
#         vinay
#         is
#         a
#         good
#         boy                        # word by word output is called tokens  ( 1 - gram)

# <<<<<<< HEAD
# # n - gram method
# =======
# >> n - gram method
# >>>>>>> d2a6df3517b1cdda6afe518f7d16ad920bced32b
#     to split the text into smaller parts (words or sentences) but in a group of n size
    
#     eg : vinay is    >> 2 - gram (bi - gram)
#          a good
# <<<<<<< HEAD

# >> Vectorization
#    to convert text into numerical form so that machine can understand it
#        >> Term Frequency (TF)
#        >> Inverse Document Frequency (IDF)
#       TFidvectorizer()
#       NLTK

#       Term Frequency (TF) = total count of a word in a sentence / total no of words in that sentence
#       Inverse Document Frequency (IDF) = log ( TD/AD)  = log(Total documents / available documents )
            
# >> similarity
#    =========
#    cosine similarity  >> used to identify the similarity between different documents.

#    if cosine similarity == 1 it matches better result will be provided
#    if consine similarity == 0 the documents does not matches
# =======
            
# >>>>>>> d2a6df3517b1cdda6afe518f7d16ad920bced32b



# """
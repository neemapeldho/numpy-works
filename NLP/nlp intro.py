# NLP (Natural Language Processing)
# =================================

"""
>> a field of artificial intelligence (AI) that enables computers to understand, interpret, and
   generate human language 

>> which convert our language into machine knowing language (text message to machine knowing)

"""

# Preprocessing steps (optional)
# ==============================

"""
>> remove unwanted space
>> convert the character into ASCII code
>> expand the short form
>> remove unwanted like(%, $, @, #, etc.) (special character)

"""

# Must Implement Steps : 
# =====================

"""
>> universities are amazing places for studying and learning new things.

>> remove the stop words 
   eg : are, for, and, the, is, etc.

>> convert all the text into lower case

>> stemming and lemmatization
   to find the root word(remove the tail part of the word)
   eg : amazing -> amaze
        studying -> study   
        leaving -> leave

>> tokenization
   to split the text into smaller parts (words or sentences)

   eg : "vinay is a good boy"      # split the words using white space
        vinay
        is
        a
        good
        boy                        # word by word output is called tokens  ( 1 - gram)

>> n - gram method
    to split the text into smaller parts (words or sentences) but in a group of n size
    
    eg : vinay is    >> 2 - gram (bi - gram)
         a good
            



"""
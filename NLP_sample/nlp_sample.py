import nltk
nltk.download('stopwords')
nltk.download('punkt_tab')
# punkt_tab provides abbreviation tables and rules that help NLTK correctly split text into sentences.
# This downloads the tokenizer model used to split text into sentences and words.
# It includes extra rules, abbreviations, and language tables used internally for tokenization.
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

sentence1 = "Earth is the third planet from the sun"

sentence2 = "jupiter is the largest planet"

stopwords = set(stopwords.words('english'))

def preprocess(text):

    tokens = word_tokenize(text.lower())
    
    new = [i for i in tokens if i not in stopwords]

    return " ".join(new)

new_sentence1 = preprocess(sentence1)
new_sentence2 = preprocess(sentence2)

print(new_sentence1)
print(new_sentence2)    

obj = TfidfVectorizer()
result_matrix = obj.fit_transform([new_sentence1,new_sentence2])

print(result_matrix)

similarity = cosine_similarity(result_matrix[0],result_matrix[1])
print(f"The similarity between sentence 1 and sentence 2 is {similarity}")

   
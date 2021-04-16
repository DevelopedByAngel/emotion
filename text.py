# X_train will contain all the sentences 
#y_train will giv 1 or 0 .
#1 means positive 
#0 means negative
X_train = ["He likes sweets",
           "India is one of the best countries in the world",
           "I am unhappy",
           "Sunita is a good girl",
           "We should love the people around us",
           "Be positive",
           "I hate prawns",
           "Mother loves her children",
           "I don’t like onions",
           "Ratul is a cold headed person"]
y_train = [1,1,0,1,1,1,0,1,0,0]
# cleaning of data
    #Tokenization. (convert big para into sent/words)
    # Tokenization o/p contains only alphanumeric words
    
    # stopwords removal-remove stop words(repetitive) if u remov them no change in meaning
    
    #stemming -watever word have u hav 2 convert it 2 root form
    # stemming algorithm reduces the words “chocolates”, “chocolatey”, “choco” to the root word, “chocolate”
    
    #Lemmatization-Lemmatization is the process of grouping 
    #together the different inflected forms of a word so they can be analysed as a single item.
    #Examples of lemmatization:

#-> rocks : rock
#> corpora : corpus
#-> better : good

import nltk
from nltk.tokenize import RegexpTokenizer #Tokenization
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
nltk.download('stopwords')
tokenizer = RegexpTokenizer(r'\w+')#regular exp for only words in concat form
stopwrd = set(stopwords.words('english'))
#stop words removal
prtstm = PorterStemmer() #stemming
def get_clean_text(text):
    text = text.lower()
    
    #Tokenization
    tokens = tokenizer.tokenize(text)
    
    #combinne the process of tokenization and stopword removal
    new_token = [token for token in tokens if token not in stopwrd]
    
    #stemming 
    stemmed_token = [prtstm.stem(tokens) for tokens in new_token]
    
    clean_txt = " ".join(stemmed_token)
    return clean_txt
X_clean = [get_clean_text(i) for i in X_train]
print(X_clean)
#process of converting text into vector is called vectorization
from sklearn.feature_extraction.text import CountVectorizer
#CountVectorizer- It is used to transform a given text into a vector on the basis of the frequency (count) 
#of each word that occurs in the entire text.
#An n-gram is just a string of n words in a row

cv = CountVectorizer(ngram_range=(1,2))
X_vectr = cv.fit_transform(X_clean).toarray()
print(X_vectr)
#to get what is the meaning of abv 0 ,1 we use get_feature_name (bag of word model)
print(cv.get_feature_names())
from sklearn.naive_bayes import MultinomialNB
mnb = MultinomialNB()
mnb.fit(X_vectr,y_train) #classifucation
 #say if its 1 or 0 
def textDetect(inp):
    X_test=[inp]
    Xt_clean = [get_clean_text(i) for i in X_test]
    Xt_vct = cv.transform(Xt_clean ).toarray()
    print(Xt_vct)
    y_pred = mnb.predict(Xt_vct)#say if its 1 or 0 
    print(y_pred)
    for i in y_pred:
        if i == 1:
            return("positive")
        else:
            return("negative")


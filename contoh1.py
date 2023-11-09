import nltk
import spacy
import string
# import warnings filter
from warnings import simplefilter
# ignore all future warnings
simplefilter(action='ignore', category=FutureWarning)
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
nltk.download('stopwords')
nlp = spacy.load('en_core_web_sm')
from sklearn.cluster import KMeans

# Contoh data teks
documents = [
    "this is example of first texts",
    "the second texts contain more words, and long",
    "the third texts is the best example",
    "the last, fourth texts is more complex example.",
    "what ever this is example of words"
]

# Tokenisasi dengan spaCy
def tokenize(text):
    tokens = nlp(text)
    tokens = [token.text for token in tokens if not token.is_punct]
    return tokens
# Hapus stopwords
def remove_stopwords(tokens):
    stop_words = set(stopwords.words('english'))
    return [token for token in tokens if token.lower() not in stop_words]
# Tokenisasi dan hapus stopwords untuk setiap dokumen
tokenized_documents = [remove_stopwords(tokenize(doc)) for doc in documents]

# Menggunakan TF-IDF untuk ekstraksi fitur
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform([' '.join(doc) for doc in tokenized_documents])
# Matriks TF-IDF
print(tfidf_matrix.toarray())

# Klastering menggunakan K-Means
num_clusters = 2  # Ganti sesuai kebutuhan
kmeans = KMeans(n_clusters=num_clusters)
kmeans.fit(tfidf_matrix)
# Label klaster untuk setiap dokumen
cluster_labels = kmeans.labels_
# Tampilkan hasil klastering
for i, doc in enumerate(documents):
    print(f"Dokumen '{doc}' termasuk ke dalam Klaster {cluster_labels[i]}")


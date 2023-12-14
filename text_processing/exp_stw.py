#Python Sastrawi merupakan library sederhana yang dapat mengubah kata berimbuhan bahasa Indonesia menjadi bentuk dasarnya. 
# Sastrawi juga dapat diinstal melalui “pip”. sintaks : pip install Sastrawi
# example code :
# import StemmerFactory class
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
# create stemmer
factory = StemmerFactory()
stemmer = factory.create_stemmer()
# stemming process
sentence = 'Penggunaan Python Sastrawi sangat sederhana seperti baris kode dibawah'
output   = stemmer.stem(sentence)
print(output)
# output result
print(stemmer.stem('jangan asal meniru-niru tindakan orang'))
# output result

import matplotlib.pyplot as plt
from nltk import word_tokenize
from nltk import FreqDist
from nltk import corpus
import nltk

# nltk.download('stopwords')
stopwords_pt = set(corpus.stopwords.words('portuguese'))
#add mais uma stopwords
stopwords_pt.add('é')

# load file
texto_com_stopwords = open("dataset/analise_exploratoria_dados_wikipedia.txt", "r")
texto_com_stopwords = texto_com_stopwords.read().lower()

tokens_texto = [x for x in texto_com_stopwords.split(" ") if x not in stopwords_pt]

freq_tokens = FreqDist(w.lower() for w in tokens_texto)

# total de palavras
print("Total de palavras [com stopwords]: {}".format(len(tokens_texto)))
print("O texto é composto por {} palavras (sem repetição)".format(len(freq_tokens)))
print("10 Palavras mais frequentes:")
print(freq_tokens.most_common(20))

# plot das 30 mais frequentes
freq_tokens.plot(20,cumulative=False)
plt.show()

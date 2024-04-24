import pandas as pd
from collections import Counter
import string
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

#need to have ntlk etc set up
#mostpopularwordcloud: literally just gives u a word cloud of popular words
## pay attention to words_to_exclude as you may not want to exclude any, or add more generic ones to exclude

#mostpopularbigrams: generates list of bigrams - can alter so results are in bar graph form

#mostpopulartrigrams: bigrams but 3

#wordgroupanalysis: breaks text data into word groups verbs, nouns and adjectives
## requires u to input POS tag, list of relevant ones written next to it as a comment
### also doesn't seem to be 100% accurate; includes some random letters

#have added comments in any places you might be interested in changing variables




#    df = pd.read_csv(file, encoding='utf-8', na_values=[''])




def mostpopularwordcloud(df):
    text_data = ' '.join(df['clean_tweet'].dropna())
    words = text_data.split()
    words_to_exclude = ['the', 'and', 'to', 'of', 'a', 'is', 'in', 'this', 'that', 'are', 
                        'it', 'with', 'have', 'will', 'on', 'from', 'for', '', 'as', 'by']
    ##REMOVE WHICHEVER WORDS GIVE NO INFO EG ARTICLES / CONNECTIVES
    translator = str.maketrans('', '', string.punctuation)
    cleaned_words = [word.translate(translator).lower() for word in words if word.lower() not in words_to_exclude]
    top_n = 50 #HOW MANY OF THE TOP WORDS YOU WANT TO RETURN
    #print(file)
    word_counts = Counter(cleaned_words)
    most_common_words = word_counts.most_common(top_n)
    print(f'Top {top_n} most frequent words: ')
    for word, count in most_common_words:
        print(f'{word}: {count}')
    
    word_counts_dict = dict(most_common_words)
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_counts_dict)
    plt.figure(figsize=(10,5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

def mostpopularbigrams(df):
    text_data = ' '.join(df['clean_tweet'].dropna())
    words = text_data.split()
    translator = str.maketrans('', '', string.punctuation)
    words_to_exclude = ['the', 'and', 'to', 'of', 'a', 'is', 'in', 'this', 'that', 'are', 
                        'it', 'with', 'have', 'will', 'on', 'from', 'for', '', 'as', 'by'] #EDIT
    cleaned_words = [word.translate(translator).lower() for word in words if word.lower() not in words_to_exclude]
    top_n = 50
    #print(file)
    bigrams = [(cleaned_words[i], cleaned_words[i + 1]) for i in range(len(cleaned_words) - 1)]
    bigram_counts = Counter(bigrams)
    most_common_bigrams = bigram_counts.most_common(top_n)
    print(f'Top {top_n} most frequent bigrams:')
    for bigram, count in most_common_bigrams:
        print(f'{bigram}: {count}')

def mostpopulartrigrams(df):
    text_data = ' '.join(df['clean_tweet'].dropna())
    words = text_data.split()
    translator = str.maketrans('', '', string.punctuation)
    words_to_exclude = []
    cleaned_words = [word.translate(translator).lower() for word in words if word.lower() not in words_to_exclude]
    trigrams = [(cleaned_words[i], cleaned_words[i+1], cleaned_words[i+2]) for i in range(len(cleaned_words) -2)]
    trigram_counts = Counter(trigrams)
    top_n = 50
    most_common_trigrams = trigram_counts.most_common(top_n)
    print(f'Top {top_n} most frequent trigrams:')
    for trigram, count in most_common_trigrams:
        print(f'{trigram}: {count}')

def get_wordnet_pos(tag): ##for lemmatisation
    if tag.startswith('J'):
        return nltk.corpus.wordnet.ADJ
    elif tag.startswith('V'):
        return nltk.corpus.wordnet.VERB
    elif tag.startswith('N'):
        return nltk.corpus.wordnet.NOUN
    elif tag.startswith('R'):
        return nltk.corpus.wordnet.ADV
    else:
        return nltk.corpus.wordnet.NOUN
    
def wordgroupanalysis(df, group_tag):
    text_data = ' '.join(df['clean_tweet'].dropna())
    words = word_tokenize(text_data)
    pos_tags = pos_tag(words)
    lemmatizer = WordNetLemmatizer()

    wordgroup = [(lemmatizer.lemmatize(word, get_wordnet_pos(tag)), tag) for word, tag in pos_tags if tag.startswith(group_tag)]
    
    df_group_pos_tags = pd.DataFrame(wordgroup, columns=['Word', 'POS'])
    word_counts = df_group_pos_tags.groupby(['Word']).size().reset_index(name='Count')
    word_counts = word_counts.sort_values(by='Count', ascending=False)
    return word_counts.head(50) #AGAIN CAN CHANGE HOW MANY ARE RETURNED


def wordgroupclouds(top_words):
    word_counts_dict = dict(zip(top_words['Word'], top_words['Count']))
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_counts_dict)
    plt.figure(figsize=(10,5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

###FUNCTION CALLS HERE ######

#CHANGE FILENAME AS NECESSARY
#mostpopularwordcloud("all_biden_youtube_comments.csv")

# mostpopularbigrams("all_trump_youtube_comments.csv")

# mostpopulartrigrams("all_trump_youtube_comments.csv")

# group_tag = 'JJ' #verbs = VB, nouns = NN, adjectives = JJ <<<<<<<<<
# top_words = wordgroupanalysis("all_biden_youtube_comments.csv", group_tag)
# wordgroupclouds(top_words)
#print(f"Top 50 most frequent {group_tag.lower()}s:")
#print(top_words)

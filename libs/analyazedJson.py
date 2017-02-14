
import json
from nltk.tokenize import word_tokenize
import re
import operator
from collections import Counter
from nltk.corpus import stopwords
import string
from nltk  import bigrams


term_to_search = "israel"

punctuation = list(string.punctuation)
print punctuation
stop = stopwords.words('english') + punctuation +['#RT','#rt','rt','RT', 'via']  + \
       [term_to_search] +["#"+term_to_search] +[u'\u2026']

emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""

regex_str = [
    emoticons_str,
    r'<[^>]+>',  # HTML tags
    r'(?:@[\w_]+)',  # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)",  # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+',  # URLs

    r'(?:(?:\d+,?)+(?:\.?\d+)?)',  # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])",  # words with - and '
    r'(?:[\w_]+)',  # other words
    r'(?:\S)'  # anything else
]

tokens_re = re.compile(r'(' + '|'.join(regex_str) + ')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^' + emoticons_str + '$', re.VERBOSE | re.IGNORECASE)


def tokenize(s):
    return tokens_re.findall(s)


def preprocess(s, lowercase=False):
    lowercase=True
    s= s.encode('ascii', 'ignore').decode('ascii') # Shoud remove for hebrew..
    #s = re.sub(r'[^\u3000-\u307F]+', "",s) #remove
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    tokens = list(set(tokens)- set(stop))

    return tokens


with open('blacklist.json', 'r') as f:
    count_terms_only = Counter()
    count_users = Counter()
    count_hashtag =Counter()
    count_bigram = Counter()
    for line in f:
        tweet = json.loads(line)  # load it as Python dict
        tweet_text= tweet["text"]


        #print tweet_text
        tokens = preprocess(tweet_text)

        print tweet_text

        terms_only = [term for term in preprocess(tweet_text) if term.lower() and not term.startswith(("#","@"))]
        hash_tag =  [term for term in preprocess(tweet_text) if term.lower() and term.startswith("#")]
        users =  [term for term in preprocess(tweet_text) if term.lower() and term.startswith("@")]
        terms_bigram = bigrams(terms_only)

        # Update the counter
        count_terms_only.update(terms_only)
        count_hashtag.update(hash_tag)
        count_users.update(users)
        count_bigram.update(terms_bigram)

        #print(word_tokenize(tweet_text))
        #print(json.dumps(tweet, indent=4))  # pr

#Need to insert the db - date + father_term + number
termsonly= count_terms_only.most_common(30)
for term in termsonly:
    print term[0]


print termsonly


hashonly = count_hashtag.most_common(20)
for term in hashonly:
    print term[0]

print count_users.most_common(10)
print count_bigram.most_common(10)
import pandas as pd
ai_df = pd.read_json('./data/xl-1542M-k40.train.jsonl', lines=True)
# Confirm length is correct (250,000 expected)
print("Number of AI text articles: " + str(len(ai_df)))

ai_df.head()
# Printing first output
print(ai_df.head())

# Only keep articles where ended == True
ai_df = ai_df[ai_df['ended']==True]

print("# of AI samples after dropping incomplete text: " + str(len(ai_df)))

# Now dropping the "ended" and "length" columns
ai_df.drop(labels=['ended', 'length', 'id'], axis=1, inplace=True)

ai_df.head()


real_df = pd.read_csv('./data/True.csv')
fake_df = pd.read_csv('./data/Fake.csv')

print("# Real articles: " + str(len(real_df)))

print("# Fake articles: " + str(len(fake_df)))
real_df.head()

# Dropping title, subject and data columns since we cant use these in AI-text
real_df.drop(labels=['title', 'subject', 'date'], axis=1, inplace=True)
fake_df.drop(labels=['title', 'subject', 'date'], axis=1, inplace=True)

real_df.head()

real_df[real_df['text'].str.contains("Reuters")]

# Fake articles that contain "Reuters" in them
fake_df[fake_df['text'].str.contains("Reuters")]



# Remove 'Reuters) - ' and anything that comes before it
real_df['text'] = real_df['text'].apply(lambda x: x.split('Reuters) - ')[-1])

# Remove 'Reuters' even if it doesnt follow format above
real_df['text'] = real_df['text'].apply(lambda x: x.replace('Reuters', ''))


# Print remaining rows containing Reuters - expecting empty DataFrame
print(real_df[real_df['text'].str.contains("Reuters")])


# Repeat for Fake df
fake_df['text'] = fake_df['text'].apply(lambda x: x.split('Reuters) - ')[-1])
fake_df['text'] = fake_df['text'].apply(lambda x: x.replace('Reuters', ''))

# Print remaining rows containing Reuters - expecting empty DataFrame
print(fake_df[fake_df['text'].str.contains("Reuters")])

# Examples of text we want to clean

# Contains '\n'
ai_df.text.iloc[0]

#Contains unicode space '\xa0'
real_df.text.iloc[13]

# Contains https link
fake_df.text.iloc[3]

import re

def clean_text(text):
  """Cleans newline characters, unix whitespace,
  and http links from text"""

  text = re.sub(r'\n', ' ', text)
  text = re.sub('\xa0', ' ', text)
  cleaned_text = re.sub('(http)(.+?)(?:\s)', ' ', text)   # 'http' followed by text up until space char

  return cleaned_text

ai_df.text.iloc[0]

clean_text(ai_df.text.iloc[0])

# Clean the text on all dfs

df_list = [real_df, fake_df, ai_df]
print(df_list)
# first commit
for df in df_list:
  df['text'] = df['text'].apply(lambda x: clean_text(x))
df['text']

real_df["group"] = "real"
fake_df["group"] = "fake_hum"
ai_df["group"] = "fake_ai"

articles_df = real_df._append([fake_df, ai_df], verify_integrity=True, ignore_index=True)

articles_df

articles_df[articles_df["group"] == 'fake_hum'] # of fake_hum articles: 21226
len(articles_df[articles_df["group"] == 'fake_hum'].text.unique()) # 16385 unique fake_hum articles


articles_df[articles_df["group"] == 'real'] # of real articles: 20253
len(articles_df[articles_df["group"] == 'real'].text.unique()) # 20043 unique real articles


articles_df[articles_df["group"] == 'fake_ai'] # of ai articles: 165190
len(articles_df[articles_df["group"] == 'fake_ai'].text.unique()) # 165121 unique ai articles

# Yes, all 3 groups have some duplicates, particularly the fake_hum group with 4841 duplicate articles.
# fake_ai and real each have < 250 duplicates
# 5,120 duplicate articles total

articles_df.drop_duplicates(subset=['text'], inplace=True, ignore_index=True)
articles_df

articles_df['length'] = articles_df['text'].apply((lambda x: len(x)))
print(articles_df['length'])

# Viewing the number of articles for each group

print("# of articles for real: " + str(len(articles_df[articles_df['group'] == 'real'])))
print("# of articles for fake_hum: " + str(len(articles_df[articles_df['group'] == 'fake_hum'])))
print("# of articles for fake_ai: " + str(len(articles_df[articles_df['group'] == 'fake_ai'])))

import matplotlib.pyplot as plt
import seaborn as sns

sns.boxplot(x='group', y='length', data=articles_df)

plt.xlabel("Group", fontsize= 12)
plt.ylabel("Length", fontsize= 12)
plt.title("Article Length by Group", fontsize=15)

# Longest fake_ai article
articles_df[articles_df.group == 'fake_ai'].length.max()

# All articles that are too long
articles_df[articles_df.length > 5693]

# importing word_tokenize to use in function below
import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')

def article_crop(article, char_limit):
  """Given a DataFrame row that contains a 'text' column and a character limit, this crops
      the text to end at the sentence after the character limit is reached

  Params
  - row: a row of a Dataframe that contains 'text' column
  - char_limit: int, once text reaches this limit, the current sentence will become the final sentence in the text
  """


  # If text is longer than char limit
  if len(article) > char_limit:

    # Split text into two groups, before and after the character limit
    before_limit = article[: char_limit]
    after_limit = article[char_limit : ]

    # If after_limit contains more than just whitespace (check is needed b/c calling sent_tokenize()[0] on whitespace will fail)
    if len(nltk.sent_tokenize(after_limit)) > 0:

      sent_after_limit = nltk.sent_tokenize(after_limit)[0] # Take 1st sentence after char_limit

      new_text = before_limit + sent_after_limit
      return new_text

    # In this case, chars after char_limit only contain whitespace
    else:
      return before_limit

  else:
    return article

  articles_df.text.iloc[63][0:5693]

  # Shows the final sentence being completed using article_crop()
  article_crop(articles_df.text.iloc[63], 5711)[5400:]
  article_crop(articles_df.text)

  article_crop(articles_df.text.iloc[63], 5711)

  article_crop(articles_df.text.iloc[63], 5711)[2040:]

  # For texts longer than 5711 chars (the longest AI text), crop when the sentence at 5711 chars ends
  articles_df['text'] = articles_df.text.apply(lambda x: article_crop(x, 5711))
  articles_df
---------------------
# Recomputing article lengths after crops
  articles_df['length'] = articles_df['text'].apply(lambda x: len(x))

  # Viewing new article lengths after crops
  sns.boxplot(x='group', y='length', data=articles_df)

  plt.xlabel("Group", fontsize=12)
  plt.ylabel("Length", fontsize=12)
  plt.title("Article Length by Group", fontsize=15)

# articles that are still really long
articles_df[articles_df.length > 8000]


# Last part of articles that are still really long
# Both are sentences separated by colons and semicolons
articles_df.text.iloc[23830][-2500:]
articles_df.text.iloc[37558][-2500:]

articles_df['sentences'] = articles_df['text'].apply(lambda x: nltk.sent_tokenize(x))
articles_df['tok'] = articles_df['text'].apply(lambda x: nltk.sent_tokenize(x))
articles_df.drop('tok', axis=1)
--------------

def lenzero(text):
  if len(text) == 0:
      lentt = 1
    else:
        lentt = len(text)
  return  lentt

def avg_words_per_sent(text):
  """Feed a list of sentences (param:text) and
  returns the average number of words per sentence"""

  num_words_list = [] # List of word count per sentence

  for sent in range(len(text)):

    # Number of words in a sentence, excludes punctuation
    num_words = len([word for word in word_tokenize(text[sent]) if word.isalnum()])

    # Add number of words for sentence to the list
    num_words_list.append(num_words)


  # Compute the average
  avg_word_per_sentences = sum(num_words_list) / lenzero(num_words_list)

  return avg_word_per_sentences



articles_df['words_per_sent'] = articles_df['sentences'].apply(lambda x: avg_words_per_sent(x))

articles_df.head()



sns.boxplot(x='group', y='words_per_sent', data=articles_df)

plt.xlabel("Group", fontsize= 14)
plt.ylabel("Words per Sentence", fontsize= 14)
plt.title("Avg words per sentence by group", fontsize=18)

---------------
# AI text higher than 100 words per sentence
articles_df[(articles_df['words_per_sent'] > 100) & (articles_df['group'] == "fake_ai")]
articles_df[(articles_df['words_per_sent'] > 100) & (articles_df['group'] == "real")]

# AI-generated lyric example
articles_df.text.iloc[43307]

# AI-generated youtube page example
articles_df.text.iloc[49514]

# Human authored text higher than 100 words per sentence
articles_df[(articles_df['words_per_sent'] > 100) & (articles_df['group'] != "fake_ai")]

articles_df.sentences.iloc[36311]

---------------
articles_df[articles_df['words_per_sent'] > 100].index


# Dropping articles with 100+ average words per sentence
articles_df.drop(articles_df[articles_df['words_per_sent'] > 100].index, inplace=True)

# Reset index
articles_df.reset_index(drop=True, inplace=True)

print("New count of articles")
print("# of articles for real: " + str(len(articles_df[articles_df['group'] == 'real'])))
print("# of articles for fake_hum: " + str(len(articles_df[articles_df['group'] == 'fake_hum'])))
print("# of articles for fake_ai: " + str(len(articles_df[articles_df['group'] == 'fake_ai'])))

---------------
# Replotting avg words per sentence
sns.boxplot(x='group', y='words_per_sent', data=articles_df)

plt.xlabel("Group", fontsize= 14)
plt.ylabel("Words per Sentence", fontsize= 14)
plt.title("Avg words per sentence by group", fontsize=16)

--------------
# Plotting probability distribution due to uneven # of samples between groups
sns.displot(articles_df, x='words_per_sent', hue='group', stat='probability', common_norm=False)

plt.ylabel("Probability", fontsize= 14)
plt.xlabel("Avg. words/sentence", fontsize= 14)
plt.title("Distribution of avg. words/sentence by group", fontsize=16)
-------------

# Create column of lowercase text
articles_df['text_lower'] = articles_df['text'].apply(lambda x: x.lower())

-------------
from nltk.corpus import stopwords
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')

stopwords = set(stopwords.words('english'))
--------------------
def tokenize_text(article):
  """ take a text string and
  - tokenizes words
  - lowers case
  - removes stopwords
  - remove non alpha tokens

  :param article_list: list of strings
  :return: list of cleaned text
  """

  tok_text = nltk.word_tokenize(article)
  tok_text = [word.lower() for word in tok_text]
  tok_text = [word for word in tok_text if word not in stopwords]
  tok_text = [word for word in tok_text if word.isalpha()]


  return tok_text
---------------
# Create a list of text articles for each group
real_text_list = list(articles_df.text[articles_df.group == "real"])
fakehum_text_list= list(articles_df.text[articles_df.group == "fake_hum"])
ai_text_list = list(articles_df.text[articles_df.group == "fake_ai"])


# Tokenize and clean the lists from stopwords
# each result is list of lists containing words for each article
real_word_list = [tokenize_text(article) for article in real_text_list]
fakehum_word_list = [tokenize_text(article) for article in fakehum_text_list]
ai_word_list = [tokenize_text(article) for article in ai_text_list]


#flatten the list of lists into a single list of words
flat_real_word_list = [word for article in real_word_list for word in article]
flat_fakehum_word_list = [word for article in fakehum_word_list for word in article]
flat_ai_word_list = [word for article in ai_word_list for word in article]

---------------
from collections import Counter

# 50 most common words for real
real_cnt = Counter(flat_real_word_list)
real_most_common = real_cnt.most_common(50)

# Show top 30
real_most_common[:30]
-----------------------------
# 50 most common words for fake_hum
fakehum_cnt = Counter(flat_fakehum_word_list)
fakehum_most_common = fakehum_cnt.most_common(50)

# Show top 30
fakehum_most_common[:30]
---------------------
# 50 most common words for ai
ai_cnt = Counter(flat_ai_word_list)
ai_most_common = ai_cnt.most_common(50)

# Show top 30
ai_most_common[:30]

------------------
from wordcloud import WordCloud
real_wordcloud = WordCloud(background_color="black", max_words=50).generate_from_frequencies(real_cnt)
plt.imshow(real_wordcloud)
plt.axis("off")
plt.title("Most common words - Real news", fontsize=18)
plt.show()
-----------
fakehum_wordcloud = WordCloud(background_color="black", max_words=50).generate_from_frequencies(fakehum_cnt)
plt.imshow(fakehum_wordcloud)
plt.axis("off")
plt.title("Most common words - Fake news - Human", fontsize=18)
plt.show()
----------------
ai_wordcloud = WordCloud(background_color="black", max_words=50).generate_from_frequencies(ai_cnt)
plt.imshow(ai_wordcloud)
plt.axis("off")
plt.title("Most common words - Fake news - AI", fontsize=18)
plt.show()
-------------------------
real_words = []
for i in range(len(real_most_common)):
  # Add the word, not the frequency count
  real_words.append(real_most_common[i][0])

# List of most 50 common words in real
real_words



fake_words = []
for i in range(len(fakehum_most_common)):
  # Add the word, not the frequency count
  fake_words.append(fakehum_most_common[i][0])

# List of most 50 common words in fake
fake_words
---------------------------
# Create set from the 50 most common words from both human-authored groups
human_words = set(real_words + fake_words)

print(len(human_words))
print("")
print(human_words)
------------------------
# Tag most common human-authored words with parts of speech
nltk.pos_tag(human_words)

----------------
# keep only nouns in human_words
tagged_human_words = nltk.pos_tag(human_words)

human_nouns = [word_tag_pair[0] for word_tag_pair in tagged_human_words if word_tag_pair[1] == 'NN']
human_nouns

------------------------
# Remove the following words: way, image, time, year, video, get, week
human_nouns = [word for word in human_nouns if word not in ['way', 'time', 'image', 'year', 'video', 'get', 'week']]

# Final list
human_nouns
-----------------------
def contains_word_in_list(text, word_list):
  """ Given a text string, returns true if string contains any word in word_list
  else returns false

  :param - text -- string
  : word_list - a list of words
  """
  if any(word in text for word in word_list):
    return True
  else:
    return False

# Create column
articles_df["contains_human_word"] = articles_df['text_lower'].apply(lambda x: contains_word_in_list(x, human_nouns))

# Lets recount how many articles we have before dropping more AI articles

print("# of articles for real: " + str(len(articles_df[articles_df['group'] == 'real'])))
print("# of articles for fake_hum: " + str(len(articles_df[articles_df['group'] == 'fake_hum'])))
print("# of articles for fake_ai: " + str(len(articles_df[articles_df['group'] == 'fake_ai'])))

---------------------------

# Drop AI_articles without human news words
articles_df.drop(articles_df[(articles_df.group=="fake_ai") & (articles_df.contains_human_word==False)].index, inplace=True)

# Drop contains_human_word column because no longer needed
articles_df.drop(['contains_human_word'], axis=1, inplace=True)

# Reset index
articles_df.reset_index(drop=True, inplace=True)

print("# of articles for real: " + str(len(articles_df[articles_df['group'] == 'real'])))
print("# of articles for fake_hum: " + str(len(articles_df[articles_df['group'] == 'fake_hum'])))
print("# of articles for fake_ai: " + str(len(articles_df[articles_df['group'] == 'fake_ai'])))

-------------------------------
# AI most common words before drop
ai_most_common[:15]
-------------------
# AI most common words after drop
new_ai_most_common = new_ai_cnt.most_common(50)
new_ai_most_common[:15]

--------------
# Compare old word cloud
ai_wordcloud = WordCloud(background_color="black", max_words=50).generate_from_frequencies(ai_cnt)
plt.imshow(ai_wordcloud)
plt.axis("off")
plt.title("Most common words - Fake news - AI - Old", fontsize=18)
plt.show()

--------------------------
# New ai word cloud

# Same process as before to generate word cloud
new_ai_text_list = list(articles_df.text[articles_df.group == "fake_ai"])
new_ai_word_list = [tokenize_text(article) for article in new_ai_text_list]
new_flat_ai_word_list = [word for article in new_ai_word_list for word in article]

new_ai_cnt = Counter(new_flat_ai_word_list)

new_ai_wordcloud = WordCloud(background_color="black", max_words=50).generate_from_frequencies(new_ai_cnt)
plt.imshow(new_ai_wordcloud)
plt.axis("off")
plt.title("Most common words - Fake news - AI - New", fontsize=18)
plt.show()
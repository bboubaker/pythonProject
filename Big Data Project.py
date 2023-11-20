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

  text = re.sub(r'\n', '', text)
  text = re.sub('\xa0', ' ', text)
  cleaned_text = re.sub('(http)(.+?)(?:\s)', ' ', text)   # 'http' followed by text up until space char

  return cleaned_text

ai_df.text.iloc[0]

clean_text(ai_df.text.iloc[0])

# Clean the text on all dfs

df_list = [real_df, fake_df, ai_df]
# first commit
for df in df_list:
  df['text'] = df['text'].apply(lambda x: clean_text(x))

import pandas as pd
import nltk
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
from nltk.corpus import wordnet

nltk.download('averaged_perceptron_tagger_eng')

lemmatizer = WordNetLemmatizer()


def get_wordnet_pos(treebank_tag):
	if treebank_tag.startswith('J'):
		return wordnet.ADJ
	elif treebank_tag.startswith('V'):
		return wordnet.VERB
	elif treebank_tag.startswith('N'):
		return wordnet.NOUN
	elif treebank_tag.startswith('R'):
		return wordnet.ADV
	else:
		return wordnet.NOUN


def process_text(text):
	tokens = [token.strip() for token in text.split(',')]
	tagged_tokens = pos_tag(tokens)
	lemmatized_tokens = [
		lemmatizer.lemmatize(token, get_wordnet_pos(tag))
		for token, tag in tagged_tokens
	]
	return ', '.join(lemmatized_tokens)


def lemmatize_dataframe(df: pd.DataFrame, column: str):
	df.loc[:, column] = df[column].apply(process_text)
	return df

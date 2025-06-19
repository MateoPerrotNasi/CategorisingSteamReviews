import pandas as pd
from nltk.corpus import stopwords


def remove_stopwords(df: pd.DataFrame, column: str) -> pd.DataFrame:
	stop_words = set(stopwords.words('english'))

	filtered_col = df[column].apply(
		lambda x: [word for word in x.split(',') if word not in stop_words]
	)

	df.loc[:, column] = filtered_col.apply(
		lambda tokens: ','.join(tokens) if tokens else ''
	)
	return df

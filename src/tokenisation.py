import pandas as pd


def tokenisation(df: pd.DataFrame, column: str) -> pd.DataFrame:
	# Tokenisation: we split the by worsds and join them with a comma
	df.loc[:, column] = (
		df[column]
		.str.split()
		.apply(lambda tokens: ','.join(tokens))
	)
	return df

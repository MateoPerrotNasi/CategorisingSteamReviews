import pandas as pd


def cleaning(df: pd.DataFrame, column: str) -> pd.DataFrame:
	# Extract the lines which are not empty and have at least 3 characters
	df_clean = df[df[column].str.len() >= 3]

	# Remove non utf-8 characters and convert to lowercase
	df_clean.loc[:, column] = (
		df_clean[column]
		.str.lower()
		.str.replace(r"[^a-zàâäéèêëîïôöùûüç\s]", "", regex=True)
	)
	return df_clean

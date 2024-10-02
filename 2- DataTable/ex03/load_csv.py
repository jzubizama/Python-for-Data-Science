import pandas as pd

def load(path: str) -> pd.DataFrame:
	try:
		dt = pd.read_csv(path)
		print("Loading dataset of dimensions ", dt.shape)
		return dt
	except:
		return None
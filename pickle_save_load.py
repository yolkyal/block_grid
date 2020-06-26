import pickle

def load(filepath):
	with open(filepath, 'rb') as f:
		return pickle.load(f)

def save(val, filepath):
	with open(filepath, 'wb') as f:
		pickle.dump(val, f)
import pickle

# saving val losses for various combinations
def write_pickle(file,data):
    with open(file, 'wb') as outfile:
        serialized = pickle.dumps(data)
        outfile.write(serialized)

def read_pickle(file):
    with open(file,'rb') as datafile:
        serialized = datafile.read()
        data = pickle.loads(serialized)
        return data

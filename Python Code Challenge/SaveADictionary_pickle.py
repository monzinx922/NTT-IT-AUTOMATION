# This is function which solution from challenge, using pickle to read and write data to file with wb(write bit) and rb(read bit)

import pickle

def save_dict(dict_to_save, file_path):
    with open(file_path, 'wb') as file:
        pickle.dump(dict_to_save, file)

def load_dict(file_path):
    with open(file_path, 'rb') as file:
        return pickle.load(file)
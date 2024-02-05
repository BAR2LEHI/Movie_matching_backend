from typing import Union
import numpy as np
from scipy.sparse import csr_matrix
import pickle

def load_model(path:str='model_files/als_model.sav'):
    with open(path, 'rb') as file:
        model = pickle.load(file)
    return model

def load_item_map(path:str='model_files/item_map.pkl'):
    with open(path, 'rb') as file:
        item_map = pickle.load(file)
    return item_map


class Recommender():
    def __init__(
                 self,
                 model=load_model(),
                 id_map=load_item_map()
                 ):
        self.catalog = id_map.external_ids
        self.id_map = id_map
        self.model = model
    
    def to_internal_csr(
           self,
           items_array: Union[list, np.array],
           items_score: Union[list, np.array]
           ):
        items_csr = np.zeros(self.id_map.size)
        items_csr[self.id_map.convert_to_internal(items_array)] = items_score
        items_csr = csr_matrix(items_csr)
        return items_csr
    
    def model_recommendations(
                            self,
                            items_array: Union[list, np.array],
                            items_score: Union[list, np.array],
                            N: int
                            ):
        
        items_csr = self.to_internal_csr(items_array,
                                        items_score)

        recs =  self.model.recommend(userid=self.id_map.size,
                                    user_items=items_csr,
                                    recalculate_user=True,
                                    N=N)[0]
        
        recs = self.id_map.convert_to_external(recs).tolist()

        return recs

class Imdb_Map():
    def __init__(self,
                 item_ids: np.array,
                 imdb_ids: np.array):
        self.item_ids = item_ids 
        self.imdb_ids = imdb_ids

    def to_imdb(self,
                  ids):
        index = np.where(np.isin(self.item_ids, ids))[0]
        imdb_ids = self.imdb_ids[index]
        return imdb_ids
    
    def from_imdb(self,
                  ids):
        index = np.where(np.isin(self.imdb_ids, ids))[0]
        imdb_ids = self.item_ids[index]
        return imdb_ids

def load_imdb_map(path: str='model_files/imdb_map.pkl'):
    with open(path, 'rb') as file:
        map = pickle.load(file)
    return map
"""
"""
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris
from src.umap_algo import umap_class
import umap 


def job(config):

    # dataset = pd.read_parquet(config.path_dataset)
    dataset = load_iris()
    
    # pipeline adapt umap that inherit from sklearn.BaseModel
    dataset_standardized = StandardScaler.fit_transform(dataset)

    model = umap.






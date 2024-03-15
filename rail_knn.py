from shapely import *
import numpy as np
from typing import List, Tuple
import math
from collections import Counter
from pandas import DataFrame
from geopandas import GeoDataFrame
import geopandas as gpd
import pandas as pd

class ShapelyDistance:
    @staticmethod
    def compute(workshop: LineString, rails: List[LineString]) -> List[Tuple[LineString, float]]:
        """
        It will compute the distance between two linestrings using Shapely.

        args:
        workshop (LineString): our arbitrary workshop for given points 
        rails (List[LineString]): gonna retrieve rail indexes and the geometry objects
        """

        distances = [(rail, hausdorff_distance(workshop, rail)) for rail in rails] # the first value in this tuple gonna be our identifier

        return distances

class Neighbors:
    @staticmethod
    def select(workshop, distances, k=7):
        """
        We gonna select k nearest neighbors of the given workshop.

        args:
        k (int): number of nearest neighbors to select
        
        returns:
        list: nearest neighbors to workshop
        """
        
        distances.sort(key=lambda x: float(x[1]))

        neighbors = [distance for distance in distances if distance[1] != 0.0][:k]

        return neighbors
    
class Response:
    def __init__(self, neighbors):
        self.neighbors = list(neighbors)

    @staticmethod
    def predict(neighbors):
        # cnt = Counter(neighbors)
        pass

    def accuracy():
        pass

    @staticmethod
    def resulting_df(neighbors: list) -> GeoDataFrame:
        df = pd.DataFrame(neighbors, columns=['geometry', 'distance'])

        return gpd.GeoDataFrame(df, geometry='geometry', crs="EPSG:2154")

def main():
    pass
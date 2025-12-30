import geopandas as gpd
import pandas as pd
import requests

class GetLocationInfo:
    def __init__(self, xy=None, brgy=None, muni_city=None):
        if xy is not None:
            self.xy = xy
            self.latitude = xy.split(',')[0]
            self.longitude = xy.split(',')[1]
        else: 
            self.latitude = None
            self.longitude = None

        self.brgy=brgy
        self.muni_city=muni_city
        self.bdrys = gpd.read_file('../files/gadm_phl.gpkg')

    def get_admin_bdrys(self, xy=None):
        bdrys = self.bdrys
        
        xy_df = pd.DataFrame({
            'name': ['Point'], 
            'latitude': [self.latitude],
            'longitude': [self.longitude]
        })

        xy_gdf = gpd.GeoDataFrame(
            xy_df, 
            geometry=gpd.points_from_xy(xy_df.longitude, xy_df.latitude),
            crs='EPSG:4326'
        )

        intersection = bdrys.sjoin(xy_gdf, how='inner')

        return {
            'province': intersection['NAME_1'].item(),
            'municpality': intersection['NAME_2'].item(),
            'barangay': intersection['NAME_3'].item()
        }
     
    def get_elevation(self, xy=None):
        response = requests.get(
            f'https://api.opentopodata.org/v1/test-dataset?locations={self.latitude},{self.longitude}'
            )
        elevation = response.json()['results'][0]['elevation']

        return elevation
    
    def get_location_info(self, xy=None):
        return {
            'boundaries': self.get_admin_bdrys(),
            'elevation': self.get_elevation()
        }
    

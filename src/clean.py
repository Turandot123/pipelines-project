import json
import os

import numpy as np
import pandas as pd

from src.api import get_oscar_winner_films, get_oscar_winner_directors


def parse_to_json(value, transform=lambda x: x):
#Parses a string value to json: changes the simple ' to " and loads the value. If the transform lambda is passed
#to the function, it is applied to the loaded value.
    if type(value) == str:
        try:
            value = json.loads(value.replace("\'", "\""))
        except json.JSONDecodeError:
            # If we don't have a valid value, we return Nan
            return np.nan
        return transform(value)
    # Non string == Nan
    return np.nan


def clean_production_companies(value):
    return parse_to_json(value, lambda lista: [element['name'] for element in lista])


def create_database():

#This function takes the input csvs and generates the output csv that is used by the rest of the program to work
 
    # Get the relevant columns from the IMDB csv
    imdb_df = pd.read_csv("input/IMDB-Movie-Data.csv", usecols=['Title', 'Director', 'Year', 'Rating', 'Votes',
                                                                'Revenue (Millions)'])
    # Rename Revenue to something more manageable
    imdb_df.rename(columns={'Revenue (Millions)': 'Revenue'}, inplace=True)
    # Get the relevant columns from the producer csv
    producers_df = pd.read_csv("input/movies_producer.csv", usecols=['title', 'production_companies'])
    # Transform the column of production companies into a list of names (removing the ids)
    producers_df['production_companies'] = producers_df['production_companies'].map(
        lambda cs: clean_production_companies(cs))
    # Rename columns to match the IMDB naming style
    producers_df.rename(columns={'title': 'Title', 'production_companies': 'Producer'}, inplace=True)
    # This database has duplicates. We observed that the first values use to be the more complete.
    producers_df.drop_duplicates(subset='Title', keep="first", inplace=True)
    # We inner join the IMDB df with the producers df to get the Producer column. We use the Title column to match
    # We make an inner join because we are not interested on rows with missing information in this case
    df = imdb_df.merge(producers_df, how='inner', on='Title')
    # We join the oscar winning films. In this case, we use a left join (or we would get just the winners!)
    df = df.merge(get_oscar_winner_films(), how='left', on='Title')
    # Same for directors
    df.merge(get_oscar_winner_directors(), how='left', on='Director')
    df.to_csv('output/database.csv')


def load_database():
#Check if we have the database generated. If not, generate it. Load it as a dataframe.

    database = pd.read_csv('output/database.csv')
    # We need to transform the producer string into a list
    database['Producer'] = database['Producer'].map(lambda cs: parse_to_json(cs))
    return database




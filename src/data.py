from src.clean import load_database

def _to_column_dict(database, column):
    return database.sort_values(column, ascending=False).head(10).set_index('Title')[column].apply(lambda x: "$ {}".format(round(x,2))).to_dict()


def get_film_data():

#Sort the film data by Rating, Revenue and Votes and extract the 10 first values

    database = load_database()
    return {
        'Rating': _to_column_dict(database, 'Rating'),
        'Revenue': _to_column_dict(database, 'Revenue'),
        'Votes': _to_column_dict(database, 'Votes'),
    }
    


def get_director_data():

#Get the revenue and oscars wined by director

    database = load_database()
    return {
        # To generate the revenue, we just sum the revenue column grouped values by director and extract it as a dict
        'Revenue': database[['Director', 'Revenue']].groupby(['Director']).sum().sort_values(
            'Revenue', ascending=False).head(10)['Revenue'].apply(lambda x: "$ {}".format(round(x,2))).to_dict(),
        # To get the oscar winners, we just have to drop the nan values of the Director oscars column
        'Oscar': database[['Director', 'Director oscars']].dropna().drop_duplicates(
            subset='Director', keep='first').sort_values('Director oscars', ascending=False).set_index(
            'Director')['Director oscars'].to_dict()
    }


def get_producer_data():

#Get the amount of films and the revenue by producer
#Explode allows us to generate a row for each value in the Producer list
    database = load_database().explode('Producer')
    return {
        # Here it's easy, we just have to count the number of rows
        'Amount': database.groupby(['Producer']).count().sort_values('Title', ascending=False).head(10)['Title'].to_dict(),
        # And here we sum the Revenue values of the grouped rows by producer
        'Revenue': database.groupby(['Producer']).sum().sort_values('Revenue', ascending=False).head(10)['Revenue'].apply(lambda x: "$ {}".format(round(x,2))).to_dict()
    }



def get_year_data(year):
    return load_database().groupby(['Year']).sum()['Revenue'].apply(lambda x: "$ {}".format(round(x,2))).to_dict().get(year, 0)

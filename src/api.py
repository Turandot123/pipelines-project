import pandas as pd
import requests
from bs4 import BeautifulSoup as bs


def _get_soup(url):
#Generates the soup object after parsing the html

    r = requests.get(url)
    return bs(r.text, 'html.parser')


def _parse_oscar_winner_film(text):
#Cleans and treats the text of the oscar winning film values

    y, t = text.split('-', 1)
    # Some years have two values, for example: "1932/1933 - Some Name". We have to check this. If this is the case,
    # we get the second year of the pair.
    y = int(y.strip()) if len(y.strip().split('/')) == 1 else int(y.strip().split('/')[1])
    t = t.strip().strip('"')
    return [t, y]


def _add_director(directors, director):
    """
    Check if the director is already in the dataframe. If it is there, it increments the number of the oscars values
    (for example, if it has a value of 2, it sets a 3). If it's not, it creates the row and fixes the value as 1.
    """
    
    if directors.loc[directors['Director'] == director].empty:
        directors.loc[len(directors)] = [director, 1]
    else:
        directors.at[
            directors.loc[directors['Director'] == director].index.values.astype(int)[0], 'Director oscars'] += 1
    return directors


def get_oscar_winner_films():
    """
    Extracts the oscar winning films from today.com
    """
    soup = _get_soup('https://www.today.com/popculture/complete-list-every-best-picture-oscar-winner-ever-t107617')
    film_list = pd.DataFrame(columns=['Title', 'Oscar Year'])
    uls = soup.findAll('ul', {'class': ''})
    for ul in uls:
        for li in ul.findAll('li'):
            if li.text.startswith('1') or li.text.startswith('2'):
                film_list.loc[len(film_list)] = _parse_oscar_winner_film(li.text)
    return film_list


def get_oscar_winner_directors():
    """
    Extracts the directors that have won an Oscar from the filmsite.org site.
    """
    soup = _get_soup('https://www.filmsite.org/bestdirs2.html')
    table = soup.find('table', {'width': '75%'})
    trs = table.findAll('tr', recursive=False)[1:]
    directors = pd.DataFrame(columns=['Director', 'Director oscars'])
    for tr in trs:
        ds = tr.findAll('td')[1].text
        # In some cases, two directors appear on the table, so we have to check this:
        if len(ds.split('\r\n')) > 1:
            # If we have two directors, we add both
            for d in ds.split('\r\n'):
                directors = _add_director(directors, d.strip('\n').strip())
        else:  # We only have one director
            directors = _add_director(directors, ds.strip('\n').strip())
    return directors

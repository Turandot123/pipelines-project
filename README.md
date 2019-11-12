


EXECUTIVE SUMMARY 

I have opted for extracting and analysing info from movies. The final result is to be able to use the terminal and send the following inquires:

During the period 2016 to 2006:

1) Insert film (generic name) in the terminal as a flag and be able to give the 10 most lucrative movies (per revenues - Million of USD), 
the 10 most popular movies (showing votes) and the 10 best rated movies by IMDb

2) Insert director (generic name) and be able to give the 10 most lucrative directors by revenues, 
the list of all directors who have won the Oscars and how many prizes they won

3) Insert producer (generic name) and be able to give the top 10 producing companies by revenues and by amount of movies released 

4) Insert a year and be able to show the amount of money collected by all the movies from that given year 

ORGANISATION OF FILES 

Files are organised as follow:

Input - were two initial CSV files are hosted IMBd and movie producers that will be manipulated to obtain a clean and transform database 
Output - clean and transformed database called database, the result of the work of manipulating CSV files and perform web scraping 
SRC- a series of .py files where python functions have been coded which serve for various tasks such as:
a) clean IMBd and movie producers CSV files
b) scrap (called api) two websites https://www.filmsite.org/bestdirs2.html and https://www.today.com/popculture/complete-list-every-best-picture-oscar-winner-ever-t107617
c) get the relevant information (queries) from the database
d) check if the user has introduced the right flag and has petioned the information from right period
e) obtain and store the database in CSV and call it and pass it to json and transform it into a panda dataframe 
Main.PY - were the ARGPARSE and PIPELINE are coded

WORK PERFORMED 

Initial databases from Keggle and manipulation:

The information I have downloaded from Keggle. It refers to two CSV files which are: IMDb database and movie producers. 
Both files are required to extract information, merge them and improve the merged database with scraping two websites. 
From the IMDb.csv we have to take: title, director, year, revenue (millions), rating, votes from 2016 to 2010 (included)
From the file Movie Producers.csv file we ONLY take production company to be able to join the the IMDb file.

Scraping: 
In terms of additional information to enrich the database and to scrap from internet:

1/ If movie won oscar best movie 
2/ If director has ever won an oscar and how many (so accumulated if yes)

Links where to scrap which I have selected: 

https://www.filmsite.org/bestdirs2.html

https://www.today.com/popculture/complete-list-every-best-picture-oscar-winner-ever-t107617





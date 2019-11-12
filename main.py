import argparse

from src.data import get_film_data, get_director_data, get_producer_data, get_year_data
from src.helpers import check_arguments, check_year
from src.output import print_results, Color


def parse_arguments():
    parser = argparse.ArgumentParser(description='Get movies information')
    parser.add_argument('--film', action='store_true', help='get the 10 most lucrative, rated and popular movies')
    parser.add_argument('--director', action='store_true', help='get the 10 most lucrative directors, and those who won an Oscar')
    parser.add_argument('--producer', action='store_true', help='get the 10 most lucrative producers and those who have more movies')
    parser.add_argument('--year', type=int, nargs='?', help='amount of money collected by all the movies from that year')
    args = parser.parse_args()
    check_arguments(args)
    return args



def get_movies():

#Generates the movie report and prints it to the console
    print_results(get_film_data())


def get_director():
#Generates the directors report and prints it to the console

    print_results(get_director_data())


def get_producer():

#Generates the producer report and prints it to the console
    print_results(get_producer_data())


def get_year(year):
#Gets the year revenue and prints it to the console

    print()
    print(f"{Color().parse(f'Total revenue for year {year}', Color().RED, False)}: "
          f"{Color().parse(f'{get_year_data(year)}', Color().BLACK, True)}")
    print()


def main():
    args = parse_arguments()
    if args.film:
        get_movies()
    elif args.director:
        get_director()
    elif args.producer:
        get_producer()
    elif args.year:
        check_year(args.year)
        get_year(args.year)
       

if __name__ == '__main__':
    main()

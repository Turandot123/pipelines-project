import argparse
import sys


def check_arguments(args: argparse.Namespace):
#Check if the user has not passed a flag or if he/she tries to pass multiple flags to the program and abort
#execution if that happens, with a descriptive message

    found_arg = False
    for arg in [args.film, args.director, args.producer, args.year]:
        if arg:
            if found_arg:
                sys.exit('only one argument flag allowed')
            found_arg = True
    if not found_arg:
        sys.exit('at least an execution flag is needed')


def check_year(year: int):
#Check if the year is between the valid values accepted by the program and abort execution if not
 
    if year < 2006 or year > 2016:
        sys.exit('only years between 2010 and 2017 are allowed')




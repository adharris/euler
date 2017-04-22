
import click
from datetime import date
from datetime import timedelta

@click.command('19')
@click.option('--start-year', '-s', type=int, default=1901)
@click.option('--end-year', '-e', type=int, default=2000)
def problem_019(start_year, end_year):
    """Counting Sundays

    You are given the following information, but you may prefer to do some
    research for yourself.
    
      * 1 Jan 1900 was a Monday.
      * Thirty days has September,  
        April, June and November.  
        All the rest have thirty-one,  
        Saving February alone,  
        Which has twenty-eight, rain or shine.  
        And on leap years, twenty-nine.
      * A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
    
    How many Sundays fell on the first of the month during the twentieth
    century (1 Jan 1901 to 31 Dec 2000)?
    """

    # Cheat. I don't do date math.

    first_day = date(start_year, 1, 1)
    last_day = date(end_year, 12, 31)
    day = first_day
    one_day = timedelta(days=1)
    sundays = 0

    while day <= last_day:
      day += one_day
      sundays += 1 if day.day == 1 and day.weekday() == 6 else 0
    
    click.echo("{} Sundays between {} and {}".format(sundays, first_day, last_day))
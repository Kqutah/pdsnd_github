import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    City=input('Choose a city(Chicago,New York city, or Washington): ')
    city=City .lower()
    while city not in CITY_DATA:
        print('please type one of the listed city')
        City=input('Choose a city(Chicago,New York city, or Washington): ')
        city=City .lower()

    file=CITY_DATA[city]
    rdf=pd.read_csv(file)
    rdf['Start Time']= pd.to_datetime(rdf['Start Time'])
    rdf['str_month']=rdf['Start Time'] .dt.month
    rdf['str_day_of_week']=rdf['Start Time'] .dt.weekday_name
    rdf['str_hour']=rdf['Start Time'] .dt.hour
    rdf['combine_station']=rdf['Start Station']+' and '+rdf['End Station']


    # TO DO: get user input for month (all, january, february, ... , june)
    months=input('Choose name of month (january,february,...,december) or type "all" : ')
    month=months .lower()
    if month != 'all':
        Month=['january', 'february', 'march', 'april', 'may', 'june','july','august','september','october','november','december']
        month=Month.index(month)+1
        rdf=rdf[rdf['str_month'] == month]


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days=input('Choose number of the day in a week (sunday=1,...,saturday=7)  or type "all" :')
    day=days.title()
    if day != 'All':
        rdf=rdf[rdf['str_day_of_week'] == day]



    print('-'*40)
    return city, month, day



def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        rdf - Pandas DataFrame containing city data filtered by month and day
    """
    file=CITY_DATA[city]
    rdf=pd.read_csv(file)
    rdf['Start Time']= pd.to_datetime(rdf['Start Time'])
    rdf['str_month']=rdf['Start Time'] .dt.month
    rdf['str_day_of_week']=rdf['Start Time'] .dt.weekday_name
    rdf['str_hour']=rdf['Start Time'] .dt.hour
    rdf['combine_station']=rdf['Start Station']+' '+rdf['End Station']

    return rdf


def time_stats(rdf):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('the most common month :' ,rdf['str_month'].mode()[0])

    # TO DO: display the most common day of week
    print('the most common day of week :',rdf['str_day_of_week'].mode()[0])

    # TO DO: display the most common start hour
    print('the most common start hour',rdf['str_hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(rdf):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('ost commonly used start station :',rdf['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print('most commonly used end station :',rdf['End Station'] .mode()[0])


    # TO DO: display most frequent combination of start station and end station trip
    print('most frequent combination of start station and end station trip :',rdf['combine_station'] .mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(rdf):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('total travel time :',rdf['Trip Duration'] .sum())

    # TO DO: display mean travel time
    print('average travel time:',rdf['Trip Duration'] .mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(rdf):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('counts of user types :\n',rdf['User Type'] .value_counts())

    # TO DO: Display counts of gender
    if 'Gender' in rdf:
        print('counts of gender :\n',rdf['Gender'] .value_counts())
    else:
        print('no gender column in this city data')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in rdf:
        print('earlist year of birth: ',rdf['Birth Year'] .min())
        print('most recent yaer of birth : ',rdf['Birth Year'] .max())
        print('most common year of birth : ',rdf['Birth Year'] .mode()[0])
    else:
        print('no birth year column in this city data')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)




def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)


        view_data=input('Do you want to view  5 rows of the data? type yes or no : ') .lower()
        start_data=0
        while view_data == 'yes':
            start_data+=5
            print(df.head(start_data))
            view_data=input('DO you want to view more 5 rows of the data? Type yes or no : ')


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

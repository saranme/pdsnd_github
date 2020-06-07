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
    while True:
        try:
            city = input('Would you like to see data for Chicago, New York City, or Washington? ').lower()
            if city.title() in ['Chicago','New York City','Washington']:
                break
        except:
            print('That\'s not a valid name')

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = input('Would you like to filter data by month or would you like to see all? Specify month or all: ')
            #convertir month en número
            months = ['January','February','March','April','May','June']
            if month.title() in months or month == 'all':
                break
        except:
            print('That\'s not a valid month')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input('Which day? ')
            days_of_week = ['Monday','Tuesday','Wedenesday','Thursday','Friday','Saturday','Sunday']
            if day.title() in days_of_week or day == 'all':
                break
        except:
            print('That\'s not a valid day')
#return city.title(), months.index(month.title()) +1, day_of_week.title(),
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
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        months = ['January','February','March','April','May','June']
        month = months.index(month.title()) + 1
        df = df[df['month']== month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    month = df['month'].mode()[0]
    months = ['January','February','March','April','May','June']
    month = months[month -1]
    print('Most common month is {}'.format(month))

    # TO DO: display the most common day of week
    day = df['day_of_week'].mode()[0]
    print('Most common day is {}'.format(day))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most common start hour is {}'.format(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    s_station = df['Start Station'].mode()[0]
    print('Most commonly used start station is {}'.format(s_station))

    # TO DO: display most commonly used end station
    e_station = df['End Station'].mode()[0]
    print('Most commonly used end station is {}'.format(e_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['Combination'] = df['Start Station'] + " - " + df['End Station']
    combination = df['Combination'].mode()[0]
    print('Most frequent combination of stations are {}'.format(combination))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum() / 3600
    print('Total travel time is {} hours'.format(total_travel_time))

    # TO DO: display mean travel time
    avg_travel_time = df['Trip Duration'].mean() / 60
    print('Average travel time is {} minutes'.format(avg_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts_users = df['User Type'].value_counts()
    print('Counts of user types:\n {}\n'.format(counts_users))

    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender = df['Gender'].value_counts()
        print('\n Counts of gender:\n {}\n'.format(gender))

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest = int(df['Birth Year'].min())
        recent = int(df['Birth Year'].max())
        common = int(df['Birth Year'].mode()[0])
        print('\n Earliest year is {}.\n Most recent year is {}.\n Most common year is {}.\n'.format(earliest,recent,common))

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

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

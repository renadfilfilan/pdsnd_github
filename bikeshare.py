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
    city = input('Enter name of city: ').lower()
    while city not in ['chicago','new york city','washington']:
        city = input('Not a valid input. Enter name of city: ').lower()
   
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Enter name of month: ').lower()
    while month not in ['all','january','february','march','april','may','june']:
        month = input('Not a valid input. Enter name of month: ').lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Enter day of week: ').lower()
    while day not in ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']:
        day = input('Not a valid input. Enter day of week: ').lower()
        
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
    df = pd.read_csv(CITY_DATA.get(city))
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('Most Common Month of Travel is: ', common_month) 

    # TO DO: display the most common day of week
    common_day = df['day'].mode()[0]
    print('Most Common Day of Travel is: ', common_day) 

    # TO DO: display the most common start hour
    common_hour = df['hour'].mode()[0]
    print('Most Common Hour of Travel is: ', common_hour) 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_sstation = df['Start Station'].mode()[0]
    print('Most Common Start Station of Travel is: ', common_sstation) 

    # TO DO: display most commonly used end station
    common_estation = df['End Station'].mode()[0]
    print('Most Common End Station of Travel is: ', common_estation) 

    # TO DO: display most frequent combination of start station and end station trip
    common_comb = (df['Start Station'] + ' to ' + df['End Station']).mode()[0]
    print('Most Common Combination of Start and End Stations are: ', common_comb) 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print('Total Travel Time is: %s seconds' % total_travel)
    
    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print('Average Travel Time is: %s seconds' % mean_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    type_count = df['User Type'].value_counts()
    print('Count of User Types is: \n',type_count)

    # TO DO: Display counts of gender
    try:
        gender_count = df['Gender'].value_counts()
        print('\nCount of Gender is: \n',gender_count)
    except:
        print('No gender data available')
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest = int(df['Birth Year'].min())
        print('\nEarliest Year of Birth is: ',earliest)
        recent = int(df['Birth Year'].max())
        print('Most Recent Year of Birth is: ',recent)
        common_birth = int(df['Birth Year'].mode()[0])
        print('Most Common Year of Birth is: ',common_birth)
    except:
        print('No birth year data available')
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    i = 0
    raw = input('Would like to see the first 5 rows of raw data? ').lower() # TO DO: convert the user input to lower case using lower() function
    pd.set_option('display.max_columns',5)

    while True:            
        if raw == 'no':
            break
        elif raw == 'yes':
            print(df[i:i+5]) # TO DO: appropriately subset/slice your dataframe to display next five rows
            raw = input('Would you like to see the next 5 rows? ').lower() # TO DO: convert the user input to lower case using lower() function
            try:
                if raw == 'no':
                    break
                elif raw == 'yes':
                    i += 5
                else:
                    raw = input("\nYour input is invalid. Please enter only 'yes' or 'no'\n").lower()
            except:
                print('No more raw data to display.')
        else:
            raw = input("\nYour input is invalid. Please enter only 'yes' or 'no'\n").lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() == 'no':
            break
        elif restart.lower() != 'yes':
            while restart.lower() != 'yes' and restart.lower() != 'no':
                restart = input('\nInvalid input. Would you like to restart? Enter yes or no.\n')


if __name__ == "__main__":
	main()

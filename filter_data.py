import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def load_data(city, month, day):

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    df['trip'] = df['Start Station'] + ' - ' + df['End Station']

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def stats1(filter):
    print("\n**************\nCalculating first statistics...")
    mode = new_df['hour'].mode()[0] #calculates peak hour
    n = (new_df.hour.values == mode).sum() #counts trips done in peak hour
    print("Most popular hour: ",mode, "\nCount: ",n, "\nfilter:" ,filter)

city = input("Choose city among chicago, new york or washington : ")
flag = input("Would you like to filter the data by month, day, both or none? ")


if flag == 'month':
    month = input("Which month january, february, march, april, may or june? ")
    new_df = load_data(city, month, 'all')
    stats1(flag)
    
elif flag == 'day':
    day = input("Which day sunday, monday, tuesday, wednesday, thursday, friday, saturday or sunday? ")
    new_df = load_data(city, 'all', day)
    stats1(flag)
    
elif flag == 'both':
    month = input("Which month january, february, march, april, may or june? ")
    day = input("Which day sunday, monday, tuesday, wednesday, thursday, friday, saturday or sunday? ")
    new_df = load_data(city, month, day)
    stats1(flag)
    
elif flag == 'none':
    new_df = load_data(city, 'all', 'all')
    stats1(flag)
    
else :
    print("Please provide a valid input...")




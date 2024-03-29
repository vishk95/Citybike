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

def novice_stats(filter):
    print("\n**************\nCalculating first statistics...")
    mode = new_df['hour'].mode()[0] #calculates peak hour
    n = (new_df.hour.values == mode).sum() #counts trips done in peak hour
    print("Most popular hour: ",mode, "\nCount: ",n, "\nfilter:" ,filter)

def trip_duration(filter):
    print("\n**************\nCalculating next stats... Trip duration:")
    total = new_df['Trip Duration'].sum()
    n = new_df['Trip Duration'].count()
    avrg = new_df['Trip Duration'].mean()
    print("Total duration: ", total, "\nCount: ",n, "\nAvg. Duration: ", avrg, "\nfilter:" ,filter)

def station(filter):
    print("\n**************\nCalculating next stats... Popular station:")
    mode_start = new_df['Start Station'].mode()[0]
    mode_end = new_df['End Station'].mode()[0]
    print("\nStart Station : ",mode_start,", Count : ",(new_df['Start Station'].values == mode_start).sum(),"\nEnd Station : ",mode_end,", Count : ",(new_df['End Station'].values == mode_end).sum(),"\nFilter : ",filter)

def popular_trip(filter):
    print("\n**************\nCalculating next stats... Popular Trip:")
    mode_trip = new_df['trip'].mode()[0]
    print("\nTrip: ", mode_trip, ", Count: ", (new_df.trip.values == mode_trip).sum(), "\nFilter :" ,filter)

def user_type(filter):
    print("\n**************\nCalculating next stats... Gender:")
    print("\nMale: ", (new_df.Gender.values == 'Male').sum(), "\nFemale: ", (new_df.Gender.values == 'Female').sum(),"\nSubscribers: ", (new_df['User Type'].values == 'Subscriber').sum(),"\nCustomer: ", (new_df['User Type'].values == 'Customer').sum(),"\nFilter :" ,filter)
    print("\n**************\nCalculating next stats... Year of Birth:")
    print("\nEldest user: ", new_df['Birth Year'].min())
    print("Most recent user: ", new_df['Birth Year'][new_df['Start Time'] == new_df['Start Time'].min()].values)
    print("Most common year of birth: ", new_df['Birth Year'].mode()[0])

def calculate(filter):
    novice_stats(filter)
    trip_duration(filter)
    station(filter)
    popular_trip(filter)
    user_type(filter)

city = input("\nChoose city among chicago, new york or washington : ")
flag = input("\nWould you like to filter the data by month, day, both or none? ")

if flag == 'month':
    month = input("Which month january, february, march, april, may or june? ")
    new_df = load_data(city, month, 'all')
    calculate(flag)
    
elif flag == 'day':
    day = input("Which day sunday, monday, tuesday, wednesday, thursday, friday, saturday or sunday? ")
    new_df = load_data(city, 'all', day)
    calculate(flag)
    
elif flag == 'both':
    month = input("Which month january, february, march, april, may or june? ")
    day = input("Which day sunday, monday, tuesday, wednesday, thursday, friday, saturday or sunday? ")
    new_df = load_data(city, month, day)
    calculate(flag)
    
elif flag == 'none':
    new_df = load_data(city, 'all', 'all')
    calculate(flag)
    
else :
    print("Please provide a valid input...")

for ind in new_df.index:
    print("\n****************************\nStart Time: ",new_df['Start Time'][ind],"\nEnd Time: ",new_df['End Time'][ind],"\nTrip Duration: ",new_df['Trip Duration'][ind],"\nStart Station: ",new_df['Start Station'][ind],"\nEnd Station: ",new_df['End Station'][ind],"\nUser Type: ",new_df['User Type'][ind],"\nGender: ",new_df['Gender'][ind],"\nBirth Year: ",new_df['Birth Year'][ind],"\n************************")
    if ind % 5 == 0 :
        permit = input("Do you want to see 5 more? (y/n)")
        if permit == 'n':
            break



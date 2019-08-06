#Use pandas to load chicago.csv into a dataframe, and find the most frequent hour when people start traveling. There isn't an hour column in this dataset, but you can create one by extracting the hour from the "Start Time" column. To do this, you can convert "Start Time" to the datetime datatype using the pandas to_datetime() method and extracting properties such as the hour with these properties.
import pandas as pd

# load data file into a dataframe
df = pd.read_csv('./chicago.csv')

# convert the Start Time column to datetime
df['Start Time'] = pd.to_datetime(df['Start Time'])

# extract hour from the Start Time column to create an hour column
df['hour'] = df['Start Time'].dt.hour

# find the most common hour (from 0 to 23)
popular_hour = df['hour'].mode()[0]

print('Most Frequent Start Hour:', popular_hour)
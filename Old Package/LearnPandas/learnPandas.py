import pandas as pd

df = pd.read_csv('responses.csv', low_memory=False)

df['year'] = pd.DatetimeIndex(df['created_time']).year
# print(df.columns)

# print(df['brand_name'].tail(5))

# print(df.iloc[0:4])

#  Iterate over Row
# for index, row in df.iterrows():
#     print(index, row['brand_name'])

#  Specific Search
# print(df.loc[df['brand_name'] == 'Zenarate'])

# print(df.describe())

# print(df.sort_values('brand_name'))                           Sort in ascending order
# print(df.sort_values('brand_name' , ascending=False))         Sort in descending order
# print(df.sort_values(['id', 'brand_name'], ascending=False))  # Sort in descending order

# df['new_col'] = df['id'] + df['session_id'] + df['story_id']  # To create new Column

# df = df.drop['new_column']   # To drop the column
# df['new_col'] = df.iloc[:,4,10].sum(axis=1)    # To create a new column which has sum of col from 4 to 9

#          TO REFRAME THE COLUMNS OF THE TABLE
# cols = df.list(df.columns)
# df = df[cols[0:4] + [cols[-1]] + cols[4:12]]

#           To save the csv file
# df.to_csv('file_name.csv')                    # with index
# df.to_csv('file_name.csv', index = False)     # without index
# df.to_excel('file_name.xls')   # To save the file as a excel file

#       To Filter the data
# new_df = df.loc[df['brand_name'] == 'Zenarate']
# new_df = df.loc[(df['brand_name'] == 'Zenarate') & (df['brand_name'] == 'Naehas')]
# new_df = df.loc[(df['brand_name'] == 'Zenarate') & (df['brand_name'] == 'Naehas') & (df[id] > 50)]

# print(df.loc[df['brand_name'].str.contains('rate')])  # To fetch all the rows in which row column name contains 'rate'
# print(~ df.loc[df['brand_name'].str.contains('rate')])  # To fetch all the rows in which row column name not contains 'rate'

# df.loc(df['brand_name'].str.contains('Zenarate | Bank of America', regex = True))  # To filter multiple columns data
# df.loc(df['brand_name'].str.contains('Zenarate | Bank of America',flags=re.I, regex = True))   # to ignore upper or lower case

# df.loc[df['brand_name']=='Zenarate' , 'meta_data'] = 'null'  # Conditional Changes


# Aggregate Functions

# df.groupby(['id']).mean().sort_values('brand_name', ascending=False)
# df.groupby(['id']).sum()
# df.groupby(['id']).count()

# print(df.groupby(['brand_name']).count()['user_id'])

# Index(['brand_id', 'brand_name', 'id', 'story_id', 'user_id', 'video_id',
#        'node_key', 'bot_response_id', 'bot_response_text',
#        'agent_response_text', 'weight', 'bot_audio_clip', 'audio_clip',
#        'created_time', 'isUploaded', 'isEncoded', 'isReviewed', 'metaData'],
#       dtype='object')

# grouped1 = df.groupby(['year', 'brand_name']).agg({'user_id': 'sum', 'story_id': 'sum', 'id': 'sum', 'node_key': 'sum'})
# group1 = grouped1[['user_id', 'story_id', 'id', 'node_key']]
# print(group1)

# grouped2 = df.groupby(['year', 'brand_name', 'user_id']).agg({'story_id': 'sum', 'id': 'sum', 'node_key': 'sum'})
# group2 = grouped2[['story_id', 'id', 'node_key']]
# print(group2)
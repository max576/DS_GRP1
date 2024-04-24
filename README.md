# DS_GRP1
Project 1: Geographic Sentiment Distribution of Trending Social Media Topics 

Links to google docs:  
https://docs.google.com/document/d/12y5kILSYFMcIpSWvk6qfEF4lb7wT_IQq8h0Obh826iU/edit?usp=sharing
https://docs.google.com/document/d/1tIbfGKZuO1QhW3nz2VZIhd6uOZD1VC3KJoK7be7fcJI/edit

To Run the dashboard, you will need to download and put the following files into the same folder:
executable.py
data_funcs.py
textfunction_for_dash.py
master.csv

By default, the master dataset does not include the covid data. If you want the covid dataset, you will need to download:
Data (folder)
data_reformat.py

To make the covid dataset part of the master dataset, just run data_reformat.py then proceed as usual to the dashboard.



To run the dashboard, you will need to run executable.py and follow its instructions.
The instructions will tell you to input filters to reduce the dataset. Here is an explaination of all of the filter options:

To not compare, the filter should look like this:
1 dataset platform place year month day hour minute second sentiment

To compare datasets, the first filter should look like this:
2 dataset platform place year month day hour minute second sentiment

And the second should look like this:
dataset platform place year month day hour minute second sentiment


All values should be separated by one space and should be taken from the following list:
(Note that for every parameter, 'all' is an option and, when used, it will not filter down that parameter)
dataset: 0) covid, 1)Afghanistan (Youtube), 2) Biden Tweets, 3) Biden Youtube, 4) Biden reelection (Youtube)
        5) Impeachment speech (Youtube), 6) Trump Tweets, 7) Trump Youtube, 8) Trump reelection (Youtube)
platform: 0) Twitter, 1) Youtube
place: Specific place name
year: 2019 - 2024
month: 1 - 12
day: 1 - 31
hour: 0 - 23
minute, second: 0 - 59
sentimemt: Any float between -1 and 1

# DS_GRP1
Project 1: Geographic Sentiment Distribution of Trending Social Media Topics 

Links to google docs:  
https://docs.google.com/document/d/12y5kILSYFMcIpSWvk6qfEF4lb7wT_IQq8h0Obh826iU/edit?usp=sharing
https://docs.google.com/document/d/1tIbfGKZuO1QhW3nz2VZIhd6uOZD1VC3KJoK7be7fcJI/edit

Before running the dashboard, you may need to install the python wordcloud module. You will need to run:

_pip install wordcloud_

To Run the dashboard, you will need to download and put the following files into the same folder:

_executable.py_

_data_funcs.py_

_textfunction_for_dash.py_

_master.csv_

By default, the master dataset does not include the covid data. If you want the covid dataset, you will need to download:

_Data (folder)_

_data_reformat.py_

To make the covid dataset part of the master dataset, just run data_reformat.py then proceed as usual to the dashboard.



To run the dashboard, you will need to run executable.py and follow its instructions.
The instructions will tell you to input filters to reduce the dataset. Here is an explaination of all of the filter options:

To not compare, the filter should look like this:

_1 dataset platform place year month day hour minute second sentiment_

To compare datasets, the first filter should look like this:

_2 dataset platform place year month day hour minute second sentiment_

And the second should look like this:

_dataset platform place year month day hour minute second sentiment_


All values should be separated by one space and should be taken from the following list
(Note that for every parameter, 'all' is an option and, when used, it will not filter down that parameter):

dataset: _0) covid, 1) Afghanistan (Youtube), 2) Biden Tweets, 3) Biden Youtube, 4) Biden reelection (Youtube) 5) Impeachment speech (Youtube), 6) Trump Tweets, 7) Trump Youtube, 8) Trump reelection (Youtube)_
        
platform: _0) Twitter, 1) Youtube_

place: Specific place name

year: _2019 - 2024_

month: _1 - 12_

day: _1 - 31_

hour: _0 - 23_

minute, second: _0 - 59_

sentimemt: Any float between _-1_ and _1_

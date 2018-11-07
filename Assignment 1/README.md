 # Topic:

News from The Associated Press's Website

# Data Source:
This dataset contains the news information from AP's website.
[https://www.apnews.com](https://www.apnews.com/)
# Data Field:
1. ```Title``` - String e.g. **Massachusetts backs transgender rights; Michigan OKs pot use**
2. ```Tag``` - String e.g. **Immigration**
3. ```Author```- String e.g. **JONATHAN LEMIRE, CATHERINE LUCEY and ZEKE MILLER**
4. ```Storylink``` - String e.g. **/705ae08bd6f44012b564b0f37b5ca089**
5. ```Time``` - String e.g. **November 6, 2018**
# Data Volume:

# License:
CC 4.0
# Obstacles and Solutions:
At first, I found that AP does not make all of its articles available for public and free use. So, I can just scrap the news data on one day. And, the news changes every day, I need to store the data I scraped yesterday and add the data I scrape today into it. 

After discussing with my groupmate, we found the csv file is appendable. When we appended it, we found there are too many data are repeated in the csv file because the news refreshes from time to time.

So, after studying the pandas, we know how to wipe the repeated data. But still, we found that the same news has different tags. Wiping again, finally we get the cleaned dataset.

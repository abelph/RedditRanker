# Reddit Ranker Code Explanation

## Extracting Data
### zst_extract.py
Use this file to extract data from pushshift.io zst files. You will need to replace the read and write paths with paths that you desire.

## Getting User-to-User Network
In main.py make sure build_network() is uncommented.

In json_reader.py, change the max value to the desired number of posts you want to look at. Change the path to where you have stored data.

Run main.py and it will output a gexf file.

## Getting Subreddit-to-Subreddit Network
In json_reader.py, change the max value to the desired number of posts you want to look at. Change the path to where you have stored data.

In main.py, uncomment get_user_activity() and build_activity_network(). Run main.py and it will output two gexf files.

## Getting User Leanings
Follow the steps above to get the subreddit-to-subreddit networks.

In main.py, uncomment assign_user_leanings(). Run main.py and it will output a JSON file with the user leanings.

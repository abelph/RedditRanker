import json
import praw


def get_political_submissions():
    approvedSubreddits = ['t5_2cneq']
    submissions = []
    i = 0
    for line in open("C:/Users/abelp/Documents/Classes/Networks/Data/RS_2019-09", 'r'):
        j = json.loads(line)
        if j['subreddit_id'] in approvedSubreddits:
            submissions.append(j)
            i += 1
            if i >= 20:
                break

    reddit = praw.Reddit(
        user_agent="Comment Extraction",
        client_id="etDodny8ugn-bhb5NQ20Vw",
        client_secret="BCD96zi9uth7HDNG7gqKvbqw13mjAg",
    )

    posts = []
    for sub in submissions:
        try:
            posts.append(reddit.submission(id=sub['id']))
        except:
            print("Unable to access post: " + sub)
    return posts

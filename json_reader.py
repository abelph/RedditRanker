import json
import praw


def get_political_submissions():
    approvedSubreddits = ['t5_2cneq', 't5_2qh31', 't5_2qh6p', 't5_2tk0i', 't5_2qh1s', 't5_2qgzy', 't5_mouw', 't5_2qh16', 't5_2qh0f', 't5_2qh2p', 't5_2r5rp', 't5_2qh1n', 't5_2qh9z', 't5_2qh13', 't5_2x4yx']
    submissions = []
    min = 0
    max = 300
    i = 0
    for line in open("C:/Users/Abel/Documents/Classes/Networks/Data/RS_2019-09", 'r'):
        j = json.loads(line)
        if j['subreddit_id'] in approvedSubreddits:
            if i > min:
                submissions.append(j)
                if i >= max:
                    break
            i += 1

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

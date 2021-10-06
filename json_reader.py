import json
import praw

comments = []
i = 0
for line in open("C:/Users/abelp/Documents/Classes/Networks/Data/RS_2019-09", 'r'):
    comments.append(json.loads(line))
    i += 1
    if i >= 10000:
        break

num = 160
print(comments[num])

reddit = praw.Reddit(
    user_agent="Comment Extraction",
    client_id="etDodny8ugn-bhb5NQ20Vw",
    client_secret="BCD96zi9uth7HDNG7gqKvbqw13mjAg",
)

submission = reddit.submission(id = str(comments[num]['id']))
#comment = reddit.comment(id='hfl96kv')
print(submission.subreddit)
print(submission.comments.list())
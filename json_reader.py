import json
import praw

approvedSubreddits = ['t5_2cneq']
submissions = []
i = 0
for line in open("C:/Users/abelp/Documents/Classes/Networks/Data/RS_2019-09", 'r'):
    j = json.loads(line)
    if j['subreddit_id'] in approvedSubreddits:
        submissions.append(j)
        i += 1
        if i >= 10000:
            break

num = 69
print(submissions[num])

reddit = praw.Reddit(
    user_agent="Comment Extraction",
    client_id="etDodny8ugn-bhb5NQ20Vw",
    client_secret="BCD96zi9uth7HDNG7gqKvbqw13mjAg",
)

submission = reddit.submission(id = str(submissions[num]['id']))
#comment = reddit.comment(id='hfl96kv')
print(submission.subreddit)
print(submission.comments[2].body)
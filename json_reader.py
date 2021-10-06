import json
import praw

comments = []
i = 0
for line in open("C:/Users/abelp/Documents/Classes/Networks/Data/RS_politics_2016/RS_politics_2016.json", 'r'):
    comments.append(json.loads(line))
    i += 1
    if i >= 10000:
        break

num = 10
print(comments[num])

reddit = praw.Reddit(
    user_agent="Comment Extraction",
    client_id="etDodny8ugn-bhb5NQ20Vw",
    client_secret="BCD96zi9uth7HDNG7gqKvbqw13mjAg",
)

comment = reddit.comment(id=str(comments[num]['id']))
#print(comment.parent())
import json
from dataclasses import dataclass
from json_reader import get_political_submissions
from vars import banned_users

@dataclass
class UserActivity:
    name: str
    subscribed: {}
    most_active: str

users = {}

def get_user_activity():
    posts = get_political_submissions()
    for post in posts:
        print("Reading Post")
        if post.author is not None and post.author.name not in users:
            users[post.author.name] = {post.subreddit.display_name: 1}
        elif post.author is not None and post.subreddit.display_name not in users[post.author.name]:
            users[post.author.name][post.subreddit.display_name] = 1
        elif post.author is not None:
            users[post.author.name][post.subreddit.display_name] += 1

        post.comments.replace_more(limit=None)
        for comment in post.comments.list():
            if comment.author is not None and comment.parent().author is not None:
                if comment.author.name not in banned_users and comment.parent().author.name not in banned_users:
                    # add commenter if he is not already in subreddit list
                    if comment.author.name not in users:
                        users[comment.author.name] = {post.subreddit.display_name: 1}
                    elif post.subreddit.display_name not in users[comment.author.name]:
                        users[comment.author.name][post.subreddit.display_name] = 1
                    else:
                        users[comment.author.name][post.subreddit.display_name] += 1

    #store as a json file
    js = json.dumps(users)
    f = open("user_activity.json", "w")
    f.write(js)
    f.close()

def grow_user_activity():
    global users
    with open("user_activity.json") as activity_file:
        users = json.load(activity_file)
        print("Read activity file")
        get_user_activity()


def rate_user_activity():
    with open("user_activity.json") as activity_file:
        users = json.load(activity_file)
        print("Read file")
        activity = {}
        for user in users:
            total = 0
            activity[user] = {}
            for sub in users[user]:
                total += users[user][sub]
            for sub in users[user]:
                activity[user][sub] = users[user][sub] / total
        return activity

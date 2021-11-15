import networkx as nx
import praw
from json_reader import get_political_submissions
from user_activity import rate_user_activity
from vars import banned_users

reddit = praw.Reddit(
    user_agent="Comment Extraction",
    client_id="etDodny8ugn-bhb5NQ20Vw",
    client_secret="BCD96zi9uth7HDNG7gqKvbqw13mjAg",
)

S = nx.DiGraph()


def build_activity_network():
    activity = rate_user_activity()
    posts = get_political_submissions()
    for post in posts:
        if post.author is not None and post.author.name in activity:
            for sub in activity[post.author.name]:
                if sub != post.subreddit.display_name and activity[post.author.name][sub] > .25:
                    if S.has_edge(sub, post.subreddit.display_name):
                        if post.score > 0:
                            S[sub][post.subreddit.display_name]['weight'] += 1
                        else:
                            S[sub][post.subreddit.display_name]['weight'] -= 1
                    else:
                        S.add_edge(sub, post.subreddit.display_name, weight=0)
                        if post.score > 0:
                            S[sub][post.subreddit.display_name]['weight'] = 1
                        else:
                            S[sub][post.subreddit.display_name]['weight'] = -1

        post.comments.replace_more(limit=None)
        for comment in post.comments.list():
            if comment.author is not None and comment.parent().author is not None:
                if comment.author.name not in banned_users and comment.parent().author.name not in banned_users:
                    for sub in activity[comment.author.name]:
                        if sub != post.subreddit.display_name and activity[comment.author.name][sub] > .25:
                            if S.has_edge(sub, post.subreddit.display_name):
                                if comment.score > 0:
                                    S[sub][post.subreddit.display_name]['weight'] += 1
                                else:
                                    S[sub][post.subreddit.display_name]['weight'] -= 1
                            else:
                                S.add_edge(sub, post.subreddit.display_name, weight=0)
                                if comment.score > 0:
                                    S[sub][post.subreddit.display_name]['weight'] = 1
                                else:
                                    S[sub][post.subreddit.display_name]['weight'] = -1

    nx.write_gexf(S, "activity.gexf")

def grow_activity_network:
    S = nx.read_gexf("activity.gexf")
    print("Read network")
    build_activity_network()
# def build_subreddit_network():
#     posts = get_political_submissions()
#     users = {}
#     for post in posts:
#         if post.author is not None and post.author.name not in users:
#             users[post.author.name] = [post.subreddit.display_name]
#         elif post.author is not None and post.subreddit.display_name not in users[post.author.name]:
#             users[post.author.name].append(post.subreddit.display_name)
#
#         #go through comments
#         post.comments.replace_more(limit=None)
#         for comment in post.comments.list():
#             #add commenter if he is not already in subreddit list
#             if comment.author is not None and comment.author.name not in users:
#                 users[comment.author.name] = [post.subreddit.display_name]
#             elif comment.author is not None and post.subreddit.display_name not in users[comment.author.name]:
#                 users[comment.author.name].append(post.subreddit.display_name)
#
#     for user in users:
#         print(users[user])
#         for i in range(len(users[user]) - 1):
#             if S.has_edge(users[user][i], users[user][i+1]):
#                 S[users[user][i]][users[user][i+1]]['weight'] += 1
#             else:
#                 S[users[user][i]][users[user][i + 1]]['weight'] = 1
#     nx.write_gexf(S, "subreddit_network.gexf")
import networkx as nx
import praw
from json_reader import get_political_submissions

reddit = praw.Reddit(
    user_agent="Comment Extraction",
    client_id="etDodny8ugn-bhb5NQ20Vw",
    client_secret="BCD96zi9uth7HDNG7gqKvbqw13mjAg",
)

G = nx.DiGraph()

banned_users = ["AutoModerator", "PoliticsModeratorBot"]


def build_network():
    posts = get_political_submissions()
    for post in posts:
        # if post.author is not None:
        # Add post author username as node if they are not in G
        if post.author is not None and not G.has_node(post.author.name):
            G.add_node(post.author.name)
        # Go through comments
        post.comments.replace_more(limit=None)
        for comment in post.comments.list():
            if comment.author is not None and comment.parent().author is not None:
                if comment.author.name not in banned_users and comment.parent().author.name not in banned_users:
                    if not G.has_node(comment.author.name):
                        G.add_node(comment.author.name)
                    if comment.parent().author.name != comment.author.name:
                        try:
                            G.add_edge(comment.author.name, comment.parent().author.name)
                        except:
                            print("Something went wrong with making an edge")
    print("Built network")
    nx.write_gexf(G, "reddit_network.gexf")

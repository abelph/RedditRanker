from network_builder import build_network
from network_builder import grow_network
from user_activity import get_user_activity
from user_activity import grow_user_activity
from user_activity import rate_user_activity
from subreddit_network import build_activity_network
from subreddit_network import grow_activity_network
from subreddit_labeler import assign_subreddit_leanings
from subreddit_labeler import assign_user_leanings

build_network()
#grow_user_activity()
get_user_activity()
#rate_user_activity()
build_activity_network()
#grow_activity_network()
#assign_subreddit_leanings()
assign_user_leanings()
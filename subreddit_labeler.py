import networkx as nx
import json
from enum import Enum
from user_activity import rate_user_activity

class Politics(Enum):
    LEFT = 1
    RIGHT = 2
    MODERATE = 3


def assign_subreddit_leanings():
    positive = nx.read_gexf("positive_activity.gexf")
    negative = nx.read_gexf("negative_activity.gexf")

    # total_pos_weight = 0
    # for e in positive.edges(data=True):
    #     total_pos_weight += e[2]['weight']
    #
    # total_neg_weight = 0
    # for e in negative.edges(data=True):
    #     total_neg_weight += e[2]['weight']
    leanings = {'Conservative': [-20, Politics.RIGHT], "democrats": [20, Politics.LEFT], 'politics': [20, Politics.LEFT],
                'prolife': [-20, Politics.RIGHT], 'prochoice': [20, Politics.LEFT], 'firearms': [-20, Politics.RIGHT],
                'liberalgunowners': [20, Politics.LEFT], 'Capitalism': [-20, Politics.RIGHT], 'socialism': [20, Politics.LEFT]}

    #sorted_edges = sorted(positive.edges(data=True), key=lambda t: t[2].get('weight', 1))
    for e in positive.edges(data=True):
        if e[0] in leanings:
            if e[1] not in leanings:
                leanings[e[1]] = [0, Politics.MODERATE]

            if e[2]['weight'] >= 200:
                if leanings[e[0]][1] == Politics.LEFT:
                    leanings[e[1]][0] += 3
                elif leanings[e[0]][1] == Politics.RIGHT:
                    leanings[e[1]][0] -= 3
                else:
                    if leanings[e[1]][1] == Politics.LEFT:
                        leanings[e[0]][0] += 3
                    elif leanings[e[1]][1] == Politics.RIGHT:
                        leanings[e[0]][0] -= 3
            elif e[2]['weight'] >= 100:
                if leanings[e[0]][1] == Politics.LEFT:
                    leanings[e[1]][0] += 2
                elif leanings[e[0]][1] == Politics.RIGHT:
                    leanings[e[1]][0] -= 2
                else:
                    if leanings[e[1]][1] == Politics.LEFT:
                        leanings[e[0]][0] += 2
                    elif leanings[e[1]][1] == Politics.RIGHT:
                        leanings[e[0]][0] -= 2
            elif e[2]['weight'] >= 20:
                if leanings[e[0]][1] == Politics.LEFT:
                    leanings[e[1]][0] += 1
                elif leanings[e[0]][1] == Politics.RIGHT:
                    leanings[e[1]][0] -= 1
                else:
                    if leanings[e[1]][1] == Politics.LEFT:
                        leanings[e[0]][0] += 1
                    elif leanings[e[1]][1] == Politics.RIGHT:
                        leanings[e[0]][0] -= 1
            else:
                if leanings[e[0]][1] == Politics.LEFT:
                    leanings[e[1]][0] += .5
                elif leanings[e[0]][1] == Politics.RIGHT:
                    leanings[e[1]][0] -= .5
                else:
                    if leanings[e[1]][1] == Politics.LEFT:
                        leanings[e[0]][0] += .5
                    elif leanings[e[1]][1] == Politics.RIGHT:
                        leanings[e[0]][0] -= .5
        elif e[1] in leanings:
            if e[0] not in leanings:
                leanings[e[0]] = [0, Politics.MODERATE]

            if e[2]['weight'] >= 200:
                if leanings[e[1]][1] == Politics.LEFT:
                    leanings[e[0]][0] += 3
                elif leanings[e[1]][1] == Politics.RIGHT:
                    leanings[e[0]][0] -= 3
            elif e[2]['weight'] >= 100:
                if leanings[e[1]][1] == Politics.LEFT:
                    leanings[e[0]][0] += 2
                elif leanings[e[1]][1] == Politics.RIGHT:
                    leanings[e[0]][0] -= 2
            elif e[2]['weight'] >= 20:
                if leanings[e[1]][1] == Politics.LEFT:
                    leanings[e[0]][0] += 1
                elif leanings[e[1]][1] == Politics.RIGHT:
                    leanings[e[0]][0] -= 1
            else:
                if leanings[e[1]][1] == Politics.LEFT:
                    leanings[e[0]][0] += .5
                elif leanings[e[1]][1] == Politics.RIGHT:
                    leanings[e[0]][0] -= .5

    for e in negative.edges(data=True):
        if e[0] in leanings:
            if e[1] not in leanings:
                leanings[e[1]] = [0, Politics.MODERATE]

            if e[2]['weight'] <= -6:
                if leanings[e[0]][1] == Politics.LEFT:
                    leanings[e[1]][0] -= 3
                elif leanings[e[0]][1] == Politics.RIGHT:
                    leanings[e[1]][0] += 3
                else:
                    if leanings[e[1]][1] == Politics.LEFT:
                        leanings[e[0]][0] -= 3
                    elif leanings[e[1]][1] == Politics.RIGHT:
                        leanings[e[0]][0] += 3
            elif e[2]['weight'] <= -3:
                if leanings[e[0]][1] == Politics.LEFT:
                    leanings[e[1]][0] -= 2
                elif leanings[e[0]][1] == Politics.RIGHT:
                    leanings[e[1]][0] += 2
                else:
                    if leanings[e[1]][1] == Politics.LEFT:
                        leanings[e[0]][0] -= 2
                    elif leanings[e[1]][1] == Politics.RIGHT:
                        leanings[e[0]][0] += 2
            else:
                if leanings[e[0]][1] == Politics.LEFT:
                    leanings[e[1]][0] -= 1
                elif leanings[e[0]][1] == Politics.RIGHT:
                    leanings[e[1]][0] += 1
                else:
                    if leanings[e[1]][1] == Politics.LEFT:
                        leanings[e[0]][0] -= 1
                    elif leanings[e[1]][1] == Politics.RIGHT:
                        leanings[e[0]][0] += 1
        if e[1] in leanings:
            if e[0] not in leanings:
                leanings[e[0]] = [0, Politics.MODERATE]

            if e[2]['weight'] <= -6:
                if leanings[e[1]][1] == Politics.LEFT:
                    leanings[e[0]][0] -= 3
                elif leanings[e[1]][1] == Politics.RIGHT:
                    leanings[e[0]][0] += 3
            elif e[2]['weight'] <= -3:
                if leanings[e[1]][1] == Politics.LEFT:
                    leanings[e[0]][0] -= 2
                elif leanings[e[1]][1] == Politics.RIGHT:
                    leanings[e[0]][0] += 2
            else:
                if leanings[e[1]][1] == Politics.LEFT:
                    leanings[e[0]][0] -= .5
                elif leanings[e[1]][1] == Politics.RIGHT:
                    leanings[e[0]][0] += .5

    for sub in leanings:
        if leanings[sub][0] < 0:
            leanings[sub][1] = Politics.RIGHT
        elif leanings[sub][0] > 0:
            leanings[sub][1] = Politics.LEFT

    print(str(leanings))
    return leanings


def assign_user_leanings():
    sub_leanings = assign_subreddit_leanings()
    activity = rate_user_activity()
    leanings = {}

    for user in activity:
        subs = sorted(activity[user].items(), key=lambda x: x[1], reverse=True)
        if subs[0][0] in sub_leanings:
            if sub_leanings[subs[0][0]][1] == Politics.LEFT:
                leanings[user] = "LEFT"
            elif sub_leanings[subs[0][0]][1] == Politics.RIGHT:
                leanings[user] = "RIGHT"
            else:
                leanings[user] = "MODERATE"

    # store as a json file
    js = json.dumps(leanings)
    f = open("user_leanings.json", "w")
    f.write(js)
    f.close()
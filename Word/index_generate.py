# index_generate.py

"""
Indexeintraege haben Form: Haupteintrag:Untereintrag1:Untereintrag2:...:Zieleintrag
"""


def generate_index(xe_list):

    index = {}
    # loop over all xe-entries
    for xe in xe_list:
        topic_list = xe.split(":")
        main_topic = topic_list[0]
        subtopic_list = topic_list[1:]
        if main_topic not in index:
            index[main_topic] = {}
            if subtopic_list:
                

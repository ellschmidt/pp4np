from random import randint
import copy

dict_en = {
    'noun': ['human being', 'morning', 'music', 'frame', 'rule', 'government', 'direction', 'role'],
    'adjective': ['possible', 'new', 'practical', 'correct'],
    'verb': ['like', 'use', 'plan']
}

story = (
    "A unicorn is nothing like a {}. " +
    "They're {} creatures. " +
    "Some have a {} mane of hair " +
    "and others have a {} {} on their head. " +
    "I would love to {} a unicorn one day."
)


def get_word(type, local_dict):
    words = local_dict[type]
    cnt = len(words) - 1
    index = randint(0, cnt)
    return local_dict[type].pop(index)

def create_story():
    dict = copy.deepcopy(dict_en)
    return story.format(
        get_word('noun', dict),
        get_word('adjective', dict),
        get_word('adjective', dict),
        get_word('adjective', dict),
        get_word('noun', dict),
        get_word('verb', dict)
    )

funnyAF1 = create_story()
funnyAF2 = create_story()

print(funnyAF1)
print(funnyAF2)

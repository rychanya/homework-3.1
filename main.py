import json


def load_descriptions_from_json():
    with open('newsafr.json', encoding='utf8') as file:
        data = json.load(file)
    return [item['description'] for item in data['rss']['channel']['items']]


def count_words(descriptions):
    words = {}
    for description in descriptions:
        description_words = filter(lambda word: len(word) > 6, description.split())
        for word in description_words:
            words.setdefault(word, 0)
            words[word] += 1
    return [(word, count) for word, count in words.items()]


def slice_ten_high_frequency(words):
    sorted_words = sorted(words, key=lambda word: word[1], reverse=True)
    return sorted_words[:10]


if __name__ == '__main__':
    des = load_descriptions_from_json()
    cw = count_words(des)
    print(slice_ten_high_frequency(cw))
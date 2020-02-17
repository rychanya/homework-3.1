import json
import xml.etree.ElementTree as ET


def load_descriptions_from_json():
    with open('newsafr.json', encoding='utf8') as file:
        data = json.load(file)
    return [item['description'] for item in data['rss']['channel']['items']]


def load_descriptions_from_xml():
    tree = ET.parse('newsafr.xml')
    descriptions = tree.findall('channel/item/description')
    return [description.text for description in descriptions]


def count_words(descriptions):
    words = {}
    for description in descriptions:
        description_words = filter(
            lambda word: len(word) > 6, 
            description.split())
        for word in description_words:
            lower_word = word.lower()
            words.setdefault(lower_word, 0)
            words[lower_word] += 1
    return words


def slice_ten_high_frequency(words):
    sorted_words = sorted(words, key=words.get, reverse=True)
    return sorted_words[:10]


def first_ten(descriptions):
    words = count_words(descriptions)
    most_wanted_words = slice_ten_high_frequency(words)
    return most_wanted_words


if __name__ == '__main__':
    descriptions_from_json = load_descriptions_from_json()
    descriptions_from_xml = load_descriptions_from_xml()
    print('Самые часто встречаемые слова в json')
    print(first_ten(descriptions_from_json))
    print('Самые часто встречаемые слова в xml')
    print(first_ten(descriptions_from_xml))

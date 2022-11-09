import math

import matplotlib.pyplot as plt

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower()

encrypted_file = open("file.txt", "r")

encrypted_Text = encrypted_file.read()



relative_frequency = {
    'e': 11.1607,
    'a': 8.4966,
    'r': 7.5809,
    'i': 7.5448,
    'o': 7.1635,
    't': 6.9509,
    'n': 6.6544,
    's': 5.7351,
    'l': 5.4893,
    'c': 4.5388,
    'u': 3.6308,
    'd': 3.3844,
    'p': 3.3844,
    'm': 3.0129,
    'h': 3.0034,
    'g': 2.4705,
    'b': 2.0720,
    'f': 1.8121,
    'y': 1.7779,
    'w': 1.2899,
    'k': 1.1016,
    'v': 1.0074,
    'x': 0.2902,
    'z': 0.2722,
    'j': 0.1965,
    'q': 0.1962
}


def calculate_frequency(text):
    dictionary = {}
    for element in text:
        if element.isalpha():
            if element.lower() not in dictionary:
                dictionary[element.lower()] = 1
            else:
                dictionary[element.lower()] += 1
    return dictionary


def draw_graph():
    plt.plot(frequency_dict.keys(), frequency_dict.values())
    plt.xlabel("Letter")
    plt.ylabel("Frequency")
    plt.title("Frequency graph")
    plt.show()


def frequency_ratio(dictionary):
    total = 0
    cipher_frequency_ratio = {}
    for element in dictionary.values():
        total += element
    for element in dictionary:
        cipher_frequency_ratio[element] = dictionary[element] / total * 100

    return cipher_frequency_ratio


def expected_frequency(dictionary, total):
    for element in dictionary:
        dictionary[element] = math.floor(dictionary[element] * total / 100)
    return dictionary


frequency_dict = calculate_frequency(encrypted_Text)
print(frequency_dict)

relative_freq = frequency_ratio(frequency_dict)
print(relative_freq)

draw_graph()

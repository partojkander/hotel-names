from random import choice


adjectives = ["Beautiful", "Happy", "Imperial", "Quiet", "Sunny"]
nouns = ["Beach", "Downs", "Hills", "Lake", "Mountains"]
suffixes = ["Spa", "Hotel", "Resorts"]


def get_hotel_name(adjective=None, noun=None, suffix=None):
    adjective_ = adjective or choice(adjectives)
    noun_ = noun or choice(nouns)
    suffix_ = suffix or choice(suffixes)
    return f"{adjective_} {noun_} {suffix_}"


def main():
    print(get_hotel_name())


if __name__ == '__main__':
    main()
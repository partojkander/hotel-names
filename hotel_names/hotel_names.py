from random import choice


adjectives = ["Beautiful", "Happy", "Imperial", "Quiet", "Sunny"]
nouns = ["Beach", "Downs", "Hills", "Lake", "Mountains"]
suffixes = ["Spa", "Hotel", "Resorts"]


def get_hotel_name(suffix=None):
    hotel_suffix = suffix or choice(suffixes)
    return f"{choice(adjectives)} {choice(nouns)} {hotel_suffix}"


def main():
    print(get_hotel_name())


if __name__ == '__main__':
    main()
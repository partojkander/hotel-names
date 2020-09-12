from random import choice


adjectives = ["Beautiful", "Happy", "Imperial", "Sunny"]
nouns = ["Beach", "Hills", "Lake", "Mountains"]
suffixes = ["and Spa", "Hotel", "Resorts"]


def get_hotel_name(suffix=True):
    hotel_suffix = choice(suffixes) if suffix else ""
    return f"{choice(adjectives)} {choice(nouns)} {hotel_suffix}"


if __name__ == '__main__':
    print(get_hotel_name())

# local libraries
from app.common.firstPerson import FirstPerson

def main():
    """Main application
    """
    samples = [
        "I feel sick",
        "Such a beautiful day!",
        "You do not effect me.",
        "I guess you are talking me.",
        "Are you talking with me?"
    ]

    firstPerson = FirstPerson()
    freq = firstPerson.frequency(samples)
    match = firstPerson.match(samples)

    print(freq)
    print(match)

if __name__ == '__main__':
    main()

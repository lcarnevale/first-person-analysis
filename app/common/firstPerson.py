# third parties libraries
from nltk import pos_tag
from nltk import word_tokenize

class FirstPerson:
    """
    """
    def __init__(self):
        """Initializes the class
        """
        self.pronounTag = 'PRP'
        self.firstPersonDataset = ['i', 'me', 'my', 'mine']

        self.responseData = dict()

    def frequency(self, questions):
        """
        """
        frequencyInDialog = 0
        len_questions = float(len(questions))

        for question in questions:
            frequencyInQuestion = 0
            tokenized_question = word_tokenize(question)
            tagged_question = pos_tag(tokenized_question)
            for tagged_word in tagged_question:
                word = tagged_word[0].lower()
                tag = tagged_word[1]
                if tag == self.pronounTag and word in self.firstPersonDataset:
                    frequencyInQuestion += 1
            frequencyInDialog += frequencyInQuestion

        return frequencyInDialog / len_questions

    def match(self, questions):
        """
        """
        matchData = list()
        for question in questions:
            isMatched = False
            tokenized_question = word_tokenize(question)
            tagged_question = pos_tag(tokenized_question)
            for tagged_word in tagged_question:
                word = tagged_word[0].lower()
                tag = tagged_word[1]
                if tag == self.pronounTag and word in self.firstPersonDataset:
                    isMatched = True
                    break

            if isMatched:
                matchData.append( (question, True) )
            else:
                matchData.append( (question, False) )

        return matchData



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

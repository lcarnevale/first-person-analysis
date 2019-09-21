# -*- coding: utf-8 -*-

"""
First singular person pronoun analysis

.. _Google Python Style Guide
    https://github.com/google/styleguide/blob/gh-pages/pyguide.md
"""

__copyright__ = 'Copyright 2019, University of Messina'
__author__ = 'Lorenzo Carnevale <lorenzocarnevale@gmail.com>'
__credits__ = ''
__description__ = 'First singular person pronoun analysis'


# third parties libraries
from nltk import pos_tag
from nltk import word_tokenize

class FirstPerson:
    """Logic of first singular person pronoun analysis

    Args:
        pronounTag (str): nltk metadata for the speech tag pronoun
        firstPersonDataset (list): dataset of first singular person pronouns
    """
    def __init__(self):
        """Initializes the class
        """
        self.pronounTag = 'PRP'
        self.firstPersonDataset = ['i', 'me', 'my', 'mine']


    def frequency(self, samples):
        """Counts frequency

        First person singular pronoun frequency, that is the number of
        occurrences, is calculated in a pool of samples.

        Args:
            samples (list): list of target samples

        Exceptions:
            ValueError: when samples' list is empty

        Returns:
            float: value of frequency
        """
        frequencyInDialog = 0
        if not samples:
            raise ValueError('No samples to analyze.')
        len_samples = float( len(samples) )

        for sample in samples:
            frequencyInSample = 0
            tokenized_sample = word_tokenize(sample)
            tagged_sample = pos_tag(tokenized_sample)
            for tagged_word in tagged_sample:
                word = tagged_word[0].lower()
                tag = tagged_word[1]
                if tag == self.pronounTag and word in self.firstPersonDataset:
                    frequencyInSample += 1
            frequencyInDialog += frequencyInSample

        return frequencyInDialog / len_samples

    def match(self, samples):
        """Matches target samples

        Extract samples that match the presence of first singular person
        pronoun.

        Args:
            samples (list): list of target samples

        Exceptions:
            ValueError: when samples' list is empty

        Returns:
            list: list of matched samples
        """
        matchData = list()
        if not samples:
            raise ValueError('No samples to analyze.')

        for sample in samples:
            isMatched = False
            tokenized_sample = word_tokenize(sample)
            tagged_sample = pos_tag(tokenized_sample)
            for tagged_word in tagged_sample:
                word = tagged_word[0].lower()
                tag = tagged_word[1]
                if tag == self.pronounTag and word in self.firstPersonDataset:
                    isMatched = True
                    break

            if isMatched:
                matchData.append( (sample, True) )
            else:
                matchData.append( (sample, False) )

        return matchData

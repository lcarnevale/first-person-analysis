# -*- coding: utf-8 -*-

"""Mapreduce implementation of First singular person pronoun analysis

.. _Google Python Style Guide
    https://github.com/google/styleguide/blob/gh-pages/pyguide.md
"""

__copyright__ = 'Copyright 2019, University of Messina'
__author__ = 'Lorenzo Carnevale <lorenzocarnevale@gmail.com>'
__credits__ = ''
__description__ = 'Mapreduce implementation of First singular person pronoun analysis'

# standard librries
import operator
# local libraries
from .mapreducer import SimpleMapReduce
# third parties libraries
from nltk import pos_tag
from nltk import word_tokenize

class FirstPersonMR:
    """Implements mapreduce logic for first singular person pronoun analysis.

    Args:
        pronounTag (str): nltk metadata for the speech tag pronoun
        firstPersonDataset (list): dataset of first singular person pronouns
    """
    def __init__(self, num_workers, chunksize):
        """Initializes the class
        """
        self.num_workers = num_workers
        self.chunksize = chunksize

        self.pronounTag = 'PRP'
        self.firstPersonDataset = ['i', 'me', 'my', 'mine']


    def _map_func(self, sample):
        """Computes occurances of first singular person pronoun in sample.

        It is the mapper method.

        Args:
            sample (str): the target sample

        Returns:
            list: list of <key, value> tuples.
        """
        frequencyInSample = 0
        output = list()
        tokenized_sample = word_tokenize(sample)
        tagged_sample = pos_tag(tokenized_sample)
        for tagged_word in tagged_sample:
            word = tagged_word[0].lower()
            tag = tagged_word[1]
            if tag == self.pronounTag and word in self.firstPersonDataset:
                output.append( (tag, 1) )

        return output

    def _reduce_func(self, item):
        """Sums occurances of first singular person pronoun.

        It is the reducer method.

        Args:
            item (tuple): <tag, occurances> pair.

        Returns:
            tuple: <tag, sum of occurances> pair.
        """
        tag, occurances = item
        return (tag, sum(occurances))

    def frequency(self, samples):
        """Computes frequency of first singular person pronouns in samples

        Args:
            samples (list): list of target samples

        Exceptions:
            ValueError: when samples list is empty

        Returns:
            int: number of first singular person pronoun occurances
        """
        if not samples:
            raise ValueError('No samples to analyze.')
        len_samples = float( len(samples) )

        mapper = SimpleMapReduce(self._map_func, self._reduce_func, self.num_workers)
        prp_counts = mapper(samples, self.chunksize)
        prp_counts.sort(key=operator.itemgetter(1))
        occurance = prp_counts[0][1]

        return occurance

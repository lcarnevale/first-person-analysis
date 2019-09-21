# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""
First singular person pronoun analysis

.. _Google Python Style Guide
    https://github.com/google/styleguide/blob/gh-pages/pyguide.md
"""

__copyright__ = 'Copyright 2019, University of Messina'
__author__ = 'Lorenzo Carnevale <lorenzocarnevale@gmail.com>'
__credits__ = ''
__description__ = ''


# standard libraries
import argparse
# local libraries
from app.common.firstPerson import FirstPerson

def main():
    """Main application
    """
    description = ('%s\n%s' % (__author__, __description__))
    epilog = ('%s\n%s' % (__credits__, __copyright__))
    parser = argparse.ArgumentParser(
        description = description,
        epilog = epilog
    )

    args = parser.parse_args()

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

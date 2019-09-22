# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""First singular person pronoun analysis

.. _Google Python Style Guide
    https://github.com/google/styleguide/blob/gh-pages/pyguide.md
"""

__copyright__ = 'Copyright 2019, University of Messina'
__author__ = 'Lorenzo Carnevale <lorenzocarnevale@gmail.com>'
__credits__ = ''
__description__ = ''


# standard libraries
import time
import resource
import argparse
# local libraries
from app.common.firstPerson import FirstPerson

def main(samples):
    """Main application
    """

    len_samples = len(samples)

    time_start = time.perf_counter()

    firstPerson = FirstPerson()
    freq = firstPerson.frequency(samples)
    # print(freq)

    time_elapsed = (time.perf_counter() - time_start)
    memBy = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024.0
    # print("%s samples %5.1f secs %5.1f Byte" % (len_samples, time_elapsed, memBy))

    return len_samples, time_elapsed, memBy


if __name__ == '__main__':
    description = ('%s\n%s' % (__author__, __description__))
    epilog = ('%s\n%s' % (__credits__, __copyright__))
    parser = argparse.ArgumentParser(
        description = description,
        epilog = epilog
    )

    parser.add_argument("-s", "--samples",
        dest="samples",
        help="Target samples",
        type=list,
        default=None)

    args = parser.parse_args()
    samples = args.samples

    if not samples:
        samples = [
            "I feel sick",
            "Such a beautiful day!",
            "You do not effect me.",
            "I guess you are talking me.",
            "Are you talking with me?"
        ] * 10000

    main(samples)

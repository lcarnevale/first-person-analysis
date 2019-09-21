# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""Mapreduce example

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
from app.common.firstPersonMR import FirstPersonMR

def main():
    """Main application
    """
    description = ('%s\n%s' % (__author__, __description__))
    epilog = ('%s\n%s' % (__credits__, __copyright__))
    parser = argparse.ArgumentParser(
        description = description,
        epilog = epilog
    )

    parser.add_argument("-w", "--workers",
        dest="num_workers",
        help="Number of workers",
        type=int,
        default=None)

    parser.add_argument("-c", "--chunksize",
        dest="chunksize",
        help="Size of chunk",
        type=int,
        default=1)

    args = parser.parse_args()
    num_workers = args.num_workers
    chunksize = args.chunksize

    samples = [
        "I feel sick",
        "Such a beautiful day!",
        "You do not effect me.",
        "I guess you are kidding me.",
        "Are you talking with me?"
    ] * 10000
    len_sample = len(samples)

    time_start = time.perf_counter()

    firstPerson = FirstPersonMR(num_workers, chunksize)
    freq = firstPerson.frequency(samples)
    print(freq)

    time_elapsed = (time.perf_counter() - time_start)
    memMb=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024.0/1024.0
    print("%s samples %5.1f secs %5.1f MByte" % (len_sample, time_elapsed,memMb))


if __name__ == '__main__':
    main()

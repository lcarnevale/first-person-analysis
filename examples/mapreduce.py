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
from multiprocessing import cpu_count
# local libraries
from app.common.firstPersonMR import FirstPersonMR

def main(samples, chunksize=1, num_workers=None):
    """Main application
    """
    len_samples = len(samples)

    time_start = time.perf_counter()

    firstPerson = FirstPersonMR(num_workers, chunksize)
    freq = firstPerson.frequency(samples)

    time_elapsed = (time.perf_counter() - time_start)
    memBy = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024.0
    # print("%s samples %5.1f secs %5.1f Byte" % (len_samples, time_elapsed, memBy))

    if not num_workers:
        num_workers = cpu_count()
    return len_samples, time_elapsed, memBy, num_workers


if __name__ == '__main__':
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

    parser.add_argument("-s", "--samples",
        dest="samples",
        help="Target samples",
        type=list,
        default=None)

    args = parser.parse_args()
    num_workers = args.num_workers
    chunksize = args.chunksize
    samples = args.samples

    if not samples:
        samples = [
            "I feel sick",
            "Such a beautiful day!",
            "You do not effect me.",
            "I guess you are kidding me.",
            "Are you talking with me?"
        ] * 10000

    main(samples, chunksize, num_workers)

# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""Performance test

That script performs time and memory tests.
Two PNG files are generated in output

.. _Google Python Style Guide
    https://github.com/google/styleguide/blob/gh-pages/pyguide.md
"""

__copyright__ = 'Copyright 2019, University of Messina'
__author__ = 'Lorenzo Carnevale <lorenzocarnevale@gmail.com>'
__credits__ = ''
__description__ = 'That script performs time and memory tests. Two PNG files are generated in output'


# standard libraries
import time
import argparse
# local libraries
from examples.linearloop import main as linearloop_main
from examples.mapreduce import main as mapreduce_main
# third parties libraries
from tqdm import tqdm
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')


description = ('%s\n%s' % (__author__, __description__))
epilog = ('%s\n%s' % (__credits__, __copyright__))
parser = argparse.ArgumentParser(
    description = description,
    epilog = epilog
)

parser.add_argument("-i", "--iterations",
    dest="iterations",
    help="Number of iterations",
    type=int,
    default=10)

args = parser.parse_args()

iterations = args.iterations
linear_time_mean = list()
linear_mem_mean = list()
mapreduce_2w_time_mean = list()
mapreduce_2w_mem_mean = list()
mapreduce_4w_time_mean = list()
mapreduce_4w_mem_mean = list()
samples = ["I am gonna show an example"]
num_samples = [100, 10000, 100000]

pbar = tqdm(num_samples)
for num_sample in pbar:
    # defining local variables
    linear_time = list()
    linear_mem = list()
    mapreduce_2w_time = list()
    mapreduce_2w_mem = list()
    mapreduce_4w_time = list()
    mapreduce_4w_mem = list()

    # creating samples
    samples_ = samples * num_sample

    # starting linear test
    for iteration in range(iterations):
        pbar.set_description("Processing linear with %s samples, iteration %s/%s" % (num_sample, iteration+1, iterations))
        len_samples, time_elapsed, memBy = linearloop_main(samples_)
        linear_time.append(time_elapsed)
        linear_mem.append(memBy)
    linear_time_mean.append( sum(linear_time) / len(linear_time) )
    linear_mem_mean.append( sum(linear_mem) / len(linear_mem) )

    # starting mapreduce test
    for iteration in range(iterations):
        pbar.set_description("Processing mapreduce with %s samples, iteration %s/%s" % (num_sample, iteration+1, iterations))
        len_samples, time_elapsed, memBy, num_workers = mapreduce_main(samples_, num_workers=2)
        mapreduce_2w_time.append(time_elapsed)
        mapreduce_2w_mem.append(memBy)
    mapreduce_2w_time_mean.append( sum(mapreduce_2w_time) / len(mapreduce_2w_time) )
    mapreduce_2w_mem_mean.append( sum(mapreduce_2w_mem) / len(mapreduce_2w_mem) )

    # starting mapreduce test
    for iteration in range(iterations):
        pbar.set_description("Processing mapreduce with %s samples, iteration %s/%s" % (num_sample, iteration+1, iterations))
        len_samples, time_elapsed, memBy, num_workers = mapreduce_main(samples_, num_workers=4)
        mapreduce_4w_time.append(time_elapsed)
        mapreduce_4w_mem.append(memBy)
    mapreduce_4w_time_mean.append( sum(mapreduce_4w_time) / len(mapreduce_4w_time) )
    mapreduce_4w_mem_mean.append( sum(mapreduce_4w_mem) / len(mapreduce_4w_mem) )


# plotting time performance
fig = plt.figure()
plt.plot(num_samples, linear_time_mean, '-b', label='linear') # solid blue
plt.plot(num_samples, mapreduce_2w_time_mean, '--r', label='mapreduce (2 workers)') # dashed red
plt.plot(num_samples, mapreduce_4w_time_mean, ':c', label='mapreduce (4 workers)') # dotted cyan
plt.title("Time performance [%s iterations]" % (iterations))
plt.xlabel("samples")
plt.ylabel("time [s]")
plt.legend()
plt.savefig("time_performance.png")

# plotting memory performance
fig = plt.figure()
plt.plot(num_samples, linear_mem_mean, '-b', label='linear') # solid blue
plt.plot(num_samples, mapreduce_2w_mem_mean, '--r', label='mapreduce (2 workers)') # dashed red
plt.plot(num_samples, mapreduce_4w_mem_mean, ':c', label='mapreduce (4 workers)') # dotted cyan
plt.title("Memory performance [%s iterations]" % (iterations))
plt.xlabel("samples")
plt.ylabel("mem [byte]")
plt.legend()
plt.savefig("mem_performance.png")

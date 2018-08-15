# What time is it?
For this activity, you will be measuring the performance characteristics of
various sorting algorithms, defined in [sort.py](sort.py).


## Timeit
Experiment with the timeit module by seeing how long the various sort
implementations take. While you could modify [sort.py](sort.py) directly, you
can take advantage of the command line interface to test different algorithms:

```console
foo@bar:~ $ python2 -m timeit "from sort import quick_sort as sort, random_seq; print sort(random_seq)"
```

The reason for the `as` keyword is so that you can change search algorithms in
one place instead of two:

In fact, you can take advantage of command substitution by typing the following
in a terminal and pressing enter:

```console
foo@bar:~ $ ^quick^merge
```
Where the word after the first `^` signifies the word in the previous command to
replace, and the word after the second `^` signifies the word to use as a
replacement.

Doing so will result in the following command:

```console
foo@bar:~ $ python2 -m timeit "from sort import bubble_sort as sort, random_seq; print sort(random_seq)"
```

## cProfile
You can measure the performance of all algorithms by using the cProfile module
and running the script:

```console
foo@bar:~ $ python2 -m cProfile -o sort.profile sort.py
```

You can then pass the resulting `sort.profile` file to the `pstats` module:

```console
foo@bar:~ $ python2 -m pstats sort.profile
```

Take a look at
[this](https://www.stefaanlippens.net/python_profiling_with_pstats_interactive_mode/)
article for help on how to analyze statistics.




# Credits
We've adapted the algorithms from 
[Popular Sorting Algorithms](http://python3.codes/popular-sorting-algorithms/).

""" List comprehensions provide a concise way to create lists.
Common applications are to make new lists where each element
is the result of some operations applied to each member
of another sequence or iterable,
or to create a subsequence of those elements that satisfy a condition."""


def squares():
    sqrs = []
    for x in range(10):
        sqrs.append(x**2)

    print(sqrs)

    "Using comprehension capability..."
    sqrs_comp = [x ** 2 for x in range(10)]

    print(sqrs_comp)


"""A list comprehension consists of 
brackets containing an expression 
followed by a 'for' clause, 
then zero or more 'for' or 'if' clauses. 
The result will be a new list resulting from evaluating the expression 
in the context of the 'for' and 'if' clauses which follow it. """


def combine_lists():
    """For example, this listcomp combines the elements of two lists if they are not equal."""
    print([(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y])
    # [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

    combs = []
    for x in [1, 2, 3]:
        for y in [3, 1, 4]:
            if x != y:
                combs.append((x, y))

    print(combs)


def transpose_matrix():
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]

    print([[row[i] for row in matrix] for i in range(4)])
    # [
    # [1, 5, 9],
    # [2, 6, 10],
    # [3, 7, 11],
    # [4, 8, 12]
    # ]

    transposed = []
    for i in range(4):
        transposed.append([row[i] for row in matrix])

    print(transposed)

    transposed = []
    for i in range(4):
        # the following 3 lines implement the nested listcomp
        transposed_row = []
        for row in matrix:
            transposed_row.append(row[i])
        transposed.append(transposed_row)

    print(transposed)

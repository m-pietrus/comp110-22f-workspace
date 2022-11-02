"""Dictionary related utility functions."""

<<<<<<< HEAD
__author__ = "730361113"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], key: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    i: int = 0
    while i < len(table):
        result.append(table[i][key])
        i += 1
    return result


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    for key in table[0]:
        result[key] = column_values(table, key)
    return result


def head(data: dict[str, list[str]], N: int) -> dict[str, list[str]]:
    """Makes a smaller table."""
    output: dict[str, list[str]] = {}
    for key in data:
        store: list[str] = []
        i: int = 0
        while i < N and i < len(data[key]):
            store.append(data[key][i])
            i += 1
        output[key] = store
    return output


def select(table: dict[str, list[str]], title: list[str]) -> dict[str, list[str]]:
    """Should produce a new table with only select columns."""
    out: dict[str, list[str]] = {}
    for string in title:
        out[string] = table[string]
    return out


def concat(a: dict[str, list[str]], b: dict[str, list[str]]) -> dict[str, list[str]]:
    """Will this on be right?!?!?"""
    output: dict[str, list[str]] = {}
    for key in a:
        output[key] = a[key]
    for k in b:
        if k in output:
            output[k] += b[k]
        else:
            output[k] = b[k]
    return output


def count(values: list[str]) -> dict[str, int]:
    """Will show how frequent each value is."""
    freq: dict[str, int] = {}
    i: int = 0
    while i < len(values):
        if values[i] in freq:
            freq[values[i]] += 1
        else:
            freq[values[i]] = 1
        i += 1
    return freq
=======
__author__ = ""

# Define your functions below
>>>>>>> d09154944ca6f9cb86e4fefc7877bd6b3426dbd5

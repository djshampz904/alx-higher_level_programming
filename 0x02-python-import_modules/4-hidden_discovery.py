#!/usr/bin/python3

import hidden_4

if __name__ == "__main__":
    names = dir(hidden_4)
    for item in names:
        if not item.startswith('__'):
            print(item)
        else:
            continue

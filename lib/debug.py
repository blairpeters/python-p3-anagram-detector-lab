#!/usr/bin/env python3

from anagram import Anagram

if __name__ == '__main__':
    import ipdb; ipdb.set_trace()
    anagram = Anagram("listen")
    print(anagram.match(["enlists", "google", "inlets", "banana"]))

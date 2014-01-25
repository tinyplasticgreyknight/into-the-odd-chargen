#!/usr/bin/env python

import yaml
from character import Character, Lackey

def main(num_chars, lackey):
    chars = []
    PersonType = Character
    if lackey: PersonType = Lackey

    for _ in range(num_chars):
        chars.append( PersonType() )

    print yaml.dump_all(chars, default_flow_style=False)

if __name__=='__main__':
    import argparse
    parser = argparse.ArgumentParser(description='This is a character generator for the /Into the Odd/ roleplaying game.')
    parser.add_argument('num_chars', type=int, nargs='?', default=1, help='The number of characters to generate (default: 1)')
    parser.add_argument('--lackey', action='store_const', const=True, default=False, help='Generate a lackey instead of a normal character')
    args = parser.parse_args()
    main(**vars(args))

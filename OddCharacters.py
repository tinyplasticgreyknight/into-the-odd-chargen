#!/usr/bin/env python

import yaml
from character import Character

def main(num_chars, num_equipment, num_traits, arcanum):
    chars = []

    arcanum = {"yes":True, "no":False, "default":None}[arcanum]

    for _ in range(num_chars):
        chars.append( Character(num_traits=num_traits, num_equipment=num_equipment, force_arcanum=arcanum) )

    print yaml.dump_all(chars, default_flow_style=False)

if __name__=='__main__':
    import argparse
    parser = argparse.ArgumentParser(description='This is a character generator for the /Into the Odd/ roleplaying game.')
    parser.add_argument('num_chars', type=int, nargs='?', default=1, help='The number of characters to generate (default: 1)')
    parser.add_argument('--num-equipment', type=int, nargs='?', default=3, help='The amount of equipment to start with (default: 3)')
    parser.add_argument('--num-traits', type=int, nargs='?', default=2, help='The number of traits to start with (default: 2)')
    parser.add_argument('--arcanum', choices=["yes", "no", "default"], default="default", help='Use --arcanum=yes to force having an Arcanum, or --arcanum=no to force having none.  By default you might get one, according to the normal rules.')
    args = parser.parse_args()
    main(**vars(args))

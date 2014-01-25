#!/usr/bin/env python

import yaml
from character import Character

def main(n=1):
    n = int(n)
    chars = []
    for _ in range(n):
        chars.append( Character() )
    print yaml.dump_all(chars, default_flow_style=False)

if __name__=='__main__':
    import sys
    main(*sys.argv[1:])

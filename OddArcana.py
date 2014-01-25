#!/usr/bin/env python

import yaml
from arcanum import Arcanum

def main(num_arcana, kind, distribution):
    arcana = []
    for _ in range(num_arcana):
        _kind = kind
        if _kind == "random":
            _kind = distribution.pick()
        arcana.append( Arcanum(_kind) )

    print yaml.dump_all(arcana, default_flow_style=False)

class Distribution(object):
    def __init__(self, s):
        fields = s.split(':')
        if len(fields) != 3:
            raise argparse.ArgumentTypeError("distribution must have three fields")
        ifields = []
        try:
            for field in fields:
                i = int(field)
                if i<0: raise ValueError
                ifields.append( i )
        except ValueError:
            raise argparse.ArgumentTypeError("distribution fields must be non-negative integers")

        self.total = sum(ifields)
        if self.total==0:
            raise argparse.ArgumentTypeError("at least one distribution field must be non-zero")

        self.lesser    = ifields[0]
        self.great     = ifields[1]
        self.legendary = ifields[2]
    def pick(self):
        import random
        r = random.randint(1, self.total)
        if r <= self.lesser:
            return "lesser"
        elif r <= (self.lesser + self.great):
            return "great"
        else:
            return "legendary"
    def __str__(self):
        return "%d:%d:%d" % (self.lesser, self.great, self.legendary)

if __name__=='__main__':
    import argparse
    parser = argparse.ArgumentParser(description='This is an Arcana generator for the /Into the Odd/ roleplaying game.')
    parser.add_argument('num_arcana', type=int, nargs='?', default=1, help='The number of Arcanum to generate (default: 1)')
    parser.add_argument('--kind', choices=["random", "lesser", "great", "legendary"], default="random", help='Which type of Arcanum should be generated? (default: random)')
    default_distr = Distribution("15:4:1")
    parser.add_argument('--distribution', metavar='x:y:z', type=Distribution, default=default_distr, help='The proportions of (lesser:great:legendary) Arcana to generate, if the "random" kind is selected (default: %s).' % default_distr)
    args = parser.parse_args()
    main(**vars(args))

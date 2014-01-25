import yaml
from util import *

class InvalidArcanumKindException(Exception):
    pass

class Arcanum:
    def __init__(self, kind="lesser"):
        if kind not in ["lesser", "great", "legendary"]:
            raise InvalidArcanumKindException
        self.kind = kind
        self.choose_description()
        self.choose_power()
    def choose_description(self):
        table_adj = "adjectives"
        table_shape = "shapes"
        if chance(datum("arcana", "chance of", "elaborate "+self.kind)):
            table_adj = "elaborate adjectives"
        if chance(datum("arcana", "chance of", "large "+self.kind)):
            table_shape = "large shapes"

        self.adjective = choose_simple_datum("arcana", table_adj)
        self.shape = choose_simple_datum("arcana", table_shape)
    def choose_power(self):
        power_table = data_table("arcana", self.kind+" powers")
        self.power = choose(power_table.keys())
        self.power_text = power_table[self.power]
    def description(self):
        return "%s %s" % (self.adjective, self.shape)
    def __str__(self):
        return "%s (%s)" % (self.description(), self.power)

def yaml_repr_arcanum(dumper, arcanum):
    def mkpair(k, v):
        k = dumper.represent_data(k)
        v = dumper.represent_data(v)
        return (k, v)
    power = OrderedDict([
        ("Name", arcanum.power),
        ("Kind", arcanum.kind),
        ("Effect", arcanum.power_text),
    ])
    value = [
        mkpair("Description", arcanum.description()),
        mkpair("Power", power),
    ]
    return yaml.nodes.MappingNode(u'tag:yaml.org,2002:map', value)

yaml.add_representer(Arcanum, yaml_repr_arcanum)

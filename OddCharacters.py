import yaml
import random
import re
from collections import OrderedDict

class InvalidArcanumKindException(Exception):
    pass

class TooManySelectionsException(Exception):
    pass

def yaml_repr_ordereddict(dumper, data):
    value = []
    for item_key, item_value in data.items():
        node_key = dumper.represent_data(item_key)
        node_value = dumper.represent_data(item_value)
        value.append((node_key, node_value))
    return yaml.nodes.MappingNode(u'tag:yaml.org,2002:map', value)

yaml.add_representer(OrderedDict, yaml_repr_ordereddict)

def d(sides=6, n=1):
    total = 0
    for _ in range(n):
        total += random.randint(1, sides)
    return total

def d6(n=1):
    return d(sides=6, n=n)

def choose(items):
    return items[d(sides=len(items))-1]

def choose_simple_datum(datafile, section):
    return choose(data_table(datafile, section))

def choose_distinct(num_selections, items):
    num_items = len(items)
    if num_selections > num_items:
        raise TooManySelectionsException
    indices = set()
    while len(indices)<num_selections:
        indices.add( d(sides=num_items)-1 )
    chosen = []
    for i in indices:
        chosen.append(items[i])
    return chosen

def chance(probability):
    pc_regexp = re.compile("([0-9]+)%")
    if type(probability) == str:
        m = pc_regexp.match(probability)
        return chance(int(m.group(1))/100.0)
    return random.random() < probability

def yaml_safe_string(s):
    s = str(s)
    escaped = re.sub(r"([\'\"])", r"\\\1", s)
    if len(escaped) != len(s):
        escaped = '"%s"' % escaped
    return escaped

def strify_list(L, title, indent=""):
    if len(L)==0:
        return ""
    s = "%s%s:\n" % (indent, title)
    for item in L:
        s += "%s- %s\n" % (indent, yaml_safe_string(item))
    return s


def main():
    char = Character(force_arcanum=True)
    print yaml.dump(char, default_flow_style=False)

if __name__=='__main__':
    main()

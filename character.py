import yaml
from util import *
from arcanum import Arcanum
from collections import OrderedDict

class Character(object):
    def __init__(self, force_arcanum=False, num_traits=2):
        self.traits = []
        self.equipment = []
        self.arcana = []
        self.roll_basics(num_traits)
        self.roll_inventory(force_arcanum)
    def roll_basics(self, num_traits):
        self.roll_scores()
        self.choose_name()
        self.home_town = choose_simple_datum("places", "origins")
        self.choose_traits(num_traits)
    def roll_inventory(self, force_arcanum):
        self.add_equipment(n=3)
        if force_arcanum or (self.wil > self.dex and self.wil > self.str):
            self.add_arcanum()
    def roll_scores(self):
        self.str = d6(n=3)
        self.dex = d6(n=3)
        self.wil = d6(n=3)
        self.hp  = d6()
    def choose_name(self):
        name_chances = data_table("names", "chance of")
        self.personal_name = choose_simple_datum("names", "personal")
        self.family_name = None
        self.epithet = None
        if chance(name_chances["family"]):
            self.family_name = choose_simple_datum("names", "family")
        if chance(name_chances["epithet"]):
            self.epithet = choose_simple_datum("names", "epithets")
    def choose_traits(self, num_traits):
        for trait in choose_distinct(num_traits, data_table("traits", "traits")):
            self.traits.append( trait )
    def add_equipment(self, n):
        indices = []
        for _ in range(n):
            cur = d6()-1
            nalready = indices.count(cur)
            indices.append( cur )
            table = "basic"
            if nalready==1:
                table = "double"
            elif nalready>1:
                table = "triple"
            self.equipment.append( data_table("equipment", table)[cur] )
    def add_arcanum(self):
        self.arcana.append( Arcanum("lesser") )
    def name(self):
        s = ""
        s += self.personal_name
        if self.family_name is not None:
            s += " %s" % self.family_name
        if self.epithet is not None:
            s += ", %s" % self.epithet
        return s

def yaml_repr_character(dumper, char):
    value = OrderedDict([
        ("Name", char.name()),
        ("Str", char.str),
        ("Dex", char.dex),
        ("Wil", char.wil),
        ("HP", char.hp),
        ("Equipment", char.equipment),
        ("Arcana", char.arcana),
        ("Origin", "You are from %s." % char.home_town),
        ("Traits", char.traits),
    ])
    if type(char)==Lackey and len(char.arcana)==0:
        del value["Arcana"]
    return dumper.represent_data(value)

class Lackey(Character):
    def __init__(self, num_traits=2):
        super(Lackey, self).__init__(num_traits)
    def roll_scores(self):
        self.str = d6(n=2)
        self.dex = d6(n=2)
        self.wil = d6(n=2)
        self.hp  = 1
    def roll_inventory(self, _):
        self.add_equipment(n=1)

yaml.add_representer(Character, yaml_repr_character)
yaml.add_representer(Lackey, yaml_repr_character)

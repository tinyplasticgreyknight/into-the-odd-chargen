# OddCharacters & OddArcana
This is a character & Arcanum generator for the *Into the Odd* roleplaying game.

## Running
Both OddCharacters and OddArcana accept the `--help` argument to print out a summary of their arguments.

### OddCharacters
You can run the `OddCharacters.py` script to generate a single character, which is printed to standard output.

You can give a number on the command line to generate multiple characters at once (useful for GMs).
> `./OddCharacters.py 3`
> *(generates three characters)*

You can specify some options to customise the character generation:
- `--arcanum=yes` forces a character to start with an arcanum, while `--arcanum=no` forces him to have none.  By default you may or may not get one depending on your ability scores, as per the normal rules.
- `--num-equipment=3` allows you to customise the amount of starting equipment.  There are no equipment tables for more than 3 starting items, but you can modify equipment.txt to allow for this.
- `--num-traits=2` allows you to customise the number of traits.

For example, this generates two characters, each with 1 piece of equipment and 2 traits.  None of them will start with Arcana.
> `./OddCharacters.py --num-equipment=1 --num-traits=2 --arcanum=no 2`

### OddArcana
You can run the `OddArcana.py` script to generate a single Arcanum of random kind, which is printed to standard output.

You can give a number on the command line to generate multiple Arcana at once.
> `./OddArcana.py 3`
> *(generates three Arcana)*

You can specify the `--kind` option to generate Arcana of a specific kind (by default it is random)
> `./OddArcana.py --kind=legendary 2`
> *(generates two legendary Arcana)*

If you are using `--kind=random` (the default), you can control the relative probabilities using the `--distribution` argument
> `./OddArcana.py --distribution=7:2:1 100`
> *(generates 100 Arcana; on average 70 of them will be lesser, 20 will be great, and 10 will be legendary)*

## Interoperativity
The output should be suitable for loading via YAML, if you want to manipulate it in some other automated tool.

## Links
- *Into the Odd*: <https://plus.google.com/communities/101074622606805297404>
- GitHub home for this project: <https://github.com/tinyplasticgreyknight/into-the-odd-chargen>
- Brian Richmond's character generator (Windows): <http://numberappearing.blogspot.co.uk/2014/01/into-odd-character-generator.html>

## Credit
- The lists of names, traits, and places of origin were created by Brian Richmond.
- The lists of Arcana adjectives/nouns are by GreyKnight.
- The Arcana powers text is from the *Into the Odd* manual.
- The Python scripts are by GreyKnight.

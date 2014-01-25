# OddCharacters
This is a character generator for the *Into the Odd* roleplaying game.

## Running
### OddCharacters
You can run the `OddCharacters.py` script to generate a single character, which is printed to standard output.
You can give a number on the command line to generate multiple characters at once (useful for GMs).
> `./OddCharacters.py 3`
> *(generates three characters)*
You can specify the `--lackey` option to generate lackeys instead of normal characters
> `./OddCharacters.py --lackey 2`
> *(generates two lackeys)*

## Interoperativity
The output should be suitable for loading via YAML, if you want to manipulate it in some other automated tool.

## Links
- Into the Odd: <https://plus.google.com/communities/101074622606805297404>
- GitHub home for this project: <https://github.com/tinyplasticgreyknight/into-the-odd-chargen>
- Brian Richmond's character generator (Windows): <http://numberappearing.blogspot.co.uk/2014/01/into-odd-character-generator.html>

## Credit
- The lists of names, traits, and places of origin were created by Brian Richmond.
- The lists of Arcana adjectives/nouns are by GreyKnight.
- The Arcana powers text is from the *Into the Odd* manual.
- The Python scripts are by GreyKnight.
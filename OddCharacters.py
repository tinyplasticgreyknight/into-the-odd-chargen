import yaml
from character import Character

def main():
    char = Character(force_arcanum=True)
    print yaml.dump(char, default_flow_style=False)

if __name__=='__main__':
    main()

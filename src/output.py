class Color:

    BLACK = ''
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

    def parse(self, text, color, bold):
    
        if bold:
            color = color + self.BOLD
        color = color + self.BOLD if bold else color
        return color + text + self.END


def print_results(results):

    print()
    for key, dictionary in results.items():
        print(Color().parse(key, Color.RED, True))
        print()
        counter = 0
        for name, value in dictionary.items():
            counter += 1
            print(f'{Color().parse(f"{counter} - {name}", Color().BLUE, False)}: {value}')
        print()


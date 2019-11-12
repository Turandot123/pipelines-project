class Color:
    """
    An utility class to store the color flags to print to console.
    """
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
        """
        Returns a formatted string ready to be printed to console
        :param text: Text to print
        :param color: Color to use
        :param bold: If the text should be bold
        :return: The formatted string
        """
        if bold:
            color = color + self.BOLD
        color = color + self.BOLD if bold else color
        return color + text + self.END


def print_results(results):
    """
    Helper function used to print the generated results to the console in a colored
    :param results: a dictionary of analysis results
    :return: None
    """
    print()
    for key, dictionary in results.items():
        print(Color().parse(key, Color.RED, True))
        print()
        counter = 0
        for name, value in dictionary.items():
            counter += 1
            print(f'{Color().parse(f"{counter} - {name}", Color().BLUE, False)}: {value}')
        print()


import diceware
from io import StringIO
import sys
import random
import pyperclip

class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio    # free up some memory
        sys.stdout = self._stdout

if __name__ == '__main__':
    with Capturing() as output:
        diceware.main(["-d", "-", "-n", "5"])
    word_list = output[0].split("-")
    word_list[random.randint(0, 4)] = str(random.randint(0, 99))
    my_pass = "-".join(word_list)
    #my_pass = str(random.randint(0, 99))+"-"+output[0]
    print(my_pass)
    pyperclip.copy(my_pass)
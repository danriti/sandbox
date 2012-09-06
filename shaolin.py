from random import randrange
import os

class Shaolin:
    """Lyric text parser."""

    def parse_lyrics_words(self, lines):
        for line in lines:
            self.words.extend(line.split())

    def read_lyric_files(self):
        for file in os.listdir('lyrics'):
            if file.endswith('.txt'):
                f = open('lyrics/%s' % file, 'r')
                lines = f.readlines()
                self.parse_lyrics_words(lines)
                f.close()

    def print_words(self):
        for word in self.words:
            print word

    def get_word_count(self):
        return len(self.words)

    def generate_password(self, min=15):
        password = ''

        while len(password) < min:
            i = randrange(self.get_word_count())
            password += self.words[i]

        return password

    def __init__(self):
        self.words = []

        self.read_lyric_files()


if __name__ == "__main__":
    print 'Shaolin!'

    s = Shaolin()
    #s.print_words()
    #print s.get_word_count()
    print s.generate_password()

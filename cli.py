import click
import itertools

def find_words(letters, wordlist):
    words = []
    for i in range(len(letters)+1):
        permutations = itertools.permutations(letters, i)
        for perm in permutations:
            word = ''.join(perm)
            if word in wordlist and word not in words:
                print(word)
                words.append(word)
    return words

def load_wordlist():
    with open("/usr/share/dict/american-english", "r") as file:
        return file.readlines()

@click.command()
@click.option('--wordlist', '-w', default='/usr/share/dict/american-english', help='A wordlist')
@click.option('--letters', prompt='The letters',
              help='The letters.')
def main(wordlist, letters):
    dictionary = []
    with open(wordlist, "r") as file:
        for line in file.readlines():
            dictionary.append(line.rstrip("\n"))
    print(find_words(letters, dictionary))

if __name__ == '__main__':
    main()

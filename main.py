from flask import Flask, request 
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

app = Flask(__name__)

@app.route("/")
def hello_world():
    letters = request.args.get('letters') 
    if not letters:
        return "<p>No letters...</p><p>Use <a href='/?letters=stpo'>example</a></p>"
    dictionary = []
    with open("/usr/share/dict/american-english", "r") as file:
        for line in file.readlines():
            dictionary.append(line.rstrip("\n"))
    return find_words(letters, dictionary)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)

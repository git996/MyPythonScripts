from textblob import TextBlob
from textblob import Word

def main():
    f = open('relativity.txt','r')
    content = f.read()


    wiki = TextBlob("My namee is John!")
    #wiki.tags
    sentiment = wiki.sentiment
    w = Word('hullo')
    print(wiki.correct())
    to_esp = wiki.translate(to='fr')
    print(to_esp)


    input()

if __name__ == "__main__":
    # execute only if run as a script
    main()

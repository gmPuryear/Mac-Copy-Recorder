# import pyperclip

# def pyperclipCopyPaste():
#     pyperclip.copy("Hello world!")
#     pyperclip.paste()

# def main():
#     pyperclipCopyPaste()


# if __name__ == "__main__":
#     main()

# mclip.py - A multi-clipboard program


import sys
import pyperclip

TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
        'busy': """Sorry, we can do this later this week or next week?""",
        'upsell': """Would you consider making this a monthly donation?"""}

if len(sys.argv) < 2:
    print("Usage: python main.py [keyphrase] - copy phrase text")
    sys.exit()

keyphrase = sys.argv[1] # first command line is the keyphrase

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print("Text for " + keyphrase + " copied to clipboard.")
else:
    print("There is no text for " + keyphrase)
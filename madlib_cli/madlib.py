from textwrap import dedent
import re


def read_template(path):
    try:
        with open(path, "r") as f:
            return f.read()
    except FileNotFoundError as fnf_error:
        raise fnf_error


def parse_template(string):
    words = tuple(re.findall(r"{([^{}]*)}", string))
    for x in words:
        string = string.replace(x, " ")
        return string, words


def merge(stripped, inputs):
    return stripped.format(*inputs)


def welcome():
    print(dedent("""
    Welcome to my Madlib!
    In order to play this game, please follow the prompts"""))


welcome()

# It was a {Adjective} and {Adjective} {Noun}.

noun = input("Please give me a noun ")
adjective = input("Please give me an Adjective ")
adjective1 = input("Please give me an Adjective ")

story = f"It was a {adjective} and {adjective1} {noun}."

print(story)


with open("madlib_cli/madlib.py", "r") as f:
    contents = f.read()


with open("madlib_cli/madlib_story.txt", "w+") as f2:
    f2.write(story)

# read_template("../tests/test_madlib.py")

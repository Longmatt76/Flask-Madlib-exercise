"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

story2 = Story(
    ["place","noun","verb","adverb","plural_noun","verb_pastense"],
    """When I was a kid I grew up in {place}, I would ride a {adjective} {noun} to school everyday
    until it {adverb} {verb_pastense} me so I started to {verb} but then a bunch of {plural_noun} ate my homework"""
)

story3 = Story(
    ["year","noun", "adjective","place","name","verb","noun","plural_noun"],
    """Back in {year} my buddy {name} used to {verb} {plural_noun} in {adjective} {place}."""
)

story4 = Story(
    ["adjective","plural_noun","noun","verb","adverb","number","verb_pasttense"],"""
    Look bro I got nutin against {plural_noun} but I'm not a {adjective} {noun} so you best {adverb} {verb} 
    off {number} times or else you are {verb_pasttense}"""
)


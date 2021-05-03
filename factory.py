"""
Learning Source Reference: https://github.com/faif/python-patterns/blob/master/patterns/creational/factory.py
"""


class GreekLocalizer:
    """A simple localizer a la gettext"""

    def __init__(self) -> None:
        self.translations = {"dog": "σκύλος", "cat": "γάτα"}

    def localize(self, msg: str) -> str:
        """We'll punt if we don't have a translation"""
        return self.translations.get(msg, msg)


class EnglishLocalizer:
    """Simply echoes the message"""

    def localize(self, msg: str) -> str:
        return msg


class GermanLocalizer:

    def __init__(self) -> None:
        self.translations = {"dog" : "hund", "cat" : "katze"}

    def localize(self, msg : str) -> str:
        return self.translations.get(msg,msg)

def get_localizer(language: str = "English") -> object:

    """Factory"""
    localizers = {
        "English": EnglishLocalizer,
        "Greek": GreekLocalizer,
        "German" : GermanLocalizer,
    }

    return localizers[language]()


def main():
    """
    # Create our localizers
    >>> e, g, ger = get_localizer(language="English"), get_localizer(language="Greek"), get_localizer(language="German")

    # Localize some text
    >>> for msg in "dog parrot cat bear".split():
    ...     print(e.localize(msg), g.localize(msg), ger.localize(msg))
    dog σκύλος hund
    parrot parrot parrot
    cat γάτα katze
    bear bear bear
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
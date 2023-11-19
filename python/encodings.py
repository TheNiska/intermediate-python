from unicodedata import normalize, combining
import string
import sys
import locale

EXPRESSIONS = '''\
    locale.getpreferredencoding()
    type(my_file)
    my_file.encoding
    sys.stdout.isatty()
    sys.stdout.encoding
    sys.stdin.isatty()
    sys.stdin.encoding
    sys.stderr.isatty()
    sys.stderr.encoding
    sys.getdefaultencoding()
    sys.getfilesystemencoding()
'''


def show_encodings() -> None:
    my_file = open('test', 'w')

    for line in EXPRESSIONS.split():
        value = eval(line)
        print(f"{line:>30} -> {value!r}")

    my_file.close()


def nfc_equal(str1: str, str2: str) -> bool:
    return normalize('NFC', str1) == normalize('NFC', str2)


def fold_equal(str1: str, str2: str) -> bool:
    return (
        normalize('NFC', str1).casefold()
        == normalize('NFC', str2).casefold()
    )


def shave_marks(text: str) -> str:
    normalized = normalize('NFD', text)
    shaved = ''.join(
        ch for ch in normalized if not combining(ch)
    )
    return normalize('NFD', shaved)


def shave_marks_latin(txt: str) -> str:
    """Remove all diacritic marks from Latin base characters"""

    norm_txt = normalize('NFD', txt)
    latin_base = False
    preserve = []
    for c in norm_txt:
        if combining(c) and latin_base:
            continue
        preserve.append(c)

        if not combining(c):
            latin_base = c in string.ascii_letters
    shaved = ''.join(preserve)
    return normalize('NFC', shaved)


if __name__ == '__main__':
    test1 = "Herr Voß: • ½ cup of Œtker™ caffè latte • bowl of açaí."
    result = shave_marks_latin(test1)
    print(result)
    show_encodings()

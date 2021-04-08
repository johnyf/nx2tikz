"""Assert that given path is a file."""
import argparse
import os.path


def isfile(path):
    """Raise `AssertionError` if `path` is not a file."""
    assert os.path.isfile(path)


def parse_args():
    """Parse command-line arguments."""
    description = 'Assert that given path is a file.'
    parser = argparse.ArgumentParser(
        description=description)
    parser.add_argument('path',
        help='file path to check')
    opts = parser.parse_args()
    return opts.path


if __name__ == '__main__':
    path = parse_args()
    isfile(path)

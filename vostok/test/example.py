import os
import sys
from vostok import Vostok, Parser

def main(file_path):
    parsed = Vostok.parse(file_path)

    parsed.entries()

main(sys.argv[1])

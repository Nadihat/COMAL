
import argparse
from comal.interpreter import Interpreter

def main():
    parser = argparse.ArgumentParser(description='A COBOL interpreter.')
    parser.add_argument('file', help='The COBOL file to execute.')
    args = parser.parse_args()

    with open(args.file, 'r') as f:
        code = f.read()

    interpreter = Interpreter(code)
    interpreter.run()

if __name__ == '__main__':
    main()

import re
import sys
import os
sys.path.append(os.path.dirname(__file__))
import settings

def main():
    with open(sys.argv[1], mode='r') as cv:
        if not cv.name.endswith('.template'):
            raise SystemExit('Wrong template name')
        out_name, _ = cv.name.rsplit('.', 1)
        out_name += '.html'
        cv_content = cv.read()
        output = cv_content.format(**settings.__dict__)
        out = open(out_name, 'w+')
        out.write(output)

if __name__ == "__main__":
    main()

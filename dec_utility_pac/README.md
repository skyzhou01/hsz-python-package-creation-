# hsz-python-package-creation

## Setup
- Create 
    - setup.py
    - LICENSE
    - Package Name

## Testing Package installation locally

- Create python virtural env and install the package by providing the full path.
    - python3 -m venv package-test-env
    - surce package-test-env/bin/activate
    - pip install -e ~/path-where-the-package/dec_utility_pac/

- Import the package 
    - from dec_utility_pac.print_example import say_hello
    - say_hello('sky')
    - help(say_hello)



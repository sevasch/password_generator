import os
import string
import argparse
import numpy as np

parser = argparse.ArgumentParser(description='Randomly generate passwords. ')

parser.add_argument('--lowercase', type=bool, default=True, help='if lowercase letters should be used (e.g. abcd)')
parser.add_argument('--uppercase', type=bool, default=True, help='if uppercase letters should be used (e.g. ABCD)')
parser.add_argument('--numbers', type=bool, default=True, help='if numbers should be used (e.g. 01234')
parser.add_argument('--symbols', type=bool, default=True, help='if random symbols should be used')
parser.add_argument('--selected_symbols', type=str, nargs='+', default=[], help='provide a list of symbols that should be used (e.g. %, &, ...)')
parser.add_argument('--number_of_passwords', type=int, default=100, help='number of passwords to create')
parser.add_argument('--password_length', type=int, default=10, help='password length')
parser.add_argument('--write_to_file', type=bool, default=False, help='if password(s) should be written to file')
parser.add_argument('--filename', type=str, default='passwordlists/pwlist.txt', help='filename to write files to (.txt)')

def create_password(args):
    def get_chars():
        return [np.random.choice(list(string.ascii_lowercase)) if args.lowercase else ''] \
                + [np.random.choice(list(string.ascii_uppercase)) if args.uppercase else ''] \
                + [np.random.choice(list(string.digits)) if args.numbers else ''] \
                + [np.random.choice(list(string.punctuation)) if args.symbols else ''] \

    password = get_chars() + args.selected_symbols

    if len(password) > args.password_length:
        np.random.shuffle(password)
        return ''.join(list(np.random.choice(password, args.password_length, replace=False)))
    else:
        while len(password) < args.password_length:
            password += np.random.choice(get_chars())
        np.random.shuffle(password)
        return ''.join(password)

def main(args):
    passwords = []
    for _ in range(args.number_of_passwords):
        passwords.append(create_password(args))

    for password in passwords:
        print(password)

    if args.write_to_file:
        if dir := os.path.dirname(args.filename):
            os.makedirs(dir, exist_ok=True)
        with open('{}.txt'.format(args.filename), 'w') as f:
            f.write('\n'.join(passwords))

if __name__ == '__main__':
    args = parser.parse_args()
    main(args)


#!/usr/bin/env python3

import argparse


# We define the necessary functions ahead of usage
def sum_ints(a, b):
    return a + b


def get_user_name():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--user', default='User')
    args = parser.parse_args()
    return args.user


# This makes sure we only run the main code if this isn't an import execution
if __name__ == '__main__':
    print(f'This is my script main function {get_user_name()}!!!')
    print(f'The sum of 40 + 40 is {sum_ints(40, 40)}')

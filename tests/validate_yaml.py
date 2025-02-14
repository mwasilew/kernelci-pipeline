#!/usr/bin/env python3
'''
Validate all yaml files in the config/ directory
'''

import os
import yaml
import sys

def validate_yaml():
    '''
    Validate all yaml files in the config/ directory
    '''
    for file in os.listdir('config/'):
        if file.endswith('.yaml'):
            with open('config/' + file, 'r') as stream:
                try:
                    yaml.safe_load(stream)
                except yaml.YAMLError as exc:
                    print(f'Error in {file}: {exc}')
                    sys.exit(1)

if __name__ == '__main__':
    validate_yaml()
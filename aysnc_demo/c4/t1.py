# -*- coding: utf-8 -*-

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--host', default='localhost')
parser.add_argument('--port', default=25000, type=int)
parser.add_argument('--channel', default='/topic/foo')
parser.add_argument('--interval', default=1, type=float)
parser.add_argument('--size', default=0, type=int)

print(parser.parse_args())
result = parser.parse_args()
print(result.host)
import grp
import os
import platform
import pwd
import sys

def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain; charset=utf-8')])
    return ['hello there'.encode('utf-8')]

if __name__ == '__main__':
    b = application(None, lambda x, y: None)
    print(b[0].decode('utf-8'))

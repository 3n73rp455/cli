import argparse
import os
import requests
import sys
from modules import auth, get


class CLI(object):

    def __init__(self, user, password, endpoint):
        self.token = auth.login(user, password)
        self.endpoint = endpoint

    def create(self):
        return

    def get(self, pk):
        pk = 1
        pw = get.password(token=self.token, pk=pk)
        return pw

    def update(self):
        return

    def delete(self):
        return

    def exit(self):
        sys.exit


def main():
    parser = argparse.ArgumentParser(description='Access enterPass API via Command Line')
    parser.add_argument('endpoint', type=str, help='What API endpoint to access')
    parser.add_argument('method', type=str, help='What method to call')
    args = parser.parse_args()

    endpoint = args.endpoint
    method = args.method

    pw = getattr(CLI(user='robin',
                     password='Welcome2',
                     endpoint=endpoint), method)(pk=1)

    print(pw)


if __name__ == "__main__":
    main()
# -*- coding: utf-8 -*-
"""
:copyright: Copyright 2019-2020 Sphinx Confluence Builder Contributors (AUTHORS)
:license: BSD-2-Clause (LICENSE)
"""

from sphinxcontrib.confluencebuilder.exceptions import ConfluenceBadApiError
from sphinxcontrib.confluencebuilder.publisher import ConfluencePublisher
from tests.lib import buildSphinx
from tests.lib import enableSphinxStatus
from tests.lib import prepareDirectories
from tests.lib import prepareSphinx
import argparse
import os
import sys

def process_sandbox(builder=None):
    test_dir = os.path.dirname(os.path.realpath(__file__))
    sandbox_dir = os.path.join(test_dir, 'sandbox')

    doc_dir, doctree_dir = prepareDirectories('sandbox-test')
    buildSphinx(sandbox_dir, doc_dir, doctree_dir, builder=builder,
        relax=True)

def process_raw_upload():
    test_dir = os.path.dirname(os.path.realpath(__file__))
    sandbox_dir = os.path.join(test_dir, 'sandbox')
    raw_file = os.path.join(sandbox_dir, 'raw.conf')

    if not os.path.exists(raw_file):
        print('[sandbox] missing file', raw_file)
        return

    doc_dir, doctree_dir = prepareDirectories('sandbox-test')
    with prepareSphinx(sandbox_dir, doc_dir, doctree_dir, relax=True) as app:
        publisher = ConfluencePublisher()
        publisher.init(app.config)
        publisher.connect()

        while True:
            data = {
                'labels': [],
            }

            with open(raw_file, 'r') as f:
                data['content'] = f.read()

            print('[sandbox] publishing page...')
            try:
                publisher.storePage('raw', data)
            except ConfluenceBadApiError as ex:
                print('[sandbox] failed to publish content:', ex)

            print('[sandbox] any key to retry; q to quit')
            if input().lower() == 'q':
                break

def main():
    enableSphinxStatus()

    parser = argparse.ArgumentParser(prog=__name__,
        description='Atlassian Confluence Sphinx Extension Sandbox')
    parser.add_argument('--builder', '-b')
    parser.add_argument('--raw-upload', '-R', action='store_true')
    parser.add_argument('--verbose', '-v', action='store_true')

    args, ___ = parser.parse_known_args(sys.argv[1:])
    parser.parse_args()

    if args.verbose:
        if 'SPHINX_VERBOSITY' not in os.environ:
            os.environ['SPHINX_VERBOSITY'] = '2'

    if args.raw_upload:
        print('[sandbox] raw-upload test')
        process_raw_upload()
    else:
        print('[sandbox] documentation test')
        process_sandbox(args.builder)

    return 0

if __name__ == '__main__':
    sys.exit(main())

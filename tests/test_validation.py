# -*- coding: utf-8 -*-
"""
:copyright: Copyright 2018-2020 Sphinx Confluence Builder Contributors (AUTHORS)
:license: BSD-2-Clause (LICENSE)
"""

from sphinxcontrib.confluencebuilder.exceptions import ConfluenceBadApiError
from tests.lib import buildSphinx
from tests.lib import enableSphinxStatus
from tests.lib import prepareConfiguration
from tests.lib import prepareDirectories
import os
import sys
import unittest

DEFAULT_TEST_BASE = 'sphinxcontrib-confluencebuilder Home'
DEFAULT_TEST_DESC = 'test state'
DEFAULT_TEST_KEY = 'test-holder'
DEFAULT_TEST_SPACE = 'confluencebuilder'
DEFAULT_TEST_URL = 'https://jdknight.atlassian.net/wiki/'
DEFAULT_TEST_USER = 'sphinxcontrib-confluencebuilder@jdknight.me'

class TestConfluenceValidation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        enableSphinxStatus()

        # build configuration
        cls.config = prepareConfiguration()
        cls.config['confluence_disable_notifications'] = True
        cls.config['confluence_page_hierarchy'] = True
        cls.config['confluence_parent_page'] = DEFAULT_TEST_BASE
        cls.config['confluence_publish'] = True
        cls.config['confluence_space_name'] = DEFAULT_TEST_SPACE
        cls.config['confluence_server_url'] = DEFAULT_TEST_URL
        cls.config['confluence_server_user'] = DEFAULT_TEST_USER
        cls.config['confluence_timeout'] = 1
        cls.test_desc = DEFAULT_TEST_DESC
        cls.test_key = DEFAULT_TEST_KEY

        # overrides from user
        try:
            from validation_test_overrides import config_overrides
            cls.config.update(config_overrides)
        except ImportError:
            pass
        try:
            from validation_test_overrides import config_test_desc
            cls.test_desc = config_test_desc
        except ImportError:
            pass
        try:
            from validation_test_overrides import config_test_key
            cls.test_key = config_test_key
        except ImportError:
            pass

        # finalize configuration
        cls.config['confluence_publish_prefix'] = ''
        cls.config['confluence_purge'] = False
        cls.config['rst_epilog'] = """
.. |test_key| replace:: {}
.. |test_desc| replace:: {}
""".format(cls.test_key, cls.test_desc)

        # find validate-sets base folder
        test_dir = os.path.dirname(os.path.realpath(__file__))
        cls.datasets = os.path.join(test_dir, 'validation-sets')

        # setup base structure
        dataset = os.path.join(cls.datasets, 'base')
        doc_dir, doctree_dir = prepareDirectories('validation-set-base')

        # build/publish test base page
        buildSphinx(dataset, doc_dir, doctree_dir, cls.config)

        # finalize configuration for tests
        cls.config['confluence_master_homepage'] = False
        cls.config['confluence_purge'] = True
        cls.config['confluence_purge_from_master'] = True
        if cls.test_key != DEFAULT_TEST_KEY:
            cls.config['confluence_publish_prefix'] = '{}-'.format(cls.test_key)
        cls.config['confluence_parent_page'] = cls.test_key

    def test_autodocs(self):
        config = dict(self.config)
        config['extensions'].append('sphinx.ext.autodoc')
        config['extensions'].append('sphinx.ext.autosummary')

        dataset = os.path.join(self.datasets, 'auto-ext')
        doc_dir, doctree_dir = prepareDirectories('validation-set-auto')
        sys.path.insert(0, os.path.join(dataset, 'src'))

        buildSphinx(dataset, doc_dir, doctree_dir, config)

        sys.path.pop(0)

    def test_common(self):
        config = dict(self.config)
        config['imgmath_image_format'] = 'svg'

        dataset = os.path.join(self.datasets, 'common')
        doc_dir, doctree_dir = prepareDirectories('validation-set-common')

        buildSphinx(dataset, doc_dir, doctree_dir, config)

    def test_common_macro_restricted(self):
        config = dict(self.config)

        dataset = os.path.join(self.datasets, 'common')
        doc_dir, doctree_dir = prepareDirectories('validation-set-common-nm')

        config['confluence_adv_restricted'] = [
            'anchor',
            'children',
            'code',
            'info',
            'viewfile',
            'jira'
        ]
        config['confluence_header_file'] = os.path.join(dataset, 'no-macro.tpl')
        config['confluence_publish_prefix'] += 'nomacro-'

        buildSphinx(dataset, doc_dir, doctree_dir, config)

    def test_header_footer(self):
        config = dict(self.config)

        dataset = os.path.join(self.datasets, 'header-footer')
        doc_dir, doctree_dir = prepareDirectories('validation-set-hf')

        config['confluence_header_file'] = os.path.join(dataset, 'header.tpl')
        config['confluence_footer_file'] = os.path.join(dataset, 'footer.tpl')

        buildSphinx(dataset, doc_dir, doctree_dir, config)

    def test_hierarchy(self):
        config = dict(self.config)
        config['confluence_max_doc_depth'] = 2
        config['confluence_page_hierarchy'] = True

        dataset = os.path.join(self.datasets, 'hierarchy')
        doc_dir, doctree_dir = prepareDirectories('validation-set-hierarchy')

        buildSphinx(dataset, doc_dir, doctree_dir, config)

    def test_nonjsonresponse(self):
        config = dict(self.config)
        config['confluence_server_url'] = 'https://example.com/'
        dataset = os.path.join(self.datasets, 'base')
        doc_dir, doctree_dir = prepareDirectories('validation-set-nonjsonresponse')

        with self.assertRaises(ConfluenceBadApiError):
            buildSphinx(dataset, doc_dir, doctree_dir, config)

if __name__ == '__main__':
    sys.exit(unittest.main(verbosity=0))

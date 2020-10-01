contributing
============

Contributions to this extension are welcome and much appreciated.

.. contents::
   :depth: 2

.. sectnum::

reporting issues
----------------

Bugs, enhancements and more can be reported to this extension's GitHub
`issue tracker`_. It is recommended to search for a related issue before
attempting to submit a new issue.

When reporting a bug, it is recommended to include at least the following:

- sphinxcontrib-confluencebuilder's extension version
- Python version
- Sphinx version

Additional logs from a ``sphinx-build`` attempt can be helpful as well (if
applicable).

submitting changes
------------------

Contributions can be provided as `pull requests`_ to this extension's GitHub
project. New contributors should familiarize themselves with the following:

- **(required)** Sign your work (`Developer’s Certificate of Origin`_). This is
  confirmed with the inclusion of ``Signed-off-by`` in submitted commit
  messages.
- Builds are required\* to pass to be accepted (\* with some exceptions in very
  specific scenarios). When a pull request is submitted, continues integration
  tests will be invoked. A developer can invoke ``tox`` at the root of the
  checked out repository to validate changes before submitting a pull request.
- Keep a narrow scope for proposed changes. Submitting multiple feature changes
  in a single pull request is not always helpful. Use multiple commits to
  separate changes over stacking all changes in a single commit (for example,
  related implementation and documentation changes can be submitted in a single
  pull request, but are best presented in their own individual commits).
- Add unit tests (if applicable). Adding unit tests to validate new changes
  helps build confidence for the new modifications and helps prevent future
  changes from breaking the new feature/fix.
- Update documentation (if applicable). If a new change introduces, for example,
  a new configuration entry or markup support has changed with a request, do not
  forget to update respective documentation as well.
- **Do not** update ``AUTHORS`` or ``CHANGES.rst``. Author information and
  change log information are managed by this extension's maintainers. These
  files may be updated during a development window and will always be updated
  during a release. If a contributor does not wish to add themselves to the
  ``AUTHORS`` document, they may opt-out be explicitly indicating in a pull
  request or issue. In select cases, users may open pull requests for these
  documents if corrections are needed.

While maintainers will help strive to review, merge changes and provide support
(when possible), the process may take some time. Please be patient and happy
coding.

guidelines
----------

This extension will support various Python interpreter versions, Sphinx versions
and Confluence versions. The goal of this extension is to include support for
all stable Python interpreters and Confluence versions which have yet to be
marked as end-of-life and support Sphinx versions with a suggested maximum of
five major-minor trees.

- Python interpreters that have not been marked as end-of-life will be supported
  by this extension. An exception exists for Python 2.7 at this time where
  support _may_ extend to the RHEL's supported end-of-life date for Python 2.7
  of June 2024 (see also `How is Python 2 supported in RHEL after 2020?`_). Note
  that this is the maximum date for support; however, support may be dropped
  earlier that this date (with a notification). At minimum, Python 2.7 will be
  supported until the end of the 2020 calendar year (a year after Python's
  end-of-life date for Python 2.7).
- Supported Confluence versions will be supported versions listed in
  `Atlassian Support End of Life Policy`_.
- Supported Sphinx versions include the last five major-minor versions of the
  application (for example: 3.2.x, 3.1.x, 3.0.x, 2.4.x, 2.3.x). An exception
  exists for Sphinx 1.8.x series, which will be supported until this extension's
  support for Python 2.7 has been dropped.

`PEP 8`_ is a standard styling guide for Python projects and is recommended for
considerations when making contributions. On that note, please read the
following:

- Line lengths are recommended to be at maximum 79 characters (relaxed to even
  80 characters) for implementation. This option is not explicitly enforced in
  styling checks primarily since there can be valid cases where lines may exceed
  such limits (e.g. a long URL in comments).
- The recommendation of two blank lines (in various scenarios) are ignored.
  Apply appropriate blank lines where it makes sense in the implementation.
- Avoid multiple imports on a single line (even for ``from ...`` usages). This
  is to help long term maintenance of imports with minimal clashing between
  various modules/types/etc. being used.

code of conduct
===============

our pledge
----------

In the interest of fostering an open and welcoming environment, we as
contributors and maintainers pledge to making participation in our project and
our community a harassment-free experience for everyone, regardless of age, body
size, disability, ethnicity, gender identity and expression, level of
experience, nationality, personal appearance, race, religion, or sexual identity
and orientation.

our standards
-------------

Examples of behavior that contributes to creating a positive environment
include:

* Using welcoming and inclusive language
* Being respectful of differing viewpoints and experiences
* Gracefully accepting constructive criticism
* Focusing on what is best for the community
* Showing empathy towards other community members

Examples of unacceptable behavior by participants include:

* The use of sexualized language or imagery and unwelcome sexual attention or
  advances
* Trolling, insulting/derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or electronic
  address, without explicit permission
* Other conduct which could reasonably be considered inappropriate in a
  professional setting

our responsibilities
--------------------

Project maintainers are responsible for clarifying the standards of acceptable
behavior and are expected to take appropriate and fair corrective action in
response to any instances of unacceptable behavior.

Project maintainers have the right and responsibility to remove, edit, or reject
comments, commits, code, wiki edits, issues, and other contributions that are
not aligned to this Code of Conduct, or to ban temporarily or permanently any
contributor for other behaviors that they deem inappropriate, threatening,
offensive, or harmful.

scope
-----

This Code of Conduct applies both within project spaces and in public spaces
when an individual is representing the project or its community. Examples of
representing a project or community include using an official project e-mail
address, posting via an official social media account, or acting as an appointed
representative at an online or offline event. Representation of a project may be
further defined and clarified by project maintainers.

enforcement
-----------

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported by contacting the project team at @tonybaloney. All complaints will be
reviewed and investigated and will result in a response that is deemed necessary
and appropriate to the circumstances. The project team is obligated to maintain
confidentiality with regard to the reporter of an incident. Further details of
specific enforcement policies may be posted separately.

Project maintainers who do not follow or enforce the Code of Conduct in good
faith may face temporary or permanent repercussions as determined by other
members of the project's leadership.

attribution
-----------

This Code of Conduct is adapted from the `Contributor Covenant`_, version 1.4.

.. _Atlassian Support End of Life Policy: https://confluence.atlassian.com/support/atlassian-support-end-of-life-policy-201851003.html
.. _Contributor Covenant: https://contributor-covenant.org/version/1/4/
.. _Developer’s Certificate of Origin: https://developercertificate.org/
.. _How is Python 2 supported in RHEL after 2020?: https://access.redhat.com/solutions/4455511
.. _PEP 8: https://www.python.org/dev/peps/pep-0008
.. _issue tracker: https://github.com/sphinx-contrib/confluencebuilder/issues
.. _pull requests: https://github.com/sphinx-contrib/confluencebuilder/pulls

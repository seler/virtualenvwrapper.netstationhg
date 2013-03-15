#!/usr/bin/env python
# encoding: utf-8
"""virtualenvwrapper.project plugin for netstation mercurial repositories
"""

import logging
import subprocess


log = logging.getLogger(__name__)


def get_url(project):
    url = 'ssh://wwwedit@bitbucket.org/hg/{project}'.format(project=project)
    return url


def template(args):
    """Clones a hg repository into the project directory.
    """
    project = args[0]
    url = get_url(project)
    if url:
        log.info('Cloning %s', url)
        subprocess.call(['hg', 'clone', url, project], shell=False)
    return

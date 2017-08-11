import sys
import logging
import pkg_resources

# Custom logger
LOG = logging.getLogger(name=__name__)
LOG.addHandler(logging.NullHandler())

# PEP 396 style version marker
try:
    __version__ = pkg_resources.get_distribution('b3').version
except pkg_resources.DistributionNotFound:
    LOG.warning("Could not get the package version from pkg_resources, you did't installed b3")
    __version__ = 'unknown'


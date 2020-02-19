import sys
import os
import logging

sys.path.append("/srv/bouyearfestival/bouyearfestival")
logging.basicConfig(stream = sys.stderr)

from server import app as application
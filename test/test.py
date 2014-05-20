import string
from optparse import OptionParser
import warnings
import collections
import sets
import signal
import subprocess
from time import strftime

import pysam
from bx.bbi.bigwig_file import BigWigFile
from bx.intervals import *
import numpy as np

from cmmodule  import ireader
from cmmodule  import BED
from cmmodule  import annoGene
from cmmodule  import bam_cigar
from cmmodule  import sam_header
from cmmodule  import wig_reader
from cmmodule  import myutils


if myutils.which('sort') is not None:
	sorted_bgr = subprocess.Popen(["sort", '-k1,1', '-k2,2n', 'a'], stdout=subprocess.PIPE)
	output = sorted_bgr.stdout.read()
	print output

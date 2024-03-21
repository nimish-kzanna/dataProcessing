# export PYTHONPATH="${PYTHONPATH}:/home/nimish/go/src/github.com/kzanna/logparser"

#!/usr/bin/env python
"""
This script demonstrates the usage of logparser to parse your own log data.
To get started, please first install the logparser via `pip install logpai`.
To get better parsing results, you are suggested to tune the hyper-parameters
`st` and `depth`.
"""

from logparser.Drain import LogParser
import gc

gc.collect()

input_dir = 'unlabelled/' # The input directory of log file
output_dir = 'label_result/'  # The output directory of parsing results
log_file = 'log'  # The input log file name
log_format = '<Content>' # Define log format to split message fields
# Regular expression list for optional preprocessing (default: [])
regex = [
    r'(/|)([0-9]+\.){3}[0-9]+(:[0-9]+|)(:|)' # IP
]
st = 0.6  # Similarity threshold
depth = 8  # Depth of all leaf nodes

parser = LogParser(log_format, indir=input_dir, outdir=output_dir,  depth=depth, st=st, rex=regex)
parser.parse(log_file)

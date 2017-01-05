"""Encoder-Decoder with search for machine translation.

In this demo, encoder-decoder architecture with attention mechanism is used for
machine translation. The attention mechanism is implemented according to
[BCB]_. The training data used is WMT15 Czech to English corpus, which you have
to download, preprocess and put to your 'datadir' in the config file. Note
that, you can use `prepare_data.py` script to download and apply all the
preprocessing steps needed automatically.  Please see `prepare_data.py` for
further options of preprocessing.

.. [BCB] Dzmitry Bahdanau, Kyunghyun Cho and Yoshua Bengio. Neural
   Machine Translation by Jointly Learning to Align and Translate.
"""

import argparse
import logging
import pprint

import configurations

from machine_translation import main

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='run.log',
                    filemode='a')
logger = logging.getLogger(__name__)

# Get the arguments
parser = argparse.ArgumentParser()
parser.add_argument(
        "--proto", default="get_config_zh2en",
        help="Prototype config to use for config")
parser.add_argument(
        "--bokeh", default=False, action="store_true",
        help="Use bokeh server for plotting")
parser.add_argument(
        "--mode", choices=["train", "test"], default='train',
        help="The mode to run. In the `train` mode a model is trained."
             " In the `translate` mode a trained model is used to translate"
             " an input file and generates tokenized translation.")
parser.add_argument(
        "--best_params", default='', help="Input the params of best model")
args = parser.parse_args()

if __name__ == "__main__":
    # Get configurations for model
    configuration = getattr(configurations, args.proto)()
    configuration['best_params'] = args.best_params
    logger.info("Model options:\n{}".format(pprint.pformat(configuration)))
    # Get data streams and call main
    main(args.mode, configuration, args.bokeh)

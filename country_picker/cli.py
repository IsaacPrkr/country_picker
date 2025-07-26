# country_picker/cli.py

import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Country Picker GUI App")
    parser.add_argument('--select', help='Pre-select a country name')
    return parser.parse_args()

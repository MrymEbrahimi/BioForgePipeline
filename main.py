import argparse
import logging
import os

from src.reporting.pipeline import run_pipeline

parser = argparse.ArgumentParser( )

parser.add_argument(
    "--input",
    required=True,
    help="Path to the input FASTA file"
)
parser.add_argument(
    "--out",
    required=True,
    help="Output directory"
)
parser.add_argument(
    "--min-length",
    type=int,
    default=0,
    help="Minimum ORF length"
)
parser.add_argument(
    "--min-weight",
    type=float,
    default=0.0,
    help="Minimum molecular weight")


args = parser.parse_args()

os.makedirs(args.out, exist_ok=True)

logging.basicConfig(
    filename=os.path.join(args.out, "bioforge.log"),
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)
run_pipeline(args.input, args.out, args.min_length, args.min_weight)
print("--- PIPELINE FINISHED ---")
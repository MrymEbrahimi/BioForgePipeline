import logging
import re

from exceptions import FastaFormatError
from record import FASTARecord

HEADER_RE = re.compile(r"^>\s*(?P<id>\S+)\s*(?P<desc>.*)$")

def _build_record(rec_id, description, sequence_lines):
    if not sequence_lines:
        raise FastaFormatError(f"Header '{rec_id}' has no sequence")
    organism_match = re.search(
        r"organism=([^=]+?)(?:\s+\w+=|$)",
        description
    )
    organism = organism_match.group(1) if organism_match else None
    return FASTARecord(rec_id, description, "".join(sequence_lines),organism)

def parse_fasta(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    if not content.strip():
        raise FastaFormatError("File is empty")

    current_id = None
    current_description = None
    current_sequence = []
    records = []
    seen_ids = set()

    for line_no, line in enumerate(content.splitlines(), start=1):
        if not line.strip():
            continue

        if line.startswith(">"):
            match = HEADER_RE.match(line)
            if not match:
                raise FastaFormatError(f"Line {line_no}: invalid header")

            if current_id is not None:
                records.append(
                    _build_record(current_id, current_description, current_sequence)
                )

            current_id = match.group("id")
            current_description = match.group("desc")
            current_sequence = []

            if current_id in seen_ids:
                logging.warning("Line %d: duplicate ID '%s'", line_no, current_id)
            seen_ids.add(current_id)
        else:
            if current_id is None:
                raise FastaFormatError(f"Line {line_no}: sequence found before header")
            current_sequence.append(line.strip().upper())

    if current_id is not None:
        records.append(_build_record(current_id, current_description, current_sequence))


    return records


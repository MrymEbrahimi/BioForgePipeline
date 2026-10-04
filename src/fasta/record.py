from dataclasses import dataclass

@dataclass
class FASTARecord:
    id: str
    description: str
    sequence: str
    organism: str | None = None
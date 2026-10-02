class FASTARecord:
    def __init__(self, id,description,sequence,organism=None):
        self.id= id
        self.description = description
        self.sequence = sequence
        self.organism = organism
        
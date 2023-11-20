import os

class DocText:
    __slots__ = ('text', 'references')
    text: str
    references: set[int] # Refs to Document[document_id]

    def __init__(self):
        pass


class Document(object):
    document_id: int # Auto-generating document ID according to it's location in folder
    document_text: DocText

    def __init__(self, filepath) -> None:
        pass


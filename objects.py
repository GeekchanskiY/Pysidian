import os

class Document(object):

    class SubDocument(object):
        def __init__(self, title: str, text: list[str], parent_doc: object|None) -> None:
            if parent_doc is not None and type(parent_doc) == type(self):
                self.parent_doc = parent_doc
            else:
                parent_doc = None

    document_id: int # Auto-generating document ID according to it's location in folder
    title: str
    root_doc: SubDocument

    def __init__(self, document_id: int, filepath: str) -> None:
        if not os.path.isfile(filepath):
            raise OSError(f'{filepath} is not a file!')
        
        if filepath[-2:] != 'md':
            raise ValueError('Document can only be created from .md docs')

        with open(file=filepath, mode='r', encoding='utf-8') as f:
            self.text = [l.replace('\n', '') for l in f.readlines()]
            
        self.title = filepath.split('/')[-1].replace('.md', '')
        
        print(self.title)


    def is_valid(seld) -> bool:
        pass


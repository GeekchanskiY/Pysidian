import os
import re

class Document(object):
    regex_image: str = r'!\[\[[^\]]*\]\]'
    regex_link: str = r'\[\[[^\]]*\]\]'
    class SubDocument(object):
        text: list[str] = []
        def __init__(self, title: str, parent_doc: object|None) -> None:
            if parent_doc is not None and type(parent_doc) == type(self):
                self.parent_doc = parent_doc
            else:
                parent_doc = None
        
        def add_line(self, text: str) -> None:
            self.text.append(text)

    

    document_id: int # Auto-generating document ID according to it's location in folder
    title: str
    root_doc: SubDocument
    links: list[str]

    def __init__(self, document_id: int, filepath: str) -> None:
        if not os.path.isfile(filepath):
            raise OSError(f'{filepath} is not a file!')
        
        if filepath[-2:] != 'md':
            raise ValueError('Document can only be created from .md docs')

        with open(file=filepath, mode='r', encoding='utf-8') as f:
            self.text = [l.replace('\n', '') for l in f.readlines()]
            
        self.title = filepath.split('/')[-1].replace('.md', '')
        self.root_doc = self.SubDocument('root', None)
        for r in self.text:
            if r.find('#') == -1:
                self.root_doc.add_line(r)
            # print(re.findall(self.regex_link, r))
        # print(self.title)


    def is_valid(seld) -> bool:
        pass


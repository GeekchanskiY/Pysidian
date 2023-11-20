import os
import re

class Document(object):
    regex_image: str = r'!\[\[[^\]]*\]\]'
    regex_link: str = r'\[\[[^\]]*\]\]'
    class SubDocument(object):
        text: list[str] = []
        subdocumets: list = []
        layer: int = 0
        def __init__(self, title: str, parent_doc: 'SubDocument or None') -> None:
            if parent_doc is not None and type(parent_doc) == type(self):
                self.parent_doc = parent_doc
                self.layer = self.parent_doc.layer + 1
            else:
                parent_doc = None
        
        def add_line(self, text: str) -> None:
            self.text.append(text)
        
        def add_subdocument(self, subdocument: object):
            if type(subdocument) != type(self):
                raise ValueError('Subdocument can only be an instance of this class!')
            if subdocument.layer >= self.layer:
                raise RuntimeError('Can\'t add child subdocument with the same layer as parent one')

    

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
        current_document_level: int = 0
        current_subdocument_queue: list[self.SubDocument] = []
        
        for r in self.text:
            line_layer_finder: int = 0

            for x in r:
                if x == '#': line_layer_finder += 1
                else: break
            
            if line_layer_finder != 0:

                if line_layer_finder >= current_document_level:
                    if current_subdocument_queue:
                        pass
                    else:
                        new_subdocument = self.SubDocument(title=r.replace('#', '').strip(), parent_doc=self.root_doc)
                        current_subdocument_queue.append(new_subdocument)
                else:
                    pass
            else:
                if current_subdocument_queue:
                    pass
            # print(re.findall(self.regex_link, r))
        # print(self.title)


    def is_valid(seld) -> bool:
        pass


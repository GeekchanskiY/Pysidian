import os
import io
import logging

from objects import Document

FORMAT = '%(asctime)s | %(pathname)s | %(vault_name)s | %(levelname)s - %(message)s'
old_factory = logging.getLogRecordFactory()

def record_factory(*args, **kwargs):
    record = old_factory(*args, **kwargs)
    record.vault_name = 'THEORY' # TODO: get vault here
    return record

logging.setLogRecordFactory(record_factory)

logging.basicConfig(format=FORMAT, level=logging.DEBUG)
logger = logging.getLogger('reader')

class Reader(object):
    workdir: str|None = None
    document_pathes: list[str] = []
    documents: list[Document] = []

    ignore_folders: list[str] = ['git',]

    def __init__(self, workdir: str) -> None:
        '''
            wodkdir: str absolute path to obsidian vault
        '''
        if os.path.isdir(workdir):
            self.workdir = workdir
        else: 
            raise ValueError('Incorrect workdir!')

        self._get_documents()

        for i, path in enumerate(self.document_pathes):
            self.documents.append(Document(i, path))


    def _get_documents(self):
        if self.workdir is None:
            raise RuntimeError('Cant get documents when workdir is not defined!')

        def get_folder_info(folder: str) -> list[str]:
            res = []
            for i in os.listdir(folder):
                if i[0] == '.': # ignores dotfiles
                    continue
                if (os.path.isdir(folder+i)):
                    for x in get_folder_info(folder+i+'/'):
                        res.append(x)
                else:
                    if (i.split('.')[1]) == 'md':
                        res.append(folder + i)
            return res
                

        self.document_pathes = get_folder_info(self.workdir)
        logger.info(f'Found {len(self.document_pathes)} documents in vault')

if __name__ == '__main__':
    folder = '/home/dmitry/repos/THEORY/'

    reader = Reader(folder)
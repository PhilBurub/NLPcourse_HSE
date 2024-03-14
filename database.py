import wget
import zipfile
import chromadb
from pathlib import Path

class VectDB:
    def __init__(self, db_path='./vectors_corpora'):
        self.path = Path(db_path)
        if not self.path.exists():
            self.path.mkdir()
        filename = wget.download('https://drive.google.com/uc?export=download&id=14diuTvu6hBNE241URCBOUxzo6CixC7gn')
        with zipfile.ZipFile(filename, 'r') as zip_ref:
            zip_ref.extractall(db_path)
        Path(filename).unlink()
        self.client = chromadb.PersistentClient(path=str(self.path.joinpath('vectors_corpora')))
        self.collection = self.client.get_collection('ontology')

    def query(self, query_text, top_n=10):
        return self.collection.query(query_texts=query_text,
                                     n_results=top_n)

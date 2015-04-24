from CodernityDB.hash_index import HashIndex
from CodernityDB.tree_index import TreeBasedIndex


class DuckTagsDataBaseIndexCreator(object):

    @staticmethod
    def create_hash_index(db_path, index_name):

        class DuckTagsHashIndex(HashIndex):
            def __init__(self, *args, **kwargs):
                kwargs['key_format'] = '16s'
                super(DuckTagsHashIndex, self).__init__(*args, **kwargs)

            def make_key_value(self, data):
                return md5(data[self.name]).digest(), None

            def make_key(self, key):
                return md5(key).digest()

        return DuckTagsHashIndex(db_path, index_name)

    @staticmethod
    def create_tree_index(db_path, index_name):

        class DuckTagsTreeIndex(TreeBasedIndex):
            def __init__(self, *args, **kwargs):
                kwargs['node_capacity'] = 10
                kwargs['key_format'] = 'I'

            def make_key_value(self, data):
                return data[self.name]

            def make_key(self, key):
                return key

        return DuckTagsTreeIndex(db_path, index_name)
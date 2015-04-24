from Src.DuckTagsDatabaseTools.DuckTagsDataBaseIndexCreator import DuckTagsDataBaseIndexCreator

import functools


def determine_search_function(search_for_files):

    @functools.wraps(search_for_files)
    def wrapper(search_manager, search_option, **search_args):

        if search_option in search_manager.search_directly_tags:
            db_index_name = search_manager.create_hash_index()
            search_manager.search_function = search_manager.__search_directly__(db_index_name)
        elif search_option in search_manager.search_with_limits_tags:
            db_index_name = search_manager.create_tree_index()
            search_manager.search_function = search_manager.__search_with_limits__(db_index_name)

        ret_value = search_for_files(search_option, **search_args)

        search_manager.search_function = None
        return ret_value

    return wrapper


class DuckTagsSearchManager(object):
    def __init__(self, db_manager):
        self.db_manager = db_manager
        self.search_directly_tags = ['artist', 'title', 'genre', 'album']
        self.search_with_limits_tags = ['year']
        self.search_function = None

    @determine_search_function
    def search_for_files(self, search_option, **search_args):
        return self.search_function(**search_args)

    def create_hash_index(self, index_name):
        data_base_index = DuckTagsDataBaseIndexCreator.create_hash_index(self.db_manager.db.path, index_name)
        self.db_manager.append_db_index(data_base_index)
        return data_base_index.name

    def create_tree_index(self, index_name):
        data_base_index = DuckTagsDataBaseIndexCreator.create_tree_index(self.db_manager.db.path, index_name)
        self.db_manager.append_db_index(data_base_index)
        return data_base_index.name

    def __search_with_limits__(self, db_index_name):

        def limit_search(**search_args):
            start = search_args['start']
            end = search_args['end']

            return self.db_manager.db.get_many(db_index_name, start=start, end=end, limit=-1, with_doc=True)

        return limit_search

    def __search_directly__(self, db_index_name):

        def direct_search(**search_args):
            searched_value = search_args['value']
            return self.db_manager.db.get_many(db_index_name, searched_value, with_doc=True)

        return direct_search
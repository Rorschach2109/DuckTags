from DuckTags_API.DuckTagsFileAPI import DuckTagsFileAPI
from DuckTags_API.DuckTagsMetadataAPI import DuckTagsMetadataAPI
from Src.DuckTagsDatabaseTools.DuckTagsMusicFileModel import DuckTagsMusicFileModel

import functools

import sqlite3 as lite


def database_access(foo):

    @functools.wraps(foo)
    def wrapper(manager, *args):
        manager.connection = lite.connect(manager.db_name)

        with manager.connection:
            manager.connection.row_factory = lite.Row
            manager.db_cursor = manager.connection.cursor()
            ret_value = foo(manager, *args)

        manager.db_cursor = None

        manager.connection.close()
        manager.connection = None

        return ret_value

    return wrapper


class DuckTagsDataBaseManager(object):
    def __init__(self):
        self.file_api = DuckTagsFileAPI()
        self.metadata_api = DuckTagsMetadataAPI()

        self.db_name = 'DuckTagsDB.db'
        self.connection = None
        self.db_cursor = None

        self.genres_table_name = 'Genres'
        self.albums_table_name = 'Albums'
        self.artists_table_name = 'Artists'
        self.music_files_table_name = 'MusicFiles'

        self.search_options = {
            'title_search': self.title_search_foo,
            'artist_search': self.artist_search_foo,
            'album_search': self.album_search_foo,
            'year_search': self.year_search_foo,
            'genre_search': self.genre_search_foo
        }

    def add_music_files_from_folder(self, folder_path):
        music_files_dict = self.__get_music_files_from_folder__(folder_path)
        for folder in music_files_dict:
            music_file_path = '/'.join([folder, music_files_dict[folder]])
            music_file_model = self.metadata_api.get_music_file_metadata(music_file_path)
            self.__insert_music_file_to_db__(music_file_model)

    @database_access
    def initialize_db(self):
        self.__create_genres_table__()
        self.__create_albums_table__()
        self.__create_artists_table__()
        self.__create_music_files_table__()

    def __create_genres_table__(self):
        self.db_cursor.execute("CREATE TABLE IF NOT EXISTS %s( \
                               Id INTEGER PRIMARY KEY, \
                               GenreName TEXT)" % self.genres_table_name)

    def __create_albums_table__(self):
        self.db_cursor.execute("CREATE TABLE IF NOT EXISTS %s( \
                               Id INTEGER PRIMARY KEY, \
                               AlbumName TEXT, \
                               AlbumYear INTEGER)" %
                               self.albums_table_name)

    def __create_artists_table__(self):
        self.db_cursor.execute("CREATE TABLE IF NOT EXISTS %s( \
                               Id INTEGER PRIMARY KEY, \
                               ArtistName TEXT)" %
                               self.artists_table_name)

    def __create_music_files_table__(self):
        self.db_cursor.execute("CREATE TABLE IF NOT EXISTS MusicFiles( \
                               Id INTEGER PRIMARY KEY, \
                               Path TEXT, \
                               Title TEXT, \
                               ArtistId, \
                               AlbumId, \
                               GenreId, \
                               FOREIGN KEY(ArtistId) REFERENCES %s(Id) \
                               FOREIGN KEY(AlbumId) REFERENCES %s(Id) \
                               FOREIGN KEY(GenreId) REFERENCES %s(Id))" %
                               (self.artists_table_name,
                                self.albums_table_name,
                                self.genres_table_name))

    def __get_music_files_from_folder__(self, folder_path):
        files_dict = self.file_api.get_files_dict_from_folder(folder_path)
        return self.file_api.get_music_files_from_files_dict(files_dict)

    @database_access
    def __insert_music_file_to_db__(self, music_file_model):
        genre_id = self.__insert_genre_to_db__(music_file_model.genre)
        album_id = self.__insert_album_to_db__(music_file_model.album, music_file_model.year)
        artist_id = self.__insert_artist_to_db__(music_file_model.artist)

        music_file_id = self.db_cursor.execute("SELECT Id FROM %s WHERE Path=?" % self.music_files_table_name,
                                               (music_file_model.path,))
        if not music_file_id:
            self.db_cursor.execute("INSERT INTO %s, VALUES(NULL, ?, ?, ?, ?, ?)" % self.music_files_table_name,
                                   (music_file_model.path, music_file_model.title, artist_id, album_id, genre_id))

    def __insert_genre_to_db__(self, genre_name):
        genre_id = self.db_cursor.execute("SELECT Id FROM %s WHERE GenreName=?" % self.genres_table_name, (genre_name,))
        if not genre_id:
            self.db_cursor.execute("INSERT INTO %s VALUES(NULL, ?)" % self.genres_table_name, (genre_name,))
            genre_id = self.db_cursor.lastrowid

        return genre_id

    def __insert_album_to_db__(self, album_name, year):
        album_id = self.db_cursor.execute("SELECT Id FROM %s WHERE AlbumName=? AND Year=?" % self.albums_table_name,
                                          (album_name, year))
        if not album_id:
            self.db_cursor.execute("INSERT INTO %s VALUES(NULL, ?, ?)" % self.albums_table_name,
                                   (album_name, year))
            album_id = self.db_cursor.lastrowid

        return album_id

    def __insert_artist_to_db__(self, artist_name):
        artist_id = self.db_cursor.execute("SELECT Id FROM %s WHERE ArtistName=?" % self.artists_table_name,
                                           (artist_name,))
        if not artist_id:
            self.db_cursor.execute("INSERT INTO %s VALUES(NULL, ?)" % self.artists_table_name, (artist_name,))
            artist_id = self.db_cursor.lastrowid

        return artist_id

    @database_access
    def clean_db(self):
        for db_table_name in [self.genres_table_name,
                              self.albums_table_name,
                              self.artists_table_name,
                              self.music_files_table_name]:
            self.db_cursor.execute("DROP TABLE IF EXISTS %s" % db_table_name)

    @database_access
    def search_for_files(self, search_option, search_pattern):
        return self.search_options[search_option](search_pattern)

    def title_search_foo(self, search_pattern):
        fetch_generator = self.db_cursor.execute("SELECT Path FROM %s WHERE LIKE ?" % self.music_files_table_name,
                                                 ('%'+search_pattern+'%')).fetchall()

        for fetch_result in fetch_generator:
            yield fetch_result['Path']

    def artist_search_foo(self, search_pattern):
        artist_id = self.db_cursor.execute("SELECT Id FROM %s WHERE ArtistName=?" % self.artists_table_name,
                                           (search_pattern,)).fetchone()

    def album_search_foo(self, search_pattern):
        pass

    def year_search_foo(self, search_pattern):
        pass

    def genre_search_foo(self, search_pattern):
        pass
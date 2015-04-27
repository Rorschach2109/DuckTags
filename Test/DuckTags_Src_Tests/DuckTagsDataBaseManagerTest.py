from Src.DuckTagsDataBaseManager import DuckTagsDataBaseManager

import unittest
import mock


class DuckTagsDataBaseManagerTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.db_manager = DuckTagsDataBaseManager()

        cls.genres_table_creation_command = "CREATE TABLE IF NOT EXISTS Genres( \
                                            Id INTEGER PRIMARY KEY, \
                                            GenreName TEXT)"
        cls.albums_table_creation_command = "CREATE TABLE IF NOT EXISTS Albums( \
                                            Id INTEGER PRIMARY KEY, \
                                            AlbumName TEXT, \
                                            AlbumYear INTEGER)"
        cls.artists_table_creation_command = "CREATE TABLE IF NOT EXISTS Artists( \
                                            Id INTEGER PRIMARY KEY, \
                                            ArtistName TEXT)"
        cls.music_files_table_creation_command = "CREATE TABLE IF NOT EXISTS MusicFiles( \
                                                Id INTEGER PRIMARY KEY, \
                                                Path TEXT, \
                                                Title TEXT, \
                                                ArtistId, \
                                                AlbumId, \
                                                GenreId, \
                                                FOREIGN KEY(ArtistId) REFERENCES Artists(Id) \
                                                FOREIGN KEY(AlbumId) REFERENCES Albums(Id) \
                                                FOREIGN KEY(GenreId) REFERENCES Genres(Id))"

        cls.genre_name = 'genre_name'
        cls.select_id_genre = "SELECT Id FROM Genres WHERE GenreName=?"
        cls.insert_genre = "INSERT INTO Genres VALUES(NULL, ?)"

        cls.album_name = 'album_name'
        cls.album_year = 1990
        cls.select_id_album = "SELECT Id FROM Albums WHERE AlbumName=? AND Year=?"
        cls.insert_album = "INSERT INTO Albums VALUES(NULL, ?, ?)"

        cls.artist_name = 'artist_name'
        cls.select_id_artist = "SELECT Id FROM Artists WHERE ArtistName=?"
        cls.insert_artist = "INSERT INTO Artists VALUES(NULL, ?)"

        cls.music_file_path = 'music_file_path'
        cls.select_id_music_file = "SELECT Id FROM MusicFiles WHERE Path=?"

        cls.drop_table_command = "DROP TABLE IF EXISTS %s"

    def test_create_genres_table(self):
        self.db_manager.db_cursor = mock.Mock()
        foo_mock = mock.Mock(return_value=None)
        self.db_manager.db_cursor.execute = foo_mock
        self.db_manager.__create_genres_table__()

        expected_arg = self.genres_table_creation_command.replace(' ', '')
        current_arg = foo_mock.call_args[0][0].replace(' ', '')

        self.assertEqual(expected_arg, current_arg)

    def test_create_albums_table(self):
        self.db_manager.db_cursor = mock.Mock()
        foo_mock = mock.Mock(return_value=None)
        self.db_manager.db_cursor.execute = foo_mock
        self.db_manager.__create_albums_table__()

        expected_arg = self.albums_table_creation_command.replace(' ', '')
        current_arg = foo_mock.call_args[0][0].replace(' ', '')

        self.assertEqual(expected_arg, current_arg)

    def test_create_artists_table(self):
        self.db_manager.db_cursor = mock.Mock()
        foo_mock = mock.Mock(return_value=None)
        self.db_manager.db_cursor.execute = foo_mock
        self.db_manager.__create_artists_table__()

        expected_arg = self.artists_table_creation_command.replace(' ', '')
        current_arg = foo_mock.call_args[0][0].replace(' ', '')

        self.assertEqual(expected_arg, current_arg)

    def test_create_music_files_table(self):
        self.db_manager.db_cursor = mock.Mock()
        foo_mock = mock.Mock(return_value=None)
        self.db_manager.db_cursor.execute = foo_mock
        self.db_manager.__create_music_files_table__()

        expected_arg = self.music_files_table_creation_command.replace(' ', '')
        current_arg = foo_mock.call_args[0][0].replace(' ', '')

        self.assertEqual(expected_arg, current_arg)

    def test_insert_genre_to_db_exists(self):
        self.db_manager.db_cursor = mock.Mock()
        foo_mock = mock.Mock(return_value=1)

        self.db_manager.db_cursor.execute = foo_mock
        self.db_manager.__insert_genre_to_db__(self.genre_name)

        expected_arg = self.select_id_genre
        current_first_arg = foo_mock.call_args[0][0]
        current_second_arg = foo_mock.call_args[0][1]

        self.assertEqual(expected_arg, current_first_arg)
        self.assertEqual((self.genre_name,), current_second_arg)

    def test_insert_genre_to_db_new(self):
        self.db_manager.db_cursor = mock.Mock()
        foo_mock = mock.Mock(return_value=None)

        self.db_manager.db_cursor.execute = foo_mock
        self.db_manager.__insert_genre_to_db__(self.genre_name)

        expected_arg = self.insert_genre
        current_first_arg = foo_mock.call_args[0][0]
        current_second_arg = foo_mock.call_args[0][1]

        self.assertEqual(expected_arg, current_first_arg)
        self.assertEqual((self.genre_name,), current_second_arg)

    def test_insert_album_to_db_exists(self):
        self.db_manager.db_cursor = mock.Mock()
        foo_mock = mock.Mock(return_value=1)

        self.db_manager.db_cursor.execute = foo_mock
        self.db_manager.__insert_album_to_db__(self.album_name, self.album_year)

        expected_arg = self.select_id_album
        current_first_arg = foo_mock.call_args[0][0]
        current_second_arg = foo_mock.call_args[0][1]

        self.assertEqual(expected_arg, current_first_arg)
        self.assertEqual((self.album_name, self.album_year), current_second_arg)

    def test_insert_album_to_db_new(self):
        self.db_manager.db_cursor = mock.Mock()
        foo_mock = mock.Mock(return_value=None)

        self.db_manager.db_cursor.execute = foo_mock
        self.db_manager.__insert_album_to_db__(self.album_name, self.album_year)

        expected_arg = self.insert_album
        current_first_arg = foo_mock.call_args[0][0]
        current_second_arg = foo_mock.call_args[0][1]

        self.assertEqual(expected_arg, current_first_arg)
        self.assertEqual((self.album_name, self.album_year), current_second_arg)

    def test_insert_artist_to_db_exists(self):
        self.db_manager.db_cursor = mock.Mock()
        foo_mock = mock.Mock(return_value=1)

        self.db_manager.db_cursor.execute = foo_mock
        self.db_manager.__insert_artist_to_db__(self.artist_name)

        expected_arg = self.select_id_artist
        current_first_arg = foo_mock.call_args[0][0]
        current_second_arg = foo_mock.call_args[0][1]

        self.assertEqual(expected_arg, current_first_arg)
        self.assertEqual((self.artist_name,), current_second_arg)

    def test_insert_artist_to_db_new(self):
        self.db_manager.db_cursor = mock.Mock()
        foo_mock = mock.Mock(return_value=None)

        self.db_manager.db_cursor.execute = foo_mock
        self.db_manager.__insert_artist_to_db__(self.artist_name)

        expected_arg = self.insert_artist
        current_first_arg = foo_mock.call_args[0][0]
        current_second_arg = foo_mock.call_args[0][1]

        self.assertEqual(expected_arg, current_first_arg)
        self.assertEqual((self.artist_name,), current_second_arg)

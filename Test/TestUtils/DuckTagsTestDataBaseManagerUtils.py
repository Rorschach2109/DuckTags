from Src.DuckTagsDatabaseTools.DuckTagsMusicFileModel import DuckTagsMusicFileModel


class DuckTagsTestDataBaseManagerUtils(object):
    files_dict_valid = {
        u'dir1/dir11': [u'file11.mp3', u'file12.mp3', u'file13.jpg'],
        u'dir2/dir21': [u'file21.mp3', u'file22.txt']
    }

    music_files_dict_valid = {
        u'dir1/dir11': [u'file11.mp3', u'file12.mp3'],
        u'dir2/dir21': [u'file21.mp3']
    }

    music_files_dict_empty = dict()

    music_files_directories_valid = [
        u'dir1/dir11/file11.mp3',
        u'dir1/dir11/file12.mp3',
        u'dir2/dir21/file21.mp3'
        ]

    music_file_model = DuckTagsMusicFileModel(
        u'path/to/music',
        {
            u'title': u'title',
            u'artist': u'artist',
            u'album': u'album',
            u'genre': u'genre',
            u'date': 1990,
            u'tracknumber': 1,
        })

    music_files_dict = {
        u'folder_path_1/artist': [u'1.mp3'],
        u'folder_path_4/artist': [u'2.mp3']
    }

    valid_first_mp3_tags = {
        u'title': u'first',
        u'artist': u'artist',
        u'album': u'album',
        u'genre': u'genre',
        u'date': 1990,
        u'tracknumber': 1
    }

    valid_second_mp3_tags = {
        u'title': u'second',
        u'artist': u'artist',
        u'album': u'album',
        u'genre': u'genre',
        u'date': 1990,
        u'tracknumber': 2
    }

    first_music_file_model = DuckTagsMusicFileModel(
        u'folder_path_1/artist/1.mp3',
        {
            u'title': u'first',
            u'artist': u'artist',
            u'album': u'album',
            u'genre': u'genre',
            u'date': 1990,
            u'tracknumber': 1
        })

    first_music_file_model_serialization = {
            u'path': u'folder_path_1/artist/1.mp3',
            u'title': u'first',
            u'artist': u'artist',
            u'album': u'album',
            u'genre': u'genre',
            u'date': 1990,
            u'tracknumber': 1
    }

    second_music_file_model = DuckTagsMusicFileModel(
        u'folder_path_4/artist/2.mp3',
        {
            u'title': u'second',
            u'artist': u'artist',
            u'album': u'album',
            u'genre': u'genre',
            u'date': 1990,
            u'tracknumber': 2
        })

    second_music_file_model_serialization = {
            u'path': u'folder_path_4/artist/2.mp3',
            u'title': u'second',
            u'artist': u'artist',
            u'album': u'album',
            u'genre': u'genre',
            u'date': 1990,
            u'tracknumber': 2
    }

    music_file_model_no_album = DuckTagsMusicFileModel(
        u'folder_path_4/artist/2.mp3',
        {
            u'title': u'second',
            u'artist': u'artist',
            u'genre': u'genre',
            u'date': 1990,
            u'tracknumber': 2
        })

    music_file_model_serialization_no_album = {
            u'path': u'folder_path_4/artist/2.mp3',
            u'title': u'second',
            u'artist': u'artist',
            u'album': u'',
            u'genre': u'genre',
            u'date': 1990,
            u'tracknumber': 2
    }
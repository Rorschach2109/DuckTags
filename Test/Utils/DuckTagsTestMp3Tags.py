from Src.DuckTagsMp3MetadataManager import DuckTagsMp3MetadataManager


class DuckTagsTestMp3Tags(object):

    valid_mp3_mutagen_tags = {
        'title': [u'title'],
        'album': [u'album'],
        'genre': [u'genre'],
        'date': [u'date']
    }

    valid_mp3_second_mutagen_tags = {
        'title': [u'title_another'],
        'album': [u'album'],
        'genre': [u'genre'],
        'date': [u'date']
    }

    valid_mp3_mutagen_empty_tags = {
        'title': [],
        'album': [],
        'genre': [],
        'date': []
    }

    valid_mp3_tags = {
        'title': u'title',
        'album': u'album',
        'genre': u'genre',
        'date': u'date'
    }

    valid_mp3_multi_files_tags = {
        'title': DuckTagsMp3MetadataManager.multiple_values_message,
        'album': u'album',
        'genre': u'genre',
        'date': u'date'
    }

    valid_mp3_multi_values_files_tags = {
        'title': DuckTagsMp3MetadataManager.multiple_values_message,
        'album': DuckTagsMp3MetadataManager.multiple_values_message,
        'genre': DuckTagsMp3MetadataManager.multiple_values_message,
        'date': DuckTagsMp3MetadataManager.multiple_values_message
    }

    valid_mp3_mutagen_tags_no_title = {
        'album': [u'album'],
        'genre': [u'genre'],
        'date': [u'date']
    }

    valid_mp3_tags_no_title = {
        'title': u'',
        'album': u'album',
        'genre': u'genre',
        'date': u'date'
    }

    valid_mp3_mutagen_tags_no_album = {
        'title': [u'title'],
        'genre': [u'genre'],
        'date': [u'date']
    }

    valid_mp3_tags_no_album = {
        'title': u'title',
        'album': u'',
        'genre': u'genre',
        'date': u'date'
    }

    valid_mp3_mutagen_tags_no_genre = {
        'title': [u'title'],
        'album': [u'album'],
        'date': [u'date']
    }

    valid_mp3_tags_no_genre = {
        'title': u'title',
        'album': u'album',
        'genre': u'',
        'date': u'date'
    }

    valid_mp3_mutagen_tags_no_date = {
        'title': [u'title'],
        'album': [u'album'],
        'genre': [u'genre'],
    }

    valid_mp3_tags_no_date = {
        'title': u'title',
        'album': u'album',
        'genre': u'genre',
        'date': u''
    }
class DuckTagsTestMp3Tags(object):

    valid_mp3_mutagen_tags = {
        'title': [u'title'],
        'album': [u'album'],
        'genre': [u'genre'],
        'date': [u'date']
    }

    valid_mp3_tags = {
        'title': u'title',
        'album': u'album',
        'genre': u'genre',
        'date': u'date'
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
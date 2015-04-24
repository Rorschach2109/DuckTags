from CodernityDB.hash_index import HashIndex


class MusicPathIndex(HashIndex):
    def __init__(self, *args, **kwargs):
        kwargs['key_format'] = '16s'
        super(MusicPathIndex, self).__init__(*args, **kwargs)

    def make_key_value(self, data):
        return md5(data[self.name]).digest(), None

    def make_key(self, key):
        return md5(key).digest()

    def get_name(self):
        return self.name
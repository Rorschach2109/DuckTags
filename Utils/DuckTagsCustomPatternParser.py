from Utils.DuckTagsUtils import DuckTagsUtils

import re


class DuckTagsCustomPatternParser(object):

    title_variable = '{{ title }}'
    artist_variable = '{{ artist }}'
    album_variable = '{{ album }}'
    date_variable = '{{ date }}'
    genre_variable = '{{ genre }}'
    track_number_variable = '{{ tracknumber }}'

    search_pattern = '{{ (\w+) }}'

    def append_pattern(self, custom_pattern):
        re_compile = re.compile(self.search_pattern)
        find_all_list = re_compile.findall(custom_pattern)

        for find_item in find_all_list:
            custom_pattern = custom_pattern.replace('{{ %s }}' % find_item, '%s')

        DuckTagsUtils.file_format_patterns = DuckTagsUtils.file_format_patterns[0:2] + [(custom_pattern, find_all_list)]

    def validate_custom_pattern(self, custom_pattern):
        re_compile = re.compile(self.search_pattern)
        return len(re_compile.findall(custom_pattern)) > 0
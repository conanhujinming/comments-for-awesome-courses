#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from urllib.parse import quote

EXCLUDE_DIRS = ['.git', 'docs', '.vscode', '.circleci', 'site', 'overrides', '.github']
README_MD = ['README.md', 'readme.md', 'index.md']

TXT_EXTS = ['md', 'txt']
TXT_URL_PREFIX = 'https://github.com/conanhujinming/comments-for-awesome-courses/blob/main/'
BIN_URL_PREFIX = 'https://github.com/conanhujinming/comments-for-awesome-courses/raw/main/'


def list_files(course: str):
    filelist_texts = '## 文件列表\n\n'
    readme_path = ''
    for root, dirs, files in os.walk(course):
        files.sort()
        level = root.replace(course, '').count(os.sep)
        indent = ' ' * 4 * level
        filelist_texts += '{}- {}\n'.format(indent, os.path.basename(root))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            if f not in README_MD:
                if f.split('.')[-1] in TXT_EXTS:
                    filelist_texts += '{}- [{}]({})\n'.format(subindent,
                                                              f, TXT_URL_PREFIX + quote('{}/{}'.format(root, f)))
                else:
                    filelist_texts += '{}- [{}]({})\n'.format(subindent,
                                                              f, BIN_URL_PREFIX + quote('{}/{}'.format(root, f)))
            elif root == course and readme_path == '':
                readme_path = '{}/{}'.format(root, f)
    return filelist_texts, readme_path


def generate_md(course: str, filelist_texts: str, readme_path: str, topic: str):
    final_texts = ['\n\n'.encode(), filelist_texts.encode()]
    if readme_path:
        with open(readme_path, 'rb') as file:
            final_texts = file.readlines() + final_texts
    topic_path = os.path.join('docs', topic)
    if not os.path.isdir(topic_path):
        os.mkdir(topic_path)
    with open(os.path.join(topic_path, '{}.md'.format(course)), 'wb') as file:
        file.writelines(final_texts)
        


if __name__ == '__main__':
    if not os.path.isdir('docs'):
        os.mkdir('docs')

    topics = list(filter(lambda x: os.path.isdir(x) and (
        x not in EXCLUDE_DIRS), os.listdir('.')))  # list topics

    for topic in topics:
        topic_path = os.path.join('.', topic)

        courses = list(filter(lambda x: os.path.isdir(os.path.join(topic_path, x)) and (
            x not in EXCLUDE_DIRS), os.listdir(topic_path)))  # list courses

        for course in courses:
            course_path = os.path.join(".", topic, course)
            filelist_texts, readme_path = list_files(course_path)
            generate_md(course, filelist_texts, readme_path, topic)

    with open('README.md', 'rb') as file:
        mainreadme_lines = file.readlines()

    with open('docs/index.md', 'wb') as file:
        file.writelines(mainreadme_lines)
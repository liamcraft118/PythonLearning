# -*- coding: utf-8 -*-


def read(file_name):
    with open(file_name, 'r') as file:
        text = file.read()
        file.close()
    return text


def write(file_name, text):
    with open(file_name, 'w') as file:
        file.write(text)
        file.close()

# -*- coding: utf-8 -*-
import re


def mobile_compile():
    return re.compile(r'^1[3587]\d{9}$|^147\d{8}')


def email_compile():
    return re.compile(r'[^\._-][\w\.-]+@(?:[A-Za-z0-9]+\.)+[A-Za-z]+')


def password_compile():
    return re.compile(r'[a-zA-Z0-9_]{6,18}')


def tel_compile():
    return re.compile(r'^0\d{2,3}[_-]\d{7,8}$|^1\d{10}$')


def bankcard_compile():
    return re.compile(r'^\d{10,20}$')


def chinese_compile():
    return re.compile(ur'^[A-Za-z0-9\u4e00-\u9fa5]+$')

#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    from msz.settings import read_env
    read_env()
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "msz.settings")
    execute_from_command_line(sys.argv)

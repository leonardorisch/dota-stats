#!/usr/bin/env python
import os
import sys
from django.conf.urls import url
from django.http import HttpResponse

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dota_stats.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
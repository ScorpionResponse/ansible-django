#!/usr/bin/env python
"""This script creates a superuser if it doesn't already exist."""
from __future__ import print_function
import os
import sys


def create_new_superuser(username, email, password):
    """Creates a new superuser unless it exists."""
    from django.contrib.auth.models import User
    if User.objects.filter(username=username).exists():
        print("Username already exists.")
    else:
        new_user = User.objects.create_superuser(username, email, password)
        print("User {} created.  CHANGED.".format(new_user))


if __name__ == '__main__':

    if len(sys.argv) != 5:
        print("Usage: {} <django_settings> <username> <email> <password>".format(sys.argv[0]))
        print("FAILED")
        sys.exit(1)

    try:
        (django_settings, username, email, password) = sys.argv[1:]
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", django_settings)

        # This is so models get loaded.
        from django.core.wsgi import get_wsgi_application
        application = get_wsgi_application()

        create_new_superuser(username, email, password)
    except Exception:
        print("An error occurred.")
        print("FAILED")
        sys.exit(1)

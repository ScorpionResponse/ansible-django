Ansible Role: django
====================

[![Build Status](https://travis-ci.org/ScorpionResponse/ansible-django.svg?branch=master)](https://travis-ci.org/ScorpionResponse/ansible-django)

Ansible role to install a Django project.

Requirements
------------

The django project itself must already contain a manage.py file and a requirements/{{ environment }}.txt file.

Role Variables
--------------

### Required
* `django_git_repo`: The git repository containing the Django application to
  install.

### Optional
* `django_base_dir`: The directory which should contain the project.  Default:
  /srv
* `django_subdirectory`: A path from the root of the repository to the folder
  containing the django application.  Default: ""  -- If assigned a value, the
  value should have a trailing slash.
* `django_user_name`: The user account to own the files. Default:
  django
* `django_group_name`: The group account to own the files. Default: django
* `django_project_name`: The name of the project folder.  Default: application
* `django_virtualenv_path`: The location to install a virtualenv.  Default:
  /srv/venv
* `django_environment`: The environment we're installing.  Default: dev

Dependencies
------------

* The ScorpionResponse.pip role will be used to install pip.

Example Playbook
----------------

Example usage:

    - hosts: all
      vars:
        - django_git_repo: "https://github.com/myacct/repo.git"
      roles:
         - { role: ScorpionResponse.django }

License
-------

BSD

Author Information
------------------

Github: https://github.com/ScorpionResponse

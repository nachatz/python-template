"""
Python Template Code
~~~~~~~~~~~~~~~~~~~~~

Sample starter code for enabling immediate development of Python applications
utilizing pytest, pylint, black, mypy, and poetry for a sustainable e2e solution.

This showcases working with a Python built library
"""

from project_template.engine import Serializer
from project_template.models import PostModel


def main():
    """ Application to fetch a PostModel, update it, and pretty-print the result using
    the 'project_template' library.
    """

    post: PostModel = Serializer.make_request()
    Serializer.update_post(post=post)
    Serializer.pretty_print(post=post)

if __name__ == "__main__":
    main()

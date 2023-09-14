"""
Python Template Code
~~~~~~~~~~~~~~~~~~~~~

Sample starter code for enabling immediate development of Python applications
utilizing pytest, pylint, black, mypy, and poetry for a sustainable e2e solution.

This showcases working with a Python built library
"""

from lib.engine.serializer import make_request, update_post, pretty_print


def main():
    """
    Main function to fetch a PostModel, update it, and pretty-print the result.
    """
    post = make_request()
    updated_post = update_post(post)
    pretty_print(updated_post)


if __name__ == "__main__":
    main()

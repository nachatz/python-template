"""
Serializer
~~~~~~~~~~~~~~~~~~~~~

Sample utility functions for serializing a API response to a pydantic model
"""

import json
import requests
from lib.models.post import PostModel

API_URL = "https://jsonplaceholder.typicode.com/posts/1"


def pretty_print(post: PostModel):
    """
    Pretty-print the attributes of a PostModel object.

    Args:
        post (PostModel): The PostModel object to pretty-print.
    """
    print(json.dumps(post.model_dump(), indent=4))


def make_request() -> PostModel:
    """


    Makes an HTTP GET request to an API and create a PostModel object from the response.

    Returns:
        PostModel: A PostModel object created from the API response.
    """
    return PostModel(**requests.get(API_URL, timeout=15).json())


# Note: This is the only testable function (the others are provided by tested libraries)
def update_post(post: PostModel) -> PostModel:
    """
    Update the 'body' attribute of a PostModel object.

    Args:
        post (PostModel): The PostModel object to update.

    Returns:
        PostModel: The updated PostModel object.
    """
    post.body = "~ Seg Fault ~"
    return post

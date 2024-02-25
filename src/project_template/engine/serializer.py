"""
Serializer
~~~~~~~~~~~~~~~~~~~~~

Sample utility functions for serializing a API response to a pydantic model
"""

import json
import requests
from project_template.models import PostModel


class Serializer:
    """ A class for serializing API responses to pydantic models.

    Attributes:
        api_url (str): The URL of the API endpoint.
    """

    api_url: str = "https://jsonplaceholder.typicode.com/posts/1"

    @staticmethod
    def update_post(*, post: PostModel) -> PostModel:
        """
        Update the 'body' attribute of a PostModel object.

        Args:
            post (PostModel): The PostModel object to update.
        """

        post.body = "~ Seg Fault ~"

    @staticmethod
    def make_request() -> PostModel:
        """ Makes an HTTP GET request to an API and create a PostModel object from the response.

        Returns:
            PostModel: A PostModel object created from the API response.
        """

        return PostModel(**requests.get(Serializer.api_url, timeout=15).json())

    @staticmethod
    def pretty_print(*, post: PostModel) -> None:
        """ Pretty-print the attributes of a PostModel object.

        Args:
            post (PostModel): The PostModel object to pretty-print.
        """

        print(json.dumps(post.model_dump(), indent=4))
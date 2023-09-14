"""
Post models
~~~~~~~~~~~~~~~~~~~~~
"""

from pydantic import BaseModel


class PostModel(BaseModel):
    """
    Represents a serializable model for a post

    Attributes:
        userId (int): The ID of the user who created the post.
        id (int): The unique ID of the post.
        title (str): The title of the post.
        body (str): The content or body of the post.

    Usage:
        You can create instances of this class to work with blog post data. For example:

        >>> post = PostModel(userId=1, id=2, title="Sample Post", body="This is the post content.")
        >>> post = PostModel(**requests.get(API_URL, timeout=15).json())
    """

    # Mixed case used since this is serialized directly from json
    userId: int  # noqa: N815
    id: int
    title: str
    body: str

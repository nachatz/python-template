from lib.engine.serializer import update_post
from lib.models.post import PostModel


def mocked_body():
    return PostModel(
        userId=1,
        id=2,
        title="Testing Code",
        body="Testing code can be very beneficial, if done properly!",
    )


def test_update_post():
    post = mocked_body()
    expected_body = "~ Seg Fault ~"
    update_post(post)

    assert post.body == expected_body
    assert isinstance(post, PostModel)


if __name__ == "__main__":
    test_update_post()

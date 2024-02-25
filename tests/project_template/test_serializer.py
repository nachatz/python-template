from project_template.engine import Serializer
from project_template.models import PostModel
from tests.utils import ProjectTemplateTestBase
from pytest import fixture

class TestSerializer(ProjectTemplateTestBase):

    """ Test Serializer class

    Validates functionality of the static methods in the Serializer class
    
    """

    @fixture(autouse=True)
    def mock_request(self, mocker: fixture) -> None:
        """" Mocks the 'make_request' method of the Serializer class

            Args: 
                mocker: fixture used to mock the 'make_request' method of the Serializer class
        """

        def dummy_request() -> PostModel:
            return PostModel(
                userId=1,
                id=2,
                title="Testing Code",
                body="Testing code can be very beneficial, if done properly!",
            )

        mocker.patch("project_template.engine.Serializer.make_request", dummy_request)

    def test_update_post(self):
        """ Validates updating a post """
        
        expected_body = "~ Seg Fault ~"
        post = Serializer.make_request()
        Serializer.update_post(post=post)

        assert post.body == expected_body
        assert isinstance(post, PostModel)


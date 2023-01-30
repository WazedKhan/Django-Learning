import pytest

from post.models import Post


@pytest.fixture
def post():
    post = Post.objects.create(
        title="My First Post", content="This is my first post content for pytest"
    )
    return post

from django.test import TestCase
from posts.models import Post
from http import HTTPStatus
from model_bakery import baker

#using baker how to create post
class HomepageTest(TestCase):
    def setUp(self):
        self.post1=baker.make(Post)
        self.post2=baker.make(Post)

    def test_homepage_returns_correct_response(self):
        response=self.client.get("/")

        self.assertTemplateUsed(response,"posts/index.html")
        self.assertEqual(response.status_code,HTTPStatus.OK)

    def test_homepage_returns_post_list(self):
        response=self.client.get('/')

        self.assertContains(response,self.post1.title)
        self.assertContains(response,self.post2.title)


#this is how we simply write test
"""class HomepageTest(TestCase):
    def setUP(self):
        self.post1=Post.objects.create(
            title="sample post 1",
            body="And the belief that follows, that is rooted deeply in thinking well of God, is: I was chosen for good."
        )
        self.post2=Post.objects.create(
            title="sample post 2",
            body="The question isnt: was I chosen? The question is: for what have I been chosen? "
        )"""
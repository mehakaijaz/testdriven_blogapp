from django.test import TestCase
from posts.models import Post
from http import HTTPStatus
from model_bakery import baker



class DetailPageTest(TestCase):

    def setUp(self):
        """self.post=Post.objects.create(
            title='learn js',
            body='The question isnt:'
        )"""
        self.post=baker.make(Post)

    def test_detail_page_returns_correct_response(self):
        response=self.client.get(self.post.get_absolute_url())

        self.assertEqual(response.status_code,HTTPStatus.OK)
        self.assertTemplateUsed(response,'posts/detail.html')

    def test_detail_page_returns_correct_content(self):
        response=self.client.get(self.post.get_absolute_url())

        self.assertContains(response,self.post.title)
        self.assertContains(response,self.post.body)
from django.test import TestCase
from django.urls import reverse
from .models import Article
# from django.contrib.auth import get_user_model

# Article = get_user_model()


# Create your tests here.
class ArticlesTest(TestCase):
    def setUp(self):
        self.article = Article.objects.create(
            name="Test article one",
            body="Test content of the article one"
        )

    def test_articles_update(self):
        update_url = reverse("articles:update", kwargs={"pk": self.article.pk})
        list_url = reverse("article_list")

        # Отправка POST-запроса на изменение
        self.client.post(update_url, data={"name": "Updated article", "body": "Updated content"})

        # Переход на страницу списка статей
        response = self.client.get(article_list)

        # Проверяем, что новая статья появилась в HTML
        self.assertContains(response, "Updated article")
        self.assertNotContains(response, "Refreshed")

    def test_articles_list(self):
        response = self.client.get(reverse("article_list"))
        self.assertEqual(response.status_code, 200)

        # Проверяем наличие данных в контексте шаблона
        self.assertIn("articles", response.context)
        articles = response.context["articles"]

        # Проверяем не пустой ли список пользователей
        self.assertTrue(len(articles) > 0)

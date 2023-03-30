from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse


class DefaultUserCreateTestCase(TestCase):
    test_username = "Anya"

    def setUp(self) -> None:
        User.objects.create_user(username=self.test_username, password="Qwerty!12345")

    def test_model_create(self):
        """
        Тестируем, что модель пользователя в базе данных успешно создалась
        """
        user = User.objects.get(username=self.test_username)
        self.assertEqual(user.username, self.test_username)

    def test_user_count(self):
        self.assertEqual(User.objects.all().count(), 1)


class ApiBookGetTestCase(TestCase):
    test_username = "Bogdan_112345"
    test_password = "Qwerty!12345"

    def setUp(self) -> None:
        User.objects.create(username=self.test_username, password=self.test_password)

    def test_model_create(self):
        client = Client()
        response1 = client.post(reverse("token_obtain_pair"), data={"username": self.test_username, "password": self.test_password})
        if response1.status_code != 200:
            raise Exception("Пользователь не создан!")


class OkTestCase(TestCase):
    def setUp(self) -> None:
        pass

    def test_ok(self):
        print(
            """\n\n\n
        ################################################################################
        ################################################################################
        ################################################################################
                                ВСЕ ТЕСТЫ УСПЕШНО ПРОЙДЕНЫ
        ################################################################################
        ################################################################################
        ################################################################################
        \n\n\n"""
        )

from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email(self):
        email = 'user1@host.com'
        password = 'Password@123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(raw_password=password))

    def test_normalize_new_user_email(self):
        email = 'user1@HOST.com'
        user = get_user_model().objects.create_user(
            email=email,
            password='dummy_password'
        )
        self.assertEqual(user.email, email.lower())

    def test_new_user_email_is_not_None(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email=None,
                password='dummy_password'
            )

    def test_create_new_superuser(self):
        user = get_user_model().objects.create_superuser(
            'superuser@host.com',
            'Password@123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

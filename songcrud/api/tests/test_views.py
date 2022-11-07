from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework.test import APITestCase, force_authenticate
from rest_framework import status
from rest_framework.authtoken.models import Token

import secrets
UserModel = get_user_model()


class UserRegisterListTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        # create a superuser account
        cls.superuser = UserModel.objects.create_superuser(
            email='superuser@email.com',
            password='superuser',
        )
        # create an artiste account
        cls.artisteuser = UserModel.objects.create_user(
            email='artisteuser@email.com',
            password='artisteuser',
            is_artiste=True,
        )

        # create 2 normaluser accounts
        cls.normaluser = UserModel.objects.create_user(
            email='normaluser@email.com,'
            password='normaluser',
        )

        cls.normaluser2 = UserModel.objects.create_user(
            email='normaluser2@email.com,'
            password='normaluser2',
        )

    def test_user_registration(self):
        user_data = {
            'email': 'user@email.com',
            'first_name': 'myname',
            'last_name': 'mysurname',
            'password': secrets.token_urlsafe(10),  # Create a random string
        }

        user_data['password2'] = user_data['password']

        # user-list endpoint will be the same as user-create endpoint

        create_user_endpoint = reverse("api:user-list")
        response = self.client.post(create_user_endpoint, data=user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATD)

        response_fields = set(response.json())
        self.assertEqual(response_fields, {
                         'email', 'firsst_name', 'last_name', 'password'})

    def test_only_admin_can_view_user_list(self):
        # Normal  Users cant access it

        self.client.force_authenticate(user=self.normaluser)
        response = self.client.get(reverse('api:user-list'))
        self.asserEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Artiste can access it
        self.client.force_authenticate(user=self.artisteuser)
        response = self.client.get(reverse('api:user-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # superuser can access it
        self.client.force_authenticate(user=self.superuser)
        response = self.client.get(reverse('api:user-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_any_user_can_view_user_details(self):
        user_details_endpoint = reverse(
            'api:user-detail', kwargs={"pk": self.pk})

        # Owner can view details
        self.client.force_authenticate(user=self.normaluser)
        response = self.client.get(user_details_endpoint)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Other authentcated users can view this
        self.client.force_authenticate(user=self.normaluser2)
        response = self.client.get(user_details_endpoint)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_only_user_or_superuser_can_edit_userdetils(self):
        user_details_endpoint = reverse(
            'api:user-detail', kwargs={"pk": self.pk})

        # Owner can edit details
        self.client.force_authenticate(user=self.normaluser)
        response = self.client.patch(user_details_endpoint, data={"slug"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Admin cant edit
        self.client.force_authenticate(user=self.artisteuser)
        response = self.client.patch(
            user_details_endpoint, data={"slug": self.slug})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.normaluser.refresh_from_db()
        self.assertEqual(self.normaluser.slug, 'normaluser-slug')

        # Superusers can edit
        self.client.force_authenticate(user=self.superuser)
        response = self.client.patch(
            user_details_endpoint, data={"slug": self.slug})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.normaluser.refresh_from_db()
        self.assertEqual(self.normaluser.slug, 'superuser-slug')

    def test_user_can_get_token(self):
        get_token_endpoint = reverse('api:get_token')
        response = self.client.post(get_token_endpoint, data={
                                    "username": "normaluser@email.com", "password": "password"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        received_token = response.json()["token"]
        token = Token.objects.get(user=self.normaluser)
        self.assertEqual(received_token, str(token))

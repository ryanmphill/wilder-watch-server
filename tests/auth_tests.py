import json
from rest_framework import status
from rest_framework.test import APITestCase
from wilderwatch_api.models import WilderUser
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class AuthTests(APITestCase):

    # Add any fixtures you want to run to build the test database
    fixtures = ['users', 'tokens', 'wilder_users', 'regions', 'studytypes', 'studies', 'observations']

    def setUp(self):
        # Set up new user to attempt login
        new_user = User.objects.create_user(
            username="janesmith",
            password="supersecret",
            email="jsmith@example.com",
            first_name="Jane",
            last_name="Smith"
        )

        # Now save the extra info in the wilderwatch_api_wilderuser table
        wilder_user = WilderUser.objects.create(
            bio="",
            user=new_user
        )

        # Use the REST Framework's token generator on the new user account
        token = Token.objects.create(user=wilder_user.user)
        self.new_test_token = token.key

    def test_register_new_user(self):
        """
        Ensure we can create a new user
        """
        # Define the endpoint in the API to which
        # the request will be sent
        url = "/register"

        # Set up data for new user to register
        new_user_data = {
            "username": "johndoe1",
            "email": "johndoe@example.com",
            "first_name": "John",
            "last_name": "Doe",
            "password": "thisisasecret"
        }

        # Initiate request and store response
        response = self.client.post(url, new_user_data, format='json')

        # Parse the JSON in the response body
        json_response = json.loads(response.content)

        # Assert that the user was created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Assert that the response that the user was created was valid
        self.assertEqual(json_response["valid"], True)

        # Store the newly created token
        johns_token = json_response["token"]

        self.client.credentials(HTTP_AUTHORIZATION=f"Token {johns_token}")

        # Ensure one-to-one relationship wilder_user was also created
        wilder_user_response = self.client.get("/users/current", format='json')

        # Assert that the user was retrieved
        self.assertEqual(wilder_user_response.status_code, status.HTTP_200_OK)

        # Parse the JSON in the response body
        wilder_user_data = json.loads(wilder_user_response.content)

        # Ensure that the corrent wilder_user object was retrieved
        self.assertEqual(wilder_user_data["user"]["first_name"], "John")
        self.assertEqual(wilder_user_data["user"]["last_name"], "Doe")
        self.assertEqual(wilder_user_data["user"]["username"], "johndoe1")

    def test_login_user(self):
        """
        Ensure we can login
        """
        
        # Define the endpoint in the API to which
        # the request will be sent
        url = "/login"

        # Define the request body
        data = {
            "username": "janesmith",
            "password": "supersecret"
        }

        # Initiate request and store response
        response = self.client.post(url, data, format='json')

        # Parse the JSON in the response body
        json_response = json.loads(response.content)

        # Assert that the user was created
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert that the response that the user was created was valid
        self.assertEqual(json_response["valid"], True)
        self.assertEqual(json_response["token"], self.new_test_token)

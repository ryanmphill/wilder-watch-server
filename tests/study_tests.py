import json
from rest_framework import status
from rest_framework.test import APITestCase
from wilderwatch_api.models import Study, WilderUser
from rest_framework.authtoken.models import Token


class StudyTests(APITestCase):

    # Add any fixtures you want to run to build the test database
    fixtures = ['users', 'tokens', 'wilder_users', 'regions', 'studytypes', 'studies', 'observations']

    def setUp(self):
        self.test_user = WilderUser.objects.first()
        token = Token.objects.get(user=self.test_user.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")

    def test_create_study(self):
        """
        Ensure we can create a new study.
        """
        # Define the endpoint in the API to which
        # the request will be sent
        url = "/studies"

        # Define the request body
        data = {
            "title": "Test Study",
            "subject": "Test Subject",
            "summary": "Test Summary",
            "details": "Test Details",
            "startDate": "2023-09-29",
            "endDate": "",
            "studyTypeId": 1,
            "regionId": 1,
            "imageUrl": "testimgurl.com"
        }

        # Initiate request and store response
        response = self.client.post(url, data, format='json')

        # Parse the JSON in the response body
        json_response = json.loads(response.content)

        # Assert that the study was created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Assert that the properties on the created resource are correct
        self.assertEqual(json_response["title"], "Test Study")
        self.assertEqual(json_response["subject"], "Test Subject")
        self.assertEqual(json_response["summary"], "Test Summary")
        self.assertEqual(json_response["details"], "Test Details")
        self.assertEqual(json_response["start_date"], "2023-09-29")
        self.assertEqual(json_response["study_type"]["id"], 1)
        self.assertEqual(json_response["region"]["id"], 1)
        self.assertEqual(json_response["image_url"], "testimgurl.com")

    def test_get_study(self):
        """
        Ensure we can get an existing study.
        """

        # Seed the database with a study
        test_study = Study()
        test_study.author = self.test_user
        test_study.title = "Test Study"
        test_study.subject = "Test Subject"
        test_study.summary = "Test Summary"
        test_study.details = "Test Details"
        test_study.start_date = "2023-09-29"
        test_study.study_type_id = 1
        test_study.region_id = 1
        test_study.image_url = "testimgurl.com"

        test_study.save()

        # Initiate request and store response
        response = self.client.get(f"/studies/{test_study.id}")

        # Parse the JSON in the response body
        json_response = json.loads(response.content)

        # Assert that the study was retrieved
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert that the values are correct
        self.assertEqual(json_response["title"], "Test Study")
        self.assertEqual(json_response["author"]["id"], self.test_user.id)
        self.assertEqual(json_response["subject"], "Test Subject")
        self.assertEqual(json_response["summary"], "Test Summary")
        self.assertEqual(json_response["details"], "Test Details")
        self.assertEqual(json_response["start_date"], "2023-09-29")
        self.assertEqual(json_response["study_type"]["id"], 1)
        self.assertEqual(json_response["region"]["id"], 1)
        self.assertEqual(json_response["image_url"], "testimgurl.com")

    def test_update_study(self):
        """
        Ensure we can change an existing study.
        """
        # Seed the database with a study
        test_study = Study()
        test_study.author = self.test_user
        test_study.title = "Test Study"
        test_study.subject = "Test Subject"
        test_study.summary = "Test Summary"
        test_study.details = "Test Details"
        test_study.start_date = "2023-09-29"
        test_study.study_type_id = 1
        test_study.region_id = 1
        test_study.image_url = "testimgurl.com"

        test_study.save()

        # DEFINE NEW PROPERTIES FOR STUDY
        data = {
            "title": "Updated Test Study",
            "subject": "Updated Test Subject",
            "summary": "Updated Test Summary",
            "details": "Updated Test Details",
            "startDate": "2023-10-01",
            "endDate": "",
            "studyTypeId": 2,
            "regionId": 2,
            "imageUrl": "updatedtestimgurl.com"
        }

        response = self.client.put(f"/studies/{test_study.id}", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # GET study again to verify changes were made
        response = self.client.get(f"/studies/{test_study.id}")
        json_response = json.loads(response.content)

        # Assert that the properties are correct
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json_response["title"], "Updated Test Study")
        self.assertEqual(json_response["author"]["id"], self.test_user.id)
        self.assertEqual(json_response["subject"], "Updated Test Subject")
        self.assertEqual(json_response["summary"], "Updated Test Summary")
        self.assertEqual(json_response["details"], "Updated Test Details")
        self.assertEqual(json_response["start_date"], "2023-10-01")
        self.assertEqual(json_response["study_type"]["id"], 2)
        self.assertEqual(json_response["region"]["id"], 2)
        self.assertEqual(json_response["image_url"], "updatedtestimgurl.com")

    def test_delete_study(self):
        """
        Ensure we can delete an existing study.
        """
        # Seed the database with a study
        test_study = Study()
        test_study.author = self.test_user
        test_study.title = "Test Study"
        test_study.subject = "Test Subject"
        test_study.summary = "Test Summary"
        test_study.details = "Test Details"
        test_study.start_date = "2023-09-29"
        test_study.study_type_id = 1
        test_study.region_id = 1
        test_study.image_url = "testimgurl.com"

        test_study.save()

        # DELETE the study that was just created
        response = self.client.delete(f"/studies/{test_study.id}")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # GET the study again to verify you get a 404 response
        response = self.client.get(f"/studies/{test_study.id}")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_add_observation_to_study_via_post_request(self):
        """
        Ensure we can add an observation to a study.
        """
        # Seed the database with a study
        test_study = Study()
        test_study.author = self.test_user
        test_study.title = "Test Study"
        test_study.subject = "Test Subject"
        test_study.summary = "Test Summary"
        test_study.details = "Test Details"
        test_study.start_date = "2023-09-29"
        test_study.study_type_id = 1
        test_study.region_id = 1
        test_study.image_url = "testimgurl.com"

        test_study.save()

        # DEFINE NEW PROPERTIES FOR THE OBSERVATION
        data = {
            "latitude": 37.778946,
            "longitude": -119.583546,
            "description": "Observation Description",
            "image": "testimgurl.com",
            "date": "2023-10-01"
        }

        obs_response = self.client.post(f"/studies/{test_study.id}/add_observation", data, format="json")

        # Parse the JSON in the response body
        json_obs_response = json.loads(obs_response.content)

        # Ensure a 201 status code was received
        self.assertEqual(obs_response.status_code, status.HTTP_201_CREATED)

        # Assert that the properties are correct
        self.assertEqual(json_obs_response["latitude"], 37.778946)
        self.assertEqual(json_obs_response["longitude"], -119.583546)
        self.assertEqual(json_obs_response["description"], "Observation Description")
        self.assertEqual(json_obs_response["image"], "testimgurl.com")
        self.assertEqual(json_obs_response["date"], "2023-10-01")

        # GET study again to verify observation is included
        study_response = self.client.get(f"/studies/{test_study.id}")
        json_study_response = json.loads(study_response.content)
        self.assertEqual(study_response.status_code, status.HTTP_200_OK)

        # Store the newly created observation id
        new_observation_id = json_obs_response["id"]

        # Store the observations list from the retrieved study
        study_observations = json_study_response["observations"]

        study_observation_ids = []

        # Extract the ids from the observatons
        for observation in study_observations:
            study_observation_ids.append(observation["id"])
        
        # Ensure that the new observation is included in the study
        self.assertEqual(new_observation_id in study_observation_ids, True)

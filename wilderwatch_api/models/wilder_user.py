from django.db import models
from django.db import connection
from django.contrib.auth.models import User


class WilderUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=1000, blank=True, null=True)
    flair = models.CharField(max_length=150, blank=True, null=True)
    image_url = models.CharField(max_length=600, blank=True, null=True, default="https://st3.depositphotos.com/6672868/13701/v/600/depositphotos_137014128-stock-illustration-user-profile-icon.jpg")
    is_researcher = models.BooleanField(default=False)

    @property
    def full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'

    @property
    def date_joined(self):
        return self.user.date_joined.date()
    
    @property
    def observation_count(self):
        return self.observations.count()
    
    @property
    def authored_studies_count(self):
        return self.studies_created.count()
    
    @property
    def studies_participated_count(self):
        query = """
            SELECT COUNT(DISTINCT study_id)
            FROM wilderwatch_api_wilderuserstudyobservation
            WHERE participant_id = %s
        """

        # Execute the raw SQL query with the user's id
        with connection.cursor() as cursor:
            cursor.execute(query, (self.id,))
            result = cursor.fetchone()

        # Return the count of distinct studies
        if result is not None:
            # extract the value from the tuple
            return result[0]
        else:
            return 0
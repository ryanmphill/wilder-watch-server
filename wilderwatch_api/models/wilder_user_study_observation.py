from django.db import models

class WilderUserStudyObservation(models.Model):
    participant = models.ForeignKey("WilderUser", on_delete=models.CASCADE, related_name="observations")
    study = models.ForeignKey("Study", on_delete=models.CASCADE, related_name="observations")
    latitude = models.FloatField()
    longitude = models.FloatField()
    description = models.CharField(max_length=7500)
    image = models.CharField(max_length=500, null=True)
    date = models.DateField()

    @property
    def participant_name(self):
        return self.participant.full_name

    @property
    def study_title(self):
        return self.study.title

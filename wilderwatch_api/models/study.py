from django.db import models

class Study(models.Model):
    author = models.ForeignKey("WilderUser", on_delete=models.CASCADE, related_name="studies_created")
    title = models.CharField(max_length=300)
    subject = models.CharField(max_length=75)
    summary = models.CharField(max_length=7500)
    details = models.CharField(max_length=7500)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(null=True)
    is_complete = models.BooleanField(default=False)
    study_type = models.ForeignKey("StudyType", on_delete=models.DO_NOTHING, related_name="studies")
    region = models.ForeignKey("Region", on_delete=models.DO_NOTHING, related_name="studies")
    image_url = models.CharField(max_length=700, blank=True, null=True)

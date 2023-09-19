from django.db import models

class Study(models.Model):
    author = models.ForeignKey("WilderUser", on_delete=models.CASCADE, related_name="studies_created")
    title = models.CharField(max_length=300)
    subject = models.CharField(max_length=75)
    summary = models.CharField(max_length=7500)
    details = models.CharField(max_length=7500)
    start_date = models.DateField()
    end_date = models.DateField(null=True)
    is_complete = models.BooleanField(default=False)
    study_type = models.ForeignKey("StudyType", on_delete=models.DO_NOTHING, related_name="studies")
    region = models.ForeignKey("Region", on_delete=models.DO_NOTHING, related_name="studies")
    image_url = models.CharField(max_length=700, null=True, default="https://images.unsplash.com/photo-1619468129361-605ebea04b44?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2071&q=80")

    @property
    def average_longitude(self):
        # Calculate the average of longitudes in all related observations
        list_of_longitudes = self.observations.values_list('longitude', flat=True)
        if list_of_longitudes:
            return sum(list_of_longitudes) / len(list_of_longitudes)
        else:
            return 0  # Handle the case where there are no related objects
    
    @property
    def average_latitude(self):
        # Calculate the average of latitudes in all related observations
        list_of_latitudes = self.observations.values_list('latitude', flat=True)
        if list_of_latitudes:
            return sum(list_of_latitudes) / len(list_of_latitudes)
        else:
            return 0  # Handle the case where there are no related objects
    
    @property
    def furthest_coordinate(self):
        # Get list of coorinates for the study
        list_of_coordinates = self.observations.values_list('longitude', 'latitude', flat=False)
        # Check if list_of_coordinates is valid
        if list_of_coordinates is not None and len(list_of_coordinates) >= 1:
            # Get the center values defined in previos @property decorators
            center_lon = self.average_longitude
            center_lat = self.average_latitude
            #Initialize variables to track furthest distance from center point
            furthest_point = None
            max_distance_squared = 0
            # Calculate distances
            for lon, lat in list_of_coordinates:
                distance_squared = (lon - center_lon)**2 + (lat - center_lat)**2
                if distance_squared >= max_distance_squared:
                    max_distance_squared = distance_squared
                    furthest_point = (lon, lat)
            return furthest_point
        else:
            return None

    @property
    def furthest_longitude(self):
        if self.furthest_coordinate:
            return self.furthest_coordinate[0]
        else:
            return None
    
    @property
    def furthest_latitude(self):
        if self.furthest_coordinate:
            return self.furthest_coordinate[1]
        else:
            return None
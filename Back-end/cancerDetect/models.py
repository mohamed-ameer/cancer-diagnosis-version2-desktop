from django.db import models

# Create your models here.
#########################################################################
#save pictures and files in media folder with user_id
def user_directory_path(instance, filename):
    #THis file will be uploaded to MEDIA_ROOT /the user_(id)/the file
    return '{0}'.format(filename)
###########################################################################

class CancerDetect(models.Model):
    picture = models.ImageField(upload_to=user_directory_path)
    # patient_name = models.CharField(max_length=100, blank=True)



# class CancerDetail(models.Model):
#     patient_name = models.CharField(max_length=100, blank=True)
#     has_cancer=models.BooleanField(blank=True, null=True)
#     cancer_type=models.CharField(max_length=100,blank=True)
#     explanation=models.CharField(max_length=1000,blank=True)
#     recommendation=models.CharField(max_length=1000,blank=True)

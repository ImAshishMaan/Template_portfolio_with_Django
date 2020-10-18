from django.db import models

# Create your models model
# add the blog app to settings
# create migration 
# migarate
# add to admin

class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def summary(self):
        return self.body[:100]          

    def pub_date_preety(self):
        return self.pub_date.strftime('%b %e %y')

    def __str__(self):
        return self.title            #for admin blog name showing

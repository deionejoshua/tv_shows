from django.db import models

class ShowsManager(models.Manager):
    def validater(self, post_data):
        errors = {}
        if len(post_data['show_title']) < 2:
            errors['show_title_error'] = "Title must be more than 2 characters"

        if len(post_data['show_network']) < 3:
            errors['show_network_error'] = "Must be more than 3 characters"

        if len(post_data['show_release_date']) == 0:
            errors['show_release_date_error'] = "You must enter a date"

        if len(post_data['show_description']) < 10:
            errors['show_description_error'] = "Description must be more than 10 characters"
        
        return errors 


class Shows(models.Model):
    show_title = models.CharField(max_length=255)
    show_network = models.CharField(max_length=255)
    show_release_date = models.DateField()
    show_description = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowsManager()


class Author(models.Model):
    Author_name = models.CharField(max_length=255)
    Author_Quotes = models.TextField()

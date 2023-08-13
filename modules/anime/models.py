# from django.db import models

# class Anime(models.Model):
#     title = models.CharField(max_length=200)
#     category_url = models.CharField(max_length=200)
#     latest_episode_int = models.IntegerField()
#     latest_episode_url = models.CharField(max_length=200)
#     picture_url = models.CharField(max_length=200)
#     status_choices = (
#         ("active", "Active"),
#         ("inactive", "Inactive"),
#     )
#     status = models.CharField(max_length=100, choices=status_choices, default="active")
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.title

# class Episode(models.Model):
#     anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
#     episode_number = models.IntegerField()
#     episode_url = models.CharField(max_length=200)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     status_choices = (
#         ("active", "Active"),
#         ("inactive", "Inactive"),
#     )
#     status = models.CharField(max_length=100, choices=status_choices, default="active")

#     def __str__(self):
#         return self.anime.title + ' Episode-' + self.episode_number
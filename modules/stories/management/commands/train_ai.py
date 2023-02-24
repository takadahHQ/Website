from django.core.management.base import BaseCommand
from modules.stories.models.stories import Stories
# import pandas as pd
# import mindsdb
  
  

  
class Command(BaseCommand):
    help = 'Train the Ai to predict stories based on likes.'
  
    # def add_arguments(self, parser):
    #     parser.add_argument('-t', '--time', type=int, help='Articles published in last t hours')
  
    def handle(self, *args, **kwargs):
        query = Stories.objects.values('title', 'slug', 'abbreviation', 'summary',  'story_type', 'following', 'likes', 'dislikes', 'author', 'language', 'genre',  'rating', 'tags')
        # data = pd.DataFrame.from_records(list(query))
        # predictor = mindsdb.Predictor(name='story_recommendation_predictor')
        # predictor.learn(
        # from_data=data,
        # target=['story_type', 'likes', 'genre']
        # )
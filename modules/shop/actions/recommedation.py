# Collect user data
user_likes = Story.objects.filter(likes=True, following=user)
user_dislikes = Story.objects.filter(dislikes=True, following=user)
user_reviews = Review.objects.filter(user=user)

# Build user profile
user_profile = {
    "genres": [story.genre for story in user_likes],
    "characters": [character for story in user_likes for character in story.characters],
    "ratings": [story.rating for story in user_likes],
}

# Analyze stories
scores = {}
for story in Story.objects.all():
    score = 0
    if story.genre in user_profile["genres"]:
        score += 1
    for character in story.characters:
        if character in user_profile["characters"]:
            score += 1
    if story.rating in user_profile["ratings"]:
        score += 1
    scores[story] = score

# Recommend stories
recommended_stories = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:10]

# Update user data
for story, score in recommended_stories:
    if not Following.objects.filter(user=user, story=story).exists():
        Following.objects.create(user=user, story=story)

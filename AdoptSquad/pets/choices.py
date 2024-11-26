from django.db.models import TextChoices


class PersonalityChoices(TextChoices):
    PLAYFUL = 'Playful', 'Playful'
    CALM = 'Calm', 'Calm'
    UNSOCIAL = 'Unsocial', 'Unsocial'
    SOCIAL = 'Social', 'Social'
    ENERGETIC = 'Energetic', 'Energetic'

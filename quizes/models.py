from django.db import models

# Create your models here.
# Use the DIFF_CHOICES FOR THE CLASSES e.g JS1, SS2 etc
DIFF_CHOICES =(
    ('easy', 'easy'),
    ('medium', 'medium'),
    ('hard', 'hard'),
)

class Quiz(models.Model):

    name = models.CharField(max_length=120)
    topic = models.CharField(max_length=120)
    number_of_questions = models.IntegerField()
    time = models.IntegerField(help_text="duration of the quiz in minutes")
    required_score_to_pass = models.IntegerField(help_text="score in %")
    difficulty =models.CharField(max_length=6, choices=DIFF_CHOICES)

    def __str__(self):
        return f"{self.name}-{self.topic}"

    def get_questions(self):
        return self.question_set.all()[:self.number_of_questions]

    class Meta:
        verbose_name_plural = 'Quizes'

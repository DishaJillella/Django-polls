
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangowebapp.settings')

import django
django.setup()

from polls.models import Question, Choice
from django.utils import timezone

# Clean up old data
Question.objects.all().delete()
Choice.objects.all().delete()

# Create questions and choices
q1 = Question.objects.create(question_text="What is your favorite movie genre?", pub_date=timezone.now())
q1.choice_set.create(choice_text='Comedy', votes=0)
q1.choice_set.create(choice_text='Action', votes=0)
q1.choice_set.create(choice_text='Sci-Fi', votes=0)

q2 = Question.objects.create(question_text="Which TV show would you recommend?", pub_date=timezone.now())
q2.choice_set.create(choice_text='Breaking Bad', votes=0)
q2.choice_set.create(choice_text='Game of Thrones', votes=0)
q2.choice_set.create(choice_text='The Office', votes=0)

print("Database populated with new questions and choices.")

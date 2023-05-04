# Generated by Django 4.2 on 2023-05-04 11:15
from django.utils import timezone
from django.db import migrations


def seed_data(apps, schema_editor):
    Question = apps.get_model('polls', 'Question')
    Choice = apps.get_model('polls', 'Choice')

    # Add "What is your name?" question
    question = Question.objects.create(
        question_text='מה הביס הכי טוב?',
        pub_date=timezone.now()
    )

    # Add "nino" and "shalom" choices
    Choice.objects.create(
        question=question,
        choice_text='א',
        votes=0
    )
    Choice.objects.create(
        question=question,
        choice_text='ב',
        votes=0
    )
    Choice.objects.create(
        question=question,
        choice_text='ג',
        votes=0
    )
    Choice.objects.create(
        question=question,
        choice_text='ד',
        votes=0
    )
    Choice.objects.create(
        question=question,
        choice_text='ה',
        votes=0
    )
    Choice.objects.create(
        question=question,
        choice_text='ו',
        votes=0
    )
    Choice.objects.create(
        question=question,
        choice_text='ז',
        votes=0
    )
    Choice.objects.create(
        question=question,
        choice_text='ח',
        votes=0
    )
    Choice.objects.create(
        question=question,
        choice_text='ט',
        votes=0
    )
    Choice.objects.create(
        question=question,
        choice_text='י',
        votes=0
    )
    Choice.objects.create(
        question=question,
        choice_text='י"א',
        votes=0
    )
    Choice.objects.create(
        question=question,
        choice_text='י"ב',
        votes=0
    )
    Choice.objects.create(
        question=question,
        choice_text='י"ג',
        votes=0
    )
    Choice.objects.create(
        question=question,
        choice_text='י"ד',
        votes=0
    )
    Choice.objects.create(
        question=question,
        choice_text='ט"ו',
        votes=0
    )
    Choice.objects.create(
        question=question,
        choice_text='ט"ז',
        votes=0
    )
    Choice.objects.create(
        question=question,
        choice_text='י"ז',
        votes=0
    )
    Choice.objects.create(
        question=question,
        choice_text='י"ח',
        votes=0
    )
    Choice.objects.create(
        question=question,
        choice_text='יט',
        votes=0
    )
    Choice.objects.create(
        question=question,
        choice_text='כ',
        votes=0
    )
    Choice.objects.create(
        question=question,
        choice_text='כ"א',
        votes=0
    )
    Choice.objects.create(
        question=question,
        choice_text='כ"ב',
        votes=0
    )
    Choice.objects.create(
        question=question,
        choice_text='כ"ג',
        votes=0
    )
    Choice.objects.create(
        question=question,
        choice_text='כ"ד',
        votes=0
    )
    Choice.objects.create(
        question=question,
        choice_text='כ"ה',
        votes=0
    )
    Choice.objects.create(
        question=question,
        choice_text='כ"ו',
        votes=0
    )
    Choice.objects.create(
        question=question,
        choice_text='כ"ז',
        votes=0
    )
    Choice.objects.create(
        question=question,
        choice_text='כ"ח',
        votes=0
    )
    Choice.objects.create(
        question=question,
        choice_text='כ"ט',
        votes=0
    )
    Choice.objects.create(
        question=question,
        choice_text='ל',
        votes=0
    )
    Choice.objects.create(
        question=question,
        choice_text='ל"א',
        votes=0
    )
    Choice.objects.create(
        question=question,
        choice_text='ל"ב',
        votes=0
    )
    Choice.objects.create(
        question=question,
        choice_text='ל"ג',
        votes=0
    )
    Choice.objects.create(
        question=question,
        choice_text='ל"ד',
        votes=0
    )
    


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_usedpassword_ip_address'),
    ]

    operations = [
        migrations.RunPython(seed_data),
    ]
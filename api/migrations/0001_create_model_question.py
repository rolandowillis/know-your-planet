# Generated by Django 3.0.4 on 2020-03-07 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(help_text='La question en 1 ou 2 phrases')),
                ('type', models.CharField(choices=[('QCM', 'Questionnaire à choix multiples (QCM)'), ('VF', 'Vrai ou Faux')], max_length=50)),
                ('category', models.CharField(choices=[('action', "Leviers d'action"), ('biodiversite', 'Biodiversité'), ('climat', 'Climat'), ('consommation', 'Consommation'), ('energie', 'Energie'), ('histoire', 'Histoire, Anthropologie'), ('pollution', 'Pollution'), ('ressources', 'Ressources (hors énergie)'), ('science', 'Science'), ('autre', 'Autre')], max_length=50)),
                ('difficulty', models.IntegerField(choices=[(1, 'Facile'), (2, 'Moyen'), (3, 'Difficile'), (4, 'Expert')], help_text='Niveau de difficulté de la question')),
                ('answer_option_a', models.CharField(max_length=150)),
                ('answer_option_b', models.CharField(max_length=150)),
                ('answer_option_c', models.CharField(max_length=150)),
                ('answer_option_d', models.CharField(max_length=150)),
                ('answer_correct', models.CharField(help_text='A, B, C ou D', max_length=50)),
                ('answer_explanation', models.TextField(blank=True, help_text="Un petit texte d'explication")),
                ('answer_additional_links', models.TextField(blank=True, help_text='Un ou des liens pour aller plus loin')),
                ('created', models.DateField()),
                ('updated', models.DateField()),
            ],
        ),
    ]

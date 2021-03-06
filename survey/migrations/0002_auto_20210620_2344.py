# Generated by Django 3.2.3 on 2021-06-20 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Improvement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(choices=[('FE', 'Frontend'), ('BE', 'Backend'), ('DV', 'Data Vizualisation')], max_length=2)),
            ],
        ),
        migrations.RemoveField(
            model_name='survey',
            name='improvement',
        ),
        migrations.AddField(
            model_name='survey',
            name='improvements',
            field=models.ManyToManyField(to='survey.Improvement'),
        ),
    ]

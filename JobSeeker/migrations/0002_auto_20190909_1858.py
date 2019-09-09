# Generated by Django 2.2.4 on 2019-09-09 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JobSeeker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expirence',
            name='expiernce_type',
            field=models.CharField(choices=[('Student activity', 'Student activity'), ('Volunteering', 'Volunteering'), ('Part time', 'Part time'), ('Freelance/Project', 'Freelance/Project'), ('Internship', 'Internship'), ('Full time', 'Full time')], max_length=25),
        ),
        migrations.AlterField(
            model_name='generalinfo',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10),
        ),
        migrations.AlterField(
            model_name='generalinfo',
            name='martial_status',
            field=models.CharField(choices=[('Married', 'Married'), ('Single', 'Single')], default='Single', max_length=10),
        ),
    ]
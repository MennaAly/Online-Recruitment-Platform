# Generated by Django 2.2.4 on 2019-09-16 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Authentication', '0001_initial'),
        ('Employer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='CurrentLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Expirence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expiernce_type', models.CharField(choices=[('Part time', 'Part time'), ('Freelance/Project', 'Freelance/Project'), ('Student activity', 'Student activity'), ('Full time', 'Full time'), ('Volunteering', 'Volunteering'), ('Internship', 'Internship')], max_length=25)),
                ('job_title', models.CharField(max_length=225)),
                ('company_name', models.CharField(max_length=225)),
                ('from_date', models.DateField()),
                ('is_work_there', models.BooleanField()),
                ('description', models.CharField(max_length=256)),
                ('starting_salary', models.IntegerField()),
                ('ending_salary', models.IntegerField()),
                ('career_level', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='JobSeeker.CurrentLevel')),
                ('company_industry', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Employer.CompanyIndustry')),
                ('company_size', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Employer.CompanySize')),
            ],
        ),
        migrations.CreateModel(
            name='GeneralInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('birth_date', models.DateField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('nationality', models.CharField(max_length=255)),
                ('martial_status', models.CharField(choices=[('Single', 'Single'), ('Married', 'Married')], default='Single', max_length=10)),
                ('num_of_dependencies', models.IntegerField()),
                ('have_driving_license', models.BooleanField(default=False)),
                ('mobile_number', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Intersts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='JobSeeker.Country')),
                ('current_level', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='JobSeeker.CurrentLevel')),
            ],
        ),
        migrations.CreateModel(
            name='JobType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SearchStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='YearsOfExpiernce',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_of_years', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=256)),
                ('profiency_rate', models.IntegerField()),
                ('interest_rate', models.IntegerField()),
                ('years_of_expiernce', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='JobSeeker.YearsOfExpiernce')),
            ],
        ),
        migrations.CreateModel(
            name='JobSeekerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_cv', models.FilePathField(null=True)),
                ('experiences', models.ManyToManyField(to='JobSeeker.Expirence')),
                ('general_info', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='JobSeeker.GeneralInfo')),
                ('general_profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Authentication.Profile')),
                ('intersts', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='JobSeeker.Intersts')),
                ('skills', models.ManyToManyField(to='JobSeeker.Skill')),
            ],
        ),
        migrations.AddField(
            model_name='intersts',
            name='job_type',
            field=models.ManyToManyField(to='JobSeeker.JobType'),
        ),
        migrations.AddField(
            model_name='intersts',
            name='role',
            field=models.ManyToManyField(to='JobSeeker.Role'),
        ),
        migrations.AddField(
            model_name='intersts',
            name='search_status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='JobSeeker.SearchStatus'),
        ),
        migrations.AddField(
            model_name='expirence',
            name='job_role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='JobSeeker.Role'),
        ),
    ]

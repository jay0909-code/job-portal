# Generated by Django 4.2.4 on 2023-08-05 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jagruti', '0004_company_description_company_website'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobDeatils',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobname', models.CharField(max_length=250)),
                ('companyname', models.CharField(max_length=250)),
                ('comapanyaddress', models.CharField(max_length=250)),
                ('jobdescription', models.TextField(max_length=250)),
                ('qualification', models.CharField(max_length=250)),
                ('responsibilities', models.CharField(max_length=250)),
                ('location', models.CharField(max_length=250)),
                ('companywebsite', models.CharField(max_length=250)),
                ('coampanyemail', models.CharField(max_length=250)),
                ('companycontact', models.CharField(max_length=250)),
                ('salarypackage', models.CharField(max_length=250)),
                ('experience', models.CharField(max_length=250)),
            ],
        ),
    ]

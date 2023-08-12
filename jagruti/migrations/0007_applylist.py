# Generated by Django 4.2.4 on 2023-08-10 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jagruti', '0006_jobdeatils_company_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Applylist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education', models.CharField(max_length=200)),
                ('website', models.CharField(max_length=200)),
                ('min_salary', models.CharField(max_length=200)),
                ('max_salary', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jagruti.candidate')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jagruti.jobdeatils')),
            ],
        ),
    ]
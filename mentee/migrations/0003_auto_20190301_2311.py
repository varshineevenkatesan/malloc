# Generated by Django 2.1.3 on 2019-03-01 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mentor', '0002_mentor_approved'),
        ('mentee', '0002_auto_20190228_1700'),
    ]

    operations = [
        migrations.CreateModel(
            name='project_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=264)),
                ('dev_type', models.CharField(max_length=264)),
                ('app_type', models.CharField(max_length=264)),
                ('mentor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mentor.Mentor')),
            ],
        ),
        migrations.AlterField(
            model_name='team_member',
            name='membername',
            field=models.CharField(default='name', max_length=264),
        ),
    ]

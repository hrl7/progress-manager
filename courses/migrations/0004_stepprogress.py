# Generated by Django 4.0.2 on 2022-02-20 09:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0003_course_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='StepProgress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(choices=[('TODO', 'Todo'), ('DOING', 'Doing'), ('DONE', 'Done'), ('GAVE_UP', 'Gave up'), ('STUCKED', 'Stucked'), ('PENDING', 'Pending')], max_length=20)),
                ('created_at', models.DateTimeField(verbose_name='date created')),
                ('updated_at', models.DateTimeField(null=True, verbose_name='date updated')),
                ('step', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.step')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
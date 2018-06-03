# Generated by Django 2.0.6 on 2018-06-02 18:55

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Blogs', '0010_auto_20180602_1619'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('create_date', models.DateTimeField(default=datetime.datetime(2018, 6, 2, 18, 55, 7, 595540, tzinfo=utc))),
                ('approved_comments', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='comments',
            name='author',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='post',
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 2, 18, 55, 7, 594937, tzinfo=utc)),
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='Blogs.Post'),
        ),
    ]
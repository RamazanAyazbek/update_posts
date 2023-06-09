# Generated by Django 4.1.5 on 2023-04-03 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commit', '0007_version_delete_post_version'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='version',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='versions', to='commit.post'),
        ),
    ]

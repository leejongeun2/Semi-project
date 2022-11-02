# Generated by Django 3.2.13 on 2022-11-02 01:18

from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('star', models.CharField(max_length=5)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('image', imagekit.models.fields.ProcessedImageField(blank=True, upload_to='images/')),
                ('content', models.TextField()),
                ('like_users', models.ManyToManyField(related_name='like_reviews', to='accounts.User')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.user')),
            ],
        ),
    ]

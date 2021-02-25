# Generated by Django 2.2.7 on 2019-11-13 11:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='articles',
            fields=[
                ('articleId', models.AutoField(primary_key=True, serialize=False)),
                ('dateposted', models.DateTimeField(default=django.utils.timezone.now)),
                ('article', models.TextField()),
                ('title', models.CharField(max_length=50)),
                ('posted', models.BooleanField(default=False)),
                ('views', models.IntegerField()),
                ('upvotes', models.IntegerField()),
                ('downvotes', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='genre',
            fields=[
                ('genreId', models.AutoField(primary_key=True, serialize=False)),
                ('genre', models.CharField(choices=[('education', 'EDUCATION'), ('horror', 'HORROR'), ('thriller', 'THRILLER'), ('comedy', 'COMEDY'), ('action', 'ACTION'), ('romance', 'ROMANCE')], default='education', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='userInfo',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='profile', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('dateofbirth', models.DateField()),
                ('emailId', models.EmailField(max_length=75)),
                ('profession', models.TextField()),
                ('gender', models.CharField(choices=[('male', 'MALE'), ('female', 'FEMALE'), ('other', 'OTHER')], default='female', max_length=50)),
                ('phonenumber', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscription_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.userInfo')),
            ],
        ),
        migrations.CreateModel(
            name='favgenres',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.ManyToManyField(to='mainapp.genre')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.userInfo')),
            ],
        ),
        migrations.CreateModel(
            name='favauthors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authorId', models.ManyToManyField(to='mainapp.articles')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.userInfo')),
            ],
        ),
        migrations.CreateModel(
            name='comments',
            fields=[
                ('commentId', models.AutoField(primary_key=True, serialize=False)),
                ('comment_data', models.TextField()),
                ('upvotes', models.IntegerField(blank=True)),
                ('downvotes', models.IntegerField(blank=True)),
                ('datecommented', models.DateTimeField(default=django.utils.timezone.now)),
                ('articleId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.articles')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.userInfo')),
            ],
        ),
        migrations.AddField(
            model_name='articles',
            name='authorId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.userInfo'),
        ),
        migrations.AddField(
            model_name='articles',
            name='genre',
            field=models.ManyToManyField(to='mainapp.genre'),
        ),
    ]
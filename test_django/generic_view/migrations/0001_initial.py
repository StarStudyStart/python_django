# Generated by Django 2.2.4 on 2020-03-04 19:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='e-mail')),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=64)),
                ('country', models.CharField(max_length=64)),
                ('city', models.CharField(max_length=64)),
                ('state_province', models.CharField(max_length=64)),
                ('website', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='书名')),
                ('publication_date', models.DateField(auto_now_add=True)),
                ('author', models.ManyToManyField(to='generic_view.Author', verbose_name='作者')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='generic_view.Publisher', verbose_name='出版商')),
            ],
        ),
    ]
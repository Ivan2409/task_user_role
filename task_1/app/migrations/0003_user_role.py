# Generated by Django 2.0.2 on 2018-02-25 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_changes_on_user_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUserRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='full_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='last_name',
            field=models.CharField(max_length=20),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_role', to='app.CustomUserRole'),
        ),
    ]

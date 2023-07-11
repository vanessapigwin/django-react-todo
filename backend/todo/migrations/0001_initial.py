# Generated by Django 4.0 on 2023-07-07 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TableTodo',
            fields=[
                ('task_id', models.AutoField(primary_key=True, serialize=False)),
                ('task_name', models.CharField(max_length=100, unique=True)),
                ('task_status', models.CharField(max_length=50)),
                ('created_on', models.DateTimeField()),
                ('finished_on', models.DateTimeField(blank=True, null=True)),
                ('task_description', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'table_todo',
                'managed': True,
            },
        ),
    ]

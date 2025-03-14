# Generated by Django 5.1.2 on 2025-01-12 14:16

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='sender',
            name='receiver',
        ),
        migrations.RemoveField(
            model_name='message',
            name='receiver',
        ),
        migrations.RemoveField(
            model_name='message',
            name='sender',
        ),
        migrations.AlterModelOptions(
            name='message',
            options={},
        ),
        migrations.RemoveField(
            model_name='message',
            name='chat',
        ),
        migrations.RemoveField(
            model_name='message',
            name='content',
        ),
        migrations.RemoveField(
            model_name='message',
            name='messageId',
        ),
        migrations.RemoveField(
            model_name='message',
            name='messageState',
        ),
        migrations.RemoveField(
            model_name='message',
            name='sentDate',
        ),
        migrations.AddField(
            model_name='message',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='message',
            name='room',
            field=models.CharField(default='roomforall', max_length=1000000),
        ),
        migrations.AddField(
            model_name='message',
            name='user',
            field=models.CharField(default='defaultuser', max_length=1000000),
        ),
        migrations.AddField(
            model_name='message',
            name='value',
            field=models.CharField(default='wazzap', max_length=1000000),
        ),
        migrations.AlterField(
            model_name='chatmanager',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chatReceiver', to='chat.user'),
        ),
        migrations.AlterField(
            model_name='chatmanager',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chatSender', to='chat.user'),
        ),
        migrations.DeleteModel(
            name='Receiver',
        ),
        migrations.DeleteModel(
            name='Sender',
        ),
    ]

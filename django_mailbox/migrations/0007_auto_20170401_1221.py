# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-04-01 12:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('django_mailbox', '0006_mailbox_last_polling'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'verbose_name': 'Message', 'verbose_name_plural': 'Messages'},
        ),
        migrations.AddField(
            model_name='message',
            name='spam',
            field=models.BooleanField(default=False, verbose_name='Spam'),
        ),
        migrations.AlterField(
            model_name='mailbox',
            name='from_email',
            field=models.CharField(blank=True, default=b'', help_text="Example: MailBot &lt;mailbot@yourdomain.com&gt;<br />'From' header to set for outgoing email.<br /><br />If you do not use this e-mail inbox for outgoing mail, this setting is unnecessary.<br />If you send e-mail without setting this, your 'From' header will'be set to match the setting `DEFAULT_FROM_EMAIL`.", max_length=255, verbose_name='From email'),
        ),
        migrations.AlterField(
            model_name='mailbox',
            name='uri',
            field=models.CharField(blank=True, default=b'', help_text="Example: imap+ssl://myusername:mypassword@someserver <br /><br />Internet transports include 'imap' and 'pop3'; common local file transports include 'maildir', 'mbox', and less commonly 'babyl', 'mh', and 'mmdf'. <br /><br />Be sure to urlencode your username and password should they contain illegal characters (like @, :, etc).", max_length=255, verbose_name='URI'),
        ),
        migrations.AlterField(
            model_name='message',
            name='eml',
            field=models.FileField(blank=True, help_text='Original full content of message', null=True, upload_to=b'messages', verbose_name='Raw message contents'),
        ),
        migrations.AlterField(
            model_name='message',
            name='in_reply_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='replies', to='django_mailbox.Message', verbose_name='In reply to'),
        ),
        migrations.AlterField(
            model_name='message',
            name='mailbox',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='messages', to='django_mailbox.Mailbox', verbose_name='Mailbox'),
        ),
        migrations.AlterField(
            model_name='message',
            name='processed',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Processed'),
        ),
        migrations.AlterField(
            model_name='messageattachment',
            name='message',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='attachments', to='django_mailbox.Message', verbose_name='Message'),
        ),
    ]

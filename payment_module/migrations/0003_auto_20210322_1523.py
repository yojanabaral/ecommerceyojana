# Generated by Django 3.1.4 on 2021-03-22 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0006_paymentgateway'),
        ('payment_module', '0002_invoice_invoicedetails'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='InvoiceDetails',
            new_name='InvoiceDetail',
        ),
    ]
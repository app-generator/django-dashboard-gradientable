# Generated by Django 2.2.10 on 2021-03-21 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_products', models.IntegerField()),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_name', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('category_description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('fax', models.CharField(max_length=255)),
                ('street', models.CharField(max_length=255)),
                ('postal_code', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('province', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Inventory_Website',
            fields=[
                ('business_licence', models.IntegerField(primary_key=True, serialize=False)),
                ('web_address', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('manager_id', models.IntegerField(primary_key=True, serialize=False)),
                ('man_fname', models.CharField(max_length=255)),
                ('man_lname', models.CharField(max_length=255)),
                ('man_salary', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('supplier_id', models.IntegerField(primary_key=True, serialize=False)),
                ('supplier_name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('fax_number', models.CharField(max_length=255)),
                ('province', models.CharField(max_length=255)),
                ('street', models.CharField(max_length=255)),
                ('postal_code', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.IntegerField(primary_key=True, serialize=False)),
                ('order_date', models.DateTimeField()),
                ('shipped_date', models.DateTimeField()),
                ('order_status', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Physical_Store',
            fields=[
                ('store_id', models.IntegerField(primary_key=True, serialize=False)),
                ('street', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('province', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('postal_code', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('fax_number', models.CharField(max_length=255)),
                ('store_name', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['store_id'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.IntegerField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=255)),
                ('product_model', models.CharField(max_length=255)),
                ('product_type', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('quantity', models.IntegerField()),
                ('product_weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('store_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Physical_Store')),
            ],
            options={
                'ordering': ['product_id'],
            },
        ),
        migrations.CreateModel(
            name='Shipper',
            fields=[
                ('shipper_id', models.IntegerField(primary_key=True, serialize=False)),
                ('shipper_name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('fax_number', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Web_Admin',
            fields=[
                ('admin_id', models.IntegerField(primary_key=True, serialize=False)),
                ('admin_fname', models.CharField(max_length=255)),
                ('admin_lname', models.CharField(max_length=255)),
                ('admin_password', models.CharField(max_length=255)),
                ('salary', models.IntegerField()),
                ('business_licence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Inventory_Website')),
            ],
        ),
        migrations.CreateModel(
            name='Supply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Product')),
                ('supplier_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Manufacturer')),
            ],
        ),
        migrations.CreateModel(
            name='ShippedBy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Order')),
                ('shipper_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Shipper')),
            ],
        ),
        migrations.CreateModel(
            name='Select',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Customer')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Customer')),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Order')),
            ],
        ),
        migrations.CreateModel(
            name='ProductFoundStore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Product')),
                ('store_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Physical_Store')),
            ],
        ),
        migrations.CreateModel(
            name='Information_Page',
            fields=[
                ('page_id', models.IntegerField(primary_key=True, serialize=False)),
                ('product_description', models.CharField(max_length=255)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Customer_Support',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cust_sup_fname', models.CharField(max_length=255)),
                ('cust_sup_lname', models.CharField(max_length=255)),
                ('business_licence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Inventory_Website')),
            ],
        ),
        migrations.CreateModel(
            name='Colour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('colour', models.CharField(max_length=255)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Product')),
            ],
        ),
        migrations.CreateModel(
            name='CatergoryHasProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Category')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Assist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('call', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('live_chat', models.CharField(max_length=255)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Customer')),
            ],
        ),
    ]

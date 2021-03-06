# Generated by Django 3.1.7 on 2021-05-05 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_customuser_all_time_emails_sent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='adoption_strategy',
            field=models.CharField(default='Affiliate Marketing', max_length=50),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='business_industry',
            field=models.CharField(default='Agriculture', max_length=50),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='business_website',
            field=models.URLField(unique=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='competitive_advantage',
            field=models.CharField(default='Cheaper & Easier', max_length=50),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='conversion_rate',
            field=models.CharField(default='~00%', max_length=50),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='core_proceed',
            field=models.CharField(default='R&D', max_length=50),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='current_arpu',
            field=models.CharField(default='~$00', max_length=50),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='current_cac',
            field=models.CharField(default='~$05', max_length=50),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='current_customers',
            field=models.CharField(default='~000', max_length=50),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='current_round',
            field=models.CharField(default='~$000K', max_length=50),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='current_stage',
            field=models.CharField(default='Bootstrap', max_length=50),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='current_valuation',
            field=models.CharField(default='~$0M', max_length=50),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='customer_ltv',
            field=models.CharField(default='~$000', max_length=50),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='estimated_tam',
            field=models.CharField(default='~$000M', max_length=50),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='exit_strategy',
            field=models.CharField(default='IPO', max_length=50),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='founder_background',
            field=models.CharField(default='Agriculture', max_length=50),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='founder_count',
            field=models.CharField(default='~2', max_length=50),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='gross_margin',
            field=models.CharField(default='~00%', max_length=50),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='incorporated_country',
            field=models.CharField(default='Canada', max_length=50),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='incorporated_state',
            field=models.CharField(default='Alberta', max_length=50),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='investor_return',
            field=models.CharField(default='~10%', max_length=50),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='magic_number',
            field=models.CharField(default='~$0M', max_length=50),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='monthly_revenue',
            field=models.CharField(default='~$00K', max_length=50),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='northstar_metric',
            field=models.CharField(default='Daily Messages', max_length=50),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='problem_discovered',
            field=models.CharField(default='Agriculture', max_length=50),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='product_availability',
            field=models.CharField(default='Countywide', max_length=50),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='raised_round',
            field=models.CharField(default='~$00K', max_length=50),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='retention_rate',
            field=models.CharField(default='~00%', max_length=50),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='solution_proposed',
            field=models.CharField(default='5G', max_length=50),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='target_market',
            field=models.CharField(default='B2B', max_length=50),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='technology_stack',
            field=models.CharField(default='5G', max_length=50),
        ),
    ]

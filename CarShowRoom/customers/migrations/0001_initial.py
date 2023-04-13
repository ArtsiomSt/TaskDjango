# Generated by Django 4.2 on 2023-04-13 12:57

import core.validation.validators
import datetime
from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("cars", "0001_initial"),
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Customer",
            fields=[
                (
                    "user_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "phone_number",
                    models.CharField(
                        blank=True,
                        max_length=20,
                        null=True,
                        validators=[core.validation.validators.validate_phone],
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            bases=("auth.user",),
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="Offer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        default=datetime.datetime(
                            2023, 4, 13, 12, 57, 9, 303038, tzinfo=datetime.timezone.utc
                        )
                    ),
                ),
                (
                    "modified_at",
                    models.DateTimeField(blank=True, default=None, null=True),
                ),
                ("is_active", models.BooleanField(default=True)),
                (
                    "max_price",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=7,
                        validators=[core.validation.validators.validate_positive],
                    ),
                ),
                (
                    "currency",
                    models.CharField(
                        choices=[
                            ("USD", "USD"),
                            ("EUR", "EUR"),
                            ("BYN", "BYN"),
                            ("RUB", "RUB"),
                        ],
                        default="USD",
                        max_length=20,
                    ),
                ),
                ("is_processed", models.BooleanField(default=False)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="ShowroomCustomer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("deals_amount", models.IntegerField(default=1)),
                ("discount", models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="TransactionHistory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        default=datetime.datetime(
                            2023, 4, 13, 12, 57, 9, 303038, tzinfo=datetime.timezone.utc
                        )
                    ),
                ),
                (
                    "modified_at",
                    models.DateTimeField(blank=True, default=None, null=True),
                ),
                ("is_active", models.BooleanField(default=True)),
                (
                    "deal_price",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=7,
                        validators=[core.validation.validators.validate_positive],
                    ),
                ),
                (
                    "currency",
                    models.CharField(
                        choices=[
                            ("USD", "USD"),
                            ("EUR", "EUR"),
                            ("BYN", "BYN"),
                            ("RUB", "RUB"),
                        ],
                        default="USD",
                        max_length=40,
                    ),
                ),
                (
                    "car",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="transactions",
                        to="cars.car",
                    ),
                ),
                (
                    "made_by_customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="transactions",
                        to="customers.customer",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]

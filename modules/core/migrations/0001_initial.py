# Generated by Django 4.1.7 on 2023-03-11 11:37

import ckeditor.fields
from django.conf import settings
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import modules.core.models.include
import modules.core.models.users


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Users",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="username",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, verbose_name="email address"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                ("pseudonym", models.CharField(blank=True, max_length=255, null=True)),
                ("bio", ckeditor.fields.RichTextField(blank=True, null=True)),
                ("location", models.CharField(blank=True, max_length=30)),
                ("birth_date", models.DateField(blank=True, null=True)),
                (
                    "profile_photo",
                    models.ImageField(
                        blank=True, max_length=2048, null=True, upload_to=""
                    ),
                ),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "gender",
                    models.CharField(
                        choices=[
                            ("male", "Male"),
                            ("female", "Female"),
                            ("human", "Human"),
                        ],
                        default="human",
                        max_length=100,
                    ),
                ),
                (
                    "kyc_status",
                    models.CharField(
                        choices=[
                            ("pending", "Pending Submission"),
                            ("verification", "Pending Verification"),
                            ("approved", "Approved"),
                            ("declined", "Declined"),
                        ],
                        default="active",
                        max_length=100,
                    ),
                ),
                ("kyc_verified_at", models.DateTimeField(blank=True, null=True)),
                ("ref_code", models.CharField(blank=True, max_length=20)),
                ("active", models.BooleanField(default=True)),
                (
                    "following",
                    models.ManyToManyField(
                        blank=True,
                        related_name="followers",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "users",
            },
            managers=[
                ("objects", modules.core.models.users.CustomUserManager()),
            ],
        ),
        migrations.CreateModel(
            name="Languages",
            fields=[
                (
                    "status",
                    models.CharField(
                        choices=[("active", "Active"), ("inactive", "Inactive")],
                        default="active",
                        max_length=100,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=255)),
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("code", models.CharField(max_length=255)),
                ("native_name", models.CharField(max_length=255)),
            ],
            options={
                "verbose_name_plural": "languages",
            },
            bases=(modules.core.models.include.CacheInvalidationMixin, models.Model),
        ),
        migrations.CreateModel(
            name="Settings",
            fields=[
                (
                    "status",
                    models.CharField(
                        choices=[("active", "Active"), ("inactive", "Inactive")],
                        default="active",
                        max_length=100,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=255)),
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("tagline", models.TextField(blank=True, null=True)),
                ("logo", models.CharField(blank=True, max_length=255, null=True)),
                ("phone", models.CharField(max_length=255)),
                ("email", models.CharField(max_length=255)),
                ("color", models.CharField(max_length=255)),
                ("theme", models.CharField(max_length=255)),
                ("footer", models.CharField(max_length=255)),
            ],
            options={
                "verbose_name_plural": "settings",
            },
            bases=(modules.core.models.include.CacheInvalidationMixin, models.Model),
        ),
        migrations.CreateModel(
            name="Site",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=255)),
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("hero_header", models.CharField(max_length=255)),
                ("hero_text", models.CharField(max_length=255)),
                ("newsletter_header", models.CharField(max_length=255)),
                ("newsletter_text", models.CharField(max_length=255)),
            ],
            options={
                "verbose_name_plural": "site",
            },
            bases=(modules.core.models.include.CacheInvalidationMixin, models.Model),
        ),
        migrations.CreateModel(
            name="Socials",
            fields=[
                (
                    "status",
                    models.CharField(
                        choices=[("active", "Active"), ("inactive", "Inactive")],
                        default="active",
                        max_length=100,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=255)),
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("icon", models.TextField(blank=True, null=True)),
                ("image", models.CharField(blank=True, max_length=255, null=True)),
                ("link", models.CharField(max_length=255)),
            ],
            options={
                "verbose_name_plural": "socials",
            },
            bases=(modules.core.models.include.CacheInvalidationMixin, models.Model),
        ),
        migrations.CreateModel(
            name="Transactions",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("payable_type", models.CharField(max_length=255)),
                ("trans_type", models.CharField(max_length=8)),
                ("amount", models.DecimalField(decimal_places=0, max_digits=64)),
                ("confirmed", models.IntegerField()),
                ("meta", models.JSONField(blank=True, null=True)),
                ("uuid", models.CharField(max_length=36, unique=True)),
                (
                    "payable_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "transactions",
            },
            bases=(modules.core.models.include.CacheInvalidationMixin, models.Model),
        ),
        migrations.CreateModel(
            name="Wallets",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=255)),
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("holder_type", models.CharField(max_length=255)),
                ("slug", models.SlugField(max_length=255)),
                ("uuid", models.CharField(max_length=36, unique=True)),
                (
                    "description",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("meta", models.JSONField(blank=True, null=True)),
                ("balance", models.DecimalField(decimal_places=0, max_digits=64)),
                ("decimal_places", models.PositiveSmallIntegerField()),
                (
                    "holder_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "wallets",
                "unique_together": {("holder_type", "holder_id", "slug")},
            },
            bases=(modules.core.models.include.CacheInvalidationMixin, models.Model),
        ),
        migrations.CreateModel(
            name="Transfers",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("from_type", models.CharField(max_length=255)),
                ("to_type", models.CharField(max_length=255)),
                (
                    "status",
                    models.CharField(
                        choices=[("active", "Active"), ("inactive", "Inactive")],
                        default="active",
                        max_length=100,
                    ),
                ),
                ("status_last", models.CharField(blank=True, max_length=8, null=True)),
                ("discount", models.DecimalField(decimal_places=0, max_digits=64)),
                ("fee", models.DecimalField(decimal_places=0, max_digits=64)),
                ("uuid", models.CharField(max_length=36, unique=True)),
                (
                    "deposit",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="deposits",
                        to="core.transactions",
                    ),
                ),
                (
                    "from_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sender",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "to_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reciever",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "withdraw",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="withdrawals",
                        to="core.transactions",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "transfers",
            },
            bases=(modules.core.models.include.CacheInvalidationMixin, models.Model),
        ),
        migrations.AddField(
            model_name="transactions",
            name="wallet",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING, to="core.wallets"
            ),
        ),
        migrations.CreateModel(
            name="Menus",
            fields=[
                (
                    "status",
                    models.CharField(
                        choices=[("active", "Active"), ("inactive", "Inactive")],
                        default="active",
                        max_length=100,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=255)),
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                (
                    "position",
                    models.CharField(
                        choices=[("header", "Header"), ("footer", "Footer")],
                        default="header",
                        max_length=100,
                    ),
                ),
                ("image", models.CharField(blank=True, max_length=255, null=True)),
                ("icon", models.CharField(blank=True, max_length=255, null=True)),
                ("link", models.CharField(max_length=255)),
                (
                    "parent_id",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.menus",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "menus",
            },
            bases=(modules.core.models.include.CacheInvalidationMixin, models.Model),
        ),
        migrations.CreateModel(
            name="Kycs",
            fields=[
                (
                    "status",
                    models.CharField(
                        choices=[("active", "Active"), ("inactive", "Inactive")],
                        default="active",
                        max_length=100,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("first_name", models.CharField(max_length=70)),
                ("last_name", models.CharField(max_length=70)),
                ("middle_name", models.CharField(blank=True, max_length=70, null=True)),
                ("country_id", models.PositiveIntegerField()),
                ("document_type", models.CharField(max_length=15)),
                ("selfie", models.ImageField(blank=True, null=True, upload_to="")),
                (
                    "rejected_reason",
                    ckeditor.fields.RichTextField(blank=True, null=True),
                ),
                ("approved_at", models.DateTimeField(blank=True, null=True)),
                ("rejected_at", models.DateTimeField(blank=True, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "kycs",
            },
            bases=(modules.core.models.include.CacheInvalidationMixin, models.Model),
        ),
        migrations.CreateModel(
            name="KycDocuments",
            fields=[
                (
                    "status",
                    models.CharField(
                        choices=[("active", "Active"), ("inactive", "Inactive")],
                        default="active",
                        max_length=100,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=255)),
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("path", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "kyc",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.kycs"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "kyc_documents",
            },
            bases=(modules.core.models.include.CacheInvalidationMixin, models.Model),
        ),
        migrations.CreateModel(
            name="Bank",
            fields=[
                (
                    "status",
                    models.CharField(
                        choices=[("active", "Active"), ("inactive", "Inactive")],
                        default="active",
                        max_length=100,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=255)),
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("holder_name", models.CharField(max_length=255)),
                ("swift", models.CharField(max_length=255)),
                ("iban", models.CharField(max_length=255)),
                ("address", models.CharField(max_length=255)),
                ("account_number", models.CharField(max_length=32)),
                (
                    "holder",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "banks",
            },
            bases=(modules.core.models.include.CacheInvalidationMixin, models.Model),
        ),
        migrations.AddField(
            model_name="users",
            name="language",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="core.languages",
            ),
        ),
        migrations.AddField(
            model_name="users",
            name="referrer",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="users",
            name="user_permissions",
            field=models.ManyToManyField(
                blank=True,
                help_text="Specific permissions for this user.",
                related_name="user_set",
                related_query_name="user",
                to="auth.permission",
                verbose_name="user permissions",
            ),
        ),
    ]

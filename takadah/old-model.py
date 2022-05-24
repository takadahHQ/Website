from django.db import models


class AuthenticationLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    authenticatable_type = models.CharField(max_length=255)
    authenticatable_id = models.PositiveBigIntegerField()
    ip_address = models.CharField(max_length=45, blank=True, null=True)
    user_agent = models.TextField(blank=True, null=True)
    login_at = models.DateTimeField(blank=True, null=True)
    login_successful = models.IntegerField()
    logout_at = models.DateTimeField(blank=True, null=True)
    cleared_by_user = models.IntegerField()
    location = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'authentication_log'


class Authors(models.Model):
    id = models.BigAutoField(primary_key=True)
    story_id = models.PositiveBigIntegerField()
    user_id = models.PositiveBigIntegerField()
    status = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'authors'


class BandwagonEvents(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    ip = models.CharField(max_length=50)
    url = models.CharField(max_length=255)
    event_at = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'bandwagon_events'


class BankAccounts(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.PositiveBigIntegerField()
    reference_number = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    iban = models.CharField(max_length=255, blank=True, null=True)
    swift = models.CharField(max_length=255, blank=True, null=True)
    ifsc = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    account_holder_name = models.CharField(max_length=255, blank=True, null=True)
    account_holder_address = models.CharField(max_length=255, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    country_id = models.PositiveBigIntegerField()
    status = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'bank_accounts'


class BetaReaders(models.Model):
    id = models.BigAutoField(primary_key=True)
    story_id = models.PositiveBigIntegerField()
    user_id = models.PositiveBigIntegerField()
    status = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'beta_readers'


class Bookmarks(models.Model):
    id = models.BigAutoField(primary_key=True)
    story_id = models.PositiveBigIntegerField()
    user_id = models.PositiveBigIntegerField()
    url = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'bookmarks'


class CanvasPosts(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    slug = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    summary = models.TextField(blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    published_at = models.DateTimeField(blank=True, null=True)
    featured_image = models.CharField(max_length=255, blank=True, null=True)
    featured_image_caption = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.CharField(max_length=36)
    meta = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'canvas_posts'
        unique_together = (('slug', 'user_id'),)


class CanvasPostsTags(models.Model):
    post_id = models.CharField(max_length=36)
    tag_id = models.CharField(max_length=36)

    class Meta:
        managed = False
        db_table = 'canvas_posts_tags'
        unique_together = (('post_id', 'tag_id'),)


class CanvasPostsTopics(models.Model):
    post_id = models.CharField(max_length=36)
    topic_id = models.CharField(max_length=36)

    class Meta:
        managed = False
        db_table = 'canvas_posts_topics'
        unique_together = (('post_id', 'topic_id'),)


class CanvasTags(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    slug = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    user_id = models.CharField(max_length=36)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'canvas_tags'
        unique_together = (('slug', 'user_id'),)


class CanvasTopics(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    slug = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    user_id = models.CharField(max_length=36)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'canvas_topics'
        unique_together = (('slug', 'user_id'),)


class CanvasUsers(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=255)
    email = models.CharField(unique=True, max_length=255)
    username = models.CharField(unique=True, max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255)
    summary = models.TextField(blank=True, null=True)
    avatar = models.CharField(max_length=255, blank=True, null=True)
    dark_mode = models.IntegerField(blank=True, null=True)
    digest = models.IntegerField(blank=True, null=True)
    locale = models.CharField(max_length=255, blank=True, null=True)
    role = models.IntegerField(blank=True, null=True)
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'canvas_users'


class CanvasViews(models.Model):
    post_id = models.CharField(max_length=36)
    ip = models.CharField(max_length=255, blank=True, null=True)
    agent = models.TextField(blank=True, null=True)
    referer = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'canvas_views'


class CanvasVisits(models.Model):
    post_id = models.CharField(max_length=36)
    ip = models.CharField(max_length=255, blank=True, null=True)
    agent = models.TextField(blank=True, null=True)
    referer = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'canvas_visits'


class Categories(models.Model):
    id = models.BigAutoField(primary_key=True)
    type_id = models.PositiveBigIntegerField()
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'categories'


class Chapters(models.Model):
    id = models.BigAutoField(primary_key=True)
    story_id = models.PositiveBigIntegerField()
    user_id = models.PositiveBigIntegerField()
    edited_by = models.PositiveBigIntegerField(blank=True, null=True)
    position = models.IntegerField()
    title = models.CharField(max_length=255)
    text = models.TextField()
    authors_note = models.TextField(blank=True, null=True)
    words = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=255)
    released_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'chapters'


class Characters(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    category_id = models.PositiveBigIntegerField()
    status = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'characters'


class Countries(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'countries'


class FailedJobs(models.Model):
    id = models.BigAutoField(primary_key=True)
    uuid = models.CharField(unique=True, max_length=255)
    connection = models.TextField()
    queue = models.TextField()
    payload = models.TextField()
    exception = models.TextField()
    failed_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'failed_jobs'


class Genres(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'genres'


class KycDocuments(models.Model):
    id = models.BigAutoField(primary_key=True)
    kyc_id = models.PositiveBigIntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    path = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'kyc_documents'


class Kycs(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.PositiveBigIntegerField()
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    middle_name = models.CharField(max_length=70, blank=True, null=True)
    country_id = models.PositiveIntegerField()
    document_type = models.CharField(max_length=15)
    selfie_id = models.PositiveBigIntegerField()
    status = models.CharField(max_length=15, blank=True, null=True)
    rejected_reason = models.TextField(blank=True, null=True)
    approved_at = models.DateTimeField(blank=True, null=True)
    rejected_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'kycs'


class Languages(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    native_name = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'languages'


class Menus(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    position = models.IntegerField(blank=True, null=True)
    parent_id = models.PositiveBigIntegerField()
    image = models.CharField(max_length=255, blank=True, null=True)
    icon = models.CharField(max_length=255, blank=True, null=True)
    link = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'menus'


class Migrations(models.Model):
    migration = models.CharField(max_length=255)
    batch = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'migrations'


class ModelChangesHistory(models.Model):
    id = models.BigAutoField(primary_key=True)
    model_id = models.PositiveBigIntegerField()
    model_type = models.CharField(max_length=255)
    before_changes = models.JSONField(blank=True, null=True)
    after_changes = models.JSONField(blank=True, null=True)
    changes = models.JSONField(blank=True, null=True)
    change_type = models.CharField(max_length=12)
    changer_type = models.CharField(max_length=255, blank=True, null=True)
    changer_id = models.PositiveBigIntegerField(blank=True, null=True)
    stack_trace = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'model_changes_history'


class Packages(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.PositiveBigIntegerField()
    story_id = models.PositiveBigIntegerField()
    name = models.CharField(max_length=255)
    advance = models.IntegerField()
    amount = models.IntegerField()
    status = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'packages'


class Pages(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.TextField(blank=True, null=True)
    slug = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    seo_title = models.TextField(blank=True, null=True)
    seo_description = models.TextField(blank=True, null=True)
    seo_keywords = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'pages'


class PasswordResets(models.Model):
    email = models.CharField(max_length=255)
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'password_resets'


class PersonalAccessTokens(models.Model):
    id = models.BigAutoField(primary_key=True)
    tokenable_type = models.CharField(max_length=255)
    tokenable_id = models.PositiveBigIntegerField()
    name = models.CharField(max_length=255)
    token = models.CharField(unique=True, max_length=64)
    abilities = models.TextField(blank=True, null=True)
    last_used_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'personal_access_tokens'


class Ratings(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'ratings'


class Reports(models.Model):
    id = models.BigAutoField(primary_key=True)
    story_id = models.PositiveBigIntegerField()
    user_id = models.PositiveBigIntegerField()
    url = models.CharField(max_length=255, blank=True, null=True)
    reason = models.TextField()
    status = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'reports'


class RouteUsage(models.Model):
    id = models.BigAutoField(primary_key=True)
    identifier = models.CharField(unique=True, max_length=40)
    method = models.CharField(max_length=12)
    path = models.TextField()
    status_code = models.PositiveSmallIntegerField()
    action = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'route_usage'


class ScheduleHistories(models.Model):
    schedule = models.ForeignKey('Schedules', models.DO_NOTHING)
    command = models.CharField(max_length=255)
    params = models.TextField(blank=True, null=True)
    output = models.TextField()
    options = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'schedule_histories'


class Schedules(models.Model):
    command = models.CharField(max_length=255)
    command_custom = models.CharField(max_length=255, blank=True, null=True)
    params = models.TextField(blank=True, null=True)
    expression = models.CharField(max_length=255)
    environments = models.CharField(max_length=255, blank=True, null=True)
    options = models.TextField(blank=True, null=True)
    log_filename = models.CharField(max_length=255, blank=True, null=True)
    even_in_maintenance_mode = models.IntegerField()
    without_overlapping = models.IntegerField()
    on_one_server = models.IntegerField()
    webhook_before = models.CharField(max_length=255, blank=True, null=True)
    webhook_after = models.CharField(max_length=255, blank=True, null=True)
    email_output = models.CharField(max_length=255, blank=True, null=True)
    sendmail_error = models.IntegerField()
    log_success = models.IntegerField()
    log_error = models.IntegerField()
    status = models.IntegerField()
    run_in_background = models.IntegerField()
    groups = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    sendmail_success = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'schedules'


class Sessions(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    user_id = models.PositiveBigIntegerField(blank=True, null=True)
    ip_address = models.CharField(max_length=45, blank=True, null=True)
    user_agent = models.TextField(blank=True, null=True)
    payload = models.TextField()
    last_activity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sessions'


class Settings(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    tagline = models.TextField(blank=True, null=True)
    logo = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    theme = models.CharField(max_length=255)
    footer = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'settings'


class SiteSearchConfigs(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    crawl_url = models.CharField(max_length=255)
    index_base_name = models.CharField(max_length=255)
    enabled = models.IntegerField()
    driver_class = models.CharField(max_length=255, blank=True, null=True)
    profile_class = models.CharField(max_length=255, blank=True, null=True)
    extra = models.JSONField(blank=True, null=True)
    index_name = models.CharField(max_length=255, blank=True, null=True)
    number_of_urls_indexed = models.IntegerField()
    pending_index_name = models.CharField(max_length=255, blank=True, null=True)
    crawling_started_at = models.DateTimeField(blank=True, null=True)
    crawling_ended_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'site_search_configs'


class Socials(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    icon = models.TextField(blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    link = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'socials'


class Sponsors(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.PositiveBigIntegerField()
    package_id = models.PositiveBigIntegerField()
    status = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'sponsors'


class StatsEvents(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    value = models.BigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'stats_events'


class Stories(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    summary = models.TextField()
    cover = models.CharField(max_length=255, blank=True, null=True)
    type_id = models.PositiveBigIntegerField(blank=True, null=True)
    tag_id = models.PositiveBigIntegerField(blank=True, null=True)
    language_id = models.PositiveBigIntegerField(blank=True, null=True)
    genre_id = models.PositiveBigIntegerField(blank=True, null=True)
    genre_2_id = models.PositiveBigIntegerField(blank=True, null=True)
    rating_id = models.PositiveBigIntegerField(blank=True, null=True)
    released_at = models.DateTimeField()
    featured = models.IntegerField()
    status = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'stories'


class Transactions(models.Model):
    id = models.BigAutoField(primary_key=True)
    payable_type = models.CharField(max_length=255)
    payable_id = models.PositiveBigIntegerField()
    wallet = models.ForeignKey('Wallets', models.DO_NOTHING)
    type = models.CharField(max_length=8)
    amount = models.DecimalField(max_digits=64, decimal_places=0)
    confirmed = models.IntegerField()
    meta = models.JSONField(blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=36)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'transactions'


class Transfers(models.Model):
    id = models.BigAutoField(primary_key=True)
    from_type = models.CharField(max_length=255)
    from_id = models.PositiveBigIntegerField()
    to_type = models.CharField(max_length=255)
    to_id = models.PositiveBigIntegerField()
    status = models.CharField(max_length=8)
    status_last = models.CharField(max_length=8, blank=True, null=True)
    deposit = models.ForeignKey(Transactions, models.DO_NOTHING)
    withdraw = models.ForeignKey(Transactions, models.DO_NOTHING)
    discount = models.DecimalField(max_digits=64, decimal_places=0)
    fee = models.DecimalField(max_digits=64, decimal_places=0)
    uuid = models.CharField(unique=True, max_length=36)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'transfers'


class Types(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'types'


class Universes(models.Model):
    id = models.BigAutoField(primary_key=True)
    category_id = models.PositiveBigIntegerField()
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'universes'


class Users(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    pseudonym = models.CharField(max_length=255, blank=True, null=True)
    bio = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(unique=True, max_length=255)
    email_verified_at = models.DateTimeField(blank=True, null=True)
    password = models.CharField(max_length=255)
    two_factor_secret = models.TextField(blank=True, null=True)
    two_factor_recovery_codes = models.TextField(blank=True, null=True)
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    timezone = models.CharField(max_length=255, blank=True, null=True)
    current_team_id = models.PositiveBigIntegerField(blank=True, null=True)
    profile_photo_path = models.CharField(max_length=2048, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    kyc_verified_at = models.DateTimeField(blank=True, null=True)
    deactivated = models.IntegerField()
    deleted = models.IntegerField()
    language_id = models.PositiveBigIntegerField(blank=True, null=True)
    referral_id = models.BigIntegerField(blank=True, null=True)
    referral_code = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class Wallets(models.Model):
    id = models.BigAutoField(primary_key=True)
    holder_type = models.CharField(max_length=255)
    holder_id = models.PositiveBigIntegerField()
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    uuid = models.CharField(unique=True, max_length=36)
    description = models.CharField(max_length=255, blank=True, null=True)
    meta = models.JSONField(blank=True, null=True)
    balance = models.DecimalField(max_digits=64, decimal_places=0)
    decimal_places = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'wallets'
        unique_together = (('holder_type', 'holder_id', 'slug'),)
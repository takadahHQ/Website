
-- Dumping structure for table db.auth_group
CREATE TABLE IF NOT EXISTS "auth_group" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(150) NOT NULL UNIQUE);

-- Data exporting was unselected.

-- Dumping structure for table db.auth_group_permissions
CREATE TABLE IF NOT EXISTS "auth_group_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "group_id" integer NOT NULL REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED, "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED);

-- Data exporting was unselected.

-- Dumping structure for table db.auth_permission
CREATE TABLE IF NOT EXISTS "auth_permission" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "content_type_id" integer NOT NULL REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED, "codename" varchar(100) NOT NULL, "name" varchar(255) NOT NULL);

-- Data exporting was unselected.

-- Dumping structure for table db.blog_category
CREATE TABLE IF NOT EXISTS "blog_category" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(200) NOT NULL, "slug" varchar(50) NOT NULL, "status" varchar(100) NOT NULL, "parent_id" bigint NULL REFERENCES "blog_category" ("id") DEFERRABLE INITIALLY DEFERRED);

-- Data exporting was unselected.

-- Dumping structure for table db.blog_post
CREATE TABLE IF NOT EXISTS "blog_post" ("slug" varchar(255) NULL, "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(255) NULL, "content" text NULL, "seo_title" varchar(255) NULL, "seo_description" text NULL, "seo_keywords" text NULL, "status" varchar(100) NOT NULL, "featured_image" varchar(255) NULL, "featured_image_caption" varchar(255) NULL, "user_id" varchar(36) NOT NULL, "meta" text NULL CHECK ((JSON_VALID("meta") OR "meta" IS NULL)), "published_at" datetime NOT NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL, "deleted_at" datetime NULL, "category_id" bigint NULL REFERENCES "blog_category" ("id") DEFERRABLE INITIALLY DEFERRED);

-- Data exporting was unselected.

-- Dumping structure for table db.blog_post_tags
CREATE TABLE IF NOT EXISTS "blog_post_tags" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "post_id" bigint NOT NULL REFERENCES "blog_post" ("id") DEFERRABLE INITIALLY DEFERRED, "tags_id" bigint NOT NULL REFERENCES "blog_tags" ("id") DEFERRABLE INITIALLY DEFERRED);

-- Data exporting was unselected.

-- Dumping structure for table db.blog_post_topics
CREATE TABLE IF NOT EXISTS "blog_post_topics" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "post_id" bigint NOT NULL REFERENCES "blog_post" ("id") DEFERRABLE INITIALLY DEFERRED, "topics_id" bigint NOT NULL REFERENCES "blog_topics" ("id") DEFERRABLE INITIALLY DEFERRED);

-- Data exporting was unselected.

-- Dumping structure for table db.blog_tags
CREATE TABLE IF NOT EXISTS "blog_tags" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "slug" varchar(255) NOT NULL, "name" varchar(255) NOT NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL);

-- Data exporting was unselected.

-- Dumping structure for table db.blog_topics
CREATE TABLE IF NOT EXISTS "blog_topics" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "slug" varchar(255) NOT NULL, "name" varchar(255) NOT NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL);

-- Data exporting was unselected.

-- Dumping structure for table db.cookie_consent_cookie
CREATE TABLE IF NOT EXISTS "cookie_consent_cookie" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(250) NOT NULL, "description" text NOT NULL, "path" text NOT NULL, "domain" varchar(250) NOT NULL, "created" datetime NOT NULL, "cookiegroup_id" integer NOT NULL REFERENCES "cookie_consent_cookiegroup" ("id") DEFERRABLE INITIALLY DEFERRED);

-- Data exporting was unselected.

-- Dumping structure for table db.cookie_consent_cookiegroup
CREATE TABLE IF NOT EXISTS "cookie_consent_cookiegroup" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "varname" varchar(32) NOT NULL, "name" varchar(100) NOT NULL, "description" text NOT NULL, "is_required" bool NOT NULL, "is_deletable" bool NOT NULL, "ordering" integer NOT NULL, "created" datetime NOT NULL);

-- Data exporting was unselected.

-- Dumping structure for table db.cookie_consent_logitem
CREATE TABLE IF NOT EXISTS "cookie_consent_logitem" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "action" integer NOT NULL, "version" varchar(32) NOT NULL, "created" datetime NOT NULL, "cookiegroup_id" bigint NOT NULL REFERENCES "cookie_consent_cookiegroup" ("id") DEFERRABLE INITIALLY DEFERRED);

-- Data exporting was unselected.

-- Dumping structure for table db.core_bank
CREATE TABLE IF NOT EXISTS "core_bank" ("status" varchar(100) NOT NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL, "name" varchar(255) NOT NULL, "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "holder_name" varchar(255) NOT NULL, "swift" varchar(255) NOT NULL, "iban" varchar(255) NOT NULL, "address" varchar(255) NOT NULL, "account_number" varchar(32) NOT NULL, "holder_id" bigint NOT NULL REFERENCES "core_users" ("id") DEFERRABLE INITIALLY DEFERRED);

-- Data exporting was unselected.

-- Dumping structure for table db.core_kycdocuments
CREATE TABLE IF NOT EXISTS "core_kycdocuments" ("status" varchar(100) NOT NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL, "name" varchar(255) NOT NULL, "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "path" varchar(255) NULL, "kyc_id" bigint NOT NULL REFERENCES "core_kycs" ("id") DEFERRABLE INITIALLY DEFERRED);

-- Data exporting was unselected.

-- Dumping structure for table db.core_kycs
CREATE TABLE IF NOT EXISTS "core_kycs" ("status" varchar(100) NOT NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL, "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "first_name" varchar(70) NOT NULL, "last_name" varchar(70) NOT NULL, "middle_name" varchar(70) NULL, "country_id" integer unsigned NOT NULL CHECK ("country_id" >= 0), "document_type" varchar(15) NOT NULL, "selfie" varchar(100) NULL, "rejected_reason" text NULL, "approved_at" datetime NULL, "rejected_at" datetime NULL, "user_id" bigint NOT NULL REFERENCES "core_users" ("id") DEFERRABLE INITIALLY DEFERRED);

-- Data exporting was unselected.

-- Dumping structure for table db.core_languages
CREATE TABLE IF NOT EXISTS "core_languages" ("status" varchar(100) NOT NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL, "name" varchar(255) NOT NULL, "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "code" varchar(255) NOT NULL, "native_name" varchar(255) NOT NULL);

-- Data exporting was unselected.

-- Dumping structure for table db.core_menus
CREATE TABLE IF NOT EXISTS "core_menus" ("status" varchar(100) NOT NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL, "name" varchar(255) NOT NULL, "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "position" varchar(100) NOT NULL, "image" varchar(255) NULL, "icon" varchar(255) NULL, "link" varchar(255) NOT NULL, "parent_id_id" bigint NULL REFERENCES "core_menus" ("id") DEFERRABLE INITIALLY DEFERRED);

-- Data exporting was unselected.

-- Dumping structure for table db.core_settings
CREATE TABLE IF NOT EXISTS "core_settings" ("status" varchar(100) NOT NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL, "name" varchar(255) NOT NULL, "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "tagline" text NULL, "logo" varchar(255) NULL, "phone" varchar(255) NOT NULL, "email" varchar(255) NOT NULL, "color" varchar(255) NOT NULL, "theme" varchar(255) NOT NULL, "footer" varchar(255) NOT NULL);

-- Data exporting was unselected.

-- Dumping structure for table db.core_site
CREATE TABLE IF NOT EXISTS "core_site" ("created_at" datetime NOT NULL, "updated_at" datetime NOT NULL, "name" varchar(255) NOT NULL, "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "hero_header" varchar(255) NOT NULL, "hero_text" varchar(255) NOT NULL, "newsletter_header" varchar(255) NOT NULL, "newsletter_text" varchar(255) NOT NULL);

-- Data exporting was unselected.

-- Dumping structure for table db.core_socials
CREATE TABLE IF NOT EXISTS "core_socials" ("status" varchar(100) NOT NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL, "name" varchar(255) NOT NULL, "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "icon" text NULL, "image" varchar(255) NULL, "link" varchar(255) NOT NULL);

-- Data exporting was unselected.

-- Dumping structure for table db.core_transactions
CREATE TABLE IF NOT EXISTS "core_transactions" ("created_at" datetime NOT NULL, "updated_at" datetime NOT NULL, "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "payable_type" varchar(255) NOT NULL, "trans_type" varchar(8) NOT NULL, "amount" decimal NOT NULL, "confirmed" integer NOT NULL, "meta" text NULL CHECK ((JSON_VALID("meta") OR "meta" IS NULL)), "uuid" varchar(36) NOT NULL UNIQUE, "payable_id_id" bigint NOT NULL REFERENCES "core_users" ("id") DEFERRABLE INITIALLY DEFERRED, "wallet_id" bigint NOT NULL REFERENCES "core_wallets" ("id") DEFERRABLE INITIALLY DEFERRED);

-- Data exporting was unselected.

-- Dumping structure for table db.core_transfers
CREATE TABLE IF NOT EXISTS "core_transfers" ("created_at" datetime NOT NULL, "updated_at" datetime NOT NULL, "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "from_type" varchar(255) NOT NULL, "to_type" varchar(255) NOT NULL, "status" varchar(100) NOT NULL, "status_last" varchar(8) NULL, "discount" decimal NOT NULL, "fee" decimal NOT NULL, "uuid" varchar(36) NOT NULL UNIQUE, "deposit_id" bigint NOT NULL REFERENCES "core_transactions" ("id") DEFERRABLE INITIALLY DEFERRED, "from_id_id" bigint NOT NULL REFERENCES "core_users" ("id") DEFERRABLE INITIALLY DEFERRED, "to_id_id" bigint NOT NULL REFERENCES "core_users" ("id") DEFERRABLE INITIALLY DEFERRED, "withdraw_id" bigint NOT NULL REFERENCES "core_transactions" ("id") DEFERRABLE INITIALLY DEFERRED);

-- Data exporting was unselected.

-- Dumping structure for table db.core_users
CREATE TABLE IF NOT EXISTS "core_users" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "password" varchar(128) NOT NULL, "last_login" datetime NULL, "is_superuser" bool NOT NULL, "username" varchar(150) NOT NULL UNIQUE, "first_name" varchar(150) NOT NULL, "last_name" varchar(150) NOT NULL, "email" varchar(254) NOT NULL, "is_staff" bool NOT NULL, "date_joined" datetime NOT NULL, "pseudonym" varchar(255) NULL, "bio" text NULL, "location" varchar(30) NOT NULL, "birth_date" date NULL, "profile_photo" varchar(2048) NULL, "updated_at" datetime NOT NULL, "gender" varchar(100) NOT NULL, "kyc_status" varchar(100) NOT NULL, "kyc_verified_at" datetime NULL, "ref_code" varchar(20) NOT NULL, "active" bool NOT NULL, "language_id" bigint NULL REFERENCES "core_languages" ("id") DEFERRABLE INITIALLY DEFERRED, "referrer_id" bigint NULL REFERENCES "core_users" ("id") DEFERRABLE INITIALLY DEFERRED);

-- Data exporting was unselected.

-- Dumping structure for table db.core_users_following
CREATE TABLE IF NOT EXISTS "core_users_following" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "from_users_id" bigint NOT NULL REFERENCES "core_users" ("id") DEFERRABLE INITIALLY DEFERRED, "to_users_id" bigint NOT NULL REFERENCES "core_users" ("id") DEFERRABLE INITIALLY DEFERRED);

-- Data exporting was unselected.

-- Dumping structure for table db.core_users_groups
CREATE TABLE IF NOT EXISTS "core_users_groups" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "users_id" bigint NOT NULL REFERENCES "core_users" ("id") DEFERRABLE INITIALLY DEFERRED, "group_id" integer NOT NULL REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED);

-- Data exporting was unselected.

-- Dumping structure for table db.core_users_user_permissions
CREATE TABLE IF NOT EXISTS "core_users_user_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "users_id" bigint NOT NULL REFERENCES "core_users" ("id") DEFERRABLE INITIALLY DEFERRED, "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED);

-- Data exporting was unselected.

-- Dumping structure for table db.core_wallets
CREATE TABLE IF NOT EXISTS "core_wallets" ("created_at" datetime NOT NULL, "updated_at" datetime NOT NULL, "name" varchar(255) NOT NULL, "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "holder_type" varchar(255) NOT NULL, "slug" varchar(255) NOT NULL, "uuid" varchar(36) NOT NULL UNIQUE, "description" varchar(255) NULL, "meta" text NULL CHECK ((JSON_VALID("meta") OR "meta" IS NULL)), "balance" decimal NOT NULL, "decimal_places" smallint unsigned NOT NULL CHECK ("decimal_places" >= 0), "holder_id_id" bigint NOT NULL REFERENCES "core_users" ("id") DEFERRABLE INITIALLY DEFERRED);

-- Data exporting was unselected.

-- Dumping structure for table db.django_admin_log
CREATE TABLE IF NOT EXISTS "django_admin_log" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "object_id" text NULL, "object_repr" varchar(200) NOT NULL, "action_flag" smallint unsigned NOT NULL CHECK ("action_flag" >= 0), "change_message" text NOT NULL, "content_type_id" integer NULL REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED, "user_id" bigint NOT NULL REFERENCES "core_users" ("id") DEFERRABLE INITIALLY DEFERRED, "action_time" datetime NOT NULL);

-- Data exporting was unselected.

-- Dumping structure for table db.django_content_type
CREATE TABLE IF NOT EXISTS "django_content_type" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "app_label" varchar(100) NOT NULL, "model" varchar(100) NOT NULL);

-- Data exporting was unselected.

-- Dumping structure for table db.django_migrations
CREATE TABLE IF NOT EXISTS "django_migrations" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "app" varchar(255) NOT NULL, "name" varchar(255) NOT NULL, "applied" datetime NOT NULL);

-- Data exporting was unselected.

-- Dumping structure for table db.django_session
CREATE TABLE IF NOT EXISTS "django_session" ("session_key" varchar(40) NOT NULL PRIMARY KEY, "session_data" text NOT NULL, "expire_date" datetime NOT NULL);

-- Data exporting was unselected.

-- Dumping structure for table db.django_site
CREATE TABLE IF NOT EXISTS "django_site" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(50) NOT NULL, "domain" varchar(100) NOT NULL UNIQUE);

-- Data exporting was unselected.

-- Dumping structure for table db.djstripe_account
CREATE TABLE IF NOT EXISTS "djstripe_account" ("djstripe_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "id" varchar(255) NOT NULL UNIQUE, "livemode" bool NULL, "created" datetime NULL, "metadata" text NULL CHECK ((JSON_VALID("metadata") OR "metadata" IS NULL)), "description" text NULL, "djstripe_created" datetime NOT NULL, "djstripe_updated" datetime NOT NULL, "business_profile" text NULL CHECK ((JSON_VALID("business_profile") OR "business_profile" IS NULL)), "business_type" varchar(10) NOT NULL, "charges_enabled" bool NOT NULL, "country" varchar(2) NOT NULL, "company" text NULL CHECK ((JSON_VALID("company") OR "company" IS NULL)), "default_currency" varchar(3) NOT NULL, "details_submitted" bool NOT NULL, "email" varchar(255) NOT NULL, "individual" text NULL CHECK ((JSON_VALID("individual") OR "individual" IS NULL)), "payouts_enabled" bool NULL, "product_description" varchar(255) NOT NULL, "requirements" text NULL CHECK ((JSON_VALID("requirements") OR "requirements" IS NULL)), "settings" text NULL CHECK ((JSON_VALID("settings") OR "settings" IS NULL)), "type" varchar(8) NOT NULL, "tos_acceptance" text NULL CHECK ((JSON_VALID("tos_acceptance") OR "tos_acceptance" IS NULL)), "djstripe_owner_account_id" varchar(255) NULL REFERENCES "djstripe_account" ("id") DEFERRABLE INITIALLY DEFERRED);

-- Data exporting was unselected.

-- Dumping structure for table db.djstripe_apikey
CREATE TABLE IF NOT EXISTS "djstripe_apikey" ("djstripe_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "livemode" bool NOT NULL, "created" datetime NULL, "djstripe_created" datetime NOT NULL, "djstripe_updated" datetime NOT NULL, "id" varchar(255) NOT NULL, "type" varchar(11) NOT NULL, "name" varchar(100) NOT NULL, "secret" varchar(128) NOT NULL UNIQUE, "djstripe_owner_account_id" varchar(255) NULL REFERENCES "djstripe_account" ("id") DEFERRABLE INITIALLY DEFERRED);

-- Data exporting was unselected.

-- Dumping structure for table db.djstripe_applicationfee
CREATE TABLE IF NOT EXISTS "djstripe_applicationfee" ("djstripe_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "id" varchar(255) NOT NULL UNIQUE, "livemode" bool NULL, "created" datetime NULL, "metadata" text NULL CHECK ((JSON_VALID("metadata") OR "metadata" IS NULL)), "description" text NULL, "djstripe_created" datetime NOT NULL, "djstripe_updated" datetime NOT NULL, "amount" bigint NOT NULL, "amount_refunded" bigint NOT NULL, "currency" varchar(3) NOT NULL, "refunded" bool NOT NULL, "balance_transaction_id" varchar(255) NOT NULL REFERENCES "djstripe_balancetransaction" ("id") DEFERRABLE INITIALLY DEFERRED, "charge_id" varchar(255) NOT NULL REFERENCES "djstripe_charge" ("id") DEFERRABLE INITIALLY DEFERRED, "djstripe_owner_account_id" varchar(255) NULL REFERENCES "djstripe_account" ("id") DEFERRABLE INITIALLY DEFERRED, "account_id" varchar(255) NOT NULL REFERENCES "djstripe_account" ("id") DEFERRABLE INITIALLY DEFERRED);

-- Data exporting was unselected.

-- Dumping structure for table db.djstripe_applicationfeerefund
CREATE TABLE IF NOT EXISTS "djstripe_applicationfeerefund" ("djstripe_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "id" varchar(255) NOT NULL UNIQUE, "livemode" bool NULL, "created" datetime NULL, "metadata" text NULL CHECK ((JSON_VALID("metadata") OR "metadata" IS NULL)), "djstripe_created" datetime NOT NULL, "djstripe_updated" datetime NOT NULL, "amount" bigint NOT NULL, "currency" varchar(3) NOT NULL, "balance_transaction_id" varchar(255) NOT NULL REFERENCES "djstripe_balancetransaction" ("id") DEFERRABLE INITIALLY DEFERRED, "fee_id" varchar(255) NOT NULL REFERENCES "djstripe_applicationfee" ("id") DEFERRABLE INITIALLY DEFERRED, "djstripe_owner_account_id" varchar(255) NULL REFERENCES "djstripe_account" ("id") DEFERRABLE INITIALLY DEFERRED);

-- Data exporting was unselected.

-- Dumping structure for table db.djstripe_balancetransaction
CREATE TABLE IF NOT EXISTS "djstripe_balancetransaction" ("djstripe_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "id" varchar(255) NOT NULL UNIQUE, "livemode" bool NULL, "created" datetime NULL, "metadata" text NULL CHECK ((JSON_VALID("metadata") OR "metadata" IS NULL)), "description" text NULL, "djstripe_created" datetime NOT NULL, "djstripe_updated" datetime NOT NULL, "amount" bigint NOT NULL, "available_on" datetime NOT NULL, "currency" varchar(3) NOT NULL, "exchange_rate" decimal NULL, "fee" bigint NOT NULL, "fee_details" text NOT NULL CHECK ((JSON_VALID("fee_details") OR "fee_details" IS NULL)), "net" bigint NOT NULL, "status" varchar(9) NOT NULL, "type" varchar(29) NOT NULL, "reporting_category" varchar(29) NOT NULL, "source" varchar(255) NOT NULL, "djstripe_owner_account_id" varchar(255) NULL REFERENCES "djstripe_account" ("id") DEFERRABLE INITIALLY DEFERRED);

-- Data exporting was unselected.

-- Dumping structure for table db.djstripe_bankaccount
CREATE TABLE IF NOT EXISTS "djstripe_bankaccount" ("djstripe_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "id" varchar(255) NOT NULL UNIQUE, "livemode" bool NULL, "created" datetime NULL, "metadata" text NULL CHECK ((JSON_VALID("metadata") OR "metadata" IS NULL)), "description" text NULL, "djstripe_created" datetime NOT NULL, "djstripe_updated" datetime NOT NULL, "account_holder_name" text NOT NULL, "account_holder_type" varchar(10) NOT NULL, "bank_name" varchar(255) NOT NULL, "country" varchar(2) NOT NULL, "currency" varchar(3) NOT NULL, "default_for_currency" bool NULL, "fingerprint" varchar(16) NOT NULL, "last4" varchar(4) NOT NULL, "routing_number" varchar(255) NOT NULL, "status" varchar(19) NOT NULL, "account_id" varchar(255) NULL REFERENCES "djstripe_account" ("id") DEFERRABLE INITIALLY DEFERRED, "customer_id" varchar(255) NULL REFERENCES "djstripe_customer" ("id") DEFERRABLE INITIALLY DEFERRED, "djstripe_owner_account_id" varchar(255) NULL REFERENCES "djstripe_account" ("id") DEFERRABLE INITIALLY DEFERRED);

-- Data exporting was unselected.

-- Dumping structure for table db.djstripe_card
CREATE TABLE IF NOT EXISTS "djstripe_card" ("djstripe_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "id" varchar(255) NOT NULL UNIQUE, "livemode" bool NULL, "created" datetime NULL, "metadata" text NULL CHECK ((JSON_VALID("metadata") OR "metadata" IS NULL)), "description" text NULL, "djstripe_created" datetime NOT NULL, "djstripe_updated" datetime NOT NULL, "address_city" text NOT NULL, "address_country" text NOT NULL, "address_line1" text NOT NULL, "address_line1_check" varchar(11) NOT NULL, "address_line2" text NOT NULL, "address_state" text NOT NULL, "address_zip" text NOT NULL, "address_zip_check" varchar(11) NOT NULL, "brand" varchar(16) NOT NULL, "country" varchar(2) NOT NULL, "cvc_check" varchar(11) NOT NULL, "dynamic_last4" varchar(4) NOT NULL, "exp_month" integer NOT NULL, "exp_year" integer NOT NULL, "fingerprint" varchar(16) NOT NULL, "funding" varchar(7) NOT NULL, "last4" varchar(4) NOT NULL, "name" text NOT NULL, "tokenization_method" varchar(11) NOT NULL, "customer_id" varchar(255) NULL REFERENCES "djstripe_customer" ("id") DEFERRABLE INITIALLY DEFERRED, "djstripe_owner_account_id" varchar(255) NULL REFERENCES "djstripe_account" ("id") DEFERRABLE INITIALLY DEFERRED, "account_id" varchar(255) NULL REFERENCES "djstripe_account" ("id") DEFERRABLE INITIALLY DEFERRED, "default_for_currency" bool NULL);

-- Data exporting was unselected.

-- Dumping structure for table db.djstripe_charge
CREATE TABLE IF NOT EXISTS "djstripe_charge" ("djstripe_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "id" varchar(255) NOT NULL UNIQUE, "livemode" bool NULL, "created" datetime NULL, "metadata" text NULL CHECK ((JSON_VALID("metadata") OR "metadata" IS NULL)), "description" text NULL, "djstripe_created" datetime NOT NULL, "djstripe_updated" datetime NOT NULL, "amount" decimal NOT NULL, "amount_refunded" decimal NOT NULL, "captured" bool NOT NULL, "currency" varchar(3) NOT NULL, "failure_code" varchar(42) NOT NULL, "failure_message" text NOT NULL, "fraud_details" text NULL CHECK ((JSON_VALID("fraud_details") OR "fraud_details" IS NULL)), "outcome" text NULL CHECK ((JSON_VALID("outcome") OR "outcome" IS NULL)), "paid" bool NOT NULL, "payment_method_details" text NULL CHECK ((JSON_VALID("payment_method_details") OR "payment_method_details" IS NULL)), "receipt_email" text NOT NULL, "receipt_number" varchar(14) NOT NULL, "receipt_url" text NOT NULL, "refunded" bool NOT NULL, "shipping" text NULL CHECK ((JSON_VALID("shipping") OR "shipping" IS NULL)), "statement_descriptor" varchar(22) NULL, "status" varchar(9) NOT NULL, "transfer_group" varchar(255) NULL, "on_behalf_of_id" varchar(255) NULL REFERENCES "djstripe_account" ("id") DEFERRABLE INITIALLY DEFERRED, "amount_captured" decimal NULL, "application" varchar(255) NOT NULL, "application_fee_amount" decimal NULL, "billing_details" text NULL CHECK ((JSON_VALID("billing_details") OR "billing_details" IS NULL)), "calculated_statement_descriptor" varchar(22) NOT NULL, "disputed" bool NOT NULL, "statement_descriptor_suffix" varchar(22) NULL, "transfer_data" text NULL CHECK ((JSON_VALID("transfer_data") OR "transfer_data" IS NULL)), "customer_id" varchar(255) NULL REFERENCES "djstripe_customer" ("id") DEFERRABLE INITIALLY DEFERRED, "dispute_id" varchar(255) NULL REFERENCES "djstripe_dispute" ("id") DEFERRABLE INITIALLY DEFERRED, "invoice_id" varchar(255) NULL REFERENCES "djstripe_invoice" ("id") DEFERRABLE INITIALLY DEFERRED, "transfer_id" varchar(255) NULL REFERENCES "djstripe_transfer" ("id") DEFERRABLE INITIALLY DEFERRED, "balance_transaction_id" varchar(255) NULL REFERENCES "djstripe_balancetransaction" ("id") DEFERRABLE INITIALLY DEFERRED, "payment_intent_id" varchar(255) NULL REFERENCES "djstripe_paymentintent" ("id") DEFERRABLE INITIALLY DEFERRED, "payment_method_id" varchar(255) NULL REFERENCES "djstripe_paymentmethod" ("id") DEFERRABLE INITIALLY DEFERRED, "djstripe_owner_account_id" varchar(255) NULL REFERENCES "djstripe_account" ("id") DEFERRABLE INITIALLY DEFERRED, "source_transfer_id" varchar(255) NULL REFERENCES "djstripe_transfer" ("id") DEFERRABLE INITIALLY DEFERRED, "application_fee_id" varchar(255) NULL REFERENCES "djstripe_applicationfee" ("id") DEFERRABLE INITIALLY DEFERRED, "source_id" varchar(255) NULL REFERENCES "djstripe_djstripepaymentmethod" ("id") DEFERRABLE INITIALLY DEFERRED);

-- Data exporting was unselected.

-- Dumping structure for table db.djstripe_countryspec
CREATE TABLE IF NOT EXISTS "djstripe_countryspec" ("djstripe_created" datetime NOT NULL, "djstripe_updated" datetime NOT NULL, "id" varchar(2) NOT NULL PRIMARY KEY, "default_currency" varchar(3) NOT NULL, "supported_bank_account_currencies" text NOT NULL CHECK ((JSON_VALID("supported_bank_account_currencies") OR "supported_bank_account_currencies" IS NULL)), "supported_payment_currencies" text NOT NULL CHECK ((JSON_VALID("supported_payment_currencies") OR "supported_payment_currencies" IS NULL)), "supported_payment_methods" text NOT NULL CHECK ((JSON_VALID("supported_payment_methods") OR "supported_payment_methods" IS NULL)), "supported_transfer_countries" text NOT NULL CHECK ((JSON_VALID("supported_transfer_countries") OR "supported_transfer_countries" IS NULL)), "verification_fields" text NOT NULL CHECK ((JSON_VALID("verification_fields") OR "verification_fields" IS NULL)));

-- Data exporting was unselected.

-- Dumping structure for table db.djstripe_coupon
CREATE TABLE IF NOT EXISTS "djstripe_coupon" ("djstripe_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "livemode" bool NULL, "created" datetime NULL, "metadata" text NULL CHECK ((JSON_VALID("metadata") OR "metadata" IS NULL)), "description" text NULL, "djstripe_created" datetime NOT NULL, "djstripe_updated" datetime NOT NULL, "id" varchar(500) NOT NULL, "amount_off" decimal NULL, "currency" varchar(3) NULL, "duration" varchar(9) NOT NULL, "duration_in_months" integer unsigned NULL CHECK ("duration_in_months" >= 0), "max_redemptions" integer unsigned NULL CHECK ("max_redemptions" >= 0), "percent_off" decimal NULL, "redeem_by" datetime NULL, "times_redeemed" integer unsigned NOT NULL CHECK ("times_redeemed" >= 0), "name" text NOT NULL, "djstripe_owner_account_id" varchar(255) NULL REFERENCES "djstripe_account" ("id") DEFERRABLE INITIALLY DEFERRED, "applies_to" text NULL CHECK ((JSON_VALID("applies_to") OR "applies_to" IS NULL)));

-- Data exporting was unselected.

-- Dumping structure for table db.djstripe_customer
CREATE TABLE IF NOT EXISTS "djstripe_customer" ("djstripe_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "id" varchar(255) NOT NULL UNIQUE, "livemode" bool NULL, "created" datetime NULL, "metadata" text NULL CHECK ((JSON_VALID("metadata") OR "metadata" IS NULL)), "description" text NULL, "djstripe_created" datetime NOT NULL, "djstripe_updated" datetime NOT NULL, "currency" varchar(3) NOT NULL, "delinquent" bool NULL, "coupon_start" datetime NULL, "coupon_end" datetime NULL, "email" text NOT NULL, "shipping" text NULL CHECK ((JSON_VALID("shipping") OR "shipping" IS NULL)), "date_purged" datetime NULL, "coupon_id" bigint NULL REFERENCES "djstripe_coupon" ("djstripe_id") DEFERRABLE INITIALLY DEFERRED, "default_source_id" varchar(255) NULL REFERENCES "djstripe_djstripepaymentmethod" ("id") DEFERRABLE INITIALLY DEFERRED, "subscriber_id" bigint NULL REFERENCES "core_users" ("id") DEFERRABLE INITIALLY DEFERRED, "address" text NULL CHECK ((JSON_VALID("address") OR "address" IS NULL)), "invoice_prefix" varchar(255) NOT NULL, "invoice_settings" text NULL CHECK ((JSON_VALID("invoice_settings") OR "invoice_settings" IS NULL)), "name" text NOT NULL, "phone" text NOT NULL, "preferred_locales" text NULL CHECK ((JSON_VALID("preferred_locales") OR "preferred_locales" IS NULL)), "tax_exempt" varchar(7) NOT NULL, "default_payment_method_id" varchar(255) NULL REFERENCES "djstripe_paymentmethod" ("id") DEFERRABLE INITIALLY DEFERRED, "djstripe_owner_account_id" varchar(255) NULL REFERENCES "djstripe_account" ("id") DEFERRABLE INITIALLY DEFERRED, "deleted" bool NULL, "balance" bigint NULL);

-- Data exporting was unselected.

-- Dumping structure for table db.djstripe_dispute
CREATE TABLE IF NOT EXISTS "djstripe_dispute" ("djstripe_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "id" varchar(255) NOT NULL UNIQUE, "livemode" bool NULL, "created" datetime NULL, "metadata" text NULL CHECK ((JSON_VALID("metadata") OR "metadata" IS NULL)), "description" text NULL, "djstripe_created" datetime NOT NULL, "djstripe_updated" datetime NOT NULL, "amount" bigint NOT NULL, "currency" varchar(3) NOT NULL, "evidence" text NOT NULL CHECK ((JSON_VALID("evidence") OR "evidence" IS NULL)), "evidence_details" text NOT NULL CHECK ((JSON_VALID("evidence_details") OR "evidence_details" IS NULL)), "is_charge_refundable" bool NOT NULL, "reason" varchar(25) NOT NULL, "status" varchar(22) NOT NULL, "djstripe_owner_account_id" varchar(255) NULL REFERENCES "djstripe_account" ("id") DEFERRABLE INITIALLY DEFERRED, "balance_transaction_id" varchar(255) NULL REFERENCES "djstripe_balancetransaction" ("id") DEFERRABLE INITIALLY DEFERRED, "charge_id" varchar(255) NULL REFERENCES "djstripe_charge" ("id") DEFERRABLE INITIALLY DEFERRED, "payment_intent_id" varchar(255) NULL REFERENCES "djstripe_paymentintent" ("id") DEFERRABLE INITIALLY DEFERRED, "balance_transactions" text NOT NULL CHECK ((JSON_VALID("balance_transactions") OR "balance_transactions" IS NULL)));

-- Data exporting was unselected.

-- Dumping structure for table db.djstripe_djstripeinvoicedefaulttaxrate
CREATE TABLE IF NOT EXISTS "djstripe_djstripeinvoicedefaulttaxrate" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "invoice_id" bigint NOT NULL REFERENCES "djstripe_invoice" ("djstripe_id") DEFERRABLE INITIALLY DEFERRED, "taxrate_id" bigint NOT NULL REFERENCES "djstripe_taxrate" ("djstripe_id") DEFERRABLE INITIALLY DEFERRED);

-- Data exporting was unselected.

-- Dumping structure for table db.djstripe_djstripeinvoiceitemtaxrate
CREATE TABLE IF NOT EXISTS "djstripe_djstripeinvoiceitemtaxrate" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "invoiceitem_id" bigint NOT NULL REFERENCES "djstripe_invoiceitem" ("djstripe_id") DEFERRABLE INITIALLY DEFERRED, "taxrate_id" bigint NOT NULL REFERENCES "djstripe_taxrate" ("djstripe_id") DEFERRABLE INITIALLY DEFERRED);

-- Data exporting was unselected.

-- Dumping structure for table db.djstripe_djstripeinvoicetotaltaxamount
CREATE TABLE IF NOT EXISTS "djstripe_djstripeinvoicetotaltaxamount" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "amount" bigint NOT NULL, "inclusive" bool NOT NULL, "invoice_id" varchar(255) NOT NULL REFERENCES "djstripe_invoice" ("id") DEFERRABLE INITIALLY DEFERRED, "tax_rate_id" varchar(255) NOT NULL REFERENCES "djstripe_taxrate" ("id") DEFERRABLE INITIALLY DEFERRED);

-- Data exporting was unselected.

-- Dumping structure for table db.djstripe_djstripepaymentmethod
CREATE TABLE IF NOT EXISTS "djstripe_djstripepaymentmethod" ("id" varchar(255) NOT NULL PRIMARY KEY, "type" varchar(50) NOT NULL);

-- Data exporting was unselected.

-- Dumping structure for table db.djstripe_djstripesubscriptiondefaulttaxrate
CREATE TABLE IF NOT EXISTS "djstripe_djstripesubscriptiondefaulttaxrate" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "subscription_id" bigint NOT NULL REFERENCES "djstripe_subscription" ("djstripe_id") DEFERRABLE INITIALLY DEFERRED, "taxrate_id" bigint NOT NULL REFERENCES "djstripe_taxrate" ("djstripe_id") DEFERRABLE INITIALLY DEFERRED);

-- Data exporting was unselected.

-- Dumping structure for table db.djstripe_djstripesubscriptionitemtaxrate
CREATE TABLE IF NOT EXISTS "djstripe_djstripesubscriptionitemtaxrate" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "subscriptionitem_id" bigint NOT NULL REFERENCES "djstripe_subscriptionitem" ("djstripe_id") DEFERRABLE INITIALLY DEFERRED, "taxrate_id" bigint NOT NULL REFERENCES "djstripe_taxrate" ("djstripe_id") DEFERRABLE INITIALLY DEFERRED);

-- Data exporting was unselected.

-- Dumping structure for table db.djstripe_djstripeupcominginvoicetotaltaxamount
CREATE TABLE IF NOT EXISTS "djstripe_djstripeupcominginvoicetotaltaxamount" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "amount" bigint NOT NULL, "inclusive" bool NOT NULL, "invoice_id" bigint NOT NULL REFERENCES "djstripe_upcominginvoice" ("djstripe_id") DEFERRABLE INITIALLY DEFERRED, "tax_rate_id" varchar(255) NOT NULL REFERENCES "djstripe_taxrate" ("id") DEFERRABLE INITIALLY DEFERRED);

-- Data exporting was unselected.

-- Dumping structure for table db.djstripe_event
CREATE TABLE IF NOT EXISTS "djstripe_event" ("djstripe_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "id" varchar(255) NOT NULL UNIQUE, "livemode" bool NULL, "created" datetime NULL, "metadata" text NULL CHECK ((JSON_VALID("metadata") OR "metadata" IS NULL)), "description" text NULL, "djstripe_created" datetime NOT NULL, "djstripe_updated" datetime NOT NULL, "data" text NOT NULL CHECK ((JSON_VALID("data") OR "data" IS NULL)), "request_id" varchar(50) NOT NULL, "idempotency_key" text NOT NULL, "type" varchar(250) NOT NULL, "djstripe_owner_account_id" varchar(255) NULL REFERENCES "djstripe_account" ("id") DEFERRABLE INITIALLY DEFERRED, "api_version" varchar(64) NOT NULL);

-- Data exporting was unselected.

-- Dumping structure for table db.djstripe_file
CREATE TABLE IF NOT EXISTS "djstripe_file" ("djstripe_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "id" varchar(255) NOT NULL UNIQUE, "livemode" bool NULL, "created" datetime NULL, "metadata" text NULL CHECK ((JSON_VALID("metadata") OR "metadata" IS NULL)), "description" text NULL, "djstripe_created" datetime NOT NULL, "djstripe_updated" datetime NOT NULL, "filename" varchar(255) NOT NULL, "purpose" varchar(35) NOT NULL, "size" integer NOT NULL, "type" varchar(4) NOT NULL, "url" varchar(200) NOT NULL, "djstripe_owner_account_id" varchar(255) NULL REFERENCES "djstripe_account" ("id") DEFERRABLE INITIALLY DEFERRED);

-- Data exporting was unselected.

-- Dumping structure for table db.djstripe_filelink
CREATE TABLE IF NOT EXISTS "djstripe_filelink" ("djstripe_created" datetime NOT NULL, "djstripe_updated" datetime NOT NULL, "djstripe_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "id" varchar(255) NOT NULL UNIQUE, "livemode" bool NULL, "created" datetime NULL, "metadata" text NULL CHECK ((JSON_VALID("metadata") OR "metadata" IS NULL)), "description" text NULL, "expires_at" datetime NULL, "url" varchar(200) NOT NULL, "djstripe_owner_account_id" varchar(255) NULL REFERENCES "djstripe_account" ("id") DEFERRABLE INITIALLY DEFERRED, "file_id" varchar(255) NOT NULL REFERENCES "djstripe_file" ("id") DEFERRABLE INITIALLY DEFERRED);

-- Data exporting was unselected.

-- Dumping structure for table db.djstripe_idempotencykey
CREATE TABLE IF NOT EXISTS "djstripe_idempotencykey" ("uuid" char(32) NOT NULL PRIMARY KEY, "action" varchar(100) NOT NULL, "livemode" bool NOT NULL, "created" datetime NOT NULL);

-- Data exporting was unselected.

-- Dumping structure for table db.djstripe_invoice
CREATE TABLE IF NOT EXISTS "djstripe_invoice" ("djstripe_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "id" varchar(255) NOT NULL UNIQUE, "livemode" bool NULL, "created" datetime NULL, "metadata" text NULL CHECK ((JSON_VALID("metadata") OR "metadata" IS NULL)), "description" text NULL, "djstripe_created" datetime NOT NULL, "djstripe_updated" datetime NOT NULL, "amount_due" decimal NOT NULL, "amount_paid" decimal NULL, "amount_remaining" decimal NULL, "application_fee_amount" decimal NULL, "attempt_count" integer NOT NULL, "attempted" bool NOT NULL, "collection_method" varchar(20) NULL, "currency" varchar(3) NOT NULL, "due_date" datetime NULL, "ending_balance" bigint NULL, "hosted_invoice_url" text NOT NULL, "invoice_pdf" text NOT NULL, "next_payment_attempt" datetime NULL, "number" varchar(64) NOT NULL, "paid" bool NOT NULL, "period_end" datetime NOT NULL, "period_start" datetime NOT NULL, "receipt_number" varchar(64) NULL, "starting_balance" bigint NOT NULL, "statement_descriptor" varchar(22) NOT NULL, "subscription_proration_date" datetime NULL, "subtotal" decimal NOT NULL, "tax" decimal NULL, "tax_percent" decimal NULL, "total" decimal NOT NULL, "webhooks_delivered_at" datetime NULL, "charge_id" bigint NULL UNIQUE REFERENCES "djstripe_charge" ("djstripe_id") DEFERRABLE INITIALLY DEFERRED, "customer_id" varchar(255) NOT NULL REFERENCES "djstripe_customer" ("id") DEFERRABLE INITIALLY DEFERRED, "subscription_id" varchar(255) NULL REFERENCES "djstripe_subscription" ("id") DEFERRABLE INITIALLY DEFERRED, "auto_advance" bool NULL, "status_transitions" text NULL CHECK ((JSON_VALID("status_transitions") OR "status_transitions" IS NULL)), "account_country" varchar(2) NOT NULL, "account_name" text NOT NULL, "customer_address" text NULL CHECK ((JSON_VALID("customer_address") OR "customer_address" IS NULL)), "customer_email" text NOT NULL, "customer_name" text NOT NULL, "customer_phone" text NOT NULL, "customer_shipping" text NULL CHECK ((JSON_VALID("customer_shipping") OR "customer_shipping" IS NULL)), "customer_tax_exempt" varchar(7) NOT NULL, "footer" text NOT NULL, "post_payment_credit_notes_amount" bigint NULL, "pre_payment_credit_notes_amount" bigint NULL, "threshold_reason" text NULL CHECK ((JSON_VALID("threshold_reason") OR "threshold_reason" IS NULL)), "status" varchar(13) NOT NULL, "discount" text NULL CHECK ((JSON_VALID("discount") OR "discount" IS NULL)), "payment_intent_id" bigint NULL UNIQUE REFERENCES "djstripe_paymentintent" ("djstripe_id") DEFERRABLE INITIALLY DEFERRED, "default_payment_method_id" varchar(255) NULL REFERENCES "djstripe_paymentmethod" ("id") DEFERRABLE INITIALLY DEFERRED, "default_source_id" varchar(255) NULL REFERENCES "djstripe_djstripepaymentmethod" ("id") DEFERRABLE INITIALLY DEFERRED, "djstripe_owner_account_id" varchar(255) NULL REFERENCES "djstripe_account" ("id") DEFERRABLE INITIALLY DEFERRED, "billing_reason" varchar(38) NOT NULL);

-- Data exporting was unselected.

-- Dumping structure for table db.djstripe_invoiceitem
CREATE TABLE IF NOT EXISTS "djstripe_invoiceitem" ("djstripe_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "id" varchar(255) NOT NULL UNIQUE, "livemode" bool NULL, "created" datetime NULL, "metadata" text NULL CHECK ((JSON_VALID("metadata") OR "metadata" IS NULL)), "description" text NULL, "djstripe_created" datetime NOT NULL, "djstripe_updated" datetime NOT NULL, "amount" decimal NOT NULL, "currency" varchar(3) NOT NULL, "date" datetime NOT NULL, "discountable" bool NOT NULL, "period" text NOT NULL CHECK ((JSON_VALID("period") OR "period" IS NULL)), "period_end" datetime NOT NULL, "period_start" datetime NOT NULL, "proration" bool NOT NULL, "quantity" integer NULL, "customer_id" varchar(255) NOT NULL REFERENCES "djstripe_customer" ("id") DEFERRABLE INITIALLY DEFERRED, "invoice_id" varchar(255) NULL REFERENCES "djstripe_invoice" ("id") DEFERRABLE INITIALLY DEFERRED, "plan_id" bigint NULL REFERENCES "djstripe_plan" ("djstripe_id") DEFERRABLE INITIALLY DEFERRED, "subscription_id" varchar(255) NULL REFERENCES "djstripe_subscription" ("id") DEFERRABLE INITIALLY DEFERRED, "djstripe_owner_account_id" varchar(255) NULL REFERENCES "djstripe_account" ("id") DEFERRABLE INITIALLY DEFERRED, "unit_amount" bigint NULL, "unit_amount_decimal" decimal NULL, "price_id" bigint NULL REFERENCES "djstripe_price" ("djstripe_id") DEFERRABLE INITIALLY DEFERRED);

-- Data exporting was unselected.

-- Dumping structure for table db.djstripe_mandate
CREATE TABLE IF NOT EXISTS "djstripe_mandate" ("djstripe_created" datetime NOT NULL, "djstripe_updated" datetime NOT NULL, "djstripe_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "id" varchar(255) NOT NULL UNIQUE, "livemode" bool NULL, "created" datetime NULL, "metadata" text NULL CHECK ((JSON_VALID("metadata") OR "metadata" IS NULL)), "description" text NULL, "customer_acceptance" text NOT NULL CHECK ((JSON_VALID("customer_acceptance") OR "customer_acceptance" IS NULL)), "payment_method_details" text NOT NULL CHECK ((JSON_VALID("payment_method_details") OR "payment_method_details" IS NULL)), "status" varchar(8) NOT NULL, "type" varchar(10) NOT NULL, "multi_use" text NULL CHECK ((JSON_VALID("multi_use") OR "multi_use" IS NULL)), "single_use" text NULL CHECK ((JSON_VALID("single_use") OR "single_use" IS NULL)), "djstripe_owner_account_id" varchar(255) NULL REFERENCES "djstripe_account" ("id") DEFERRABLE INITIALLY DEFERRED, "payment_method_id" varchar(255) NOT NULL REFERENCES "djstripe_paymentmethod" ("id") DEFERRABLE INITIALLY DEFERRED);

-- Data exporting was unselected.

-- Dumping structure for table db.djstripe_order
CREATE TABLE IF NOT EXISTS "djstripe_order" ("djstripe_created" datetime NOT NULL, "djstripe_updated" datetime NOT NULL, "djstripe_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "id" varchar(255) NOT NULL UNIQUE, "livemode" bool NULL, "created" datetime NULL, "metadata" text NULL CHECK ((JSON_VALID("metadata") OR "metadata" IS NULL)), "description" text NULL, "amount_subtotal" bigint NOT NULL, "amount_total" bigint NOT NULL, "application" varchar(255) NOT NULL, "automatic_tax" text NOT NULL CHECK ((JSON_VALID("automatic_tax") OR "automatic_tax" IS NULL)), "billing_details" text NULL CHECK ((JSON_VALID("billing_details") OR "billing_details" IS NULL)), "client_secret" text NOT NULL, "currency" varchar(3) NOT NULL, "discounts" text NULL CHECK ((JSON_VALID("discounts") OR "discounts" IS NULL)), "ip_address" char(39) NULL, "line_items" text NOT NULL CHECK ((JSON_VALID("line_items") OR "line_items" IS NULL)), "payment" text NOT NULL CHECK ((JSON_VALID("payment") OR "payment" IS NULL)), "shipping_cost" text NULL CHECK ((JSON_VALID("shipping_cost") OR "shipping_cost" IS NULL)), "shipping_details" text NULL CHECK ((JSON_VALID("shipping_details") OR "shipping_details" IS NULL)), "status" varchar(10) NOT NULL, "tax_details" text NULL CHECK ((JSON_VALID("tax_details") OR "tax_details" IS NULL)), "total_details" text NOT NULL CHECK ((JSON_VALID("total_details") OR "total_details" IS NULL)), "customer_id" varchar(255) NULL REFERENCES "djstripe_customer" ("id") DEFERRABLE INITIALLY DEFERRED, "djstripe_owner_account_id" varchar(255) NULL REFERENCES "djstripe_account" ("id") DEFERRABLE INITIALLY DEFERRED, "payment_intent_id" varchar(255) NULL REFERENCES "djstripe_paymentintent" ("id") DEFERRABLE INITIALLY DEFERRED);

-- Data exporting was unselected.

-- Dumping structure for table db.djstripe_paymentintent
CREATE TABLE IF NOT EXISTS "djstripe_paymentintent" ("djstripe_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "id" varchar(255) NOT NULL UNIQUE, "livemode" bool NULL, "created" datetime NULL, "metadata" text NULL CHECK ((JSON_VALID("metadata") OR "metadata" IS NULL)), "djstripe_created" datetime NOT NULL, "djstripe_updated" datetime NOT NULL, "amount" bigint NOT NULL, "amount_capturable" bigint NOT NULL, "amount_received" bigint NOT NULL, "canceled_at" datetime NULL, "cancellation_reason" varchar(21) NOT NULL, "capture_method" varchar(9) NOT NULL, "client_secret" text NOT NULL, "confirmation_method" varchar(9) NOT NULL, "currency" varchar(3) NOT NULL, "description" text NOT NULL, "last_payment_error" text NULL CHECK ((JSON_VALID("last_payment_error") OR "last_payment_error" IS NULL)), "next_action" text NULL CHECK ((JSON_VALID("next_action") OR "next_action" IS NULL)), "payment_method_types" text NOT NULL CHECK ((JSON_VALID("payment_method_types") OR "payment_method_types" IS NULL)), "receipt_email" varchar(255) NOT NULL, "setup_future_usage" varchar(11) NULL, "shipping" text NULL CHECK ((JSON_VALID("shipping") OR "shipping" IS NULL)), "statement_descriptor" varchar(22) NOT NULL, "status" varchar(23) NOT NULL, "transfer_data" text NULL CHECK ((JSON_VALID("transfer_data") OR "transfer_data" IS NULL)), "transfer_group" varchar(255) NOT NULL, "customer_id" varchar(255) NULL REFERENCES "djstripe_customer" ("id") DEFERRABLE INITIALLY DEFERRED, "on_behalf_of_id" varchar(255) NULL REFERENCES "djstripe_account" ("id") DEFERRABLE INITIALLY DEFERRED, "payment_method_id" varchar(255) NULL REFERENCES "djstripe_paymentmethod" ("id") DEFERRABLE INITIALLY DEFERRED, "djstripe_owner_account_id" varchar(255) NULL REFERENCES "djstripe_account" ("id") DEFERRABLE INITIALLY DEFERRED);

-- Data exporting was unselected.

-- Dumping structure for table db.djstripe_paymentmethod
CREATE TABLE IF NOT EXISTS "djstripe_paymentmethod" ("djstripe_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "id" varchar(255) NOT NULL UNIQUE, "livemode" bool NULL, "created" datetime NULL, "metadata" text NULL CHECK ((JSON_VALID("metadata") OR "metadata" IS NULL)), "djstripe_created" datetime NOT NULL, "djstripe_updated" datetime NOT NULL, "billing_details" text NOT NULL CHECK ((JSON_VALID("billing_details") OR "billing_details" IS NULL)), "card" text NULL CHECK ((JSON_VALID("card") OR "card" IS NULL)), "card_present" text NULL CHECK ((JSON_VALID("card_present") OR "card_present" IS NULL)), "alipay" text NULL CHECK ((JSON_VALID("alipay") OR "alipay" IS NULL)), "au_becs_debit" text NULL CHECK ((JSON_VALID("au_becs_debit") OR "au_becs_debit" IS NULL)), "bacs_debit" text NULL CHECK ((JSON_VALID("bacs_debit") OR "bacs_debit" IS NULL)), "bancontact" text NULL CHECK ((JSON_VALID("bancontact") OR "bancontact" IS NULL)), "eps" text NULL CHECK ((JSON_VALID("eps") OR "eps" IS NULL)), "fpx" text NULL CHECK ((JSON_VALID("fpx") OR "fpx" IS NULL)), "giropay" text NULL CHECK ((JSON_VALID("giropay") OR "giropay" IS NULL)), "ideal" text NULL CHECK ((JSON_VALID("ideal") OR "ideal" IS NULL)), "interac_present" text NULL CHECK ((JSON_VALID("interac_present") OR "interac_present" IS NULL)), "oxxo" text NULL CHECK ((JSON_VALID("oxxo") OR "oxxo" IS NULL)), "p24" text NULL CHECK ((JSON_VALID("p24") OR "p24" IS NULL)), "sepa_debit" text NULL CHECK ((JSON_VALID("sepa_debit") OR "sepa_debit" IS NULL)), "sofort" text NULL CHECK ((JSON_VALID("sofort") OR "sofort" IS NULL)), "customer_id" varchar(255) NULL REFERENCES "djstripe_customer" ("id") DEFERRABLE INITIALLY DEFERRED, "djstripe_owner_account_id" varchar(255) NULL REFERENCES "djstripe_account" ("id") DEFERRABLE INITIALLY DEFERRED, "type" varchar(17) NOT NULL, "acss_debit" text NULL CHECK ((JSON_VALID("acss_debit") OR "acss_debit" IS NULL)), "afterpay_clearpay" text NULL CHECK ((JSON_VALID("afterpay_clearpay") OR "afterpay_clearpay" IS NULL)), "boleto" text NULL CHECK ((JSON_VALID("boleto") OR "boleto" IS NULL)), "grabpay" text NULL CHECK ((JSON_VALID("grabpay") OR "grabpay" IS NULL)), "wechat_pay" text NULL CHECK ((JSON_VALID("wechat_pay") OR "wechat_pay" IS NULL)));

-- Data exporting was unselected.

-- Dumping structure for table db.djstripe_payout
CREATE TABLE IF NOT EXISTS "djstripe_payout" ("djstripe_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "id" varchar(255) NOT NULL UNIQUE, "livemode" bool NULL, "created" datetime NULL, "metadata" text NULL CHECK ((JSON_VALID("metadata") OR "metadata" IS NULL)), "description" text NULL, "djstripe_created" datetime NOT NULL, "djstripe_updated" datetime NOT NULL, "amount" decimal NOT NULL, "arrival_date" datetime NOT NULL, "currency" varchar(3) NOT NULL, "failure_message" text NOT NULL, "method" varchar(8) NOT NULL, "statement_descriptor" varchar(255) NOT NULL, "status" varchar(10) NOT NULL, "type" varchar(12) NOT NULL, "destination_id" varchar(255) NULL REFERENCES "djstripe_bankaccount" ("id") DEFERRABLE INITIALLY DEFERRED, "balance_transaction_id" varchar(255) NULL REFERENCES "djstripe_balancetransaction" ("id") DEFERRABLE INITIALLY DEFERRED, "failure_balance_transaction_id" varchar(255) NULL REFERENCES "djstripe_balancetransaction" ("id") DEFERRABLE INITIALLY DEFERRED, "djstripe_owner_account_id" varchar(255) NULL REFERENCES "djstripe_account" ("id") DEFERRABLE INITIALLY DEFERRED, "automatic" bool NOT NULL, "source_type" varchar(12) NOT NULL, "failure_code" varchar(32) NOT NULL);

-- Data exporting was unselected.

-- Dumping structure for table db.djstripe_plan
CREATE TABLE IF NOT EXISTS "djstripe_plan" ("djstripe_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "id" varchar(255) NOT NULL UNIQUE, "livemode" bool NULL, "created" datetime NULL, "metadata" text NULL CHECK ((JSON_VALID("metadata") OR "metadata" IS NULL)), "description" text NULL, "djstripe_created" datetime NOT NULL, "djstripe_updated" datetime NOT NULL, "active" bool NOT NULL, "aggregate_usage" varchar(18) NOT NULL, "amount" decimal NULL, "amount_decimal" decimal NULL, "billing_scheme" varchar(8) NOT NULL, "currency" varchar(3) NOT NULL, "interval" varchar(5) NOT NULL, "interval_count" integer unsigned NULL CHECK ("interval_count" >= 0), "nickname" text NOT NULL, "tiers" text NULL CHECK ((JSON_VALID("tiers") OR "tiers" IS NULL)), "tiers_mode" varchar(9) NULL, "transform_usage" text NULL CHECK ((JSON_VALID("transform_usage") OR "transform_usage" IS NULL)), "trial_period_days" integer NULL, "usage_type" varchar(8) NOT NULL, "product_id" varchar(255) NULL REFERENCES "djstripe_product" ("id") DEFERRABLE INITIALLY DEFERRED, "djstripe_owner_account_id" varchar(255) NULL REFERENCES "djstripe_account" ("id") DEFERRABLE INITIALLY DEFERRED);

-- Data exporting was unselected.

-- Dumping structure for table db.djstripe_price
CREATE TABLE IF NOT EXISTS "djstripe_price" ("djstripe_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "id" varchar(255) NOT NULL UNIQUE, "livemode" bool NULL, "created" datetime NULL, "metadata" text NULL CHECK ((JSON_VALID("metadata") OR "metadata" IS NULL)), "description" text NULL, "djstripe_created" datetime NOT NULL, "djstripe_updated" datetime NOT NULL, "active" bool NOT NULL, "currency" varchar(3) NOT NULL, "nickname" varchar(250) NOT NULL, "recurring" text NULL CHECK ((JSON_VALID("recurring") OR "recurring" IS NULL)), "type" varchar(9) NOT NULL, "unit_amount" bigint NULL, "unit_amount_decimal" decimal NULL, "billing_scheme" varchar(8) NOT NULL, "tiers" text NULL CHECK ((JSON_VALID("tiers") OR "tiers" IS NULL)), "tiers_mode" varchar(9) NULL, "djstripe_owner_account_id" varchar(255) NULL REFERENCES "djstripe_account" ("id") DEFERRABLE INITIALLY DEFERRED, "product_id" varchar(255) NOT NULL REFERENCES "djstripe_product" ("id") DEFERRABLE INITIALLY DEFERRED, "lookup_key" varchar(250) NULL, "transform_quantity" text NULL CHECK ((JSON_VALID("transform_quantity") OR "transform_quantity" IS NULL)));

-- Data exporting was unselected.

-- Dumping structure for table db.djstripe_product
CREATE TABLE IF NOT EXISTS "djstripe_product" ("djstripe_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "id" varchar(255) NOT NULL UNIQUE, "livemode" bool NULL, "created" datetime NULL, "metadata" text NULL CHECK ((JSON_VALID("metadata") OR "metadata" IS NULL)), "description" text NULL, "djstripe_created" datetime NOT NULL, "djstripe_updated" datetime NOT NULL, "name" text NOT NULL, "type" varchar(7) NOT NULL, "active" bool NULL, "attributes" text NULL CHECK ((JSON_VALID("attributes") OR "attributes" IS NULL)), "caption" text NOT NULL, "deactivate_on" text NULL CHECK ((JSON_VALID("deactivate_on") OR "deactivate_on" IS NULL)), "images" text NULL CHECK ((JSON_VALID("images") OR "images" IS NULL)), "package_dimensions" text NULL CHECK ((JSON_VALID("package_dimensions") OR "package_dimensions" IS NULL)), "shippable" bool NULL, "url" varchar(799) NULL, "statement_descriptor" varchar(22) NOT NULL, "unit_label" varchar(12) NOT NULL, "djstripe_owner_account_id" varchar(255) NULL REFERENCES "djstripe_account" ("id") DEFERRABLE INITIALLY DEFERRED);

-- Data exporting was unselected.

-- Dumping structure for table db.djstripe_refund
CREATE TABLE IF NOT EXISTS "djstripe_refund" ("djstripe_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "id" varchar(255) NOT NULL UNIQUE, "livemode" bool NULL, "created" datetime NULL, "metadata" text NULL CHECK ((JSON_VALID("metadata") OR "metadata" IS NULL)), "description" text NULL, "djstripe_created" datetime NOT NULL, "djstripe_updated" datetime NOT NULL, "amount" bigint NOT NULL, "currency" varchar(3) NOT NULL, "failure_reason" varchar(24) NOT NULL, "reason" varchar(25) NOT NULL, "receipt_number" varchar(9) NOT NULL, "status" varchar(9) NOT NULL, "charge_id" varchar(255) NOT NULL REFERENCES "djstripe_charge" ("id") DEFERRABLE INITIALLY DEFERRED, "balance_transaction_id" varchar(255) NULL REFERENCES "djstripe_balancetransaction" ("id") DEFERRABLE INITIALLY DEFERRED, "failure_balance_transaction_id" varchar(255) NULL REFERENCES "djstripe_balancetransaction" ("id") DEFERRABLE INITIALLY DEFERRED, "djstripe_owner_account_id" varchar(255) NULL REFERENCES "djstripe_account" ("id") DEFERRABLE INITIALLY DEFERRED);

-- Data exporting was unselected.

-- Dumping structure for table db.djstripe_scheduledqueryrun
CREATE TABLE IF NOT EXISTS "djstripe_scheduledqueryrun" ("djstripe_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "id" varchar(255) NOT NULL UNIQUE, "livemode" bool NULL, "created" datetime NULL, "metadata" text NULL CHECK ((JSON_VALID("metadata") OR "metadata" IS NULL)), "description" text NULL, "djstripe_created" datetime NOT NULL, "djstripe_updated" datetime NOT NULL, "data_load_time" datetime NOT NULL, "error" text NULL CHECK ((JSON_VALID("error") OR "error" IS NULL)), "result_available_until" datetime NOT NULL, "sql" text NOT NULL, "status" varchar(9) NOT NULL, "title" text NOT NULL, "djstripe_owner_account_id" varchar(255) NULL REFERENCES "djstripe_account" ("id") DEFERRABLE INITIALLY DEFERRED, "file_id" varchar(255) NULL REFERENCES "djstripe_file" ("id") DEFERRABLE INITIALLY DEFERRED);

-- Data exporting was unselected.

-- Dumping structure for table db.djstripe_session
CREATE TABLE IF NOT EXISTS "djstripe_session" ("djstripe_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "id" varchar(255) NOT NULL UNIQUE, "livemode" bool NULL, "created" datetime NULL, "metadata" text NULL CHECK ((JSON_VALID("metadata") OR "metadata" IS NULL)), "description" text NULL, "djstripe_created" datetime NOT NULL, "djstripe_updated" datetime NOT NULL, "billing_address_collection" varchar(8) NOT NULL, "cancel_url" text NOT NULL, "client_reference_id" text NOT NULL, "customer_email" varchar(255) NOT NULL, "display_items" text NULL CHECK ((JSON_VALID("display_items") OR "display_items" IS NULL)), "locale" varchar(255) NOT NULL, "payment_method_types" text NOT NULL CHECK ((JSON_VALID("payment_method_types") OR "payment_method_types" IS NULL)), "submit_type" varchar(6) NOT NULL, "success_url" text NOT NULL, "customer_id" varchar(255) NULL REFERENCES "djstripe_customer" ("id") DEFERRABLE INITIALLY DEFERRED, "payment_intent_id" varchar(255) NULL REFERENCES "djstripe_paymentintent" ("id") DEFERRABLE INITIALLY DEFERRED, "subscription_id" varchar(255) NULL REFERENCES "djstripe_subscription" ("id") DEFERRABLE INITIALLY DEFERRED, "mode" varchar(12) NOT NULL, "djstripe_owner_account_id" varchar(255) NULL REFERENCES "djstripe_account" ("id") DEFERRABLE INITIALLY DEFERRED);

-- Data exporting was unselected.

-- Dumping structure for table db.djstripe_setupintent
CREATE TABLE IF NOT EXISTS "djstripe_setupintent" ("djstripe_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "id" varchar(255) NOT NULL UNIQUE, "livemode" bool NULL, "created" datetime NULL, "metadata" text NULL CHECK ((JSON_VALID("metadata") OR "metadata" IS NULL)), "description" text NULL, "djstripe_created" datetime NOT NULL, "djstripe_updated" datetime NOT NULL, "application" varchar(255) NOT NULL, "cancellation_reason" varchar(21) NOT NULL, "client_secret" text NOT NULL, "last_setup_error" text NULL CHECK ((JSON_VALID("last_setup_error") OR "last_setup_error" IS NULL)), "next_action" text NULL CHECK ((JSON_VALID("next_action") OR "next_action" IS NULL)), "payment_method_types" text NOT NULL CHECK ((JSON_VALID("payment_method_types") OR "payment_method_types" IS NULL)), "status" varchar(23) NOT NULL, "usage" varchar(11) NOT NULL, "customer_id" varchar(255) NULL REFERENCES "djstripe_customer" ("id") DEFERRABLE INITIALLY DEFERRED, "on_behalf_of_id" varchar(255) NULL REFERENCES "djstripe_account" ("id") DEFERRABLE INITIALLY DEFERRED, "payment_method_id" varchar(255) NULL REFERENCES "djstripe_paymentmethod" ("id") DEFERRABLE INITIALLY DEFERRED, "djstripe_owner_account_id" varchar(255) NULL REFERENCES "djstripe_account" ("id") DEFERRABLE INITIALLY DEFERRED);

-- Data exporting was unselected.

-- Dumping structure for table db.djstripe_shippingrate
CREATE TABLE IF NOT EXISTS "djstripe_shippingrate" ("djstripe_created" datetime NOT NULL, "djstripe_updated" datetime NOT NULL, "djstripe_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "id" varchar(255) NOT NULL UNIQUE, "livemode" bool NULL, "created" datetime NULL, "metadata" text NULL CHECK ((JSON_VALID("metadata") OR "metadata" IS NULL)), "active" bool NOT NULL, "display_name" varchar(50) NOT NULL, "fixed_amount" text NOT NULL CHECK ((JSON_VALID("fixed_amount") OR "fixed_amount" IS NULL)), "type" varchar(12) NOT NULL, "delivery_estimate" text NULL CHECK ((JSON_VALID("delivery_estimate") OR "delivery_estimate" IS NULL)), "tax_behavior" varchar(11) NOT NULL, "djstripe_owner_account_id" varchar(255) NULL REFERENCES "djstripe_account" ("id") DEFERRABLE INITIALLY DEFERRED, "tax_code_id" varchar(255) NULL REFERENCES "djstripe_taxcode" ("id") DEFERRABLE INITIALLY DEFERRED);

-- Data exporting was unselected.

-- Dumping structure for table db.djstripe_source
CREATE TABLE IF NOT EXISTS "djstripe_source" ("djstripe_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "id" varchar(255) NOT NULL UNIQUE, "livemode" bool NULL, "created" datetime NULL, "metadata" text NULL CHECK ((JSON_VALID("metadata") OR "metadata" IS NULL)), "description" text NULL, "djstripe_created" datetime NOT NULL, "djstripe_updated" datetime NOT NULL, "amount" decimal NULL, "client_secret" varchar(255) NOT NULL, "currency" varchar(3) NOT NULL, "flow" varchar(17) NOT NULL, "owner" text NOT NULL CHECK ((JSON_VALID("owner") OR "owner" IS NULL)), "statement_descriptor" varchar(255) NOT NULL, "status" varchar(10) NOT NULL, "type" varchar(20) NOT NULL, "usage" varchar(10) NOT NULL, "code_verification" text NULL CHECK ((JSON_VALID("code_verification") OR "code_verification" IS NULL)), "receiver" text NULL CHECK ((JSON_VALID("receiver") OR "receiver" IS NULL)), "redirect" text NULL CHECK ((JSON_VALID("redirect") OR "redirect" IS NULL)), "source_data" text NOT NULL CHECK ((JSON_VALID("source_data") OR "source_data" IS NULL)), "customer_id" varchar(255) NULL REFERENCES "djstripe_customer" ("id") DEFERRABLE INITIALLY DEFERRED, "djstripe_owner_account_id" varchar(255) NULL REFERENCES "djstripe_account" ("id") DEFERRABLE INITIALLY DEFERRED);

-- Data exporting was unselected.

-- Dumping structure for table db.djstripe_subscription
CREATE TABLE IF NOT EXISTS "djstripe_subscription" ("djstripe_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "id" varchar(255) NOT NULL UNIQUE, "livemode" bool NULL, "created" datetime NULL, "metadata" text NULL CHECK ((JSON_VALID("metadata") OR "metadata" IS NULL)), "description" text NULL, "djstripe_created" datetime NOT NULL, "djstripe_updated" datetime NOT NULL, "application_fee_percent" decimal NULL, "collection_method" varchar(20) NOT NULL, "billing_cycle_anchor" datetime NULL, "cancel_at_period_end" bool NOT NULL, "canceled_at" datetime NULL, "current_period_end" datetime NOT NULL, "current_period_start" datetime NOT NULL, "days_until_due" integer NULL, "discount" text NULL CHECK ((JSON_VALID("discount") OR "discount" IS NULL)), "ended_at" datetime NULL, "next_pending_invoice_item_invoice" datetime NULL, "pending_invoice_item_interval" text NULL CHECK ((JSON_VALID("pending_invoice_item_interval") OR "pending_invoice_item_interval" IS NULL)), "pending_update" text NULL CHECK ((JSON_VALID("pending_update") OR "pending_update" IS NULL)), "quantity" integer NULL, "start_date" datetime NULL, "status" varchar(18) NOT NULL, "trial_end" datetime NULL, "trial_start" datetime NULL, "customer_id" varchar(255) NOT NULL REFERENCES "djstripe_customer" ("id") DEFERRABLE INITIALLY DEFERRED, "plan_id" bigint NULL REFERENCES "djstripe_plan" ("djstripe_id") DEFERRABLE INITIALLY DEFERRED, "billing_thresholds" text NULL CHECK ((JSON_VALID("billing_thresholds") OR "billing_thresholds" IS NULL)), "cancel_at" datetime NULL, "pending_setup_intent_id" varchar(255) NULL REFERENCES "djstripe_setupintent" ("id") DEFERRABLE INITIALLY DEFERRED, "default_payment_method_id" varchar(255) NULL REFERENCES "djstripe_paymentmethod" ("id") DEFERRABLE INITIALLY DEFERRED, "default_source_id" varchar(255) NULL REFERENCES "djstripe_djstripepaymentmethod" ("id") DEFERRABLE INITIALLY DEFERRED, "djstripe_owner_account_id" varchar(255) NULL REFERENCES "djstripe_account" ("id") DEFERRABLE INITIALLY DEFERRED, "schedule_id" bigint NULL REFERENCES "djstripe_subscriptionschedule" ("djstripe_id") DEFERRABLE INITIALLY DEFERRED, "latest_invoice_id" varchar(255) NULL REFERENCES "djstripe_invoice" ("id") DEFERRABLE INITIALLY DEFERRED, "proration_behavior" varchar(17) NOT NULL, "proration_date" datetime NULL, "pause_collection" text NULL CHECK ((JSON_VALID("pause_collection") OR "pause_collection" IS NULL)));

-- Data exporting was unselected.

-- Dumping structure for table db.djstripe_subscriptionitem
CREATE TABLE IF NOT EXISTS "djstripe_subscriptionitem" ("djstripe_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "id" varchar(255) NOT NULL UNIQUE, "livemode" bool NULL, "created" datetime NULL, "metadata" text NULL CHECK ((JSON_VALID("metadata") OR "metadata" IS NULL)), "description" text NULL, "djstripe_created" datetime NOT NULL, "djstripe_updated" datetime NOT NULL, "quantity" integer unsigned NULL CHECK ("quantity" >= 0), "plan_id" bigint NOT NULL REFERENCES "djstripe_plan" ("djstripe_id") DEFERRABLE INITIALLY DEFERRED, "subscription_id" varchar(255) NOT NULL REFERENCES "djstripe_subscription" ("id") DEFERRABLE INITIALLY DEFERRED, "djstripe_owner_account_id" varchar(255) NULL REFERENCES "djstripe_account" ("id") DEFERRABLE INITIALLY DEFERRED, "billing_thresholds" text NULL CHECK ((JSON_VALID("billing_thresholds") OR "billing_thresholds" IS NULL)), "price_id" bigint NULL REFERENCES "djstripe_price" ("djstripe_id") DEFERRABLE INITIALLY DEFERRED, "proration_behavior" varchar(17) NOT NULL, "proration_date" datetime NULL);

-- Data exporting was unselected.

-- Dumping structure for table db.djstripe_subscriptionschedule
CREATE TABLE IF NOT EXISTS "djstripe_subscriptionschedule" ("djstripe_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "id" varchar(255) NOT NULL UNIQUE, "livemode" bool NULL, "created" datetime NULL, "metadata" text NULL CHECK ((JSON_VALID("metadata") OR "metadata" IS NULL)), "description" text NULL, "djstripe_created" datetime NOT NULL, "djstripe_updated" datetime NOT NULL, "canceled_at" datetime NULL, "completed_at" datetime NULL, "current_phase" text NULL CHECK ((JSON_VALID("current_phase") OR "current_phase" IS NULL)), "default_settings" text NULL CHECK ((JSON_VALID("default_settings") OR "default_settings" IS NULL)), "end_behavior" varchar(7) NOT NULL, "phases" text NULL CHECK ((JSON_VALID("phases") OR "phases" IS NULL)), "released_at" datetime NULL, "status" varchar(11) NOT NULL, "customer_id" bigint NOT NULL REFERENCES "djstripe_customer" ("djstripe_id") DEFERRABLE INITIALLY DEFERRED, "djstripe_owner_account_id" varchar(255) NULL REFERENCES "djstripe_account" ("id") DEFERRABLE INITIALLY DEFERRED, "released_subscription_id" bigint NULL REFERENCES "djstripe_subscription" ("djstripe_id") DEFERRABLE INITIALLY DEFERRED, "subscription_id" bigint NULL REFERENCES "djstripe_subscription" ("djstripe_id") DEFERRABLE INITIALLY DEFERRED);

-- Data exporting was unselected.

-- Dumping structure for table db.djstripe_taxcode
CREATE TABLE IF NOT EXISTS "djstripe_taxcode" ("djstripe_created" datetime NOT NULL, "djstripe_updated" datetime NOT NULL, "djstripe_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "id" varchar(255) NOT NULL UNIQUE, "livemode" bool NULL, "created" datetime NULL, "description" text NULL, "name" varchar(128) NOT NULL, "djstripe_owner_account_id" varchar(255) NULL REFERENCES "djstripe_account" ("id") DEFERRABLE INITIALLY DEFERRED);

-- Data exporting was unselected.

-- Dumping structure for table db.djstripe_taxid
CREATE TABLE IF NOT EXISTS "djstripe_taxid" ("djstripe_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "id" varchar(255) NOT NULL UNIQUE, "livemode" bool NULL, "created" datetime NULL, "djstripe_created" datetime NOT NULL, "djstripe_updated" datetime NOT NULL, "country" varchar(2) NOT NULL, "type" varchar(7) NOT NULL, "value" varchar(50) NOT NULL, "verification" text NOT NULL CHECK ((JSON_VALID("verification") OR "verification" IS NULL)), "customer_id" varchar(255) NOT NULL REFERENCES "djstripe_customer" ("id") DEFERRABLE INITIALLY DEFERRED, "djstripe_owner_account_id" varchar(255) NULL REFERENCES "djstripe_account" ("id") DEFERRABLE INITIALLY DEFERRED);

-- Data exporting was unselected.

-- Dumping structure for table db.djstripe_taxrate
CREATE TABLE IF NOT EXISTS "djstripe_taxrate" ("djstripe_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "id" varchar(255) NOT NULL UNIQUE, "livemode" bool NULL, "created" datetime NULL, "metadata" text NULL CHECK ((JSON_VALID("metadata") OR "metadata" IS NULL)), "description" text NULL, "djstripe_created" datetime NOT NULL, "djstripe_updated" datetime NOT NULL, "active" bool NOT NULL, "display_name" varchar(50) NOT NULL, "inclusive" bool NOT NULL, "jurisdiction" varchar(50) NOT NULL, "percentage" decimal NOT NULL, "djstripe_owner_account_id" varchar(255) NULL REFERENCES "djstripe_account" ("id") DEFERRABLE INITIALLY DEFERRED, "country" varchar(2) NOT NULL, "state" varchar(2) NOT NULL, "tax_type" varchar(50) NOT NULL);

-- Data exporting was unselected.

-- Dumping structure for table db.djstripe_transfer
CREATE TABLE IF NOT EXISTS "djstripe_transfer" ("djstripe_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "id" varchar(255) NOT NULL UNIQUE, "livemode" bool NULL, "created" datetime NULL, "metadata" text NULL CHECK ((JSON_VALID("metadata") OR "metadata" IS NULL)), "description" text NULL, "djstripe_created" datetime NOT NULL, "djstripe_updated" datetime NOT NULL, "amount" decimal NOT NULL, "amount_reversed" decimal NULL, "currency" varchar(3) NOT NULL, "destination_payment" varchar(255) NULL, "reversed" bool NOT NULL, "source_transaction" varchar(255) NULL, "source_type" varchar(16) NOT NULL, "transfer_group" varchar(255) NOT NULL, "balance_transaction_id" varchar(255) NULL REFERENCES "djstripe_balancetransaction" ("id") DEFERRABLE INITIALLY DEFERRED, "djstripe_owner_account_id" varchar(255) NULL REFERENCES "djstripe_account" ("id") DEFERRABLE INITIALLY DEFERRED, "destination" varchar(255) NULL);

-- Data exporting was unselected.

-- Dumping structure for table db.djstripe_transferreversal
CREATE TABLE IF NOT EXISTS "djstripe_transferreversal" ("djstripe_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "id" varchar(255) NOT NULL UNIQUE, "livemode" bool NULL, "created" datetime NULL, "metadata" text NULL CHECK ((JSON_VALID("metadata") OR "metadata" IS NULL)), "description" text NULL, "djstripe_created" datetime NOT NULL, "djstripe_updated" datetime NOT NULL, "amount" bigint NOT NULL, "currency" varchar(3) NOT NULL, "balance_transaction_id" varchar(255) NULL REFERENCES "djstripe_balancetransaction" ("id") DEFERRABLE INITIALLY DEFERRED, "transfer_id" varchar(255) NOT NULL REFERENCES "djstripe_transfer" ("id") DEFERRABLE INITIALLY DEFERRED, "djstripe_owner_account_id" varchar(255) NULL REFERENCES "djstripe_account" ("id") DEFERRABLE INITIALLY DEFERRED);

-- Data exporting was unselected.

-- Dumping structure for table db.djstripe_upcominginvoice
CREATE TABLE IF NOT EXISTS "djstripe_upcominginvoice" ("djstripe_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "livemode" bool NULL, "created" datetime NULL, "metadata" text NULL CHECK ((JSON_VALID("metadata") OR "metadata" IS NULL)), "description" text NULL, "djstripe_created" datetime NOT NULL, "djstripe_updated" datetime NOT NULL, "account_country" varchar(2) NOT NULL, "account_name" text NOT NULL, "amount_due" decimal NOT NULL, "amount_paid" decimal NULL, "amount_remaining" decimal NULL, "application_fee_amount" decimal NULL, "attempt_count" integer NOT NULL, "attempted" bool NOT NULL, "auto_advance" bool NULL, "collection_method" varchar(20) NULL, "currency" varchar(3) NOT NULL, "customer_address" text NULL CHECK ((JSON_VALID("customer_address") OR "customer_address" IS NULL)), "customer_email" text NOT NULL, "customer_name" text NOT NULL, "customer_phone" text NOT NULL, "customer_shipping" text NULL CHECK ((JSON_VALID("customer_shipping") OR "customer_shipping" IS NULL)), "customer_tax_exempt" varchar(7) NOT NULL, "due_date" datetime NULL, "ending_balance" bigint NULL, "footer" text NOT NULL, "hosted_invoice_url" text NOT NULL, "invoice_pdf" text NOT NULL, "next_payment_attempt" datetime NULL, "number" varchar(64) NOT NULL, "paid" bool NOT NULL, "period_end" datetime NOT NULL, "period_start" datetime NOT NULL, "post_payment_credit_notes_amount" bigint NULL, "pre_payment_credit_notes_amount" bigint NULL, "receipt_number" varchar(64) NULL, "starting_balance" bigint NOT NULL, "statement_descriptor" varchar(22) NOT NULL, "status_transitions" text NULL CHECK ((JSON_VALID("status_transitions") OR "status_transitions" IS NULL)), "subscription_proration_date" datetime NULL, "subtotal" decimal NOT NULL, "tax" decimal NULL, "tax_percent" decimal NULL, "threshold_reason" text NULL CHECK ((JSON_VALID("threshold_reason") OR "threshold_reason" IS NULL)), "total" decimal NOT NULL, "webhooks_delivered_at" datetime NULL, "charge_id" bigint NULL UNIQUE REFERENCES "djstripe_charge" ("djstripe_id") DEFERRABLE INITIALLY DEFERRED, "customer_id" varchar(255) NOT NULL REFERENCES "djstripe_customer" ("id") DEFERRABLE INITIALLY DEFERRED, "default_payment_method_id" varchar(255) NULL REFERENCES "djstripe_paymentmethod" ("id") DEFERRABLE INITIALLY DEFERRED, "payment_intent_id" bigint NULL UNIQUE REFERENCES "djstripe_paymentintent" ("djstripe_id") DEFERRABLE INITIALLY DEFERRED, "subscription_id" varchar(255) NULL REFERENCES "djstripe_subscription" ("id") DEFERRABLE INITIALLY DEFERRED, "status" varchar(13) NOT NULL, "default_source_id" varchar(255) NULL REFERENCES "djstripe_djstripepaymentmethod" ("id") DEFERRABLE INITIALLY DEFERRED, "discount" text NULL CHECK ((JSON_VALID("discount") OR "discount" IS NULL)), "djstripe_owner_account_id" varchar(255) NULL REFERENCES "djstripe_account" ("id") DEFERRABLE INITIALLY DEFERRED, "billing_reason" varchar(38) NOT NULL);

-- Data exporting was unselected.

-- Dumping structure for table db.djstripe_usagerecord
CREATE TABLE IF NOT EXISTS "djstripe_usagerecord" ("djstripe_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "id" varchar(255) NOT NULL UNIQUE, "livemode" bool NULL, "created" datetime NULL, "djstripe_created" datetime NOT NULL, "djstripe_updated" datetime NOT NULL, "quantity" integer unsigned NOT NULL CHECK ("quantity" >= 0), "subscription_item_id" varchar(255) NOT NULL REFERENCES "djstripe_subscriptionitem" ("id") DEFERRABLE INITIALLY DEFERRED, "djstripe_owner_account_id" varchar(255) NULL REFERENCES "djstripe_account" ("id") DEFERRABLE INITIALLY DEFERRED, "action" varchar(9) NOT NULL, "timestamp" datetime NULL);

-- Data exporting was unselected.

-- Dumping structure for table db.djstripe_usagerecordsummary
CREATE TABLE IF NOT EXISTS "djstripe_usagerecordsummary" ("djstripe_created" datetime NOT NULL, "djstripe_updated" datetime NOT NULL, "djstripe_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "id" varchar(255) NOT NULL UNIQUE, "livemode" bool NULL, "created" datetime NULL, "period" text NULL CHECK ((JSON_VALID("period") OR "period" IS NULL)), "period_end" datetime NULL, "period_start" datetime NULL, "total_usage" integer unsigned NOT NULL CHECK ("total_usage" >= 0), "djstripe_owner_account_id" varchar(255) NULL REFERENCES "djstripe_account" ("id") DEFERRABLE INITIALLY DEFERRED, "invoice_id" varchar(255) NULL REFERENCES "djstripe_invoice" ("id") DEFERRABLE INITIALLY DEFERRED, "subscription_item_id" varchar(255) NOT NULL REFERENCES "djstripe_subscriptionitem" ("id") DEFERRABLE INITIALLY DEFERRED);

-- Data exporting was unselected.

-- Dumping structure for table db.djstripe_webhookendpoint
CREATE TABLE IF NOT EXISTS "djstripe_webhookendpoint" ("djstripe_created" datetime NOT NULL, "djstripe_updated" datetime NOT NULL, "djstripe_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "id" varchar(255) NOT NULL UNIQUE, "livemode" bool NULL, "created" datetime NULL, "metadata" text NULL CHECK ((JSON_VALID("metadata") OR "metadata" IS NULL)), "description" text NULL, "enabled_events" text NOT NULL CHECK ((JSON_VALID("enabled_events") OR "enabled_events" IS NULL)), "secret" varchar(256) NOT NULL, "status" varchar(8) NOT NULL, "url" varchar(2048) NOT NULL, "application" varchar(255) NOT NULL, "djstripe_owner_account_id" varchar(255) NULL REFERENCES "djstripe_account" ("id") DEFERRABLE INITIALLY DEFERRED, "djstripe_uuid" char(32) NULL UNIQUE, "api_version" varchar(64) NOT NULL);

-- Data exporting was unselected.

-- Dumping structure for table db.djstripe_webhookeventtrigger
CREATE TABLE IF NOT EXISTS "djstripe_webhookeventtrigger" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "remote_ip" char(39) NOT NULL, "headers" text NOT NULL CHECK ((JSON_VALID("headers") OR "headers" IS NULL)), "body" text NOT NULL, "valid" bool NOT NULL, "processed" bool NOT NULL, "exception" varchar(128) NOT NULL, "traceback" text NOT NULL, "djstripe_version" varchar(32) NOT NULL, "created" datetime NOT NULL, "updated" datetime NOT NULL, "event_id" varchar(255) NULL REFERENCES "djstripe_event" ("id") DEFERRABLE INITIALLY DEFERRED, "stripe_trigger_account_id" varchar(255) NULL REFERENCES "djstripe_account" ("id") DEFERRABLE INITIALLY DEFERRED, "webhook_endpoint_id" varchar(255) NULL REFERENCES "djstripe_webhookendpoint" ("id") DEFERRABLE INITIALLY DEFERRED);

-- Data exporting was unselected.

-- Dumping structure for table db.flags_flagstate
CREATE TABLE IF NOT EXISTS "flags_flagstate" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(64) NOT NULL, "condition" varchar(64) NOT NULL, "value" varchar(127) NOT NULL, "required" bool NOT NULL);

-- Data exporting was unselected.

-- Dumping structure for table db.flag_flag
CREATE TABLE IF NOT EXISTS "flag_flag" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "object_id" integer unsigned NOT NULL CHECK ("object_id" >= 0), "state" smallint NOT NULL, "count" integer unsigned NOT NULL CHECK ("count" >= 0), "content_type_id" integer NOT NULL REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED, "creator_id" bigint NULL REFERENCES "core_users" ("id") DEFERRABLE INITIALLY DEFERRED, "moderator_id" bigint NULL REFERENCES "core_users" ("id") DEFERRABLE INITIALLY DEFERRED);

-- Data exporting was unselected.

-- Dumping structure for table db.flag_flaginstance
CREATE TABLE IF NOT EXISTS "flag_flaginstance" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "date_flagged" datetime NOT NULL, "reason" smallint NOT NULL, "info" text NULL, "flag_id" bigint NOT NULL REFERENCES "flag_flag" ("id") DEFERRABLE INITIALLY DEFERRED, "user_id" bigint NOT NULL REFERENCES "core_users" ("id") DEFERRABLE INITIALLY DEFERRED);

-- Data exporting was unselected.

-- Dumping structure for table db.newsfeed_issue
CREATE TABLE IF NOT EXISTS "newsfeed_issue" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(128) NOT NULL, "issue_number" integer unsigned NOT NULL UNIQUE CHECK ("issue_number" >= 0), "publish_date" datetime NOT NULL, "issue_type" smallint unsigned NOT NULL CHECK ("issue_type" >= 0), "short_description" text NULL, "is_draft" bool NOT NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL);

-- Data exporting was unselected.

-- Dumping structure for table db.newsfeed_newsletter
CREATE TABLE IF NOT EXISTS "newsfeed_newsletter" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "subject" varchar(128) NOT NULL, "schedule" datetime NULL, "is_sent" bool NOT NULL, "sent_at" datetime NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL, "issue_id" bigint NOT NULL REFERENCES "newsfeed_issue" ("id") DEFERRABLE INITIALLY DEFERRED);

-- Data exporting was unselected.

-- Dumping structure for table db.newsfeed_post
CREATE TABLE IF NOT EXISTS "newsfeed_post" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(255) NOT NULL, "source_url" varchar(200) NOT NULL, "is_visible" bool NOT NULL, "short_description" text NOT NULL, "order" integer unsigned NOT NULL CHECK ("order" >= 0), "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL, "category_id" integer NULL REFERENCES "newsfeed_postcategory" ("id") DEFERRABLE INITIALLY DEFERRED, "issue_id" bigint NULL REFERENCES "newsfeed_issue" ("id") DEFERRABLE INITIALLY DEFERRED);

-- Data exporting was unselected.

-- Dumping structure for table db.newsfeed_postcategory
CREATE TABLE IF NOT EXISTS "newsfeed_postcategory" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(255) NOT NULL, "order" integer unsigned NOT NULL CHECK ("order" >= 0));

-- Data exporting was unselected.

-- Dumping structure for table db.newsfeed_subscriber
CREATE TABLE IF NOT EXISTS "newsfeed_subscriber" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "email_address" varchar(254) NOT NULL UNIQUE, "token" varchar(128) NOT NULL UNIQUE, "verified" bool NOT NULL, "subscribed" bool NOT NULL, "verification_sent_date" datetime NULL, "created_at" datetime NOT NULL);

-- Data exporting was unselected.

-- Dumping structure for table db.otp_email_emaildevice
CREATE TABLE IF NOT EXISTS "otp_email_emaildevice" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(64) NOT NULL, "confirmed" bool NOT NULL, "user_id" bigint NOT NULL REFERENCES "core_users" ("id") DEFERRABLE INITIALLY DEFERRED, "token" varchar(16) NULL, "valid_until" datetime NOT NULL, "email" varchar(254) NULL, "throttling_failure_count" integer unsigned NOT NULL CHECK ("throttling_failure_count" >= 0), "throttling_failure_timestamp" datetime NULL);

-- Data exporting was unselected.

-- Dumping structure for table db.otp_static_staticdevice
CREATE TABLE IF NOT EXISTS "otp_static_staticdevice" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(64) NOT NULL, "confirmed" bool NOT NULL, "user_id" bigint NOT NULL REFERENCES "core_users" ("id") DEFERRABLE INITIALLY DEFERRED, "throttling_failure_count" integer unsigned NOT NULL CHECK ("throttling_failure_count" >= 0), "throttling_failure_timestamp" datetime NULL);

-- Data exporting was unselected.

-- Dumping structure for table db.otp_static_statictoken
CREATE TABLE IF NOT EXISTS "otp_static_statictoken" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "token" varchar(16) NOT NULL, "device_id" integer NOT NULL REFERENCES "otp_static_staticdevice" ("id") DEFERRABLE INITIALLY DEFERRED);

-- Data exporting was unselected.

-- Dumping structure for table db.otp_totp_totpdevice
CREATE TABLE IF NOT EXISTS "otp_totp_totpdevice" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(64) NOT NULL, "confirmed" bool NOT NULL, "key" varchar(80) NOT NULL, "step" smallint unsigned NOT NULL CHECK ("step" >= 0), "t0" bigint NOT NULL, "digits" smallint unsigned NOT NULL CHECK ("digits" >= 0), "tolerance" smallint unsigned NOT NULL CHECK ("tolerance" >= 0), "drift" smallint NOT NULL, "last_t" bigint NOT NULL, "user_id" bigint NOT NULL REFERENCES "core_users" ("id") DEFERRABLE INITIALLY DEFERRED, "throttling_failure_count" integer unsigned NOT NULL CHECK ("throttling_failure_count" >= 0), "throttling_failure_timestamp" datetime NULL);

-- Data exporting was unselected.

-- Dumping structure for table db.pages_page
CREATE TABLE IF NOT EXISTS "pages_page" ("slug" varchar(255) NULL, "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(255) NULL, "content" text NULL, "seo_title" varchar(255) NULL, "seo_description" text NULL, "seo_keywords" text NULL, "status" varchar(100) NOT NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL, "parent_id" bigint NULL REFERENCES "pages_page" ("id") DEFERRABLE INITIALLY DEFERRED);

-- Data exporting was unselected.

-- Dumping structure for table db.reversion_revision
CREATE TABLE IF NOT EXISTS "reversion_revision" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "date_created" datetime NOT NULL, "comment" text NOT NULL, "user_id" bigint NULL REFERENCES "core_users" ("id") DEFERRABLE INITIALLY DEFERRED);

-- Data exporting was unselected.

-- Dumping structure for table db.reversion_version
CREATE TABLE IF NOT EXISTS "reversion_version" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "object_id" varchar(191) NOT NULL, "format" varchar(255) NOT NULL, "serialized_data" text NOT NULL, "object_repr" text NOT NULL, "content_type_id" integer NOT NULL REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED, "revision_id" integer NOT NULL REFERENCES "reversion_revision" ("id") DEFERRABLE INITIALLY DEFERRED, "db" varchar(191) NOT NULL);

-- Data exporting was unselected.

-- Dumping structure for table db.stories_author
CREATE TABLE IF NOT EXISTS "stories_author" ("status" varchar(100) NOT NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL, "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "story_id" bigint NULL REFERENCES "stories_stories" ("id") DEFERRABLE INITIALLY DEFERRED, "user_id" bigint NULL REFERENCES "core_users" ("id") DEFERRABLE INITIALLY DEFERRED);

-- Data exporting was unselected.

-- Dumping structure for table db.stories_bookmark
CREATE TABLE IF NOT EXISTS "stories_bookmark" ("status" varchar(100) NOT NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL, "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "url" varchar(255) NULL, "story_id" bigint NOT NULL REFERENCES "stories_stories" ("id") DEFERRABLE INITIALLY DEFERRED, "user_id" bigint NULL REFERENCES "core_users" ("id") DEFERRABLE INITIALLY DEFERRED);

-- Data exporting was unselected.

-- Dumping structure for table db.stories_categories
CREATE TABLE IF NOT EXISTS "stories_categories" ("status" varchar(100) NOT NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL, "name" varchar(255) NOT NULL, "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "slug" varchar(30) NULL UNIQUE, "category_type_id" bigint NULL REFERENCES "stories_type" ("id") DEFERRABLE INITIALLY DEFERRED);

-- Data exporting was unselected.

-- Dumping structure for table db.stories_chapter
CREATE TABLE IF NOT EXISTS "stories_chapter" ("status" varchar(100) NOT NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL, "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "position" integer NOT NULL, "slug" varchar(50) NULL UNIQUE, "title" varchar(255) NOT NULL, "text" text NOT NULL, "authors_note" text NULL, "words" integer NULL, "released_at" datetime NOT NULL, "edited_by_id" bigint NOT NULL REFERENCES "core_users" ("id") DEFERRABLE INITIALLY DEFERRED, "story_id" bigint NOT NULL REFERENCES "stories_stories" ("id") DEFERRABLE INITIALLY DEFERRED, "user_id" bigint NOT NULL REFERENCES "core_users" ("id") DEFERRABLE INITIALLY DEFERRED);

-- Data exporting was unselected.

-- Dumping structure for table db.stories_character
CREATE TABLE IF NOT EXISTS "stories_character" ("status" varchar(100) NOT NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL, "name" varchar(255) NOT NULL, "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "slug" varchar(30) NULL UNIQUE, "category_id" bigint NULL REFERENCES "stories_categories" ("id") DEFERRABLE INITIALLY DEFERRED, "story_id" bigint NULL REFERENCES "stories_stories" ("id") DEFERRABLE INITIALLY DEFERRED);

-- Data exporting was unselected.

-- Dumping structure for table db.stories_editor
CREATE TABLE IF NOT EXISTS "stories_editor" ("status" varchar(100) NOT NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL, "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "story_id" bigint NULL REFERENCES "stories_stories" ("id") DEFERRABLE INITIALLY DEFERRED, "user_id" bigint NULL REFERENCES "core_users" ("id") DEFERRABLE INITIALLY DEFERRED);

-- Data exporting was unselected.

-- Dumping structure for table db.stories_genre
CREATE TABLE IF NOT EXISTS "stories_genre" ("status" varchar(100) NOT NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL, "name" varchar(255) NOT NULL, "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "description" text NULL, "slug" varchar(30) NULL UNIQUE);

-- Data exporting was unselected.

-- Dumping structure for table db.stories_history
CREATE TABLE IF NOT EXISTS "stories_history" ("status" varchar(100) NOT NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL, "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "url" varchar(255) NULL, "chapter_id" bigint NOT NULL REFERENCES "stories_chapter" ("id") DEFERRABLE INITIALLY DEFERRED, "story_id" bigint NOT NULL REFERENCES "stories_stories" ("id") DEFERRABLE INITIALLY DEFERRED, "user_id" bigint NULL REFERENCES "core_users" ("id") DEFERRABLE INITIALLY DEFERRED);

-- Data exporting was unselected.

-- Dumping structure for table db.stories_language
CREATE TABLE IF NOT EXISTS "stories_language" ("status" varchar(100) NOT NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL, "name" varchar(255) NOT NULL, "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "slug" varchar(30) NULL UNIQUE, "code" varchar(255) NOT NULL, "native_name" varchar(255) NOT NULL);

-- Data exporting was unselected.

-- Dumping structure for table db.stories_rating
CREATE TABLE IF NOT EXISTS "stories_rating" ("status" varchar(100) NOT NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL, "name" varchar(255) NOT NULL, "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "description" text NULL, "slug" varchar(30) NULL UNIQUE);

-- Data exporting was unselected.

-- Dumping structure for table db.stories_review
CREATE TABLE IF NOT EXISTS "stories_review" ("status" varchar(100) NOT NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL, "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "text" text NOT NULL, "chapter_id" bigint NULL REFERENCES "stories_chapter" ("id") DEFERRABLE INITIALLY DEFERRED, "parent_id" bigint NULL REFERENCES "stories_review" ("id") DEFERRABLE INITIALLY DEFERRED, "story_id" bigint NOT NULL REFERENCES "stories_stories" ("id") DEFERRABLE INITIALLY DEFERRED, "user_id" bigint NOT NULL REFERENCES "core_users" ("id") DEFERRABLE INITIALLY DEFERRED);

-- Data exporting was unselected.

-- Dumping structure for table db.stories_stories
CREATE TABLE IF NOT EXISTS "stories_stories" ("created_at" datetime NOT NULL, "updated_at" datetime NOT NULL, "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(255) NOT NULL, "slug" varchar(50) NULL UNIQUE, "abbreviation" varchar(15) NOT NULL UNIQUE, "summary" text NOT NULL, "cover" varchar(255) NULL, "released_at" datetime NOT NULL, "featured" bool NOT NULL, "featured_at" datetime NULL, "status" varchar(100) NOT NULL, "language_id" bigint NOT NULL REFERENCES "stories_language" ("id") DEFERRABLE INITIALLY DEFERRED, "rating_id" bigint NULL REFERENCES "stories_rating" ("id") DEFERRABLE INITIALLY DEFERRED, "story_type_id" bigint NOT NULL REFERENCES "stories_type" ("id") DEFERRABLE INITIALLY DEFERRED);

-- Data exporting was unselected.

-- Dumping structure for table db.stories_stories_characters
CREATE TABLE IF NOT EXISTS "stories_stories_characters" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "stories_id" bigint NOT NULL REFERENCES "stories_stories" ("id") DEFERRABLE INITIALLY DEFERRED, "character_id" bigint NOT NULL REFERENCES "stories_character" ("id") DEFERRABLE INITIALLY DEFERRED);

-- Data exporting was unselected.

-- Dumping structure for table db.stories_stories_dislikes
CREATE TABLE IF NOT EXISTS "stories_stories_dislikes" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "stories_id" bigint NOT NULL REFERENCES "stories_stories" ("id") DEFERRABLE INITIALLY DEFERRED, "users_id" bigint NOT NULL REFERENCES "core_users" ("id") DEFERRABLE INITIALLY DEFERRED);

-- Data exporting was unselected.

-- Dumping structure for table db.stories_stories_following
CREATE TABLE IF NOT EXISTS "stories_stories_following" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "stories_id" bigint NOT NULL REFERENCES "stories_stories" ("id") DEFERRABLE INITIALLY DEFERRED, "users_id" bigint NOT NULL REFERENCES "core_users" ("id") DEFERRABLE INITIALLY DEFERRED);

-- Data exporting was unselected.

-- Dumping structure for table db.stories_stories_genre
CREATE TABLE IF NOT EXISTS "stories_stories_genre" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "stories_id" bigint NOT NULL REFERENCES "stories_stories" ("id") DEFERRABLE INITIALLY DEFERRED, "genre_id" bigint NOT NULL REFERENCES "stories_genre" ("id") DEFERRABLE INITIALLY DEFERRED);

-- Data exporting was unselected.

-- Dumping structure for table db.stories_stories_likes
CREATE TABLE IF NOT EXISTS "stories_stories_likes" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "stories_id" bigint NOT NULL REFERENCES "stories_stories" ("id") DEFERRABLE INITIALLY DEFERRED, "users_id" bigint NOT NULL REFERENCES "core_users" ("id") DEFERRABLE INITIALLY DEFERRED);

-- Data exporting was unselected.

-- Dumping structure for table db.stories_type
CREATE TABLE IF NOT EXISTS "stories_type" ("status" varchar(100) NOT NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL, "name" varchar(255) NOT NULL, "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "slug" varchar(30) NULL UNIQUE);

-- Data exporting was unselected.

-- Dumping structure for table db.stories_universe
CREATE TABLE IF NOT EXISTS "stories_universe" ("status" varchar(100) NOT NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL, "name" varchar(255) NOT NULL, "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "slug" varchar(30) NULL UNIQUE, "category_id_id" bigint NOT NULL REFERENCES "stories_categories" ("id") DEFERRABLE INITIALLY DEFERRED);

-- Data exporting was unselected.

-- Dumping structure for table db.subscriptions_packages
CREATE TABLE IF NOT EXISTS "subscriptions_packages" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "status" varchar(100) NOT NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL, "name" varchar(255) NOT NULL, "advance" integer NOT NULL, "amount" integer NOT NULL, "story_id" bigint NOT NULL REFERENCES "stories_stories" ("id") DEFERRABLE INITIALLY DEFERRED, "user_id" bigint NOT NULL REFERENCES "core_users" ("id") DEFERRABLE INITIALLY DEFERRED);

-- Data exporting was unselected.

-- Dumping structure for table db.subscriptions_sponsors
CREATE TABLE IF NOT EXISTS "subscriptions_sponsors" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "status" varchar(100) NOT NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL, "payment_date" date NOT NULL, "package_id" bigint NOT NULL REFERENCES "subscriptions_packages" ("id") DEFERRABLE INITIALLY DEFERRED, "user_id" bigint NOT NULL REFERENCES "core_users" ("id") DEFERRABLE INITIALLY DEFERRED, "expire_at" date NOT NULL);

-- Data exporting was unselected.

-- Dumping structure for table db.taggit_tag
CREATE TABLE IF NOT EXISTS "taggit_tag" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(100) NOT NULL UNIQUE, "slug" varchar(100) NOT NULL UNIQUE);

-- Data exporting was unselected.

-- Dumping structure for table db.taggit_taggeditem
CREATE TABLE IF NOT EXISTS "taggit_taggeditem" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "object_id" integer NOT NULL, "content_type_id" integer NOT NULL REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED, "tag_id" integer NOT NULL REFERENCES "taggit_tag" ("id") DEFERRABLE INITIALLY DEFERRED);

-- Data exporting was unselected.

-- Dumping structure for table db.two_factor_phonedevice
CREATE TABLE IF NOT EXISTS "two_factor_phonedevice" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(64) NOT NULL, "confirmed" bool NOT NULL, "number" varchar(128) NOT NULL, "key" varchar(40) NOT NULL, "method" varchar(4) NOT NULL, "user_id" bigint NOT NULL REFERENCES "core_users" ("id") DEFERRABLE INITIALLY DEFERRED, "throttling_failure_count" integer unsigned NOT NULL CHECK ("throttling_failure_count" >= 0), "throttling_failure_timestamp" datetime NULL);

-- Data exporting was unselected.

-- Dumping structure for table db.watson_searchentry
CREATE TABLE IF NOT EXISTS "watson_searchentry" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "engine_slug" varchar(200) NOT NULL, "object_id_int" integer NULL, "title" varchar(1000) NOT NULL, "description" text NOT NULL, "content" text NOT NULL, "url" varchar(1000) NOT NULL, "meta_encoded" text NOT NULL, "content_type_id" integer NOT NULL REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED, "object_id" varchar(191) NOT NULL);


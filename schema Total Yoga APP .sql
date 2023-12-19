CREATE TABLE "accounts" (
  "id" int PRIMARY KEY,
  "first_name" varchar,
  "last_name" varchar,
  "username" varchar UNIQUE,
  "email" varchar UNIQUE,
  "phone_number" varchar,
  "dob" date,
  "datetime" timestamp,
  "date_time" timestamp,
  "credit_amount" int DEFAULT 0,
  "date_joined" timestamp,
  "last_login" timestamp,
  "is_active" bool DEFAULT false
);

CREATE TABLE "user_profiles" (
  "user_id" int,
  "discription" text,
  "city" varchar,
  "state" varchar,
  "country" varchar,
  "profile_picture" varchar,
  "profile_background" varchar,
  "datetime" timestamp
);

CREATE TABLE "about_users" (
  "id" int PRIMARY KEY,
  "user_id" int,
  "is_activated" bool DEFAULT false,
  "datetime" timestamp
);

CREATE TABLE "batches" (
  "id" int PRIMARY KEY,
  "time_slot" varchar
);

CREATE TABLE "participants" (
  "id" int PRIMARY KEY,
  "user_id" int,
  "name" varchar,
  "age" int,
  "email" varchar,
  "email_activated" bool DEFAULT false
);

CREATE TABLE "enrollments" (
  "id" int PRIMARY KEY,
  "user_id" int,
  "participant_id" int,
  "selected_batch_id" int,
  "payment_status" bool DEFAULT false
);

CREATE TABLE "monthly_fees" (
  "id" int PRIMARY KEY,
  "user_id" int,
  "enrollment_id" int,
  "amount" "decimal(6, 2)" DEFAULT 500,
  "paid_date" date
);

COMMENT ON COLUMN "accounts"."datetime" IS 'Timestamp for account creation';

COMMENT ON COLUMN "user_profiles"."profile_picture" IS 'Path to the profile picture';

COMMENT ON COLUMN "user_profiles"."profile_background" IS 'Path to the profile background';

COMMENT ON COLUMN "user_profiles"."datetime" IS 'Timestamp for user profile creation';

COMMENT ON COLUMN "about_users"."datetime" IS 'Timestamp for about_user creation';

COMMENT ON COLUMN "batches"."time_slot" IS 'e.g., 6-7AM, 7-8AM, 8-9AM, 5-6PM';

ALTER TABLE "user_profiles" ADD FOREIGN KEY ("user_id") REFERENCES "accounts" ("id");

ALTER TABLE "about_users" ADD FOREIGN KEY ("user_id") REFERENCES "accounts" ("id");

ALTER TABLE "participants" ADD FOREIGN KEY ("user_id") REFERENCES "accounts" ("id");

ALTER TABLE "enrollments" ADD FOREIGN KEY ("user_id") REFERENCES "accounts" ("id");

ALTER TABLE "enrollments" ADD FOREIGN KEY ("participant_id") REFERENCES "participants" ("id");

ALTER TABLE "enrollments" ADD FOREIGN KEY ("selected_batch_id") REFERENCES "batches" ("id");

ALTER TABLE "monthly_fees" ADD FOREIGN KEY ("user_id") REFERENCES "accounts" ("id");

ALTER TABLE "monthly_fees" ADD FOREIGN KEY ("enrollment_id") REFERENCES "enrollments" ("id");

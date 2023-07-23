-- migrate:up
ALTER TABLE events_v2 RENAME COLUMN name TO event_name;
ALTER TABLE events_v2 ALTER COLUMN client_user_id DROP NOT NULL;
ALTER TABLE events_v2 RENAME TO events;

-- migrate:down


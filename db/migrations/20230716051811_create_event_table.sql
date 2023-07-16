-- migrate:up
CREATE TABLE IF NOT EXISTS events (
  event_id   UUID        NOT NULL PRIMARY KEY,
  name       TEXT,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
	user_id    UUID        NOT NULL,
  properties JSONB
);

-- migrate:down


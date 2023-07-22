-- migrate:up

CREATE TABLE IF NOT EXISTS events_v2 (
  event_id            UUID        NOT NULL PRIMARY KEY,
  name                TEXT        NOT NULL,
  event_type          TEXT        NOT NULL,
  event_status        TEXT        NOT NULL,
  created_at          TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  client_created_at   TIMESTAMPTZ NOT NULL,
  client_completed_at TIMESTAMPTZ NOT NULL,
  client_user_id      TEXT        NOT NULL,
  project_id          UUID        NOT NULL,
  properties          JSONB
);

CREATE INDEX ON events_v2 (project_id, created_at DESC);

-- migrate:down

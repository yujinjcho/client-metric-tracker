-- migrate:up
CREATE TABLE IF NOT EXISTS event_updates (
  event_update_id UUID NOT NULL PRIMARY KEY,
  event_id        UUID references events(event_id),
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  properties JSONB
)


-- migrate:down


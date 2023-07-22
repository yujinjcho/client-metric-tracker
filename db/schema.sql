SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: event_updates; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.event_updates (
    event_update_id uuid NOT NULL,
    event_id uuid,
    created_at timestamp with time zone DEFAULT now() NOT NULL,
    properties jsonb
);


--
-- Name: events; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.events (
    event_id uuid NOT NULL,
    name text,
    created_at timestamp with time zone DEFAULT now() NOT NULL,
    user_id uuid NOT NULL,
    properties jsonb
);


--
-- Name: events_v2; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.events_v2 (
    event_id uuid NOT NULL,
    name text NOT NULL,
    event_type text NOT NULL,
    event_status text NOT NULL,
    created_at timestamp with time zone DEFAULT now() NOT NULL,
    client_created_at timestamp with time zone NOT NULL,
    client_completed_at timestamp with time zone NOT NULL,
    client_user_id text NOT NULL,
    project_id uuid NOT NULL,
    properties jsonb
);


--
-- Name: schema_migrations; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.schema_migrations (
    version character varying(128) NOT NULL
);


--
-- Name: test; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.test (
    id text
);


--
-- Name: event_updates event_updates_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.event_updates
    ADD CONSTRAINT event_updates_pkey PRIMARY KEY (event_update_id);


--
-- Name: events events_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.events
    ADD CONSTRAINT events_pkey PRIMARY KEY (event_id);


--
-- Name: events_v2 events_v2_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.events_v2
    ADD CONSTRAINT events_v2_pkey PRIMARY KEY (event_id);


--
-- Name: schema_migrations schema_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.schema_migrations
    ADD CONSTRAINT schema_migrations_pkey PRIMARY KEY (version);


--
-- Name: events_v2_project_id_created_at_idx; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX events_v2_project_id_created_at_idx ON public.events_v2 USING btree (project_id, created_at DESC);


--
-- Name: event_updates event_updates_event_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.event_updates
    ADD CONSTRAINT event_updates_event_id_fkey FOREIGN KEY (event_id) REFERENCES public.events(event_id);


--
-- PostgreSQL database dump complete
--


--
-- Dbmate schema migrations
--

INSERT INTO public.schema_migrations (version) VALUES
    ('20230716040008'),
    ('20230716051811'),
    ('20230719021756'),
    ('20230719022703');

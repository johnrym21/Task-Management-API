CREATE TABLE IF NOT EXISTS public.tasks
(
    id integer NOT NULL DEFAULT nextval('tasks_id_seq'::regclass),
    title text COLLATE pg_catalog."default",
    description text COLLATE pg_catalog."default",
    completed boolean,
    priority integer,
    due_date date,
    category text COLLATE pg_catalog."default",
    CONSTRAINT tasks_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE public.tasks
    OWNER to postgres;
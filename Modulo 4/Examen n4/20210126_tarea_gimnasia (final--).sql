--
-- PostgreSQL database dump
--

-- Dumped from database version 13.1
-- Dumped by pg_dump version 13.1

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
-- Name: categoria; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.categoria (
    id_categoria integer NOT NULL,
    id_pase_diario integer NOT NULL,
    nombre_categoria character varying(255),
    precio_categoria integer
);


ALTER TABLE public.categoria OWNER TO postgres;

--
-- Name: cliente; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.cliente (
    id_cliente integer NOT NULL,
    id_suscripcion integer NOT NULL,
    nombre_cliente character varying(255),
    apellido_cliente character varying(255),
    telefono numeric,
    email character varying(255),
    dia_pago_suscripcion date,
    usuario_activo boolean
);


ALTER TABLE public.cliente OWNER TO postgres;

--
-- Name: pase_diario; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.pase_diario (
    id_pase_diario integer NOT NULL,
    id_cliente integer NOT NULL,
    precio_suscripcion integer,
    fecha_pase_diario date,
    nombre_pase_diario character varying(255)
);


ALTER TABLE public.pase_diario OWNER TO postgres;

--
-- Name: producto; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.producto (
    id_producto integer NOT NULL,
    nombre_producto character varying(255),
    precio_producto numeric
);


ALTER TABLE public.producto OWNER TO postgres;

--
-- Name: suscripcion; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.suscripcion (
    id_suscripcion integer NOT NULL,
    nombre_suscripcion character varying(255),
    precio_suscripcion integer
);


ALTER TABLE public.suscripcion OWNER TO postgres;

--
-- Name: transaccion; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.transaccion (
    id_transaccion integer NOT NULL,
    id_cliente integer NOT NULL,
    fecha_transaccion date
);


ALTER TABLE public.transaccion OWNER TO postgres;

--
-- Name: venta; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.venta (
    id_transaccion integer NOT NULL,
    id_producto integer NOT NULL,
    cantidad numeric
);


ALTER TABLE public.venta OWNER TO postgres;

--
-- Data for Name: categoria; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.categoria (id_categoria, id_pase_diario, nombre_categoria, precio_categoria) FROM stdin;
1	1	baile entretenido	2000
2	1	aerobox	3500
3	2	Kickboxing	4000
4	3	máquinas	2000
5	4	full	6000
\.


--
-- Data for Name: cliente; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.cliente (id_cliente, id_suscripcion, nombre_cliente, apellido_cliente, telefono, email, dia_pago_suscripcion, usuario_activo) FROM stdin;
1	1	Miguel	Vázquez	22159001401	Miguel.Vázquez@gmail.com	2021-02-01	\N
2	2	Pascual	Ibarra	22159001402	Pascual.Ibarra@gmail.com	2021-02-01	\N
3	3	Humberto	Velasco	22159001403	Humberto.Velasco@gmail.com	2021-02-01	\N
4	4	Miguel	Díaz	22159001404	Miguel.Díaz@gmail.com	2021-02-01	\N
5	5	Adan	Arias	22159001405	Adan.Arias@gmail.com	2021-02-01	\N
6	6	Francisco	Sánchez	22159001406	Francisco.Sánchez@gmail.com	2021-02-01	\N
7	3	Marcela	Toro	22159001407	Marcela.Toro@gmail.com	2021-02-01	\N
8	4	Fredy	Pérez	22159001408	Fredy.Pérez@gmail.com	2021-02-01	\N
9	5	Héctor	Guajardo	22159001409	Héctor.Guajardo@gmail.com	2021-02-01	\N
10	6	Francisco	Alarcon	22159001410	Francisco.Alarcon@gmail.com	2021-02-01	\N
11	3	Clemente	Diaz	22159001411	Clemente.Diaz@gmail.com	2021-02-01	\N
12	4	Julio	Díaz	22159001412	Julio.Díaz@gmail.com	2021-02-01	\N
13	5	Carlos	Díaz	22159001413	Carlos.Díaz@gmail.com	2021-02-01	\N
14	6	Juan	Núñez	22159001414	Juan.Núñez@gmail.com	2021-02-01	\N
15	4	José	Vivaldo	22159001415	José.Vivaldo@gmail.com	2021-02-01	\N
16	5	Miguel	Velasco	22159001416	Miguel.Velasco@gmail.com	2021-02-01	\N
17	6	Jesús	Barrios	22159001417	Jesús.Barrios@gmail.com	2021-02-01	\N
18	1	Gabriel	Dominguez	22159001418	Gabriel.Dominguez@gmail.com	2021-02-01	\N
19	2	Julián	Briz	22159001419	Julián.Briz@gmail.com	2021-02-01	\N
20	2	Juan	Vergara	22159001420	Juan.Vergara@gmail.com	2021-02-01	\N
\.


--
-- Data for Name: pase_diario; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.pase_diario (id_pase_diario, id_cliente, precio_suscripcion, fecha_pase_diario, nombre_pase_diario) FROM stdin;
1	1	2000	2021-01-01	baile entretenido
2	1	3500	2021-01-01	aerobox
3	2	4000	2021-01-10	 Kickboxing
4	3	2000	2021-01-15	máquinas
5	4	6000	2021-01-26	full
\.


--
-- Data for Name: producto; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.producto (id_producto, nombre_producto, precio_producto) FROM stdin;
1	bebidas	1000
2	galletas	500
3	jugos	500
4	camisetas	15000
5	reloj deportivo	25000
6	cuerdas	15000
7	mochila	26000
8	guantes fitness	20000
9	bolso sport	35000
10	guantes pesas	26000
\.


--
-- Data for Name: suscripcion; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.suscripcion (id_suscripcion, nombre_suscripcion, precio_suscripcion) FROM stdin;
1	mensual full	20000
2	semanal full	2000
3	estudiante full	10000
4	tres veces a la semanal	15600
5	plan oficina	20000
6	plan covid	18000
\.


--
-- Data for Name: transaccion; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.transaccion (id_transaccion, id_cliente, fecha_transaccion) FROM stdin;
1	1	2021-01-01
2	1	2021-01-05
3	2	2021-01-10
4	3	2021-01-12
5	4	2021-01-15
6	5	2021-01-20
7	5	2021-01-26
8	7	2021-01-27
9	7	0201-01-28
\.


--
-- Data for Name: venta; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.venta (id_transaccion, id_producto, cantidad) FROM stdin;
1	1	1
1	2	2
3	3	3
4	4	1
4	5	4
6	6	2
7	7	4
8	8	1
9	9	1
\.


--
-- Name: categoria categoria_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.categoria
    ADD CONSTRAINT categoria_pkey PRIMARY KEY (id_categoria);


--
-- Name: cliente cliente_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cliente
    ADD CONSTRAINT cliente_pkey PRIMARY KEY (id_cliente);


--
-- Name: pase_diario pase_diario_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pase_diario
    ADD CONSTRAINT pase_diario_pkey PRIMARY KEY (id_pase_diario);


--
-- Name: producto producto_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.producto
    ADD CONSTRAINT producto_pkey PRIMARY KEY (id_producto);


--
-- Name: suscripcion suscripcion_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.suscripcion
    ADD CONSTRAINT suscripcion_pkey PRIMARY KEY (id_suscripcion);


--
-- Name: transaccion transaccion_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.transaccion
    ADD CONSTRAINT transaccion_pkey PRIMARY KEY (id_transaccion);


--
-- Name: categoria categoria_id_pase_diario_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.categoria
    ADD CONSTRAINT categoria_id_pase_diario_fkey FOREIGN KEY (id_pase_diario) REFERENCES public.pase_diario(id_pase_diario);


--
-- Name: cliente cliente_id_suscripcion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cliente
    ADD CONSTRAINT cliente_id_suscripcion_fkey FOREIGN KEY (id_suscripcion) REFERENCES public.suscripcion(id_suscripcion);


--
-- Name: pase_diario pase_diario_id_cliente_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pase_diario
    ADD CONSTRAINT pase_diario_id_cliente_fkey FOREIGN KEY (id_cliente) REFERENCES public.cliente(id_cliente);


--
-- Name: transaccion transaccion_id_cliente_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.transaccion
    ADD CONSTRAINT transaccion_id_cliente_fkey FOREIGN KEY (id_cliente) REFERENCES public.cliente(id_cliente);


--
-- Name: venta venta_id_producto_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.venta
    ADD CONSTRAINT venta_id_producto_fkey FOREIGN KEY (id_producto) REFERENCES public.producto(id_producto);


--
-- Name: venta venta_id_transaccion_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.venta
    ADD CONSTRAINT venta_id_transaccion_fkey FOREIGN KEY (id_transaccion) REFERENCES public.transaccion(id_transaccion);


--
-- PostgreSQL database dump complete
--


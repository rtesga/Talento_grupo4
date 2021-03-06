PGDMP     #    #                 y           GymASIA_Final    9.5.24    9.5.24 #    c           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                       false            d           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                       false            e           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                       false            f           1262    49420    GymASIA_Final    DATABASE     �   CREATE DATABASE "GymASIA_Final" WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'Spanish_Chile.1252' LC_CTYPE = 'Spanish_Chile.1252';
    DROP DATABASE "GymASIA_Final";
             postgres    false                        2615    2200    public    SCHEMA        CREATE SCHEMA public;
    DROP SCHEMA public;
             postgres    false            g           0    0    SCHEMA public    COMMENT     6   COMMENT ON SCHEMA public IS 'standard public schema';
                  postgres    false    6            h           0    0    SCHEMA public    ACL     �   REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;
                  postgres    false    6                        3079    12355    plpgsql 	   EXTENSION     ?   CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;
    DROP EXTENSION plpgsql;
                  false            i           0    0    EXTENSION plpgsql    COMMENT     @   COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';
                       false    1            �            1259    49514 	   categoria    TABLE     �   CREATE TABLE public.categoria (
    id_categoria integer NOT NULL,
    id_pase_diario integer NOT NULL,
    nombre_categoria character varying(255),
    precio_categoria integer
);
    DROP TABLE public.categoria;
       public         postgres    false    6            �            1259    49452    cliente    TABLE     1  CREATE TABLE public.cliente (
    id_cliente integer NOT NULL,
    id_suscripcion integer NOT NULL,
    nombre_cliente character varying(255),
    apellido_cliente character varying(255),
    telefono numeric,
    email character varying(255),
    dia_pago_suscripcion date,
    usuario_activo boolean
);
    DROP TABLE public.cliente;
       public         postgres    false    6            �            1259    49499    pase_diario    TABLE     �   CREATE TABLE public.pase_diario (
    id_pase_diario integer NOT NULL,
    id_cliente integer NOT NULL,
    precio_suscripcion integer,
    fecha_pase_diario date,
    nombre_pase_diario character varying(255)
);
    DROP TABLE public.pase_diario;
       public         postgres    false    6            �            1259    49475    producto    TABLE     �   CREATE TABLE public.producto (
    id_producto integer NOT NULL,
    nombre_producto character varying(255),
    precio_producto numeric
);
    DROP TABLE public.producto;
       public         postgres    false    6            �            1259    49447    suscripcion    TABLE     �   CREATE TABLE public.suscripcion (
    id_suscripcion integer NOT NULL,
    nombre_suscripcion character varying(255),
    precio_suscripcion integer
);
    DROP TABLE public.suscripcion;
       public         postgres    false    6            �            1259    49465    transaccion    TABLE     �   CREATE TABLE public.transaccion (
    id_transaccion integer NOT NULL,
    id_cliente integer NOT NULL,
    fecha_transaccion date
);
    DROP TABLE public.transaccion;
       public         postgres    false    6            �            1259    49483    venta    TABLE     {   CREATE TABLE public.venta (
    id_transaccion integer NOT NULL,
    id_producto integer NOT NULL,
    cantidad numeric
);
    DROP TABLE public.venta;
       public         postgres    false    6            `          0    49514 	   categoria 
   TABLE DATA               e   COPY public.categoria (id_categoria, id_pase_diario, nombre_categoria, precio_categoria) FROM stdin;
    public       postgres    false    187   �'       [          0    49452    cliente 
   TABLE DATA               �   COPY public.cliente (id_cliente, id_suscripcion, nombre_cliente, apellido_cliente, telefono, email, dia_pago_suscripcion, usuario_activo) FROM stdin;
    public       postgres    false    182   P(       _          0    49499    pase_diario 
   TABLE DATA               |   COPY public.pase_diario (id_pase_diario, id_cliente, precio_suscripcion, fecha_pase_diario, nombre_pase_diario) FROM stdin;
    public       postgres    false    186   #*       ]          0    49475    producto 
   TABLE DATA               Q   COPY public.producto (id_producto, nombre_producto, precio_producto) FROM stdin;
    public       postgres    false    184   �*       Z          0    49447    suscripcion 
   TABLE DATA               ]   COPY public.suscripcion (id_suscripcion, nombre_suscripcion, precio_suscripcion) FROM stdin;
    public       postgres    false    181   @+       \          0    49465    transaccion 
   TABLE DATA               T   COPY public.transaccion (id_transaccion, id_cliente, fecha_transaccion) FROM stdin;
    public       postgres    false    183   �+       ^          0    49483    venta 
   TABLE DATA               F   COPY public.venta (id_transaccion, id_producto, cantidad) FROM stdin;
    public       postgres    false    185   ,       �           2606    49518    categoria_pkey 
   CONSTRAINT     `   ALTER TABLE ONLY public.categoria
    ADD CONSTRAINT categoria_pkey PRIMARY KEY (id_categoria);
 B   ALTER TABLE ONLY public.categoria DROP CONSTRAINT categoria_pkey;
       public         postgres    false    187    187            �           2606    49459    cliente_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.cliente
    ADD CONSTRAINT cliente_pkey PRIMARY KEY (id_cliente);
 >   ALTER TABLE ONLY public.cliente DROP CONSTRAINT cliente_pkey;
       public         postgres    false    182    182            �           2606    49503    pase_diario_pkey 
   CONSTRAINT     f   ALTER TABLE ONLY public.pase_diario
    ADD CONSTRAINT pase_diario_pkey PRIMARY KEY (id_pase_diario);
 F   ALTER TABLE ONLY public.pase_diario DROP CONSTRAINT pase_diario_pkey;
       public         postgres    false    186    186            �           2606    49482    producto_pkey 
   CONSTRAINT     ]   ALTER TABLE ONLY public.producto
    ADD CONSTRAINT producto_pkey PRIMARY KEY (id_producto);
 @   ALTER TABLE ONLY public.producto DROP CONSTRAINT producto_pkey;
       public         postgres    false    184    184            �           2606    49451    suscripcion_pkey 
   CONSTRAINT     f   ALTER TABLE ONLY public.suscripcion
    ADD CONSTRAINT suscripcion_pkey PRIMARY KEY (id_suscripcion);
 F   ALTER TABLE ONLY public.suscripcion DROP CONSTRAINT suscripcion_pkey;
       public         postgres    false    181    181            �           2606    49469    transaccion_pkey 
   CONSTRAINT     f   ALTER TABLE ONLY public.transaccion
    ADD CONSTRAINT transaccion_pkey PRIMARY KEY (id_transaccion);
 F   ALTER TABLE ONLY public.transaccion DROP CONSTRAINT transaccion_pkey;
       public         postgres    false    183    183            �           2606    49519    categoria_id_pase_diario_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.categoria
    ADD CONSTRAINT categoria_id_pase_diario_fkey FOREIGN KEY (id_pase_diario) REFERENCES public.pase_diario(id_pase_diario);
 Q   ALTER TABLE ONLY public.categoria DROP CONSTRAINT categoria_id_pase_diario_fkey;
       public       postgres    false    2015    187    186            �           2606    49460    cliente_id_suscripcion_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.cliente
    ADD CONSTRAINT cliente_id_suscripcion_fkey FOREIGN KEY (id_suscripcion) REFERENCES public.suscripcion(id_suscripcion);
 M   ALTER TABLE ONLY public.cliente DROP CONSTRAINT cliente_id_suscripcion_fkey;
       public       postgres    false    2007    182    181            �           2606    49504    pase_diario_id_cliente_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.pase_diario
    ADD CONSTRAINT pase_diario_id_cliente_fkey FOREIGN KEY (id_cliente) REFERENCES public.cliente(id_cliente);
 Q   ALTER TABLE ONLY public.pase_diario DROP CONSTRAINT pase_diario_id_cliente_fkey;
       public       postgres    false    186    182    2009            �           2606    49470    transaccion_id_cliente_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.transaccion
    ADD CONSTRAINT transaccion_id_cliente_fkey FOREIGN KEY (id_cliente) REFERENCES public.cliente(id_cliente);
 Q   ALTER TABLE ONLY public.transaccion DROP CONSTRAINT transaccion_id_cliente_fkey;
       public       postgres    false    182    183    2009            �           2606    49494    venta_id_producto_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.venta
    ADD CONSTRAINT venta_id_producto_fkey FOREIGN KEY (id_producto) REFERENCES public.producto(id_producto);
 F   ALTER TABLE ONLY public.venta DROP CONSTRAINT venta_id_producto_fkey;
       public       postgres    false    184    185    2013            �           2606    49489    venta_id_transaccion_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.venta
    ADD CONSTRAINT venta_id_transaccion_fkey FOREIGN KEY (id_transaccion) REFERENCES public.transaccion(id_transaccion);
 I   ALTER TABLE ONLY public.venta DROP CONSTRAINT venta_id_transaccion_fkey;
       public       postgres    false    2011    183    185            `   b   x�3�4�LJ��IUH�+)J-I��L��4200�2J%��'�Wp��9�8�3����y�& E&�Ɯ���f�%C��r�p����p��x1z\\\ ���      [   �  x���=O�0������G6
U�J�*�:���U��X8�����c\>L]���O�(���0X�]%����K%�!�� �"�D��c���K���!�bv����C+^fWp���pO�EAK�p[�a��B�-�y�;4%�������E9�0�ɖ01���������!afx�ɺ�{�QdO'�z�F�˂����m�LF`��1�13b�+{0'2n� hH)�[{����Mş�����:�M,:	g�� ]]ď�t4,c�͵�(���o51G�&aIL��+%���B�9?�XX�ҹ�F��߁s��R�W�����~�-bI�aŠ.C�� k�ʕ� b���%C*ŭ��#H�m�3�Fu9���%\��K���a�1-��1��d��bw���wiX�B�N�7�2���`�{.jԥ�0;�9BM�:T<b������{      _   u   x�3�4�4200 F�� ę�������WR�Z������eTel��*1�(?)��˘ӈ��CN���l�df^:�	�1�������f�%s�r�p�!��q����p��qqq u�$�      ]   �   x�=�A� ��+|A
0��/��n���y@��m��A�/0Zke1��(v[L���}G��(Gg\�6J<5����c�#��������7&�U~b���I�O���ꚿ8	7R���F_�JR&ω�M)�q�49      Z   k   x�M�;�0C��9���aX��J! �r~�g���g[v����JKV��.���l�-HLylI^�n�H���L��m��C�{ؕ��%�`�/��fp㍦
/ͺ(~      \   F   x�M���0���(q�����s Bj*������7ؠU7v�����@�ʘ{'���ޚ���}�| (�`      ^   5   x���	  ���0Bkպ���a�A(HROEY�Ei���ߴ�r�7$}Ԓ      
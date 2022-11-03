create database jogo_do_bicho;
create user 'admin_bicho'@'localhost' identified by '12345678';
grant all privileges on jogo_do_bicho.* to 'admin_bicho'@'localhost';
flush privileges;

drop database jogo_do_bicho;

commit;
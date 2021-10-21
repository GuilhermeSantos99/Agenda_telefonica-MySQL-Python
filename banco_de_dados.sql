create table if not exists contatos (
id int not null auto_increment,
nome varchar(30) not null unique,
telefone varchar(20) not null unique,
primary key (id)
) default charset utf8;
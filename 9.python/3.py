3.
create table user(
id int comment '编号',
name varchar(50) comment '姓名',
age int comment '年龄',
sex varchar(1) comment '性别',
phone char(13) comment '联系方式'
)comment '用户表';

insert into user (id,name,sex,age,phone)
values (1,'刘一','女',20,'12345678912'),
       (2,'张二','男',18,'23456789123'),
       (3,'李三','男',38,'34567891234'),
       (4,'赵四','女',18,'45678912345'),
       (5,'徐五','女',16,'56789123456'),
       (6,'杨六','男',28,'67891234567'),
       (7,'周七','男',40,'78912345678');











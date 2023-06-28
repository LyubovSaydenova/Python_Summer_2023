drop table if exists book
create table book (
    title varchar,
    author varchar,
    price integer
);
insert into book values
('Война и мир', 'Л.Н.Толстой', 123),
('Евгений Онегин', 'А.С.Пушкин', 234),
('Анна Каренина', 'Л.Н.Толстой', 345),
('Мёртвые души', 'Н.В.Гоголь', 456)
select * from book order by author ASC
select * from book order by price DESC
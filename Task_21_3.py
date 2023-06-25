create table book (
    book_id integer,
    book_title varchar,
	book_author varchar,
	publisher_id integer
);
insert into book values
(1, 'Война и мир', 'Л.Н.Толстой', 123),
(2, 'Евгений Онегин', 'А.С.Пушкин', 234),
(3, 'Анна Каренина', 'Л.Н.Толстой', 345),
(4, 'Мёртвые души', 'Н.В.Гоголь', 456)
select * from book
select * from book where book_author like '%Толстой'
select * from book where book_title like 'Евгений%'
select * from book where publisher_id = 456
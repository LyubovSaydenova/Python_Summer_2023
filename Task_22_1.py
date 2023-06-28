drop table if exists book
create table book (
    title varchar,
    author varchar,
    price integer,
	amount integer
);
insert into book values
('Война и мир', 'Толстой', 300, 5),
('Евгений Онегин', 'Пушкин', 200, 10),
('Анна Каренина', 'Толстой', 250, 4),
('Мёртвые души', 'Гоголь', 200, 7)
select title, author, amount,
	(
	select avg(amount)
	from book
	) as Среднее_количество
from book
where abs(amount - (select avg(amount) from book)) >25;
select * from book order by author asc, price desc
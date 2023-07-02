insert into author values (7, "Маяковский")
update book set author_id = 7 where book_id = 103
create view min_sum_amount as
select min(sum_amount)
from (select sum(amount) as sum_amount from book
group by author_id) query_in
select * from min_sum_amount
select name_author
from author left join book
on author.author_id = book.author_id
group by name_author
having sum(amount) = (select * from min_sum_amount)
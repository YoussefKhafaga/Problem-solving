# Write your MySQL query statement below
select name from Customer where  referee_id != 2 Union all select name from Customer where referee_id IS NULL;
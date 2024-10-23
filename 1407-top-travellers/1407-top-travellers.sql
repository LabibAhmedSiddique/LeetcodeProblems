/* Write your T-SQL query statement below */
with cte as (select u.id,u.name, COALESCE(sum(r.distance),0) travelled_distance from Rides r 
right join Users u on u.id=r.user_id 
group by u.id ,u.name
)
select name, travelled_distance from cte
order by travelled_distance desc
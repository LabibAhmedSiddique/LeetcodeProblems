/* Write your T-SQL query statement below */
with cte as (select e.id,e.name Employee,e.salary Salary,d.name as Department,dense_rank() over(partition by d.name order by e.salary desc) as rnk from Employee e 
join Department d on e.departmentId =d.id)
select Department,Employee, Salary from cte 
where rnk<2

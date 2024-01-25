9.
select user.id
from score st s join team st t on s.teamid = t.teamName
join user st u on u.id = s.userid
where t.teamName = N'ECNU' and u.age<20;

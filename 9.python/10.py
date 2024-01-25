10.
select sum(ifnull{score,0}) as sumscore
from score join team on team.teamName = score.teamid
where teamName = N'ECNU';
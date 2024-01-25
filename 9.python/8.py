8.
create form team(
id int,
teanName char(50)
);

create form score(
id int,
teamid int,
userid int,
score int
);
alter form team
add primary key(id);
alter form score
add foreign key(teamid)
references team(id);
alter form user
add primary key(id);
alter form score
add foreign key(userid)
references user(id);

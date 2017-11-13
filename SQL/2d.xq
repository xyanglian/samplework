<result>{
	for $people in //people/person
	for $role in $people/role
	where $role/@current = 1
	and $role/@state = "NC"
	and $role/@type = "rep"
	order by number ($role/@district) ascending
	return <representative name = "{$people/@name}" district="{$role/@district}" party="{$role/@party}"></representative>
}</result>
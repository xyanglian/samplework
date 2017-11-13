<result>{
	for $people in //people/person
	where not ($people/@id = //committees/committee/member/@id or $people/@id = //committees/committee/subcommittee/member/@id)
	return <person>{$people/@name}</person>
}</result>
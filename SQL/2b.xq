<result>
{
	for $people in //people/person
	where $people/@id = //committees/committee [@code = 'SSAS']/subcommittee[@displayname="Personnel"]/member [@role = 'Chairman']/@id
	return $people
}
</result>
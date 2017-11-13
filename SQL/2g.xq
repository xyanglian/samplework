<result>{

	for $party in distinct-values(//people/person/role[@current="1"]/@party)
	return 
	element {$party} {

	element M { attribute count {
	count (//people/person[
	@gender="M" and ./role[@current="1"]/@party=$party])}},

	element F {attribute count{
	count(//people/person[@gender="F" and ./role[@current="1" ]/@party=$party])}}
	
	

	
	}

}


</result>
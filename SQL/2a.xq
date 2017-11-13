<result>
 {

   for $people in //people/person
  where $people[starts-with (@name, 'Susan')] 
	or $people[starts-with(@name, 'Suzan')]

	return $people

  }
</result>

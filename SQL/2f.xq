<result>{

	for $people in //people/person

	return
	if (some $role in $people/role satisfies
		$role/@party != $people/role[@current = 1]/@party)
	then <member name="{$people/@name}">
		{$people/role [@current = 1]}
		{$people/role[@party != $people/role[@current=1]/@party]}

	</member>

	else ()
	
}
</result>
			
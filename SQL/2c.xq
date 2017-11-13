<result>
{
 
   for $people in //people/person

  return

  if (($people/role[@current='1' and @type="sen"])
	and 
	(some $role in $people/role satisfies
	$role/@startdate < xs:date("1980-01-01") ) )

then <senator name = "{$people/@name}" ></senator>

else()

}
</result>
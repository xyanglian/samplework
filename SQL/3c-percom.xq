		<congress>{
			<house>{
			for $person in /congress/people/person
			where $person/role[@current='1' and @type="rep"]
			return
			  <person name='{$person/@name}'>{
				for $committee in //committees/committee,
					$member in $committee/member
				where $member/@id = $person/@id
				return <committee name="{$committee/@displayname}" role="{if ($member/@role) then $member/@role else 'Member'}">{

					for $subcommittee in $committee/subcommittee,
						$member1 in $subcommittee/member
					where $member1/@id = $person/@id
					return <subcommittee name="{$subcommittee/@displayname}"
										 role="{if ($member/@role) then $member/@role else 'Member'}"/>
				}</committee>
			  }</person>
			}</house>,


			<senate>{
			for $person in /congress/people/person
			where $person/role[@current='1' and @type="sen"]
			return
			  <person name='{$person/@name}'>{
				for $committee in //committees/committee,
					$member in $committee/member
				where $member/@id = $person/@id
				return <committee name="{$committee/@displayname}" role="{if ($member/@role) then $member/@role else 'Member'}">{
					for $subcommittee in $committee/subcommittee,
						$member1 in $subcommittee/member
					where $member1/@id = $person/@id
					return <subcommittee name="{$subcommittee/@displayname}"
										 role="{if ($member1/@role) then $member1/@role else 'Member'}"/>
				}</committee>
			  }</person>
			}</senate>

		}</congress>

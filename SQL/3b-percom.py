

import sys
from xml.dom.minidom import parse, getDOMImplementation
parsed = parse(sys.argv[1])
congress = parsed.documentElement
result = getDOMImplementation().createDocument(None, 'congress', None)
hou=result.createElement('house')
sen=result.createElement('senate')
firstelement = result.documentElement
firstelement.appendChild(hou)
firstelement.appendChild(sen)

everyone = congress.getElementsByTagName('person') 
committees = congress.getElementsByTagName('committee') 

for per in everyone:
  personchildnodes = per.childNodes
  for rol in personchildnodes:
    if rol.nodeName=='role' and rol.getAttribute('current') =='1' and rol.getAttribute('type') =='rep':
      person=result.createElement('person')
      name = per.getAttribute('name')
      person.setAttribute('name',name)
      for commit in committees:
        commitchildNodes =commit.childNodes
        for mem in commitchildNodes:
          if mem.nodeName=='member'and mem.getAttribute('id')== per.getAttribute('id'):
            committee = result.createElement('committee')
            committeeName = commit.getAttribute('displayname') 
            committee.setAttribute('name',committeeName)

            if mem.hasAttribute('role') is False:
              committee.setAttribute('role','Member')
            elif mem.hasAttribute('role') is True:
              committee.setAttribute('role',mem.getAttribute('role'))

            for subc in commitchildNodes:
              if subc.nodeName=='subcommittee':
                subcommitteChildNodes = subc.childNodes
                for mem1 in subcommitteChildNodes:
                  if mem1.nodeName=='member' and mem1.getAttribute('id')== per.getAttribute('id'):
                    subcommittee = result.createElement('subcommittee')
                    subcommitteeName = subc.getAttribute('displayname')
                    subcommittee.setAttribute('name',subcommitteeName)

                    if mem1.hasAttribute('role') is False:
                      subcommittee.setAttribute('role','Member')
                    elif mem1.hasAttribute('role') is True:
                      subcommittee.setAttribute('role',mem1.getAttribute('role'))

                    committee.appendChild(subcommittee)
               
                
            person.appendChild(committee)

 
      hou.appendChild(person)

    elif rol.nodeName=='role' and rol.getAttribute('current') =='1' and rol.getAttribute('type') =='sen':

      person=result.createElement('person')
      name = per.getAttribute('name')
      person.setAttribute('name',name)
      for commit in committees:
        commitchildNodes =commit.childNodes
        for mem in commitchildNodes:
          if mem.nodeName=='member'and mem.getAttribute('id')== per.getAttribute('id'):
            committee = result.createElement('committee')
            committeeName = commit.getAttribute('displayname') 
            committee.setAttribute('name',committeeName)
            
            if mem.hasAttribute('role') is False:
              committee.setAttribute('role','Member')

            elif mem.hasAttribute('role') is True:
              committee.setAttribute('role',mem.getAttribute('role'))


            for subc in commitchildNodes:
              if subc.nodeName=='subcommittee':
                subcommitteChildNodes = subc.childNodes
                for mem1 in subcommitteChildNodes:
                  if mem1.nodeName=='member' and mem1.getAttribute('id')== per.getAttribute('id'):
                    subcommittee = result.createElement('subcommittee')
                    subcommitteeName = subc.getAttribute('displayname')
                    subcommittee.setAttribute('name',subcommitteeName)

                    if mem1.hasAttribute('role') is False:
                      subcommittee.setAttribute('role','Member')

                    elif mem1.hasAttribute('role') is True:
                      subcommittee.setAttribute('role',mem1.getAttribute('role'))

                    committee.appendChild(subcommittee)
               
                
            person.appendChild(committee)

 
      sen.appendChild(person)



print(str(result.toprettyxml(indent=' '*4, encoding='utf-8'), 'utf-8'))

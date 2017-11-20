from Person import Person
import DatabaseProvider

person_1 = Person("100009757303780")
person_1.setName("Name1 Surname1")
node_1 = DatabaseProvider.CreatePerson(person_1)

person_2 = Person("86868468458")
person_2.setName("Name2 Surname2")
node_2 = DatabaseProvider.CreatePerson(person_2)

person_3 = Person("56565656", "Name 3 Surname3")
node_3 = DatabaseProvider.CreatePerson(person_3)

DatabaseProvider.MakeFriends(node_1,node_2)
DatabaseProvider.MakeFriends(node_2,node_3)
DatabaseProvider.MakeFriends(node_3,node_1)
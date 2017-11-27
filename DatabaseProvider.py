from py2neo import Graph, Node, Relationship
graph = Graph()

def CreatePersonNode(person):
	existing_person = graph.find_one("Person", "id",person.id)
	if existing_person is None:
		node = Node("Person", name=person.name, id = person.id)
		graph.create(node)
		return node
	else:
		print("Person already exists")
		return existing_person

def MakeFriends(friend_node_1, friend_node_2):
	existing_relation = graph.match_one(friend_node_1, "KNOWS", friend_node_2)
	if existing_relation is None:
		print("Create new relation")
		rel = Relationship(friend_node_1, "KNOWS", friend_node_2)
		graph.create(rel)
	else:
		print("Relationship is already exists")
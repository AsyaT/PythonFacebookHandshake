from py2neo import Graph, Node, Relationship
graph = Graph()

def CreatePerson(person):
	node = Node("Person", name=person.name, id = person.id)
	graph.create(node)
	return node

def MakeFriends(friend_node_1, friend_node_2):
	rel = Relationship(friend_node_1, "KNOWS", friend_node_2)
	graph.create(rel)
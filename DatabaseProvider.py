import Person
from py2neo import Graph, Node, Relationship
graph = Graph()

def CreatePerson(person):
	node = Node("Person", name=person.name, id = person.id)
	return node

def MakeFriends(friend_1, friend_2):
	Relationship(friend_1, "KNOWS", friend_2)
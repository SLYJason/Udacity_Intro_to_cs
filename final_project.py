#!/usr/bin/env python
def create_data_structure(string_input):
    if string_input == '':
        return {}
    network = {}
    string_input = string_input.split('.')
    for index in range(len(string_input)-1):
        user = ''
        if index%2 == 0:
            string1 = string_input[index]
            user = string1[:string1.find(' ')]
            connections = string1[string1.find('to ')+3:].split(', ')
            network[user] = [connections]
        else:
            string2 = string_input[index]
            user = string2[:string2.find(' ')]
            likes = string2[string2.find('play ')+5:].split(', ')
            network[user].append(likes)       
    return network
    
def get_connections(network, user):
    if user not in network:
        return None
    return network[user][0] 
    
def get_games_liked(network, user): 
    if user not in network:
        return None
    return network[user][1]
    
def add_connection(network, user_A, user_B):
    if user_A in network and user_B in network:
        if user_B in network[user_A][0]:
            return network
        else:
	        network[user_A][0].append(user_B)
	        return network
    return False

def add_new_user(network, user, games): 
    if user in network:
        return network
    network[user] = [[],[]]
    network[user][1] = games
    return network

def get_secondary_connections(network, user):
	if user not in network:
	    return None
	secondary_connections = []
	user_primary_connections = network[user][0]
	for e in user_primary_connections:
	    secondary_connections += network[e][0]
	return list(set(secondary_connections))
	
def count_common_connections(network, user_A, user_B):
    if user_A not in network or user_B not in network:
        return False
    common = 0
    for con_A in network[user_A][0]:
        if con_A in network[user_B][0]:
            common += 1
    return common
    
def find_path_to_friend(network, user_A, user_B, path=None):
	# your RECURSIVE solution here!
	if user_A not in network or user_B not in network:
	    return None
	if path is None:
	    path = []
	path = path + [user_A]
	if user_B in network[user_A][0]:
	    return path + [user_B]
	for node in network[user_A][0]:
	    if node not in path:
	        newpath = find_path_to_friend(network, node, user_B, path)
	        if newpath:
	            return newpath
	return None

example_input = "John is connected to Bryant, Debra, Walter.\
John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.\
Bryant is connected to Olive, Ollie, Freda, Mercedes.\
Bryant likes to play City Comptroller: The Fiscal Dilemma, Super Mushroom Man.\
Mercedes is connected to Walter, Robin, Bryant.\
Mercedes likes to play The Legend of Corgi, Pirates in Java Island, Seahorse Adventures.\
Olive is connected to John, Ollie.\
Olive likes to play The Legend of Corgi, Starfleet Commander.\
Debra is connected to Walter, Levi, Jennie, Robin.\
Debra likes to play Seven Schemers, Pirates in Java Island, Dwarves and Swords.\
Walter is connected to John, Levi, Bryant.\
Walter likes to play Seahorse Adventures, Ninja Hamsters, Super Mushroom Man.\
Levi is connected to Ollie, John, Walter.\
Levi likes to play The Legend of Corgi, Seven Schemers, City Comptroller: The Fiscal Dilemma.\
Ollie is connected to Mercedes, Freda, Bryant.\
Ollie likes to play Call of Arms, Dwarves and Swords, The Movie: The Game.\
Jennie is connected to Levi, John, Freda, Robin.\
Jennie likes to play Super Mushroom Man, Dinosaur Diner, Call of Arms.\
Robin is connected to Ollie.\
Robin likes to play Call of Arms, Dwarves and Swords.\
Freda is connected to Olive, John, Debra.\
Freda likes to play Starfleet Commander, Ninja Hamsters, Seahorse Adventures."
network = create_data_structure(example_input)
path = find_path_to_friend(network, 'John', 'Levi')
print path
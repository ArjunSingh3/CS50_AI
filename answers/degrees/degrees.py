import csv
import sys

from util import Node, StackFrontier, QueueFrontier

# Maps names to a set of corresponding person_ids
names = {}

# Maps person_ids to a dictionary of: name, birth, movies (a set of movie_ids)
people = {}

# Maps movie_ids to a dictionary of: title, year, stars (a set of person_ids)
movies = {}


def load_data(directory):
    """
    Load data from CSV files into memory.
    """
    # Load people
    with open(f"{directory}/people.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            people[row["id"]] = {
                "name": row["name"],
                "birth": row["birth"],
                "movies": set()
            }
            if row["name"].lower() not in names:
                names[row["name"].lower()] = {row["id"]}
            else:
                names[row["name"].lower()].add(row["id"])

    # Load movies
    with open(f"{directory}/movies.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            movies[row["id"]] = {
                "title": row["title"],
                "year": row["year"],
                "stars": set()
            }

    # Load stars
    with open(f"{directory}/stars.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                people[row["person_id"]]["movies"].add(row["movie_id"])
                movies[row["movie_id"]]["stars"].add(row["person_id"])
            except KeyError:
                pass


def main():
    if len(sys.argv) > 2:
        sys.exit("Usage: python degrees.py [directory]")
    directory = sys.argv[1] if len(sys.argv) == 2 else "large"

    # Load data from files into memory
    print("Loading data...")
    load_data(directory)
    print("Data loaded.")

    source = person_id_for_name(input("Name: "))
    if source is None:
        sys.exit("Person not found.")
    target = person_id_for_name(input("Name: "))
    if target is None:
        sys.exit("Person not found.")

    path = shortest_path(source, target)

    if path is None:
        print("Not connected.")
    else:
        degrees = len(path)
        print(f"{degrees} degrees of separation.")
        path = [(None, source)] + path
        for i in range(degrees):
            person1 = people[path[i][1]]["name"]
            person2 = people[path[i + 1][1]]["name"]
            movie = movies[path[i + 1][0]]["title"]
            print(f"{i + 1}: {person1} and {person2} starred in {movie}")


def shortest_path(source, target):
    """
    Returns the shortest list of (movie_id, person_id) pairs
    that connect the source to the target.

    If no possible path, returns None.
    """

    # Keep track of the number of states explored
    num_states_explored = 0

    # Initialize frontier to just the starting position
    start = Node(state = source, parent = None, action = None)
    frontier = QueueFrontier()
    frontier.add(start)

    # Initialize an empty explored set
    explored = set()

    """
        # No need to store different paths because BFS will always find
        # the fastest or shortest path from the source to the target
        # Keep Looking until solution is found
    """
    while True:
        # Went through everything and did not reach the destination:
        if frontier.empty():
            raise Exception("No Solution")

        # Choose a node from the frontier
        node = frontier.remove()
        print("Looping Check point 1")
        num_states_explored += 1

        # if the current node is the solution then make two arrays and back track to find the path tha was followed
        """if node.state == target:
            print("Found Solution")
            # movies
            actions = []
            # people
            cells = []
            # solution
            extra = []
            while node.parent is not None:
                actions.append(node.action)
                cells.append(node.state)
                node = node.parent
            actions.reverse()
            cells.reverse()
            
            # Make sure the return type/ Check to see you are returning what you should despite calculating the correct answer
            
            x = zip(actions, cells)
            for movie, person in x:
                extra.append((movie, person))
            return extra"""

        # Add the explored set to the explored set
        # so that it can be found when back tracking
        explored.add(node.state)

        # Add Neighbours to Frontier:
        """
            # This means add the child nodes of the current nodes 
            # This is done to iterate over the tree
            
            # It currently does not work
        """
        print("Adding neighbors to frontier")
        for action, state in neighbors_for_person(node.state):
            #print("Looping through the Neigbors array")
            if not frontier.contains_state(state) and state not in explored:
                #print("Not in frontier and not in explored, hence adding to Queue")
                child = Node(state=state,parent=node, action=action)
                frontier.add(child)
                if child.state == target:
                    #print("Found Solution")
                    # movies
                    actions = []
                    # people
                    cells = []
                    # solution
                    extra = []
                    while child.parent is not None:
                        actions.append(child.action)
                        cells.append(child.state)
                        child = child.parent
                    actions.reverse()
                    cells.reverse()
                    
                    # Make sure the return type/ Check to see you are returning what you should despite calculating the correct answer
                   
                    x = zip(actions,cells)
                    for movie, person in x:
                        extra.append((movie,person))
                    return extra



def person_id_for_name(name):
    """
    Returns the IMDB id for a person's name,
    resolving ambiguities as needed.
    """
    person_ids = list(names.get(name.lower(), set()))
    if len(person_ids) == 0:
       # console.log("🚀 ~ file: degrees.py:193 ~ len(person_ids):", len(person_ids))
        return None
    elif len(person_ids) > 1:
        print(f"Which '{name}'?")
        for person_id in person_ids:
            person = people[person_id]
            name = person["name"]
            birth = person["birth"]
            print(f"ID: {person_id}, Name: {name}, Birth: {birth}")
        try:
            person_id = input("Intended Person ID: ")
            if person_id in person_ids:
                return person_id
        except ValueError:
            pass
        return None
    else:
        return person_ids[0]


def neighbors_for_person(person_id):
    """
    Returns (movie_id, person_id) pairs for people
    who starred with a given person.
    """
    movie_ids = people[person_id]["movies"]
    neighbors = set()
    for movie_id in movie_ids:
        for person_id in movies[movie_id]["stars"]:
            neighbors.add((movie_id, person_id))
    return neighbors


if __name__ == "__main__":
    main()

"""Dijkstra's algorithm: lesson 1.

We will build this slowly. Today we only make a tiny map.
"""


# Think of each letter as a place and each number as the travel cost.
graph = {
    "A": {"B": 4, "C": 1},
    "B": {"D": 1},
    "C": {"B": 2, "D": 5},
    "D": {},
}


print("From A, we can go to:", graph["A"])


# Our first guesses for the cheapest costs.
# We know that staying at A costs 0.
# We have not reached the other places yet, so their cost is infinity.
distances = {
    "A": 0,
    "B": float("inf"),
    "C": float("inf"),
    "D": float("inf"),
}

print("Starting distances:", distances)


# We are standing at A. Let's look at each place we can reach from A.
current_place = "A"
for neighbor, road_cost in graph[current_place].items():
    new_cost = distances[current_place] + road_cost

    # Keep the cheaper price if we found one.
    if new_cost < distances[neighbor]:
        distances[neighbor] = new_cost

print("After checking A:", distances)


# We need to remember which places we have already checked.
# A has already been checked above, so mark it as visited.
visited = {"A"}


def choose_cheapest_unvisited():
    """Return the unvisited place with the smallest known distance."""
    cheapest_place = None
    cheapest_distance = float("inf")

    for place, distance in distances.items():
        if place not in visited and distance < cheapest_distance:
            cheapest_place = place
            cheapest_distance = distance

    return cheapest_place


next_place = choose_cheapest_unvisited()
print("Cheapest unvisited place:", next_place)


# Now visit C and inspect its roads.
visited.add(next_place)
for neighbor, road_cost in graph[next_place].items():
    new_cost = distances[next_place] + road_cost

    if new_cost < distances[neighbor]:
        distances[neighbor] = new_cost

print("Visited places:", visited)
print("Distances after checking C:", distances)


# We can now repeat the same steps until every reachable place is visited.
while True:
    current_place = choose_cheapest_unvisited()

    if current_place is None:
        break

    visited.add(current_place)

    for neighbor, road_cost in graph[current_place].items():
        new_cost = distances[current_place] + road_cost

        if new_cost < distances[neighbor]:
            distances[neighbor] = new_cost

print("Final distances:", distances)


# ---------------------------------------------------------------------------
# Reusable version
# The lesson above stays unchanged. This function packages the same idea so
# we can use it with different graphs and starting places.

def dijkstra(graph, start):
    """Return the cheapest known distance from start to every place."""
    distances = {place: float("inf") for place in graph}
    distances[start] = 0
    visited = set()

    while True:
        current_place = None
        current_distance = float("inf")

        for place, distance in distances.items():
            if place not in visited and distance < current_distance:
                current_place = place
                current_distance = distance

        if current_place is None:
            break

        visited.add(current_place)

        for neighbor, road_cost in graph[current_place].items():
            new_cost = distances[current_place] + road_cost

            if new_cost < distances[neighbor]:
                distances[neighbor] = new_cost

    return distances


print("Reusable function:", dijkstra(graph, "A"))


class Map:
    """A map that can find cheap travel costs."""

    def __init__(self, graph):
        self.graph = graph

    def cheapest_distances_from(self, start):
        return dijkstra(self.graph, start)


city_map = Map(graph)
print("Reusable class:", city_map.cheapest_distances_from("A"))

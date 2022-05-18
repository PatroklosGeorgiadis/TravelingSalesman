import random


class Reproduction:

    def generate_child(self, partner):
        """
        This method is used to generate the child of two members of the current population and return it
        Args:
            self: The first parent
            partner: The second parent
        """
        # single point crossover (random amount of cities from each parent)
        crossover_point = random.randint(1, 3) + 1
        # all the cities that will be used from the 1st parent
        visited = [self[5]]
        for a in range(crossover_point):
            visited.insert(a, self[a])
        # all the cities that will be used, if not already, from the 2nd parent
        partner_cities = [partner[1], partner[2], partner[3], partner[4]]
        for b in range(crossover_point - 1, 4):
            updt_idx = 0
            temp = partner_cities[b]
            partner_cities.pop(b)
            partner_cities.insert(updt_idx, temp)
            updt_idx += 1
        print("visited: " + str(visited) + " partner_cities: " + str(partner_cities))
        # repeat until all cities of the 2nd parent are implemented in the child trip
        for x in range(len(partner_cities)):
            # if the city is already in the child trip, skip
            if partner_cities[x] in visited:
                continue
            else:
                # insert the city in the child trip
                visited.insert(crossover_point, partner_cities[x])
                # increase the index of the next city to be inserted by 1
                crossover_point += 1
        return visited

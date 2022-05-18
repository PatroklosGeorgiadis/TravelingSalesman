class Reproduction:

    def generate_child(self, partner):
        """
        This method is used to generate the child of two members of the current population and return it
        Args:
            self: The first parent
            partner: The second parent
        """
        # single point crossover (2 cities from 1st parent, 2 cities from second)

        # all the cities that will be used from the 1st parent
        visited = [self[0], self[1], self[2], self[5]]
        # all the cities that will be used, if not already, from the 2nd parent
        partner_cities = [partner[3], partner[4], partner[1], partner[2]]
        # repeat until all cities of the 2nd parent are implemented in the child trip
        for x in range(len(partner_cities)):
            # if the city is already in the child trip, skip
            if partner_cities[x] in visited:
                continue
            else:
                # the first time a city from the 2nd parent isn't included, it is inserted as the 4th city in the child
                if len(visited) == 4:
                    visited.insert(3, partner_cities[x])
                # the second time a city from the 2nd parent isn't included, it is inserted as the 5th
                else:
                    visited.insert(4, partner_cities[x])
        return visited

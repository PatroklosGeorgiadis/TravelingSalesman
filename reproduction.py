class Reproduction:

    def generate_child(self, partner):
        #single point crossover (2 cities from 1st parent, 2 cities from second)
        visited = [self[0], self[1], self[2], self[5]]
        partner_cities = [partner[3], partner[4], partner[1], partner[2]]
        for x in range(len(partner_cities)):
            if partner_cities[x] in visited:
                continue
            else:
                if len(visited) == 4:
                    visited.insert(3, partner_cities[x])
                else:
                    visited.insert(4, partner_cities[x])
        return visited

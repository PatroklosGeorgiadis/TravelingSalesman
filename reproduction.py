class Reproduction:

    def generate_child(self, partner):
        visited = [self[0], self[2], self[3], self[5]]
        partner_cities = [partner[4], partner[1], partner[2], partner[3]]
        for x in range(len(partner_cities)):
            if partner_cities[x] in visited:
                continue
            else:
                if len(visited) == 4:
                    visited.insert(3, partner_cities[x])
                else:
                    visited.insert(1, partner_cities[x])
        return visited

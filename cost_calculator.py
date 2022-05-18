# all possible paths and their costs
pathsdict = {
        "AB": 4,
        "AC": 4,
        "AD": 7,
        "AE": 3,
        "BC": 2,
        "BD": 3,
        "BE": 5,
        "CD": 2,
        "CE": 3,
        "DE": 6
    }


class CostCalculator:

    def path_cost(self):
        """
        This method is used to calculate and return the cost of an entire trip, from start to end.
        """
        i = 0
        cost: int = 0
        # until the algorithm crosses all of the paths between the cities on this trip
        while i < len(self) - 2:
            try:
                # search the dictionary pathsdirect, to find the appropriate cost of this path
                path = self[i] + self[i+1]
                cost += pathsdict[path]
            except:
                # if the path can't be found, reverse the order of the cities
                path = self[i + 1] + self[i]
                cost += pathsdict[path]
            i += 1

        return 10/cost


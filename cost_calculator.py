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

    def path_cost(trip):
        i = 0
        cost = 0
        while i < len(trip) - 2:
            try:
                path = trip[i] + trip[i+1]
                cost += pathsdict[path]
            except:
                path = trip[i + 1] + trip[i]
                cost += pathsdict[path]
            i += 1

        return 1/cost

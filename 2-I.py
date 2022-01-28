import itertools as itt
def main():
    portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]

    D = [
            [0,8943,8019,3652,10545],
            [8943,0,2619,6317,2078],
            [8019,2619,0,5836,4939],
            [3652,6317,5836,0,7825],
            [10545,2078,4939,7825,0]
        ]

    shortest_distance, shortest_route, co2 = 10000000, [], 0.020

    routes = list(itt.permutations(portnames))
    for route in routes:
        if (route[0] == portnames[0]):
            distance, num_routes = 0, []
            for city in route:
                num_routes.append(portnames.index(city))
            for i in range(len(num_routes) - 1):
                start_index = num_routes[i]
                end_index = num_routes[i+1]
                distance += D[start_index][end_index]
            if distance < shortest_distance:
                shortest_distance = distance
                shortest_route = route
            emissions = distance * co2
            print(" ".join(route) + " %.1f kg" % emissions)
main()

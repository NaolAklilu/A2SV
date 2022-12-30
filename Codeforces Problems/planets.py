testCases = int(input())

for _ in range(testCases):
    n , c = list(map(int, input().split(" ")))

    orbit_dic = {}
    
    planets = list(map(int, input().split(" ")))
    
    for planet in planets:
        if planet in orbit_dic.keys():
            orbit_dic[planet] += 1
        else:
            orbit_dic[planet] = 1
    
    min_cost = 0
    
    for planet in orbit_dic:
        if orbit_dic[planet] >= c:
            min_cost += c
        else:
            min_cost += orbit_dic[planet]
            
    print(min_cost)

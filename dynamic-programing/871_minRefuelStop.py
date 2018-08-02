for (int i = 0; i <= n; i++) dp[i][0] = startFuel;

for (int i = 0; i < n; i++)
	for (int j = 0; j <= i; j++) {
		if (i >= j+1)
			dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j+1]);
		if (dp[i][j] >= stations[i][0])
			dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + stations[i][1]);
	}

def minRefuelStops(target, startFuel, stations):
    """
    :type target: int
    :type startFuel: int
    :type stations: List[List[int]]
    :rtype: int
    """



    if startFuel >= target:
        return 0
    if len(stations)>0 and startFuel< stations[0][0]:
        return -1

    stations.insert(0, [0, startFuel])

    print(stations)








print(minRefuelStops(100, 10, [[10,60], [20, 30], [30, 30], [60, 40]]))
print(minRefuelStops(1,1,[]))
print(minRefuelStops(100, 1, [[10, 100]]))
print(minRefuelStops(100, 50, [[25, 50], [50, 25]]))
print(minRefuelStops(1000, 299,[[13,21],[26,115],[100,47],[225,99],[299,141],[444,198],[608,190],[636,157],[647,255],[841,123]]))

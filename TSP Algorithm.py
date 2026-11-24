def TSP(curr, visited, cost, dp):
  n = len(cost)

  if len(visited) == n:
    return cost[curr][0]

  key = (curr, tuple(sorted(visited)))
  if key in dp:
    return dp[key]

  ans = float("inf")
  for i in range(n):
    if i not in visited:
      visited.append(i)
      total = cost[curr][i] + TSP(i, visited, cost, dp)
      ans = min(ans, total)
      visited.pop()

  dp[key] = ans
  return ans


def solveTSP(cost):
  dp = {}
  return TSP(0, [0], cost, dp)


if __name__ == "__main__":
  cost_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
  ]
  print("Minimum TSP Cost:", solveTSP(cost_matrix))

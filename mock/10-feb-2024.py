pairs = [["alice", "bob"], ["bob", "charlie"], ["bob", "dave"], ["charan", "varun"]]

from collections import defaultdict

# Map each manager to their employees.
org_structure = defaultdict(list)
for boss, employee in pairs:
    org_structure[boss].append(employee)

all_nodes = set()
employees = set()
for boss, employee in pairs:
    all_nodes.add(boss)
    all_nodes.add(employee)
    employees.add(employee)

# Roots: those who are never employees (they have no boss)
roots = [node for node in all_nodes if node not in employees]


scores = {}

def dfs(employee):
    total = 1  # count the employee
    for subordinate in org_structure[employee]:
        total += dfs(subordinate)
    scores[employee] = total
    return total

# Process each tree in the forest
for root in roots:
    dfs(root)

print(scores)

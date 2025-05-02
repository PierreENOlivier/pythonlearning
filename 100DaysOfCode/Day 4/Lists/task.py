europe_membership = \
    ["Belgium", "France", "Germany",  "Italy", "Luxembourg", "Netherlands",
     "Denmark", "Ireland", "United Kingdom",
     "Greece",
     "Spain", "Portugal"]

print(europe_membership[0])
print(europe_membership[1])
print(europe_membership[-2])

europe_membership[0] = "Tomorrowland"
print(europe_membership)

europe_membership.append("Pierreland")
print(europe_membership)

europe_membership.extend(["Ernestoland", "Babuland"])
print(europe_membership)

europe_membership + ["Newland"]
print(europe_membership)

europe_membership = europe_membership + ["Newland"]
print(europe_membership)

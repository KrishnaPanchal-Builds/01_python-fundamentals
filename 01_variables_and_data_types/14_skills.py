"""
File: 14_sets.py

Project: Unique Skill Analyzer

Concepts Covered:
- Sets
- Adding Elements
- Removing Elements
- Union
- Intersection
- Difference
- Symmetric Difference
- Duplicate Removal
"""

print("=" * 60)
print("UNIQUE SKILL ANALYZER")
print("=" * 60)

candidate_1 = set(
    input(
        "Enter Candidate 1 Skills (comma separated): "
    ).title().split(",")
)

candidate_2 = set(
    input(
        "Enter Candidate 2 Skills (comma separated): "
    ).title().split(",")
)

candidate_1 = {skill.strip() for skill in candidate_1}
candidate_2 = {skill.strip() for skill in candidate_2}

print("\n" + "=" * 60)
print("SKILL ANALYSIS")
print("=" * 60)

print("\nCandidate 1 Skills:")
print(candidate_1)

print("\nCandidate 2 Skills:")
print(candidate_2)

print("\nCommon Skills:")
print(candidate_1.intersection(candidate_2))

print("\nAll Unique Skills:")
print(candidate_1.union(candidate_2))

print("\nSkills Only Candidate 1 Has:")
print(candidate_1.difference(candidate_2))

print("\nSkills Only Candidate 2 Has:")
print(candidate_2.difference(candidate_1))

print("\nNon-Common Skills:")
print(candidate_1.symmetric_difference(candidate_2))

print("\n" + "=" * 60)
print("DUPLICATE REMOVAL DEMO")
print("=" * 60)

skills = [
    "Python",
    "SQL",
    "Python",
    "Pandas",
    "SQL",
    "NumPy",
    "Machine Learning"
]

print("Original List:")
print(skills)

unique_skills = set(skills)

print("\nAfter Removing Duplicates:")
print(unique_skills)

print("\n" + "=" * 60)
print("SET MODIFICATION")
print("=" * 60)

new_skill = input(
    "\nEnter a New Skill to Add: "
).title()

candidate_1.add(new_skill)

print("Updated Candidate 1 Skills:")
print(candidate_1)

remove_skill = input(
    "\nEnter a Skill to Remove: "
).title()

candidate_1.discard(remove_skill)

print("Final Candidate 1 Skills:")
print(candidate_1)

print("\nProgram Completed Successfully.")

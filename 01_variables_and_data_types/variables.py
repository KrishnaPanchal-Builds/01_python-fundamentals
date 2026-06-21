# AI Engineer Journey Tracker

name = "Krishna Panchal"
current_age = 20
target_age = 25

python_skill = 35.5
ml_skill = 0.0

years_remaining = target_age - current_age

print("=" * 50)
print("AI ENGINEERING JOURNEY TRACKER")
print("=" * 50)

print(f"Name: {name}")
print(f"Current Age: {current_age}")
print(f"Target Age: {target_age}")

print("\nCurrent Skills")
print(f"Python Progress: {python_skill}%")
print(f"Machine Learning Progress: {ml_skill}%")

print("\nPlanning")
print(f"Years Remaining Until Target: {years_remaining}")

total_progress = (python_skill + ml_skill) / 2

print(f"Overall Progress Score: {total_progress:.2f}%")

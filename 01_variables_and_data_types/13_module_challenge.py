"""
===============================================================================
File    : 13_module_challenge.py
Project : AI Smart City Management System
Author  : Krishna Panchal

Module Challenge Part 1
Citizen Registration & Digital Identity

Concepts Covered
----------------
✓ Variables
✓ Data Types
✓ Type Casting
✓ User Input
✓ String Operations
✓ Boolean Logic
✓ Identity Operators
✓ Membership Operators
✓ Lists
✓ Dictionaries
===============================================================================
"""

print("=" * 80)
print("AI SMART CITY MANAGEMENT SYSTEM")
print("=" * 80)

# ------------------------------------------------------------------------------
# CITY INFORMATION
# ------------------------------------------------------------------------------

CITY_NAME = "Neo Smart City"
CITY_CODE = "NSC2026"
COUNTRY = "India"

print(f"City Name : {CITY_NAME}")
print(f"City Code : {CITY_CODE}")
print(f"Country   : {COUNTRY}")

print("\n" + "=" * 80)

# ------------------------------------------------------------------------------
# CITIZEN REGISTRATION
# ------------------------------------------------------------------------------

citizen_name = input("Citizen Name              : ").title()

citizen_id = input("Citizen ID                : ").upper()

age = int(
    input("Age                       : ")
)

gender = input(
    "Gender                    : "
).title()

phone = input(
    "Phone Number              : "
)

email = input(
    "Email                     : "
).lower()

occupation = input(
    "Occupation                : "
).title()

area = input(
    "Residential Area          : "
).title()

# ------------------------------------------------------------------------------
# HOUSEHOLD INFORMATION
# ------------------------------------------------------------------------------

family_members = int(
    input("\nNumber of Family Members  : ")
)

house_type = input(
    "House Type (Flat/Villa)   : "
).title()

vehicle_count = int(
    input("Number of Vehicles        : ")
)

# ------------------------------------------------------------------------------
# DIGITAL SERVICES
# ------------------------------------------------------------------------------

print("\nAvailable Smart City Services")

services = [
    "Water Supply",
    "Electricity",
    "Healthcare",
    "Public Transport",
    "Waste Management",
    "Emergency Services"
]

for index, service in enumerate(services, start=1):
    print(f"{index}. {service}")

selected_services = [
    service.strip().title()
    for service in input(
        "\nSubscribed Services (comma separated): "
    ).split(",")
]

# ------------------------------------------------------------------------------
# CITIZEN PROFILE
# ------------------------------------------------------------------------------

citizen_profile = {
    "Name": citizen_name,
    "Citizen ID": citizen_id,
    "Occupation": occupation,
    "Area": area,
    "Family Members": family_members,
    "House Type": house_type,
    "Vehicles": vehicle_count
}

citizen_reference = citizen_profile
citizen_copy = citizen_profile.copy()

# ------------------------------------------------------------------------------
# VALIDATION
# ------------------------------------------------------------------------------

print("\n" + "=" * 80)
print("PROFILE VALIDATION")
print("=" * 80)

email_valid = "@" in email

phone_valid = len(phone) == 10

has_transport = (
    "Public Transport"
    in selected_services
)

has_healthcare = (
    "Healthcare"
    in selected_services
)

print(f"Email Valid             : {email_valid}")
print(f"Phone Valid             : {phone_valid}")
print(f"Uses Public Transport   : {has_transport}")
print(f"Healthcare Registered   : {has_healthcare}")

# ------------------------------------------------------------------------------
# IDENTITY OPERATORS
# ------------------------------------------------------------------------------

print("\n" + "=" * 80)
print("OBJECT IDENTITY")
print("=" * 80)

print(
    f"citizen_profile is citizen_reference : "
    f"{citizen_profile is citizen_reference}"
)

print(
    f"citizen_profile == citizen_copy      : "
    f"{citizen_profile == citizen_copy}"
)

print(
    f"citizen_profile is citizen_copy      : "
    f"{citizen_profile is citizen_copy}"
)

print("\nMemory Addresses")

print(f"Original  : {id(citizen_profile)}")
print(f"Reference : {id(citizen_reference)}")
print(f"Copy      : {id(citizen_copy)}")

# ------------------------------------------------------------------------------
# PROFILE SUMMARY
# ------------------------------------------------------------------------------

print("\n" + "=" * 80)
print("DIGITAL CITIZEN PROFILE")
print("=" * 80)

for key, value in citizen_profile.items():
    print(f"{key:<20}: {value}")

print("\nSubscribed Services")

for service in selected_services:
    print(f"• {service}")

print("\nRegistration Completed Successfully.")

# ===============================================================================
# PART 2 : SMART UTILITIES & RESOURCE ANALYTICS
# ===============================================================================

print("\n" + "=" * 80)
print("SMART UTILITIES & RESOURCE ANALYTICS")
print("=" * 80)

# ------------------------------------------------------------------------------
# MONTHLY RESOURCE CONSUMPTION
# ------------------------------------------------------------------------------

electricity_units = float(
    input("\nMonthly Electricity Consumption (kWh): ")
)

water_usage = float(
    input("Monthly Water Consumption (Litres)   : ")
)

gas_usage = float(
    input("Monthly Cooking Gas Usage (kg)       : ")
)

waste_generated = float(
    input("Monthly Waste Generated (kg)         : ")
)

recycled_waste = float(
    input("Waste Recycled (kg)                  : ")
)

# ------------------------------------------------------------------------------
# SMART TARIFFS
# ------------------------------------------------------------------------------

ELECTRICITY_RATE = 8.50
WATER_RATE = 0.07
GAS_RATE = 95.00
WASTE_COLLECTION_RATE = 12.00

electricity_bill = electricity_units * ELECTRICITY_RATE

water_bill = water_usage * WATER_RATE

gas_bill = gas_usage * GAS_RATE

waste_bill = waste_generated * WASTE_COLLECTION_RATE

total_utility_bill = (
    electricity_bill +
    water_bill +
    gas_bill +
    waste_bill
)

# ------------------------------------------------------------------------------
# RESOURCE ANALYTICS
# ------------------------------------------------------------------------------

recycling_percentage = (
    recycled_waste / waste_generated
) * 100 if waste_generated > 0 else 0

average_daily_electricity = electricity_units / 30

average_daily_water = water_usage / 30

average_daily_gas = gas_usage / 30

# ------------------------------------------------------------------------------
# SUSTAINABILITY SCORE
# ------------------------------------------------------------------------------

sustainability_score = 0

if electricity_units <= 250:
    sustainability_score += 2

if water_usage <= 15000:
    sustainability_score += 2

if recycling_percentage >= 60:
    sustainability_score += 2

if gas_usage <= 25:
    sustainability_score += 2

if vehicle_count <= 1:
    sustainability_score += 2

# ------------------------------------------------------------------------------
# RESOURCE STATUS
# ------------------------------------------------------------------------------

if sustainability_score >= 9:
    sustainability_status = "Excellent"

elif sustainability_score >= 7:
    sustainability_status = "Very Good"

elif sustainability_score >= 5:
    sustainability_status = "Good"

else:
    sustainability_status = "Needs Improvement"

# ------------------------------------------------------------------------------
# SMART UTILITY REPORT
# ------------------------------------------------------------------------------

print("\n" + "=" * 80)
print("MONTHLY SMART UTILITY REPORT")
print("=" * 80)

print(f"Electricity Bill         : ₹{electricity_bill:,.2f}")
print(f"Water Bill               : ₹{water_bill:,.2f}")
print(f"Cooking Gas Bill         : ₹{gas_bill:,.2f}")
print(f"Waste Collection Bill    : ₹{waste_bill:,.2f}")

print("-" * 80)

print(f"Total Utility Bill       : ₹{total_utility_bill:,.2f}")

print("-" * 80)

print(f"Average Daily Electricity: {average_daily_electricity:.2f} kWh")
print(f"Average Daily Water      : {average_daily_water:.2f} Litres")
print(f"Average Daily Gas Usage  : {average_daily_gas:.2f} kg")

print("-" * 80)

print(f"Waste Generated          : {waste_generated:.2f} kg")
print(f"Recycled Waste           : {recycled_waste:.2f} kg")
print(f"Recycling Percentage     : {recycling_percentage:.2f}%")

print("-" * 80)

print(f"Sustainability Score     : {sustainability_score}/10")
print(f"Sustainability Status    : {sustainability_status}")

# ------------------------------------------------------------------------------
# GREEN RECOMMENDATIONS
# ------------------------------------------------------------------------------

recommendations = []

if electricity_units > 250:
    recommendations.append(
        "Reduce electricity usage by using energy-efficient appliances."
    )

if water_usage > 15000:
    recommendations.append(
        "Reduce water consumption and fix any leakages."
    )

if recycling_percentage < 60:
    recommendations.append(
        "Increase household waste segregation and recycling."
    )

if gas_usage > 25:
    recommendations.append(
        "Optimize cooking gas usage through efficient practices."
    )

if vehicle_count > 1:
    recommendations.append(
        "Use public transport or carpool to reduce emissions."
    )

print("\n" + "=" * 80)
print("AI SMART RECOMMENDATIONS")
print("=" * 80)

if recommendations:

    for index, recommendation in enumerate(
        recommendations,
        start=1
    ):
        print(f"{index}. {recommendation}")

else:
    print("Excellent! Your household demonstrates sustainable resource usage.")

print("\nPart 2 Completed Successfully.")

# ===============================================================================
# PART 3 : TRANSPORTATION, SAFETY & SMART CITY ANALYTICS
# ===============================================================================

print("\n" + "=" * 80)
print("TRANSPORTATION, SAFETY & SMART CITY ANALYTICS")
print("=" * 80)

# ------------------------------------------------------------------------------
# TRANSPORTATION DETAILS
# ------------------------------------------------------------------------------

monthly_public_transport_trips = int(
    input("\nPublic Transport Trips Per Month : ")
)

monthly_private_vehicle_trips = int(
    input("Private Vehicle Trips Per Month  : ")
)

monthly_cycling_walk_trips = int(
    input("Walking/Cycling Trips Per Month  : ")
)

# ------------------------------------------------------------------------------
# SAFETY & EMERGENCY
# ------------------------------------------------------------------------------

emergency_contact_registered = (
    input("\nEmergency Contact Registered (yes/no): ")
    .strip()
    .lower() == "yes"
)

first_aid_trained = (
    input("First Aid Training Completed (yes/no): ")
    .strip()
    .lower() == "yes"
)

disaster_alert_subscription = (
    input("Subscribed to Disaster Alerts (yes/no): ")
    .strip()
    .lower() == "yes"
)

# ------------------------------------------------------------------------------
# ENVIRONMENTAL PARTICIPATION
# ------------------------------------------------------------------------------

trees_planted = int(
    input("\nTrees Planted This Year : ")
)

community_events = int(
    input("Community Events Joined : ")
)

# ------------------------------------------------------------------------------
# DIGITAL SERVICES
# ------------------------------------------------------------------------------

digital_payments = int(
    input("\nDigital Payments This Month : ")
)

online_city_services = int(
    input("Online City Services Used   : ")
)

# ------------------------------------------------------------------------------
# SMART CITY SCORE
# ------------------------------------------------------------------------------

smart_city_score = 0

if monthly_public_transport_trips >= 20:
    smart_city_score += 2

if monthly_cycling_walk_trips >= 15:
    smart_city_score += 2

if emergency_contact_registered:
    smart_city_score += 1

if first_aid_trained:
    smart_city_score += 1

if disaster_alert_subscription:
    smart_city_score += 1

if trees_planted >= 5:
    smart_city_score += 1

if community_events >= 3:
    smart_city_score += 1

if digital_payments >= 20:
    smart_city_score += 1

# ------------------------------------------------------------------------------
# SMART CITIZEN STATUS
# ------------------------------------------------------------------------------

if smart_city_score >= 9:
    citizen_status = "Smart Citizen Champion"

elif smart_city_score >= 7:
    citizen_status = "Highly Responsible Citizen"

elif smart_city_score >= 5:
    citizen_status = "Responsible Citizen"

else:
    citizen_status = "Needs More Participation"

# ------------------------------------------------------------------------------
# CARBON FOOTPRINT (SIMPLIFIED)
# ------------------------------------------------------------------------------

estimated_carbon_points = (
    monthly_private_vehicle_trips * 2
    - monthly_public_transport_trips
    - monthly_cycling_walk_trips
)

estimated_carbon_points = max(0, estimated_carbon_points)

# ------------------------------------------------------------------------------
# SMART CITY REPORT
# ------------------------------------------------------------------------------

print("\n" + "=" * 80)
print("SMART CITY REPORT")
print("=" * 80)

print(f"Public Transport Trips      : {monthly_public_transport_trips}")
print(f"Private Vehicle Trips       : {monthly_private_vehicle_trips}")
print(f"Walking/Cycling Trips       : {monthly_cycling_walk_trips}")

print("-" * 80)

print(f"Emergency Contact           : {emergency_contact_registered}")
print(f"First Aid Trained           : {first_aid_trained}")
print(f"Disaster Alert Subscriber   : {disaster_alert_subscription}")

print("-" * 80)

print(f"Trees Planted               : {trees_planted}")
print(f"Community Events            : {community_events}")

print("-" * 80)

print(f"Digital Payments            : {digital_payments}")
print(f"Online City Services Used   : {online_city_services}")

print("-" * 80)

print(f"Estimated Carbon Points     : {estimated_carbon_points}")
print(f"Smart City Score            : {smart_city_score}/10")
print(f"Citizen Status              : {citizen_status}")

# ------------------------------------------------------------------------------
# IMPROVEMENT SUGGESTIONS
# ------------------------------------------------------------------------------

suggestions = []

if monthly_public_transport_trips < 20:
    suggestions.append("Use public transport more frequently.")

if monthly_cycling_walk_trips < 15:
    suggestions.append("Walk or cycle for short-distance travel.")

if not first_aid_trained:
    suggestions.append("Complete a certified first-aid course.")

if not disaster_alert_subscription:
    suggestions.append("Subscribe to the city's disaster alert system.")

if trees_planted < 5:
    suggestions.append("Participate in tree plantation drives.")

if community_events < 3:
    suggestions.append("Join more community initiatives.")

print("\n" + "=" * 80)
print("SMART CITY SUGGESTIONS")
print("=" * 80)

if suggestions:
    for index, suggestion in enumerate(suggestions, start=1):
        print(f"{index}. {suggestion}")
else:
    print("Outstanding! You are an exemplary smart citizen.")

print("\nPart 3 Completed Successfully.")

# ===============================================================================
# PART 4 : EXECUTIVE SMART CITY DASHBOARD & FINAL REPORT
# ===============================================================================

print("\n" + "=" * 80)
print("EXECUTIVE SMART CITY DASHBOARD")
print("=" * 80)

# ------------------------------------------------------------------------------
# OVERALL SMART CITY INDEX
# ------------------------------------------------------------------------------

overall_score = (
    sustainability_score +
    smart_city_score
)

maximum_score = 20

overall_percentage = (
    overall_score /
    maximum_score
) * 100

# ------------------------------------------------------------------------------
# CITIZEN CLASSIFICATION
# ------------------------------------------------------------------------------

if overall_percentage >= 90:

    citizen_classification = "Platinum Smart Citizen"

elif overall_percentage >= 80:

    citizen_classification = "Gold Smart Citizen"

elif overall_percentage >= 70:

    citizen_classification = "Silver Smart Citizen"

elif overall_percentage >= 60:

    citizen_classification = "Bronze Smart Citizen"

else:

    citizen_classification = "Developing Smart Citizen"

# ------------------------------------------------------------------------------
# DIGITAL READINESS INDEX
# ------------------------------------------------------------------------------

digital_readiness = sum([

    has_transport,

    has_healthcare,

    emergency_contact_registered,

    disaster_alert_subscription,

    digital_payments >= 20,

    online_city_services >= 5

])

# ------------------------------------------------------------------------------
# GREEN INDEX
# ------------------------------------------------------------------------------

green_index = sum([

    recycling_percentage >= 60,

    electricity_units <= 250,

    water_usage <= 15000,

    trees_planted >= 5,

    monthly_cycling_walk_trips >= 15,

    vehicle_count <= 1

])

# ------------------------------------------------------------------------------
# EXECUTIVE REPORT
# ------------------------------------------------------------------------------

print("\n" + "=" * 80)
print("CITIZEN EXECUTIVE REPORT")
print("=" * 80)

print(f"Citizen Name             : {citizen_name}")
print(f"Citizen ID               : {citizen_id}")
print(f"Occupation               : {occupation}")
print(f"Residential Area         : {area}")

print("-" * 80)

print(f"Utility Bill             : ₹{total_utility_bill:,.2f}")
print(f"Sustainability Score     : {sustainability_score}/10")
print(f"Smart City Score         : {smart_city_score}/10")

print("-" * 80)

print(f"Digital Readiness        : {digital_readiness}/6")
print(f"Green Index              : {green_index}/6")

print("-" * 80)

print(f"Overall Score            : {overall_score}/{maximum_score}")
print(f"Overall Percentage       : {overall_percentage:.2f}%")

print(f"Citizen Category         : {citizen_classification}")

print("=" * 80)

# ------------------------------------------------------------------------------
# ACHIEVEMENTS
# ------------------------------------------------------------------------------

print("SMART CITY ACHIEVEMENTS")
print("-" * 80)

if sustainability_score >= 8:
    print("🌱 Sustainability Champion")

if smart_city_score >= 8:
    print("🏙 Smart Citizen Award")

if recycling_percentage >= 80:
    print("♻ Recycling Excellence")

if trees_planted >= 10:
    print("🌳 Green Ambassador")

if monthly_cycling_walk_trips >= 25:
    print("🚴 Eco Mobility Leader")

if digital_readiness == 6:
    print("💻 Digital Citizen")

print("=" * 80)

# ------------------------------------------------------------------------------
# AI IMPROVEMENT ROADMAP
# ------------------------------------------------------------------------------

print("AI IMPROVEMENT ROADMAP")
print("-" * 80)

roadmap = [

    "Reduce electricity consumption using smart appliances.",

    "Increase rainwater harvesting and water conservation.",

    "Improve household waste segregation.",

    "Plant more trees every year.",

    "Use public transport whenever possible.",

    "Participate in community welfare programs.",

    "Increase usage of digital public services.",

    "Stay prepared for emergencies.",

    "Support renewable energy initiatives.",

    "Encourage sustainable living in your neighborhood."

]

for step, item in enumerate(roadmap, start=1):

    print(f"{step}. {item}")

print("=" * 80)

# ------------------------------------------------------------------------------
# MODULE 1 REVISION CHECKLIST
# ------------------------------------------------------------------------------

print("MODULE 1 REVISION")
print("-" * 80)

concepts = [

    "Variables",

    "Data Types",

    "Type Casting",

    "User Input",

    "String Operations",

    "Mathematical Operations",

    "Boolean Logic",

    "Identity Operators",

    "Membership Operators",

    "Variable Scope",

    "Lists",

    "Tuples",

    "Sets",

    "Dictionaries"

]

for index, concept in enumerate(concepts, start=1):

    print(f"{index}. {concept}")

print("=" * 80)

# ------------------------------------------------------------------------------
# FINAL MESSAGE
# ------------------------------------------------------------------------------

if overall_percentage >= 90:

    final_message = (
        "Outstanding! You are an exemplary smart citizen and a role model "
        "for sustainable urban living."
    )

elif overall_percentage >= 75:

    final_message = (
        "Excellent work! Continue improving your environmental and digital "
        "participation."
    )

elif overall_percentage >= 60:

    final_message = (
        "Good progress. Focus on sustainability and community engagement "
        "to improve further."
    )

else:

    final_message = (
        "This is a solid beginning. Small improvements in daily habits will "
        "make a significant difference over time."
    )

print("FINAL MESSAGE")
print("-" * 80)
print(final_message)

print("\n" + "=" * 80)
print("MODULE CHALLENGE COMPLETED SUCCESSFULLY")
print("CONGRATULATIONS! YOU HAVE COMPLETED MODULE 1")
print("=" * 80)

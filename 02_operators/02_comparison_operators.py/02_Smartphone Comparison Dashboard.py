"""
======================================================================
🐍 Python Fundamentals

Module 02 : Operators

Mini Project : Smartphone Comparison Dashboard

Description:
This project demonstrates the practical use of Python
comparison operators by comparing two smartphones based
on their specifications.

The program analyzes specifications and displays meaningful
comparison results using Boolean expressions.

Concepts Used:
• Equal To (==)
• Not Equal To (!=)
• Greater Than (>)
• Less Than (<)
• Greater Than or Equal To (>=)
• Less Than or Equal To (<=)

Difficulty Level : Beginner
Python Version   : 3.x

Author : Krishna Panchal
======================================================================
"""


# ====================================================================
#             SMARTPHONE COMPARISON DASHBOARD
# ====================================================================

print("=" * 70)
print("              SMARTPHONE COMPARISON DASHBOARD")
print("=" * 70)

print("""
Welcome!

This application compares two smartphones based on their
key specifications.

The comparison results will demonstrate how Python
comparison operators work in real-world applications.

Let's begin!
""")


# ====================================================================
# PHONE 1 DETAILS
# ====================================================================

print("\n" + "=" * 70)
print("📱 PHONE 1 DETAILS")
print("=" * 70)

brand_1 = input("Brand Name                 : ")
model_1 = input("Model Name                 : ")

price_1 = float(input("Price (₹)                  : "))
ram_1 = int(input("RAM (GB)                   : "))
storage_1 = int(input("Storage (GB)               : "))
battery_1 = int(input("Battery Capacity (mAh)     : "))
camera_1 = int(input("Primary Camera (MP)        : "))
display_1 = float(input("Display Size (Inches)      : "))
refresh_rate_1 = int(input("Refresh Rate (Hz)          : "))


# ====================================================================
# PHONE 2 DETAILS
# ====================================================================

print("\n" + "=" * 70)
print("📱 PHONE 2 DETAILS")
print("=" * 70)

brand_2 = input("Brand Name                 : ")
model_2 = input("Model Name                 : ")

price_2 = float(input("Price (₹)                  : "))
ram_2 = int(input("RAM (GB)                   : "))
storage_2 = int(input("Storage (GB)               : "))
battery_2 = int(input("Battery Capacity (mAh)     : "))
camera_2 = int(input("Primary Camera (MP)        : "))
display_2 = float(input("Display Size (Inches)      : "))
refresh_rate_2 = int(input("Refresh Rate (Hz)          : "))


# ====================================================================
# COMPARISON DASHBOARD
# ====================================================================

print("\n" + "=" * 70)
print("             SMARTPHONE COMPARISON REPORT")
print("=" * 70)

print(f"""
Phone 1 : {brand_1} {model_1}
Phone 2 : {brand_2} {model_2}
""")


# ====================================================================
# PRICE COMPARISON
# ====================================================================

print("\n💰 PRICE COMPARISON")
print("-" * 70)

print(f"{brand_1} is more expensive than {brand_2}: {price_1 > price_2}")
print(f"{brand_1} is cheaper than {brand_2}: {price_1 < price_2}")
print(f"Both phones have the same price: {price_1 == price_2}")


# ====================================================================
# RAM COMPARISON
# ====================================================================

print("\n🧠 RAM COMPARISON")
print("-" * 70)

print(f"{brand_1} has more RAM than {brand_2}: {ram_1 > ram_2}")
print(f"Both phones have the same RAM: {ram_1 == ram_2}")


# ====================================================================
# STORAGE COMPARISON
# ====================================================================

print("\n💾 STORAGE COMPARISON")
print("-" * 70)

print(f"{brand_1} has more storage than {brand_2}: {storage_1 > storage_2}")
print(f"Both phones have the same storage: {storage_1 == storage_2}")


# ====================================================================
# BATTERY COMPARISON
# ====================================================================

print("\n🔋 BATTERY COMPARISON")
print("-" * 70)

print(f"{brand_1} has a larger battery than {brand_2}: {battery_1 > battery_2}")
print(f"Both phones have the same battery capacity: {battery_1 == battery_2}")

# ====================================================================
# CAMERA COMPARISON
# ====================================================================

print("\n📷 CAMERA COMPARISON")
print("-" * 70)

print(f"{brand_1} has a higher camera resolution than {brand_2}: {camera_1 > camera_2}")
print(f"Both phones have the same camera resolution: {camera_1 == camera_2}")

# ====================================================================
# DISPLAY COMPARISON
# ====================================================================

print("\n🖥️ DISPLAY COMPARISON")
print("-" * 70)

print(f"{brand_1} has a larger display than {brand_2}: {display_1 > display_2}")
print(f"Both phones have the same display size: {display_1 == display_2}")

# ====================================================================
# REFRESH RATE COMPARISON
# ====================================================================

print("\n⚡ REFRESH RATE COMPARISON")
print("-" * 70)

print(f"{brand_1} offers a smoother display than {brand_2}: {refresh_rate_1 > refresh_rate_2}")
print(f"Both phones have the same refresh rate: {refresh_rate_1 == refresh_rate_2}")

# ====================================================================
# COMPLETE SPECIFICATION SUMMARY
# ====================================================================

print("\n" + "=" * 70)
print("              COMPLETE SPECIFICATION SUMMARY")
print("=" * 70)

print(f"""
{'Specification':<25}{brand_1 + ' ' + model_1:<20}{brand_2 + ' ' + model_2}

{'Price':<25}₹{price_1:<18,.2f}₹{price_2:<18,.2f}
{'RAM':<25}{str(ram_1) + ' GB':<20}{str(ram_2) + ' GB'}
{'Storage':<25}{str(storage_1) + ' GB':<20}{str(storage_2) + ' GB'}
{'Battery':<25}{str(battery_1) + ' mAh':<20}{str(battery_2) + ' mAh'}
{'Camera':<25}{str(camera_1) + ' MP':<20}{str(camera_2) + ' MP'}
{'Display':<25}{str(display_1) + '"':<20}{str(display_2) + '"'}
{'Refresh Rate':<25}{str(refresh_rate_1) + ' Hz':<20}{str(refresh_rate_2) + ' Hz'}
""")

# ====================================================================
# DASHBOARD SUMMARY
# ====================================================================

print("\n" + "=" * 70)
print("                    DASHBOARD SUMMARY")
print("=" * 70)

print("""
This project demonstrated how comparison operators can be
used to compare real-world data.

Instead of comparing random numbers, we compared smartphone
specifications such as price, RAM, storage, battery,
camera, display, and refresh rate.

Every comparison produced a Boolean result:

✔ True
✔ False

Comparison operators are widely used in product comparison
websites, shopping applications, recommendation systems,
and decision-making software.
""")

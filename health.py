# The role of this AI is to track the health of a person.
# Cups of water drunk.
# Balanced Diet.
# Track the type of food you eat.
# Determines the  type of food,
# Amount of food you should take.
# Recommend healthy foods to take.

# A basic function-based Health Tracking AI

# --- MOCK FOOD DATABASE ---
# The AI needs "knowledge" to determine food types and amounts.
FOOD_DATABASE = {
    "apple": {"type": "Fruit", "carbs": 25, "protein": 0, "vitamins": 10, "portion": "1 medium apple"},
    "chicken": {"type": "Lean Meat", "carbs": 0, "protein": 30, "vitamins": 2, "portion": "150g (about the size of your palm)"},
    "rice": {"type": "Grain/Carbohydrate", "carbs": 45, "protein": 4, "vitamins": 0, "portion": "1 cup cooked"},
    "broccoli": {"type": "Vegetable", "carbs": 6, "protein": 3, "vitamins": 15, "portion": "1 cup chopped"},
    "salmon": {"type": "Fish/Healthy Fat", "carbs": 0, "protein": 25, "vitamins": 5, "portion": "120g fillet"},
    "oats": {"type": "Grain/Carbohydrate", "carbs": 27, "protein": 5, "vitamins": 1, "portion": "1/2 cup dry"}
}

def track_water(current_cups, new_cups):
    """Tracks water intake and gives hydration feedback."""
    total_cups = current_cups + new_cups
    
    print(f"\n--- Hydration Check ---")
    print(f"Total cups drunk today: {total_cups}")
    
    if total_cups < 4:
        print("Warning: You are dehydrated! Please drink more water immediately.")
    elif total_cups < 8:
        print(f"Good start, but you need {8 - total_cups} more cups to hit your daily goal.")
    elif total_cups == 8:
        print("Perfect! You hit your daily goal of 8 cups. Keep it up!")
    elif total_cups <= 12:
        print("Great job staying hydrated!")
    else:
        print("You might be overhydrating. Slow down on the water to avoid flushing out electrolytes.")
        
    return total_cups

def analyze_and_log_food(food_name, health_profile):
    """Determines food type, portion size, and logs macros to the health profile."""
    food_name = food_name.lower().strip()
    
    print(f"\n--- Analyzing Food ---")
    
    # Check if the AI knows about the food
    if food_name not in FOOD_DATABASE:
        print(f"Error: I don't have data for '{food_name}'.")
        print(f"Known foods: {', '.join(FOOD_DATABASE.keys())}")
        return health_profile

    food_data = FOOD_DATABASE[food_name]
    
    # 1. Determine type and amount
    print(f"Food Type: {food_data['type']}")
    print(f"Recommended Amount: {food_data['portion']}")
    
    # 2. Log the nutritional data
    health_profile['carbs'] += food_data['carbs']
    health_profile['proteins'] += food_data['protein']
    health_profile['vitamins'] += food_data['vitamins']
    health_profile['meals_eaten'].append(food_name)
    
    # 3. Give immediate feedback on the specific food
    if food_data['carbs'] > 30:
        print("Note: This is high in carbohydrates. Good for energy, but watch your portions if you are sitting all day.")
    elif food_data['protein'] > 20:
        print("Note: Excellent protein source! Great for muscle repair and keeping you full.")
    elif food_data['vitamins'] > 10:
        print("Note: Very high in vitamins and micronutrients. Excellent choice!")
        
    return health_profile

def recommend_healthy_foods(health_profile):
    """Analyzes the daily intake and recommends what to eat next."""
    print("\n--- AI Dietary Recommendations ---")
    
    recommendations = []
    
    # Check Protein
    if health_profile['proteins'] < 40:
        recommendations.append("You need more protein. Try eating 'chicken' or 'salmon'.")
    elif health_profile['proteins'] > 100:
        recommendations.append("You've had plenty of protein today. Focus on veggies next.")
        
    # Check Vitamins
    if health_profile['vitamins'] < 15:
        recommendations.append("Your vitamin intake is low. Add some 'broccoli' or an 'apple'.")
        
    # Check Carbs
    if health_profile['carbs'] < 30:
        recommendations.append("You need more energy (carbs). Have some 'rice' or 'oats'.")
    elif health_profile['carbs'] > 120:
        recommendations.append("You've had enough carbs today. Stick to proteins and vegetables.")
        
    # Print results
    if not recommendations:
        print("Your diet looks incredibly well-balanced today! Keep it up.")
    else:
        for rec in recommendations:
            print(f"-> {rec}")

def view_summary(health_profile):
    """Prints a summary of the day's tracking."""
    print("\n--- Daily Health Summary ---")
    print(f"Water: {health_profile['water_cups']} cups")
    print(f"Total Carbs: {health_profile['carbs']}g")
    print(f"Total Protein: {health_profile['proteins']}g")
    print(f"Total Vitamins: {health_profile['vitamins']} units")
    print(f"Foods eaten: {', '.join(health_profile['meals_eaten']) if health_profile['meals_eaten'] else 'None yet'}")
    print("-" * 30)

def main():
    """The main interactive loop for the AI."""
    # Initialize the user's health profile (acts as our memory)
    health_profile = {
        "water_cups": 0,
        "carbs": 0,
        "proteins": 0,
        "vitamins": 0,
        "meals_eaten": []
    }
    
    print("Welcome to your Personal Health AI!")
    
    while True:
        print("\nWhat would you like to do?")
        print("1. Log water intake")
        print("2. Log food eaten")
        print("3. Get food recommendations")
        print("4. View daily summary")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            try:
                cups = int(input("How many cups of water did you just drink? "))
                health_profile['water_cups'] = track_water(health_profile['water_cups'], cups)
            except ValueError:
                print("Error: Please enter a valid number.")
                
        elif choice == '2':
            food = input(f"What did you eat? (Options: {', '.join(FOOD_DATABASE.keys())}): ")
            health_profile = analyze_and_log_food(food, health_profile)
            
        elif choice == '3':
            recommend_healthy_foods(health_profile)
            
        elif choice == '4':
            view_summary(health_profile)
            
        elif choice == '5':
            print("Stay healthy! Goodbye.")
            break
            
        else:
            print("Invalid choice. Please select 1 through 5.")

# This ensures the program runs when the file is executed
if __name__ == "__main__":
    main()
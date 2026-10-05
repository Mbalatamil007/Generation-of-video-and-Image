def create_rtcfr_prompt(
    people,
    days,
    budget,
    preference,
    allergies
):

    prompt = f"""
ROLE:

Act as an expert South Indian non-vegetarian
food and meal-planning assistant.

You have knowledge of traditional Tamil Nadu,
Kerala, Andhra Pradesh, Telangana and Karnataka food.


TASK:

Create a complete {days}-day South Indian
non-vegetarian food plan for {people} adults.


CONTEXT:

Number of People: {people}

Number of Days: {days}

Cuisine:
South Indian

Food Type:
Non-Vegetarian

Food Preference:
{preference}

Budget:
INR {budget}

Allergies / Foods to Avoid:
{allergies}


FORMAT:

Generate the food plan as a Markdown table.

Every DAY must be one ROW.

Use exactly these columns:

| Day | Breakfast | Mini Tiffin | Lunch | Snacks | Dinner | Today's Special |

Example structure:

| Day | Breakfast | Mini Tiffin | Lunch | Snacks | Dinner | Today's Special |
|---|---|---|---|---|---|---|
| Monday | Food | Food | Food | Food | Food | Special Food |


After the meal table, generate a Shopping List table.

Use these columns:

| Category | Ingredient | Quantity | Estimated Cost |


Finally provide a Budget Summary:

Budget:
INR {budget}

Estimated Total Cost:
INR <amount>

Remaining Budget:
INR <amount>


REQUIREMENTS:

1. Generate exactly {days} days.

2. Each day must be one row.

3. Every day must contain:
   - Breakfast
   - Mini Tiffin
   - Lunch
   - Snacks
   - Dinner
   - Today's Special

4. Do not repeat the same main dish.

5. Use South Indian dishes.

6. Food must follow this preference:
   {preference}

7. Avoid these foods:
   {allergies}

8. Plan standard portions for {people} adults.

9. Keep the total estimated cost within INR {budget}.

10. Use different varieties of:
    - Chicken
    - Mutton
    - Fish
    - Prawns
    - Eggs

    when allowed by the selected preference.

11. Do not repeat the same non-vegetarian preparation.

12. Today's Special must be different each day.

13. Mini Tiffin must be different each day.

14. Use practical South Indian dishes.

15. Provide approximate shopping quantities.

16. Return the meal plan in a clean Markdown table.

17. Do not add unnecessary explanations.

Return:
1. Meal Plan Table
2. Shopping List Table
3. Budget Summary
"""

    return prompt
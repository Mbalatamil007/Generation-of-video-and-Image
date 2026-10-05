from rtcfr_prompt import create_rtcfr_prompt
from meal_generator import generate_meal_plan
from validator import validate_inputs


def main():
    print("=" * 70)
    print(" AI-POWERED SOUTH INDIAN NON-VEGETARIAN MEAL PLANNER")
    print(" RTCFR Framework + Python + Ollama + Qwen3:1.7B")
    print("=" * 70)

    try:
        # User inputs
        people = int(input("\nEnter number of people: "))
        days = int(input("Enter number of days (1-7): "))
        budget = int(input("Enter total budget in INR: "))

        preference = input(
            "Enter food preference "
            "(Chicken/Mutton/Fish/Prawns/Eggs/All): "
        ).strip()

        allergies = input(
            "Enter allergies or foods to avoid "
            "(Enter None if no allergies): "
        ).strip()

        # Validate input
        valid, message = validate_inputs(
            people,
            days,
            budget,
            preference
        )

        if not valid:
            print("\nInput Error:")
            print(message)
            return

        print("\nInput validation successful.")

        # Create RTCFR prompt
        print("Creating RTCFR prompt...")

        prompt = create_rtcfr_prompt(
            people,
            days,
            budget,
            preference,
            allergies
        )

        # Generate meal plan
        print("Sending request to Ollama qwen3:1.7b...")
        print("Please wait while the meal plan is generated...\n")

        meal_plan = generate_meal_plan(prompt)

        # Display result
        print("=" * 70)
        print(" GENERATED SOUTH INDIAN MEAL PLAN")
        print("=" * 70)

        print(meal_plan)

        print("\n" + "=" * 70)
        print(" Meal plan generation completed.")
        print("=" * 70)

    except ValueError:
        print(
            "\nInvalid input. Please enter numeric values "
            "for people, days and budget."
        )

    except KeyboardInterrupt:
        print("\n\nApplication stopped by user.")

    except Exception as error:
        print(f"\nUnexpected error: {error}")


if __name__ == "__main__":
    main()
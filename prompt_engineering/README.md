# RTCFR South Indian Food Planner

## Project Title

AI-Powered 7-Day South Indian Non-Vegetarian
Food Planner using RTCFR Framework, Python,
Ollama and Qwen3 1.7B.

## Project Objective

This project uses Generative AI to generate
a personalized South Indian non-vegetarian
food plan.

The application collects:

- Number of people
- Number of days
- Budget
- Food preference
- Allergies / foods to avoid

## Technologies Used

- Python
- Ollama
- Qwen3 1.7B
- RTCFR Prompt Engineering Framework
- Requests
- VS Code
- Git
- GitHub

## RTCFR Framework

### R - Role

Expert South Indian non-vegetarian meal planner.

### T - Task

Generate a personalized 7-day food plan.

### C - Context

The context includes:

- Number of people
- Number of days
- Budget
- South Indian cuisine
- Food preferences
- Allergies

### F - Format

The AI generates:

Day | Breakfast | Mini Tiffin | Lunch | Snacks | Dinner | Today's Special

It also generates:

- Shopping List
- Approximate Quantity
- Estimated Cost
- Remaining Budget

### R - Requirements

- Maximum 7 days
- South Indian food
- Non-vegetarian
- Different dishes
- Avoid repeated main dishes
- Different Mini Tiffin every day
- Different Today's Special every day
- Follow user preferences
- Avoid allergy foods
- Stay within budget

## Architecture

User
  |
  v
app.py
  |
  v
validator.py
  |
  v
rtcfr_prompt.py
  |
  v
RTCFR Prompt
  |
  v
Ollama API
  |
  v
Qwen3 1.7B
  |
  v
meal_generator.py
  |
  v
Generated Meal Plan

## Project Structure

RTCFR-Food-Project/

    app.py
    meal_generator.py
    rtcfr_prompt.py
    validator.py
    7day_food_plan.md
    requirements.txt
    README.md
    .gitignore

## Setup

### Create Virtual Environment

python -m venv venv

### Activate Virtual Environment

Windows:

venv\Scripts\activate

### Install Dependencies

pip install -r requirements.txt

### Check Ollama

ollama --version

### Check Installed Models

ollama list

Make sure the following model is available:

qwen3:1.7b

### Test Qwen

ollama run qwen3:1.7b

### Run Project

python app.py

## Example Input

Number of people:

10

Number of days:

7

Budget:

100000

Food preference:

All

Allergies:

None

## Expected Output

The application generates:

1. 7-Day Meal Plan
2. Breakfast
3. Mini Tiffin
4. Lunch
5. Snacks
6. Dinner
7. Today's Special
8. Shopping List
9. Estimated Cost
10. Remaining Budget

## Sample Food Plan

See:

7day_food_plan.md

## Project Architecture

See the complete project architecture here:

[Project Architecture](project_architecture.md)

## RTCFR Prompt Architecture

![RTCFR Prompt Architecture](rtcfr_prompt_architecture.png)
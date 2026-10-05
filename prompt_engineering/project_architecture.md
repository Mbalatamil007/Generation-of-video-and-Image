# Project Architecture

                     USER
                       │
                       ▼
              ┌─────────────────┐
              │   User Input    │
              │                 │
              │ • No. of people │
              │ • No. of days   │
              │ • Food type     │
              │ • Budget        │
              │ • Allergies     │
              │ • Preferences   │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │ RTCFR Framework │
              │                 │
              │ R → Role        │
              │ T → Task        │
              │ C → Context     │
              │ F → Format      │
              │ R → Requirement │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │ Prompt Builder  │
              │                 │
              │ Creates final   │
              │ structured      │
              │ GenAI prompt    │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │  Ollama / LLM   │
              │  qwen3:1.7b     │
              │                 │
              │ • Analyze input │
              │ • Select foods  │
              │ • Avoid repeats │
              │ • Balance meals │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │Validation Layer │
              │                 │
              │ ✓ 7 days        │
              │ ✓ South Indian  │
              │ ✓ Non-veg       │
              │ ✓ No repetition │
              │ ✓ Budget check  │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │ Final Meal Plan │
              │                 │
              │ • Table Output  │
              │ • Shopping List │
              │ • Cost Estimate │
              └─────────────────┘
def get_weather_advice(weather):
    if weather == "rainy":
        return "Take an umbrella and wear waterproof shoes."
    elif weather == "sunny":
        return "Wear sunglasses and stay hydrated."
    elif weather == "cloudy":
        return "Carry a light jacket just in case."
    elif weather == "snowy":
        return "Dress warmly and allow extra travel time."
    else:
        return "I do not recognize that weather, so prepare for anything."


def get_energy_advice(energy):
    if energy == "high":
        return "Use your energy for the most important or difficult task."
    elif energy == "medium":
        return "Work at a steady pace and take short breaks."
    elif energy == "low":
        return "Start with small tasks and avoid overloading your schedule."
    else:
        return "I do not recognize that energy level, so plan a balanced day."


def get_work_advice(work_today):
    if work_today == "yes":
        return "Review your priorities and focus on your top three tasks."
    elif work_today == "no":
        return "Use the day to rest, reset, or work on a personal goal."
    else:
        return "I do not recognize that answer, so plan your day carefully."


def get_combined_advice(weather, energy, work_today):
    if weather == "rainy" and energy == "low" and work_today == "yes":
        return (
            "Today may feel heavy, so keep your schedule simple "
            "and start with one important task."
        )

    elif weather == "sunny" and energy == "high" and work_today == "no":
        return (
            "This is a great day for exercise, learning, "
            "or working on a personal objective."
        )

    elif energy == "low" and work_today == "no":
        return (
            "Focus on rest, recovery, and maybe play a game "
            "for a little while."
        )

    elif energy == "high" and work_today == "yes":
        return (
            "Use your strong energy to handle your most "
            "challenging task first."
        )

    else:
        return (
            "Balance your day based on your energy, "
            "schedule, and environment."
        )


def run_assistant():
    print("Welcome to the Smart Daily Assistant!")
    print(
        "Answer a few questions and I will recommend "
        "an action for your day.\n"
    )

    weather = input(
        "What is the weather like today? "
        "sunny/rainy/cloudy/snowy: "
    ).strip().lower()

    energy = input(
        "What is your energy level? "
        "high/medium/low: "
    ).strip().lower()

    work_today = input(
        "Do you have work today? yes/no: "
    ).strip().lower()

    weather_advice = get_weather_advice(weather)
    energy_advice = get_energy_advice(energy)
    work_advice = get_work_advice(work_today)
    combined_advice = get_combined_advice(
        weather,
        energy,
        work_today
    )

    print("\nHere is your smart recommendation for today:")
    print("- " + weather_advice)
    print("- " + energy_advice)
    print("- " + work_advice)

    print("\nOverall recommendation:")
    print("- " + combined_advice)


if __name__ == "__main__":
    run_assistant()
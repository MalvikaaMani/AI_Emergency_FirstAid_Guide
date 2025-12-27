def get_readiness_checklist(category: str):
    checklist_map = {
        "🩸 Trauma": [
            "Clean cloth or sterile gauze",
            "Disposable gloves if available",
            "Phone with emergency numbers",
            "Arrange transport to hospital"
        ],
        "❤️ Cardiac": [
            "Keep the person seated and calm",
            "Loosen tight clothing",
            "Phone ready to call emergency services",
            "Aspirin if prescribed and available"
        ],
        "🧠 Neurological": [
            "Keep person still and safe",
            "Note time of symptom onset",
            "Clear surrounding hazards",
            "Emergency contact phone ready"
        ],
        "☠️ Poisoning": [
            "Container of ingested substance",
            "Emergency phone numbers",
            "Do NOT give food or drink",
            "Ensure person is breathing"
        ],
        "🌡 Environmental": [
            "Move to safe temperature-controlled area",
            "Dry blankets or cooling cloths",
            "Water (only if appropriate)",
            "Emergency contact phone ready"
        ]
    }

    return checklist_map.get(
        category,
        [
            "Emergency contact phone ready",
            "Clear surroundings",
            "Stay calm",
            "Arrange medical help"
        ]
    )


def get_timeline_tip(category: str):
    timeline_map = {
        "🩸 Trauma": "⏱ First 5–10 minutes are critical to control bleeding.",
        "❤️ Cardiac": "⏱ The first hour (Golden Hour) is crucial for survival.",
        "🧠 Neurological": "⏱ Immediate action improves recovery chances.",
        "☠️ Poisoning": "⏱ Delays can increase toxin absorption—act immediately.",
        "🌡 Environmental": "⏱ Rapid temperature correction is essential."
    }

    return timeline_map.get(
        category,
        "⏱ Seek medical help as soon as possible."
    )

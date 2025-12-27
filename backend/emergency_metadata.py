def get_emergency_category(query: str) -> str:
    q = query.lower()

    if any(x in q for x in ["bleeding", "burn", "fracture", "dog bite", "snake bite", "cut"]):
        return "🩸 Trauma"

    if any(x in q for x in ["heart", "chest pain", "cardiac"]):
        return "❤️ Cardiac"

    if any(x in q for x in ["stroke", "fainted", "collapsed", "unconscious"]):
        return "🧠 Neurological"

    if any(x in q for x in ["heat", "hypothermia", "cold"]):
        return "🌡 Environmental"

    if any(x in q for x in ["poison", "chemical", "ingestion"]):
        return "☠️ Poisoning"

    return "⚠️ General Emergency"

def get_emergency_severity(query: str, similarity_distance: float) -> str:
    q = query.lower()

    if any(x in q for x in ["heart", "stroke", "snake", "electric", "unconscious"]):
        return "🔴 Critical"

    if similarity_distance < 0.6:
        return "🟠 High"

    if similarity_distance < 1.0:
        return "🟡 Medium"

    return "🟢 Low"


def get_donts(category: str):
    donts_map = {
        "🩸 Trauma": [
            "Do not apply ice directly on open wounds",
            "Do not remove deeply embedded objects",
            "Do not delay emergency services"
        ],
        "❤️ Cardiac": [
            "Do not let the person walk",
            "Do not give food or water",
            "Do not ignore chest pain"
        ],
        "🧠 Neurological": [
            "Do not give food or water",
            "Do not let the person sleep",
            "Do not delay emergency care"
        ],
        "☠️ Poisoning": [
            "Do not induce vomiting",
            "Do not give milk or water unless instructed",
            "Do not wait for symptoms to worsen"
        ],
        "🌡 Environmental": [
            "Do not use hot water suddenly",
            "Do not rub frostbitten skin",
            "Do not give alcohol"
        ]
    }

    return donts_map.get(category, ["Do not delay emergency services"])

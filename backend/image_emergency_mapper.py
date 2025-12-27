def map_medical_label_to_query(label: str):
    """
    Maps CLIP medical label to a RAG-compatible emergency query.
    """
    label = label.lower()

    if "bleeding" in label or "cut" in label:
        return "A person has heavy bleeding from a cut wound"

    if "burn" in label:
        return "A person has severe burn injury"

    if "broken bone" in label:
        return "A person has a fracture or broken bone"
    
    if "redness" in label or "swelling" in label or "skin_rash" in label :
        return "person has skin rash and possible allergic reaction"

    return None

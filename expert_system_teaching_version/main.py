from kb_loader import load_rules
from engine import ForwardChainingEngine

KB_PATH = "kb/laptop_rules.json"

def collect_initial_facts():
    facts = []

    budget = input("What is your budget level for your purchase? (low/medium/high)").lower()
    if budget in ["low", "medium", "high"]:
        facts.append(f"budget_{budget}")
    if input("Is portability important? (y/n): ").lower().startswith("y"):
        facts.append("portable")
    if input("Do you need long battery life? (y/n): ").lower().startswith("y"):
        facts.append("long_battery")
    if input("Will you do gaming? (y/n): ").lower().startswith("y"):
        facts.append("gaming")
    if input("Will you be doing creative work? (y/n): ").lower().startswith("y"):
        facts.append("creative_work")
    if input("Is this office only? (y/n): ").lower().startswith("y"):
        facts.append("office_only")
    pref_os = input("What is your prefered operating system? (windows/mac/linux)").lower()
    if pref_os in ["windows", "mac", "linux"]:
        facts.append(f"pref_os_{pref_os}")
    if input("Do you need AI acceleration? (y/n): ").lower().startswith("y"):
        facts.append("ai_accel")
    if input("Do you want a large screen? (y/n): ").lower().startswith("y"):
        facts.append("large_screen")
    if input("Do you travel often? (y/n): ").lower().startswith("y"):
        facts.append("travel_often")
    return facts

def main():
    # TODO: Load rules, create engine, assert facts, and run inference

    rules = load_rules(KB_PATH)
    facts = collect_initial_facts()
    
    engine = ForwardChainingEngine(rules)
    engine.assert_facts(facts)
    engine.run()

    results = engine.conclusions()

    print("----recommendations ----")
    for rec in results["recommendations"]:
        clean_rec = rec.replace('recommend:','').replace('_',' ').title()
        print(f"{clean_rec}")

    print("----specifications----")
    for spec in results["specifications"]:
        clean_spec = spec.replace('spec','').replace('_',' ').title()
        print(f"{clean_spec}")

    
    pass

if __name__ == "__main__":
    main()

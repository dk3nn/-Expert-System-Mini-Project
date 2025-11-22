from dataclasses import dataclass
from typing import List, Set, Dict, Any

@dataclass
class Rule:
    antecedents: List[str] #if conditions
    consequent: str #then
    priority: int = 0 #importance
    name: str = ""  

class ForwardChainingEngine:
    def __init__(self, rules: List[Rule]):
        self.rules = rules
        self.facts: Set[str] = set()
        self.trace: List[Dict[str, Any]] = []


    def assert_facts(self, initial: List[str]) -> None:
        """Store initial facts into the working memory."""
        self.facts.update(initial)


    def can_fire(self, rule: Rule) -> bool:
        """TODO: Return True if all antecedents are true and consequent not yet known."""


        all_met = all(antecedent in self.facts for antecedent in rule.antecedents)
        consequent_new = rule.consequent not in self.facts
        if rule.consequent.startswith("recommend:") and any(f.startswith("recommend:") for f in self.facts):
            return False
        
        return all_met and consequent_new


    def run(self) -> None:
        """TODO: Implement the forward chaining loop."""
        # while there are rules that can fire:
        #     select one rule (students decide tie-breaking)
        #     add its consequent to facts
        #     record in trace


        changed = True
        while changed:
            changed = False
            
            fireable = [rule for rule in self.rules if self.can_fire(rule)]
          
            fireable.sort(key=lambda r: r.priority, reverse=True)

            for rule in fireable:
            
                self.facts.add(rule.consequent)
                self.trace.append({"rule": rule.name, "fired": rule.consequent, "facts": self.facts.copy()})
                changed = True
                break


    def conclusions(self) -> Dict[str, List[str]]:
        """TODO: Return separated results (recommendations, specs, other facts)."""


        recommendations = [f for f in self.facts if f.startswith("recommend:")]
        specifications = [f for f in self.facts if f.startswith("spec:")]
        other_facts = [f for f in self.facts if f.startswith(("recommend:", "spec:"))]

        return {
            "recommendations": recommendations,
            "specifications": specifications,
            "other_facts": other_facts
        }
        pass

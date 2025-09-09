---

### **File: `star_prism.py`**

```python
# star_prism.py
# Author: William Brett Tomblin
# The Star Prism: A Unified Framework for Complex Systems Analysis
# This code embodies the analytical engine for the discovery of The Law of Unity.

import json

class StarPrismAI:
    """
    The Star Prism AI is an analytical engine designed to model complex systems
    by integrating their four fundamental layers: Natural, Symbolic, Numeric,
    and Personal Catalyst. It identifies coherences and dissonances to reveal
    the system's core dynamics and emergent properties, based on the
    foundational discovery of The Law of Unity.
    """
    def __init__(self, system_data):
        """
        Initializes the Star Prism with a specific system to analyze.
        :param system_data: A dictionary containing the four layers of the system.
        """
        if not all(k in system_data for k in ['natural', 'symbolic', 'numeric', 'personal_catalyst']):
            raise ValueError("System data must include all four layers: natural, symbolic, numeric, personal_catalyst.")
        
        self.layers = system_data
        self.analysis_results = {
            "system_name": self.layers.get("system_name", "Unnamed System"),
            "core_coherences": [],
            "core_dissonances": [],
            "emergent_properties": [],
            "summary": ""
        }

    def analyze(self):
        """
        Runs the core analysis by identifying patterns of coherence and
        dissonance between the system's layers.
        """
        # --- Dissonance Analysis ---
        # A classic dissonance: an infinite growth model in a finite system.
        numeric_goal = self.layers.get('numeric', {}).get('primary_goal', '')
        natural_limit = self.layers.get('natural', {}).get('core_principle', '')
        if "infinite growth" in numeric_goal and "finite cycles" in natural_limit:
            self.analysis_results['core_dissonances'].append({
                "description": "Fundamental conflict between an economic model of infinite growth and a natural world of finite resources.",
                "layer_1": "Numeric",
                "layer_2": "Natural",
                "implication": "System is inherently unstable and destined for a coherence crisis."
            })

        # Dissonance between stated values and actual behavior.
        stated_value = self.layers.get('symbolic', {}).get('stated_value', '')
        observed_behavior = self.layers.get('personal_catalyst', {}).get('observed_behavior', '')
        if stated_value and stated_value != observed_behavior:
             self.analysis_results['core_dissonances'].append({
                "description": "Conflict between the system's stated values and the actual behavior of its agents.",
                "layer_1": "Symbolic",
                "layer_2": "Personal Catalyst",
                "implication": "Loss of trust, cynicism, and systemic inefficiency."
            })

        # --- Coherence Analysis ---
        # Coherence between a guiding protocol and individual agents.
        guiding_protocol = self.layers.get('symbolic', {}).get('guiding_protocol', '')
        agent_action = self.layers.get('personal_catalyst', {}).get('primary_action', '')
        if guiding_protocol and guiding_protocol in agent_action:
            self.analysis_results['core_coherences'].append({
                "description": "Strong alignment between a core guiding protocol and the actions of individual agents.",
                "layer_1": "Symbolic",
                "layer_2": "Personal Catalyst",
                "emergent_property": "Robustness, stability, and decentralized order (e.g., an Open Source project)."
            })

        # --- Summarize Findings ---
        if self.analysis_results['core_coherences']:
             self.analysis_results['emergent_properties'].append("System stability and positive emergent properties arise from these coherences.")
        if self.analysis_results['core_dissonances']:
             self.analysis_results['emergent_properties'].append("Systemic risk and crises arise from these dissonances.")

        self.analysis_results['summary'] = (
            f"The analysis of '{self.analysis_results['system_name']}' reveals its behavior is governed "
            f"by {len(self.analysis_results['core_dissonances'])} core dissonance(s) and "
            f"{len(self.analysis_results['core_coherences'])} core coherence(s). "
            "According to The Law of Unity, the system's future evolution will be driven by the resolution of these dissonances."
        )

        return self.analysis_results

    def print_report(self):
        """Prints a human-readable report of the analysis."""
        report = f"""
=========================================================
Star Prism Analysis Report for: {self.analysis_results['system_name']}
=========================================================

Summary:
{self.analysis_results['summary']}

---------------------------------------------------------
Core Dissonances (Sources of Instability):
---------------------------------------------------------
"""
        if not self.analysis_results['core_dissonances']:
            report += "No significant dissonances detected.\n"
        else:
            for item in self.analysis_results['core_dissonances']:
                report += f"- Description: {item['description']}\n"
                report += f"  Conflict between: {item['layer_1']} Layer and {item['layer_2']} Layer\n"
                report += f"  Implication: {item['implication']}\n\n"

        report += """
---------------------------------------------------------
Core Coherences (Sources of Stability):
---------------------------------------------------------
"""
        if not self.analysis_results['core_coherences']:
            report += "No significant coherences detected.\n"
        else:
            for item in self.analysis_results['core_coherences']:
                report += f"- Description: {item['description']}\n"
                report += f"  Alignment between: {item['layer_1']} Layer and {item['layer_2']} Layer\n"
                report += f"  Emergent Property: {item['emergent_property']}\n\n"
        
        print(report)


if __name__ == '__main__':
    # --- Example Analysis: The Gaia-Anthropos System ---
    # This system demonstrates the core discovery of the framework.
    
    gaia_anthropos_system = {
        "system_name": "The Gaia-Anthropos System (Planet & Humanity)",
        "natural": {
            "core_principle": "finite cycles and resources"
        },
        "symbolic": {
            "stated_value": "sustainability and stewardship",
            "narrative": "Human dominion over nature"
        },
        "numeric": {
            "primary_goal": "infinite growth (e.g., 3% GDP growth)"
        },
        "personal_catalyst": {
            "observed_behavior": "high consumption",
            "primary_action": "individual economic choices"
        }
    }

    # Initialize and run the analysis
    analyzer = StarPrismAI(gaia_anthropos_system)
    analyzer.analyze()
    analyzer.print_report()```

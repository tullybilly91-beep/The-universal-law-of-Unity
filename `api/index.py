```python
from flask import Flask, request, jsonify

# --- Start of StarPrismAI Class ---
class StarPrismAI:
    def __init__(self, system_data):
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
        # A simplified version of your analysis logic for the app
        if "infinite growth" in self.layers.get('numeric', {}).get('primary_goal', '') and "finite cycles" in self.layers.get('natural', {}).get('core_principle', ''):
            self.analysis_results['core_dissonances'].append({
                "description": "Fundamental conflict between an economic model of infinite growth and a natural world of finite resources.",
                "layer_1": "Numeric", "layer_2": "Natural", "implication": "System is inherently unstable and destined for a coherence crisis."
            })
        if self.layers.get('symbolic', {}).get('stated_value', '') and self.layers.get('symbolic', {}).get('stated_value', '') != self.layers.get('personal_catalyst', {}).get('observed_behavior', ''):
             self.analysis_results['core_dissonances'].append({
                "description": "Conflict between the system's stated values and the actual behavior of its agents.",
                "layer_1": "Symbolic", "layer_2": "Personal Catalyst", "implication": "Loss of trust, cynicism, and systemic inefficiency."
            })
        if self.layers.get('symbolic', {}).get('guiding_protocol', '') and self.layers.get('symbolic', {}).get('guiding_protocol', '') in self.layers.get('personal_catalyst', {}).get('primary_action', ''):
            self.analysis_results['core_coherences'].append({
                "description": "Strong alignment between a core guiding protocol and the actions of individual agents.",
                "layer_1": "Symbolic", "layer_2": "Personal Catalyst", "emergent_property": "Robustness, stability, and decentralized order."
            })
        self.analysis_results['summary'] = (f"The analysis of '{self.analysis_results['system_name']}' is complete. According to The Law of Unity, its future will be driven by the resolution of its dissonances.")
        return self.analysis_results
# --- End of StarPrismAI Class ---

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['GET', 'POST'])
def catch_all(path):
    if request.method == 'POST':
        try:
            system_data = request.json
            analyzer = StarPrismAI(system_data)
            results = analyzer.analyze()
            return jsonify(results)
        except Exception as e:
            return jsonify({"error": str(e)}), 400
    # This is what Vercel needs to find the root of the app
    return "Backend for Star Prism AI. This is a serverless function."
```

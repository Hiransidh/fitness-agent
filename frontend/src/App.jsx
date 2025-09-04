import { useState } from "react";
import axios from "axios";

function App() {
  const [goal, setGoal] = useState("");
  const [plan, setPlan] = useState("");

  const getPlan = async () => {
    try {
      const res = await axios.get("http://127.0.0.1:8000/plan", {
        params: { goal },
      });
      setPlan(res.data.plan);
    } catch (err) {
      console.error(err);
      setPlan("Error fetching plan");
    }
  };

  return (
    <div style={{ padding: "30px", fontFamily: "Arial" }}>
      <h2>Fitness & Diet Recommender</h2>
      <input
        type="text"
        placeholder="Enter your goal (e.g. muscle, weight loss)"
        value={goal}
        onChange={(e) => setGoal(e.target.value)}
        style={{ padding: "8px", marginRight: "10px" }}
      />
      <button onClick={getPlan} style={{ padding: "8px 16px" }}>
        Get Plan
      </button>

      {plan && (
        <div style={{ marginTop: "20px", fontWeight: "bold" }}>
          {plan}
        </div>
      )}
    </div>
  );
}

export default App;

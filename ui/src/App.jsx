
import { useEffect, useState } from "react";
import "./App.css";

function App() {
  /* =========================================================
     SIMULATION 1 STATE
  ========================================================= */

  const [simulation1Running, setSimulation1Running] = useState(false);
const [simulation1Paused, setSimulation1Paused] = useState(false);
const [simulation1Stage, setSimulation1Stage] = useState(0);
const [vehiclePosition, setVehiclePosition] = useState(5);
const [vehicleTarget, setVehicleTarget] = useState(5);
  
  /* =========================================================
     SIMULATION 2 STATE
  ========================================================= */

  const [simulation2Running, setSimulation2Running] = useState(false);
  const [simulation2Stage, setSimulation2Stage] = useState(0);

  /* =========================================================
     SIMULATION DATA
  ========================================================= */

  const currentCondition = 61;
  const predictedDeterioration = 14;
  const predictedCondition = 47;
  const repairedCondition = 86;

  /* =========================================================
     SIMULATION 1
  ========================================================= */

  useEffect(() => {
  if (!simulation1Running || simulation1Paused) return;

  const timers = [];

  // Stage 1 - Vehicle starts travelling
  timers.push(
    setTimeout(() => {
      setSimulation1Stage(1);
      setVehicleTarget(20);
    }, 500)
  );

  // Stage 2 - Deterioration detected
  timers.push(
    setTimeout(() => {
      setSimulation1Stage(2);
      setVehicleTarget(40);
    }, 4000)
  );

  // Stage 3 - AI prediction
  timers.push(
    setTimeout(() => {
      setSimulation1Stage(3);
      setVehicleTarget(55);
    }, 7500)
  );

  // Stage 4 - Government alert
  timers.push(
    setTimeout(() => {
      setSimulation1Stage(4);
      setVehicleTarget(65);
    }, 11000)
  );

  // Stage 5 - Inspection and repair
  timers.push(
    setTimeout(() => {
      setSimulation1Stage(5);
      setVehicleTarget(75);
    }, 14500)
  );

  // Stage 6 - Completed
  timers.push(
    setTimeout(() => {
      setSimulation1Stage(6);
      setVehicleTarget(88);
      setSimulation1Running(false);
    }, 18000)
  );

  return () => {
    timers.forEach((timer) => clearTimeout(timer));
  };
}, [simulation1Running, simulation1Paused]);
useEffect(() => {
  if (!simulation1Running || simulation1Paused) return;

  const interval = setInterval(() => {
    setVehiclePosition((current) => {
      if (current >= vehicleTarget) {
        return current;
      }

      return Math.min(current + 0.12, vehicleTarget);
    });
  }, 50);

  return () => clearInterval(interval);
}, [simulation1Running, simulation1Paused, vehicleTarget]);
 
/* =========================================================
   SIMULATION 1 CONTROLS
========================================================= */

const startSimulation1 = () => {
  setSimulation1Stage(0);
  setVehiclePosition(5);
  setVehicleTarget(5);
  setSimulation1Paused(false);
  setSimulation1Running(true);
};

const togglePauseSimulation1 = () => {
  if (!simulation1Running) return;

  setSimulation1Paused((prev) => !prev);
};

const resetSimulation1 = () => {
  setSimulation1Running(false);
  setSimulation1Paused(false);
  setSimulation1Stage(0);
  setVehiclePosition(5);
  setVehicleTarget(5);
};

/* =========================================================
     SIMULATION 2
  ========================================================= */

  useEffect(() => {
    if (!simulation2Running) return;

    const timers = [];

    timers.push(
      setTimeout(() => {
        setSimulation2Stage(1);
      }, 1500)
    );

    timers.push(
      setTimeout(() => {
        setSimulation2Stage(2);
      }, 4000)
    );

    timers.push(
      setTimeout(() => {
        setSimulation2Stage(3);
      }, 6500)
    );

    timers.push(
      setTimeout(() => {
        setSimulation2Stage(4);
      }, 9000)
    );

    timers.push(
      setTimeout(() => {
        setSimulation2Stage(5);
        setSimulation2Running(false);
      }, 11500)
    );

    return () => {
      timers.forEach((timer) => clearTimeout(timer));
    };
  }, [simulation2Running]);


  const startSimulation2 = () => {
    setSimulation2Stage(0);
    setSimulation2Running(true);
  };


  const resetSimulation2 = () => {
    setSimulation2Running(false);
    setSimulation2Stage(0);
  };


  /* =========================================================
     ROAD CLASS
  ========================================================= */

  const getRoadClass = () => {
    return "road-asphalt";
  };


  /* =========================================================
     SIMULATION 2 ROAD DATA
  ========================================================= */

  const roadSections = [
    {
      id: "R-14",
      condition: "Good",
      damage: false,
      type: "normal",
    },
    {
      id: "R-15",
      condition: "Moderate",
      damage: true,
      type: "crack",
    },
    {
      id: "R-16",
      condition: "Poor",
      damage: true,
      type: "pothole",
    },
    {
      id: "R-17",
      condition: "Critical",
      damage: true,
      type: "severe",
    },
    {
      id: "R-18",
      condition: "Good",
      damage: false,
      type: "normal",
    },
  ];


  return (
    <div className="app">

      {/* =====================================================
          HEADER
      ===================================================== */}

      <header className="header">

        <div>
          <div className="logo">
            🛣️ RoadGuard AI
          </div>

          <div className="subtitle">
            AI-Based Road Deterioration Prediction & Preventive Maintenance
          </div>
        </div>

        <div className="status">
          <span className="status-dot"></span>
          Monitoring System
        </div>

      </header>


      <main>

        {/* ===================================================
            HERO
        =================================================== */}

        <section className="hero">

          <div>

            <p className="eyebrow">
              PREDICTIVE ROAD MAINTENANCE
            </p>

            <h1>
              Detect road deterioration
              <br />
              <span>before it becomes severe.</span>
            </h1>

            <p className="hero-text">
              RoadGuard AI uses road history, traffic, rainfall,
              road age and existing damage to predict future
              deterioration and support preventive maintenance.
            </p>

          </div>


          <div className="hero-stat">

            <div className="road-number">
              AI
            </div>

            <div className="road-label">
              Predictive Monitoring
            </div>

            <div className="risk-badge">
              ACTIVE
            </div>

          </div>

        </section>


        {/* ===================================================
            SIMULATION 1
        =================================================== */}

        <section className="simulation-card first-simulation">

          <div className="simulation-top">

            <div>

              <p className="eyebrow">
                SIMULATION 01
              </p>

              <h2>
                🚗 Vehicle Journey & Predictive Maintenance
              </h2>

              <p className="section-description">
                Follow a vehicle travelling through a road section
                while RoadGuard AI monitors its deterioration.
              </p>

            </div>

            

              <div className="simulation-buttons">
  <button onClick={startSimulation1}>
    Start Simulation
  </button>

  <button
    onClick={togglePauseSimulation1}
    disabled={!simulation1Running}
    className="pause-button"
  >
    {simulation1Paused ? "▶ Resume" : "⏸ Pause"}
  </button>

  <button onClick={resetSimulation1}>
    ↻ Reset
  </button>
</div>
          </div>


          {/* PROGRESS */}

          <div className="progress-section">

            <div className="progress-header">

              <span>
                Simulation Progress
              </span>

              <strong>
                {simulation1Stage === 0 && "Ready"}
                {simulation1Stage === 1 && "Vehicle travelling"}
                {simulation1Stage === 2 && "Deterioration detected"}
                {simulation1Stage === 3 && "AI prediction"}
                {simulation1Stage === 4 && "Government alert"}
                {simulation1Stage === 5 && "Inspection & repair"}
                {simulation1Stage === 6 && "Completed"}
              </strong>

            </div>


            <div className="progress-bar">

              <div
                className="progress-fill"
                style={{
                  width: `${(simulation1Stage / 6) * 100}%`,
                }}
              />

            </div>

          </div>


          {/* ROAD */}

          <div className={`road ${getRoadClass()}`}>

            <div className="road-shoulder left"></div>
            <div className="road-shoulder right"></div>

            <div className="road-line"></div>

            {simulation1Stage >= 2 && (
              <>
                <div className="road-crack c1"></div>
                <div className="road-crack c2"></div>
                <div className="road-pothole p1"></div>
                <div className="road-pothole p2"></div>
              </>
            )}

            {simulation1Stage >= 5 && (
              <>
                <div className="repair-patch rp1"></div>
                <div className="repair-patch rp2"></div>
              </>
            )}

            <div
              className="vehicle"
              style={{
                left: `${vehiclePosition}%`,
              }}
            >
              🚗
            </div>

            <div className="road-label-inside">
              ROAD SECTION R-17
            </div>

          </div>


          {/* EVENT */}

          <div className="event-area">

            {simulation1Stage === 0 && (
              <div className="event neutral">
                <div className="event-icon">🚗</div>

                <div>
                  <h3>
                    Vehicle ready
                  </h3>

                  <p>
                    Start the simulation to begin the road journey.
                  </p>
                </div>
              </div>
            )}


            {simulation1Stage === 1 && (
              <div className="event normal">

                <div className="event-icon">
                  🚗
                </div>

                <div>
                  <h3>
                    Vehicle is travelling normally
                  </h3>

                  <p>
                    The road is currently usable while deterioration
                    continues in the background.
                  </p>
                </div>

              </div>
            )}


            {simulation1Stage === 2 && (
              <div className="event warning">

                <div className="event-icon">
                  ⚠️
                </div>

                <div>
                  <h3>
                    Road deterioration detected
                  </h3>

                  <p>
                    Traffic, rainfall, road age and existing damage
                    are contributing to road deterioration.
                  </p>
                </div>

              </div>
            )}


            {simulation1Stage === 3 && (
              <div className="event danger">

                <div className="event-icon">
                  🤖
                </div>

                <div>
                  <h3>
                    AI predicts high deterioration risk
                  </h3>

                  <p>
                    The model predicts significant deterioration
                    during the next six months.
                  </p>
                </div>

              </div>
            )}


            {simulation1Stage === 4 && (
              <div className="event alert">

                <div className="event-icon">
                  🚨
                </div>

                <div>
                  <h3>
                    Government maintenance alert
                  </h3>

                  <p>
                    Road Section R-17 has been flagged for inspection.
                  </p>
                </div>

              </div>
            )}


            {simulation1Stage === 5 && (
              <div className="event maintenance">

                <div className="event-icon">
                  👷
                </div>

                <div>
                  <h3>
                    Inspection and preventive repair
                  </h3>

                  <p>
                    The maintenance team inspects the section
                    and performs simulated repair.
                  </p>
                </div>

              </div>
            )}


            {simulation1Stage === 6 && (
              <div className="event success">

                <div className="event-icon">
                  ✅
                </div>

                <div>
                  <h3>
                    Preventive maintenance completed
                  </h3>

                  <p>
                    Road condition has improved and the vehicle
                    continues through the repaired section.
                  </p>
                </div>

              </div>
            )}

          </div>


          {/* METRICS */}

          <div className="analysis-grid">

            <div className="analysis-card">

              <div className="card-title">
                🤖 AI Prediction
              </div>

              <div className="metrics">

                <div className="metric">
                  <span>Current Condition</span>
                  <strong>{currentCondition}%</strong>
                </div>

                <div className="metric">
                  <span>Predicted Deterioration</span>
                  <strong>
                    {predictedDeterioration} pts
                  </strong>
                </div>

                <div className="metric">
                  <span>Future Condition</span>
                  <strong>
                    {predictedCondition}%
                  </strong>
                </div>

              </div>

            </div>


            <div className="analysis-card">

              <div className="card-title">
                🌦️ Contributing Factors
              </div>

              <div className="factor-row">
                <span>Road Age</span>
                <strong>12 years</strong>
              </div>

              <div className="factor-row">
                <span>Traffic</span>
                <strong>High</strong>
              </div>

              <div className="factor-row">
                <span>Rainfall</span>
                <strong>96 mm</strong>
              </div>

              <div className="factor-row">
                <span>Existing Damage</span>
                <strong>39%</strong>
              </div>

            </div>

          </div>


          {simulation1Stage === 6 && (

            <div className="outcome">

              <p className="eyebrow">
                SIMULATION OUTCOME
              </p>

              <h2>
                Preventive intervention completed
              </h2>

              <div className="before-after">

                <div className="condition-box before">
                  <span>
                    BEFORE REPAIR
                  </span>

                  <strong>
                    {currentCondition}%
                  </strong>

                  <small>
                    High deterioration risk
                  </small>
                </div>


                <div className="arrow">
                  →
                </div>


                <div className="condition-box after">
                  <span>
                    AFTER REPAIR
                  </span>

                  <strong>
                    {repairedCondition}%
                  </strong>

                  <small>
                    Improved road condition
                  </small>
                </div>

              </div>

            </div>

          )}

        </section>


        {/* ===================================================
            SIMULATION 2
        =================================================== */}

        <section className="simulation-card second-simulation">

          <div className="simulation-top">

            <div>

              <p className="eyebrow">
                SIMULATION 02
              </p>

              <h2>
                🗺️ Road Condition Inspection
              </h2>

              <p className="section-description">
                See exactly which road sections are deteriorating
                and where maintenance attention is required.
              </p>

            </div>


            <div className="simulation-actions">

              <button
                className="start-button"
                onClick={startSimulation2}
                disabled={simulation2Running}
              >
                {simulation2Running
                  ? "Scanning Road..."
                  : "▶ Scan Road"}
              </button>

              <button
                className="reset-button"
                onClick={resetSimulation2}
              >
                ↻ Reset
              </button>

            </div>

          </div>


          {/* ROAD MAP */}

          <div className="inspection-road">

            <div className="inspection-road-line"></div>


            {roadSections.map((section, index) => {

              const isActive =
                simulation2Stage >= 2 &&
                section.damage;

              const isCritical =
                simulation2Stage >= 3 &&
                section.id === "R-17";

              const isRepaired =
                simulation2Stage >= 5 &&
                section.id === "R-17";

              return (

                <div
                  key={section.id}
                  className={`road-section
                    ${section.type}
                    ${isActive ? "damaged" : ""}
                    ${isCritical ? "critical" : ""}
                    ${isRepaired ? "repaired" : ""}
                  `}
                >

                  <div className="section-number">
                    {section.id}
                  </div>


                  <div className="section-road">

                    {!isRepaired &&
                      section.type === "crack" &&
                      simulation2Stage >= 2 && (
                        <div className="small-crack">
                          ╱╲╱
                        </div>
                      )
                    }


                    {!isRepaired &&
                      section.type === "pothole" &&
                      simulation2Stage >= 2 && (
                        <>
                          <div className="small-pothole"></div>
                          <div className="small-pothole second"></div>
                        </>
                      )
                    }


                    {!isRepaired &&
                      section.type === "severe" &&
                      simulation2Stage >= 2 && (
                        <>
                          <div className="large-crack">
                            ╱╲╱╲
                          </div>

                          <div className="large-pothole"></div>

                          <div className="warning-marker">
                            ⚠️
                          </div>
                        </>
                      )
                    }


                    {isRepaired && (
                      <div className="section-repair">
                        ✓ REPAIRED
                      </div>
                    )}

                  </div>


                  <div className="condition-label">

                    <span>
                      Condition
                    </span>

                    <strong>
                      {isRepaired
                        ? "Maintained"
                        : section.condition}
                    </strong>

                  </div>

                </div>

              );

            })}

          </div>


          {/* INSPECTION STATUS */}

          <div className="inspection-status">

            {simulation2Stage === 0 && (
              <div className="inspection-message neutral">
                <strong>
                  Road inspection ready
                </strong>

                <span>
                  Start the scan to identify deteriorating sections.
                </span>
              </div>
            )}


            {simulation2Stage === 1 && (
              <div className="inspection-message normal">
                <strong>
                  🔍 Scanning road sections...
                </strong>

                <span>
                  RoadGuard AI is analyzing road-condition data.
                </span>
              </div>
            )}


            {simulation2Stage === 2 && (
              <div className="inspection-message warning">
                <strong>
                  ⚠️ Damaged sections identified
                </strong>

                <span>
                  R-15, R-16 and R-17 show signs of deterioration.
                </span>
              </div>
            )}


            {simulation2Stage === 3 && (
              <div className="inspection-message danger">
                <strong>
                  🚨 R-17 requires immediate inspection
                </strong>

                <span>
                  R-17 has the most severe simulated deterioration.
                </span>
              </div>
            )}


            {simulation2Stage === 4 && (
              <div className="inspection-message alert">
                <strong>
                  👷 Maintenance team assigned to R-17
                </strong>

                <span>
                  The section has been prioritized for preventive maintenance.
                </span>
              </div>
            )}


            {simulation2Stage === 5 && (
              <div className="inspection-message success">
                <strong>
                  ✅ R-17 maintenance completed
                </strong>

                <span>
                  The simulated damaged section has been repaired.
                </span>
              </div>
            )}

          </div>


          {/* LEGEND */}

          <div className="legend">

            <div>
              <span className="legend-dot good"></span>
              Good
            </div>

            <div>
              <span className="legend-dot moderate"></span>
              Moderate
            </div>

            <div>
              <span className="legend-dot poor"></span>
              Poor
            </div>

            <div>
              <span className="legend-dot critical-dot"></span>
              Critical
            </div>

          </div>

        </section>


        {/* ===================================================
            EXPLANATION
        =================================================== */}

        <section className="explanation">

          <p className="eyebrow">
            HOW ROADGUARD AI WORKS
          </p>

          <h2>
            From road history to preventive action
          </h2>

          <div className="workflow">

            <div className="workflow-item">
              <span>01</span>
              <strong>Collect</strong>
              <p>
                Road condition, traffic, rainfall and repair history.
              </p>
            </div>

            <div className="workflow-arrow">
              →
            </div>

            <div className="workflow-item">
              <span>02</span>
              <strong>Predict</strong>
              <p>
                Estimate future deterioration using the ML model.
              </p>
            </div>

            <div className="workflow-arrow">
              →
            </div>

            <div className="workflow-item">
              <span>03</span>
              <strong>Alert</strong>
              <p>
                Identify sections requiring inspection.
              </p>
            </div>

            <div className="workflow-arrow">
              →
            </div>

            <div className="workflow-item">
              <span>04</span>
              <strong>Maintain</strong>
              <p>
                Officials inspect and perform preventive maintenance.
              </p>
            </div>

          </div>

        </section>

      </main>


      <footer>
        RoadGuard AI • Educational predictive road-maintenance simulation
      </footer>

    </div>
  );
}

export default App;

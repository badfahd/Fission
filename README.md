# 3D Nuclear Fission Kinematics Simulation

A computational physics simulation modeling neutron-induced nuclear fission, built in Python using VPython[span_0](start_span)[span_0](end_span)[span_1](start_span)[span_1](end_span). This project models collision detection, multi-body momentum conservation via symmetrical 120° angular fragment separation, and secondary high-energy neutron emission[span_2](start_span)[span_2](end_span)[span_3](start_span)[span_3](end_span).

## 🔬 Physics Model & Architecture

This simulation replicates the core mechanical steps of a neutron-nucleus interaction:

1. **Scene Setup & Initial State:** 
   - A target heavy nucleus (red sphere) is initialized at the coordinate origin `(0, 0, 0)`[span_4](start_span)[span_4](end_span).
   - An incident neutron (white sphere) approaches along a linear trajectory from `(-4, 0, 0)` with a velocity scalar $v = 2$[span_5](start_span)[span_5](end_span).
2. **Collision Detection Engine:** 
   - Uses a continuous time-step loop (`vp.rate(100)` with $dt = 0.01$) to advance the neutron's position[span_6](start_span)[span_6](end_span).
   - Employs vector magnitude checking (`vp.mag(Neutron.pos) <= Nucleus.radius`) to trigger the reaction when the neutron enters the nuclear radius[span_7](start_span)[span_7](end_span)[span_8](start_span)[span_8](end_span).
3. **Fission State Transition & Momentum Conservation:** 
   - Upon impact, the parent objects (`Nucleus` and `Neutron`) are hidden (`visible = False`), and a boolean control flag (`fission_occured = True`) manages the state change[span_9](start_span)[span_9](end_span).
   - Two daughter fragments (`frag_1` and `frag_2`) are spawned at the reaction center[span_10](start_span)[span_10](end_span).
   - Trigonometric vector components using $\pm \pi/3$ radians ($\pm 60^\circ$) ensure a precise **120° angular separation** to conserve momentum[span_11](start_span)[span_11](end_span).
4. **Secondary Neutron Cascades:** 
   - Multiple secondary neutrons (cyan spheres) are dynamically instantiated and assigned varied high-velocity vectors (`vels`) to simulate prompt neutron emission during fission[span_12](start_span)[span_12](end_span).
#OUTPUT:

https://github.com/user-attachments/assets/14f41c1e-fe70-4b30-a668-6b94b628c0b0


---

## 🛠️ Tech Stack & Requirements

* **Language:** Python 3.x
* **3D Graphics & Physics Engine:** VPython (`vpython`)
* **Mathematical Operations:** Python standard `math` library (`cos`, `sin`, `pi`)[span_13](start_span)[span_13](end_span)

---

## 🚀 Getting Started

### Prerequisites
Ensure you have VPython installed in your Python environment:
```bash
pip install vpython

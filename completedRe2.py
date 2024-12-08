import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

# Page Title
st.title("Laminar vs. Turbulent Flow Visualization")
st.write("""
Explore the differences between laminar and turbulent flow by adjusting parameters like velocity, viscosity, and pipe diameter. Learn how the Reynolds number predicts flow behavior!
""")

# Sidebar inputs for parameters
st.sidebar.header("Adjust Flow Parameters")
velocity = st.sidebar.slider("Flow Velocity (m/s)", 0.1, 10.0, 1.0, 0.1)
viscosity = st.sidebar.slider("Fluid Viscosity (Pa·s)", 0.001, 0.1, 0.01, 0.001)
density = st.sidebar.slider("Fluid Density (kg/m³)", 500.0, 1500.0, 1000.0, 10.0)
diameter = st.sidebar.slider("Pipe Diameter (m)", 0.01, 0.5, 0.1, 0.01)

# Calculate Reynolds Number
reynolds_number = (density * velocity * diameter) / viscosity
st.sidebar.write(f"**Reynolds Number**: {reynolds_number:.2f}")

# Display flow type based on Reynolds Number
if reynolds_number < 2000:
    flow_type = "Laminar Flow"
    st.success(f"The flow is **{flow_type}** (Re < 2000).")
elif reynolds_number > 4000:
    flow_type = "Turbulent Flow"
    st.error(f"The flow is **{flow_type}** (Re > 4000).")
else:
    flow_type = "Transitional Flow"
    st.warning(f"The flow is in the **{flow_type}** regime (2000 < Re < 4000).")

# Reynolds Number Concept Section
st.header("What is the Reynolds Number?")
st.write("""
The Reynolds number (Re) is a dimensionless quantity that predicts the flow regime in fluid dynamics. It is calculated using the formula:

$$ Re = \\frac{\\rho v L}{\\mu} $$

where:
- \\( ρ \\): Fluid density (kg/m³)
- \\( v \\): Flow velocity (m/s)
- \\( L \\): Pipe diameter (m)
- \\( µ \\): Fluid viscosity (Pa·s)

### Interpretation of Reynolds Number:
- **Laminar Flow**: Re < 2000 (Smooth and orderly flow)
- **Transitional Flow**: 2000 < Re < 4000 (Mix of laminar and turbulent)
- **Turbulent Flow**: Re > 4000 (Chaotic and irregular flow)
""")

# Include a related picture for the Reynolds number
st.image(
    HEAD
    "/Users/gf/biotransport/Re.png",
    caption="Flow regimes based on Reynolds Number",
    use_column_width=True

    "/Users/gf/Desktop/umass/Biotransport art document/Re.png",
    caption="Flow regimes based on Reynolds Number",
    use_container_width=True
     05262429 (Initial commit of Streamlit app)
)

# Flow Visualization
st.header("Flow Visualization")
def generate_flow_plot(flow_type):
    x = np.linspace(0, 10, 500)
    y = np.sin(x) if flow_type == "Turbulent Flow" else x * 0.1

    fig, ax = plt.subplots(figsize=(6, 4))
    if flow_type == "Laminar Flow":
        for i in np.linspace(0, 1, 10):
            ax.plot(x, y + i, color='blue', linewidth=1.5)
        ax.set_title("Laminar Flow: Smooth Streamlines")
    elif flow_type == "Turbulent Flow":
        for i in np.linspace(0, 1, 10):
            noise = np.random.normal(0, 0.1, len(x))
            ax.plot(x, y + i + noise, color='red', linewidth=1.0)
        ax.set_title("Turbulent Flow: Chaotic Streamlines")
    else:
        for i in np.linspace(0, 1, 10):
            noise = np.random.normal(0, 0.05, len(x))
            ax.plot(x, y + i + noise, color='orange', linewidth=1.2)
        ax.set_title("Transitional Flow: Mix of Laminar and Turbulent")

    ax.set_xlabel("Flow Direction")
    ax.set_ylabel("Streamlines")
    ax.grid(True)
    st.pyplot(fig)

generate_flow_plot(flow_type)

# Particle Movement Animation
st.header("Particle Movement Animation")
st.write("Observe the movement of particles to distinguish between laminar and turbulent flow. The movement dynamically changes based on the Reynolds number.")

fig, ax = plt.subplots(figsize=(6, 4))
ax.set_xlim(0, 10)
ax.set_ylim(0, 5)

# Initialize particle positions
num_particles = st.slider("Number of Particles", 5, 100, 20)
animation_speed = st.slider("Animation Speed", 1, 10, 5)
particles = np.zeros((num_particles, 2))
particles[:, 1] = np.linspace(0.5, 4.5, num_particles)
particles[:, 0] = np.zeros(num_particles)

scat = ax.scatter(particles[:, 0], particles[:, 1], s=50, c='blue')

def update(frame):
    global particles

    if reynolds_number < 2000:  # Laminar flow
        particles[:, 0] += 0.05 * animation_speed
    elif reynolds_number > 4000:  # Turbulent flow
        particles[:, 0] += 0.1 * animation_speed
        particles[:, 1] += np.random.uniform(-0.2, 0.2, num_particles) * (reynolds_number / 4000)
    else:  # Transitional flow
        particles[:, 0] += 0.075 * animation_speed
        particles[:, 1] += np.random.uniform(-0.1, 0.1, num_particles) * (reynolds_number / 4000)

    particles[:, 1] = np.clip(particles[:, 1], 0.5, 4.5)
    particles[:, 0] = particles[:, 0] % 10
    scat.set_offsets(particles)
    return scat,

anim = FuncAnimation(fig, update, frames=200, interval=50, blit=True)

# Save animation as GIF and display
gif_path = "particle_animation.gif"
anim.save(gif_path, writer=PillowWriter(fps=20))
<<<<<<< HEAD
st.image(gif_path, caption=f"Particle Movement ({flow_type}) Based on Reynolds Number", use_column_width=True)
=======
st.image(gif_path, caption=f"Particle Movement ({flow_type}) Based on Reynolds Number", use_container_width=True)
>>>>>>> 05262429 (Initial commit of Streamlit app)

import rebound
import matplotlib.patheffects as pe
from datetime import date
sim = rebound.Simulation()
bodies = ["Sun", "Mercury", "Venus", "Earth", "Mars", "12249", "Jupiter", "Saturn"]
sim.add(bodies)
op1 = rebound.OrbitPlot(sim, particles=[1,2,3,4,6,7],xlim=[-5.5,5.5],ylim=[-5.5,5.5],figsize=(9,9))
op2 = rebound.OrbitPlot(sim, particles=[5], ax=op1.ax, fig=op1.fig, lw=5, color="blue")
op2.particles.set_color(["blue"])
op2.particles.set_edgecolor("black")


for i, n in enumerate(bodies):
    if n == "12249":
        n = "Minor Planet 12249\nHanno Rein\n(1988 SH2)"
    op2.ax.annotate(n, xy=(sim.particles[i].x+0.021, sim.particles[i].y+0.075),path_effects=[pe.withStroke(linewidth=2, foreground="white")])
op2.ax.annotate("Last update: "+str(date.today()), xy=(5, -5),ha="right")
op2.fig.savefig("orbit.png")


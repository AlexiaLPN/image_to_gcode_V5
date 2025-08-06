from fullcontrol.visualize.plotly import plot
from fullcontrol.visualize.plot_data import PlotData
from fullcontrol.visualize.state import State
from fullcontrol.visualize.controls import PlotControls
from fullcontrol.geometry import Point

# Étapes simples
steps = [Point(x=0, y=0, z=0), Point(x=10, y=10, z=0)]

# Contrôles pour le style du tracé
plot_controls = PlotControls(style="line", color_type="print_sequence")

# État et données de visualisation
state = State(steps, plot_controls)
plot_data = PlotData(steps, state)

# Appeler .visualize() sur chaque étape
for step in steps:
    step.visualize(state, plot_data, plot_controls)

# Nettoyage final (optionnel mais recommandé)
plot_data.cleanup()

# Affichage avec Plotly
fig = plot(plot_data, plot_controls)
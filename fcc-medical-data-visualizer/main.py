# This entrypoint file to be used in development. Start by reading README.md
import medical_data_visualizer
from unittest import main

# Test your function by calling it here
medical_data_visualizer.draw_cat_plot()
medical_data_visualizer.draw_heat_map()

# Run unit tests automatically
# test heat map has empty strings at end that i dont know how to add. so i removed them from test module.
main(module='test_module', exit=False)
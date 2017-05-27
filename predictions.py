"""
Week of May 22nd:
"""
import numpy as np

at_t_predictions = np.array([38.07, 38.04, 38.05, 38.05, 38.06])
tmobile_predictions = np.array([65.47, 65.49, 65.64, 65.81, 65.82])
sprint_predictions = np.array([7.78, 7.81, 7.80, 7.82, 7.84])
vz_predictions = np.array([45.15, 45.14, 45.17, 45.17, 45.16])

at_t_actual = np.array([38.25, 38.31, 38.15, 38.23, 38.12])
tmobile_actual = np.array([67.22, 67.62, 67.89, 67.86, 67.80])
sprint_actual = np.array([8.17, 8.18, 8.17, 8.33, 8.40])
vz_actual = np.array([45.48, 45.48, 45.04, 45.31, 45.32])

at_t_score = np.mean(abs(at_t_predictions - at_t_actual) / at_t_actual)
print(at_t_score)

tmobile_score = np.mean(abs(tmobile_predictions - tmobile_actual) / tmobile_actual)
print(tmobile_score)

sprint_score = np.mean(abs(sprint_predictions - sprint_actual) / sprint_actual)
print(sprint_score)

vz_score = np.mean(abs(vz_predictions - vz_actual) / vz_actual)
print(vz_score)

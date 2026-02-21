"""
experiment_core.py

Scientific Engine with Full Transparency & Reproducibility

🇯🇲 Performance Evaluation of Urgency-Aware Edge-Assisted
Security Transmission in Jamaican Motel Infrastructure
"""

import random
import statistics
import math
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# ==========================================================
# GLOBAL CONFIGURATION
# ==========================================================

RANDOM_SEED = 42
random.seed(RANDOM_SEED)

MOTEL_CONFIG = {
    "cameras": 12,
    "door_sensors": 20,
    "alarm_devices": 5
}

SIMULATION_DURATION_MINUTES = 60
MONTE_CARLO_RUNS = 30

CLOUD_LATENCY_MS = 300
EDGE_LATENCY_MS = 50

CLOUD_BANDWIDTH_MBPS = 10
EDGE_BANDWIDTH_MBPS = 100

CLOUD_ENERGY_PER_KB = 0.5
EDGE_ENERGY_PER_KB = 0.1

EDGE_ALERT_METADATA_KB = 5
ROUTINE_COMPRESSION_RATIO = 0.5


# ==========================================================
# EVENT MODEL
# ==========================================================

EVENT_TYPES = [
    ("camera_snapshot", 500, 0.15),
    ("motion_event", 200, 0.10),
    ("door_status", 5, 0.50),
    ("alarm_trigger", 100, 0.05),
    ("routine_ping", 2, 0.20),
]


def generate_event():
    names = [e[0] for e in EVENT_TYPES]
    sizes = [e[1] for e in EVENT_TYPES]
    weights = [e[2] for e in EVENT_TYPES]

    choice = random.choices(range(len(EVENT_TYPES)), weights=weights)[0]

    urgency = 1 if names[choice] in ["alarm_trigger", "motion_event"] else 0

    return names[choice], sizes[choice], urgency


# ==========================================================
# METRIC CALCULATIONS
# ==========================================================

def calculate_cloud_metrics(data_kb):
    latency = CLOUD_LATENCY_MS + (data_kb / CLOUD_BANDWIDTH_MBPS)
    energy = data_kb * CLOUD_ENERGY_PER_KB
    bandwidth = data_kb
    return latency, bandwidth, energy


def calculate_edge_metrics(event_name, data_kb, urgency):

    latency = EDGE_LATENCY_MS + (data_kb / EDGE_BANDWIDTH_MBPS)
    energy = data_kb * EDGE_ENERGY_PER_KB

    if urgency == 1:
        bandwidth = EDGE_ALERT_METADATA_KB
    else:
        bandwidth = data_kb * ROUTINE_COMPRESSION_RATIO

    return latency, bandwidth, energy


# ==========================================================
# MONTE CARLO EXPERIMENT
# ==========================================================

def run_experiment():

    baseline_results = []
    optimized_results = []

    sample_run_log = []
    event_distribution = {e[0]: 0 for e in EVENT_TYPES}

    total_devices = (
        MOTEL_CONFIG["cameras"]
        + MOTEL_CONFIG["door_sensors"]
        + MOTEL_CONFIG["alarm_devices"]
    )

    total_events = total_devices * SIMULATION_DURATION_MINUTES

    for run in range(MONTE_CARLO_RUNS):

        base_lat_total = 0
        opt_lat_total = 0

        base_bw_total = 0
        opt_bw_total = 0

        base_en_total = 0
        opt_en_total = 0

        for event_index in range(total_events):

            name, data_kb, urgency = generate_event()
            event_distribution[name] += 1

            lat_b, bw_b, en_b = calculate_cloud_metrics(data_kb)
            lat_o, bw_o, en_o = calculate_edge_metrics(name, data_kb, urgency)

            base_lat_total += lat_b
            opt_lat_total += lat_o

            base_bw_total += bw_b
            opt_bw_total += bw_o

            base_en_total += en_b
            opt_en_total += en_o

            # Save first 10 events for transparency log
            if run == 0 and event_index < 10:
                sample_run_log.append({
                    "event": name,
                    "data_kb": data_kb,
                    "urgency": urgency,
                    "baseline_latency": round(lat_b, 2),
                    "optimized_latency": round(lat_o, 2),
                    "baseline_bandwidth": round(bw_b, 2),
                    "optimized_bandwidth": round(bw_o, 2)
                })

        baseline_results.append((
            base_lat_total / total_events,
            base_bw_total / total_events,
            base_en_total / total_events
        ))

        optimized_results.append((
            opt_lat_total / total_events,
            opt_bw_total / total_events,
            opt_en_total / total_events
        ))

    return {
        "baseline": baseline_results,
        "optimized": optimized_results,
        "event_distribution": event_distribution,
        "sample_log": sample_run_log,
        "total_events": total_events
    }


# ==========================================================
# PDF EXPORT WITH METHODOLOGY
# ==========================================================

def export_pdf(results):

    doc = SimpleDocTemplate("IoT_Research_Report.pdf")
    styles = getSampleStyleSheet()
    elements = []

    elements.append(Paragraph("IoT Transmission Research Report", styles["Heading1"]))
    elements.append(Spacer(1, 12))

    elements.append(Paragraph("Methodology Summary:", styles["Heading2"]))
    elements.append(Spacer(1, 8))

    elements.append(Paragraph(
        f"Total Devices: {sum(MOTEL_CONFIG.values())}", styles["Normal"]
    ))
    elements.append(Paragraph(
        f"Simulation Duration: {SIMULATION_DURATION_MINUTES} minutes", styles["Normal"]
    ))
    elements.append(Paragraph(
        f"Monte Carlo Runs: {MONTE_CARLO_RUNS}", styles["Normal"]
    ))
    elements.append(Paragraph(
        f"Random Seed: {RANDOM_SEED} (Reproducible)", styles["Normal"]
    ))
    elements.append(Spacer(1, 12))

    elements.append(Paragraph(
        "Latency Formula:", styles["Heading3"]
    ))
    elements.append(Paragraph(
        "Latency = Base_Latency + (Data_Size / Bandwidth)", styles["Normal"]
    ))

    doc.build(elements)

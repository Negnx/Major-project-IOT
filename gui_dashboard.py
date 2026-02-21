"""
gui_dashboard.py

Jamaican Motel Security System Research Project

Structured Research Dashboard
Edge Computing + Genetic Algorithm Routing Model
"""

import tkinter as tk
from tkinter import ttk, messagebox
import statistics
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from experiment_core import (
    run_experiment,
    export_pdf,
    EVENT_TYPES,
    SIMULATION_DURATION_MINUTES,
    MONTE_CARLO_RUNS
)


# ==========================================================
# MAIN GUI
# ==========================================================

def run_gui():

    root = tk.Tk()
    root.title("Jamaican Motel Security System Research Project")
    root.geometry("1700x950")

    style = ttk.Style()
    style.configure("Header.TLabel", font=("Arial", 16, "bold"))

    notebook = ttk.Notebook(root)
    notebook.pack(fill="both", expand=True)

    # ==========================================================
    # TAB 1 — RESEARCH FOUNDATION
    # ==========================================================

    foundation_tab = ttk.Frame(notebook)
    notebook.add(foundation_tab, text="Research Foundation")

    ttk.Label(
        foundation_tab,
        text="Research Questions & Conceptual Justification",
        style="Header.TLabel"
    ).pack(pady=15)

        # ==========================================================
    # Research Questions (Official Wording – Unchanged)
    # ==========================================================

    rq_frame = ttk.LabelFrame(foundation_tab, text="1.4 Research Questions")
    rq_frame.pack(fill="x", padx=40, pady=10)

    # -----------------------------
    # RQ1 (Exact Wording)
    # -----------------------------

    ttk.Label(
        rq_frame,
        text="Is the use of edge computing and genetic algorithms effective in "
            "improving data transmission speed and efficiency in property "
            "security IoT devices?",
        font=("Arial", 11, "bold"),
        wraplength=1600,
        justify="left"
    ).pack(anchor="w", padx=20, pady=(10, 5))

    ttk.Label(
        rq_frame,
        text="Conceptual Justification (Before Simulation):\n"
            "Edge computing processes urgent events locally to reduce WAN "
            "round-trip delay. The Genetic Algorithm evaluates routing "
            "configurations and selects the strategy that minimizes overall "
            "system cost using weighted performance factors.",
        wraplength=1550,
        justify="left"
    ).pack(anchor="w", padx=20, pady=(0, 15))


    # -----------------------------
    # RQ2 (Exact Wording)
    # -----------------------------

    ttk.Label(
        rq_frame,
        text="How does the proposed transmission strategy affect bandwidth usage, "
            "latency, and energy consumption compared to traditional IoT "
            "transmission methods?",
        font=("Arial", 11, "bold"),
        wraplength=1600,
        justify="left"
    ).pack(anchor="w", padx=20, pady=(10, 5))

    ttk.Label(
        rq_frame,
        text="Conceptual Justification (Before Simulation):\n"
            "By routing emergency events to the edge and compressing routine "
            "traffic before cloud transmission, the proposed model is expected "
            "to reduce latency, lower WAN bandwidth usage, and decrease "
            "transmission energy consumption compared to a cloud-only model.",
        wraplength=1550,
        justify="left"
    ).pack(anchor="w", padx=20, pady=(0, 15))


    # -----------------------------
    # Key Research Metrics
    # -----------------------------

    metrics_frame = ttk.LabelFrame(foundation_tab, text="Key Research Metrics")
    metrics_frame.pack(fill="x", padx=40, pady=10)

    metrics_table = ttk.Treeview(
        metrics_frame,
        columns=("Metric", "What It Measures", "Security Relevance"),
        show="headings",
        height=3
    )

    for col in metrics_table["columns"]:
        metrics_table.heading(col, text=col)
        metrics_table.column(col, width=550)

    metrics_table.pack()

    metrics_data = [
        ("Latency",
         "Time required to process a security event",
         "Determines how fast the system reacts to emergencies"),
        ("Bandwidth",
         "Amount of data transmitted over WAN",
         "High usage may congest network during peak events"),
        ("Energy",
         "Power used for data transmission",
         "Impacts sustainability and device efficiency")
    ]

    for row in metrics_data:
        metrics_table.insert("", "end", values=row)

    # -----------------------------
    # Routing Model
    # -----------------------------

    routing_frame = ttk.LabelFrame(foundation_tab, text="Routing Priority Model (Edge + GA)")
    routing_frame.pack(fill="x", padx=40, pady=10)

    routing_table = ttk.Treeview(
        routing_frame,
        columns=("Decision Factor", "Weight", "Purpose"),
        show="headings",
        height=3
    )

    for col in routing_table["columns"]:
        routing_table.heading(col, text=col)
        routing_table.column(col, width=550)

    routing_table.pack()

    routing_data = [
        ("Latency", "0.5", "Fast emergency response is highest priority"),
        ("Bandwidth", "0.3", "Reduce WAN congestion"),
        ("Energy", "0.2", "Improve transmission efficiency")
    ]

    for row in routing_data:
        routing_table.insert("", "end", values=row)

    ttk.Label(
        routing_frame,
        text="Emergency events → Edge Gateway\n"
             "Routine events → Cloud (compressed)\n"
             "Genetic Algorithm selects routing that minimizes weighted cost.",
        wraplength=1600,
        justify="left"
    ).pack(pady=10)

    # ==========================================================
    # TAB 2 — EXPERIMENTAL EVALUATION
    # ==========================================================

    results_tab = ttk.Frame(notebook)
    notebook.add(results_tab, text="Experimental Evaluation")

    ttk.Label(
        results_tab,
        text="Monte Carlo Simulation Results",
        style="Header.TLabel"
    ).pack(pady=15)

    control_frame = ttk.Frame(results_tab)
    control_frame.pack(pady=5)

    status_label = ttk.Label(control_frame, text="Status: Ready")
    status_label.pack(side="left", padx=20)

    run_button = ttk.Button(control_frame, text="Run Simulation")
    run_button.pack(side="left", padx=20)

    export_button = ttk.Button(control_frame, text="Export PDF")
    export_button.pack(side="left", padx=20)

    results_table = ttk.Treeview(
        results_tab,
        columns=("Metric", "Baseline", "Edge + GA", "Improvement (%)", "Interpretation"),
        show="headings",
        height=3
    )

    for col in results_table["columns"]:
        results_table.heading(col, text=col)
        results_table.column(col, width=300)

    results_table.pack(pady=20)

    graph_frame = ttk.Frame(results_tab)
    graph_frame.pack(fill="both", expand=True, padx=40)

    fig = Figure(figsize=(14, 4))
    ax1 = fig.add_subplot(131)
    ax2 = fig.add_subplot(132)
    ax3 = fig.add_subplot(133)

    canvas = FigureCanvasTkAgg(fig, master=graph_frame)
    canvas.get_tk_widget().pack(fill="both", expand=True)

    # ==========================================================
    # TAB 3 — SIMULATION TRANSPARENCY
    # ==========================================================

    transparency_tab = ttk.Frame(notebook)
    notebook.add(transparency_tab, text="Simulation Transparency")

    ttk.Label(
        transparency_tab,
        text="Simulation Model Transparency",
        style="Header.TLabel"
    ).pack(pady=15)

    transparency_text = tk.Text(transparency_tab, wrap="word")
    transparency_text.pack(fill="both", expand=True, padx=40, pady=20)

    transparency_text.insert("1.0",
        "EVENT GENERATION MODEL\n\n"
    )

    for event in EVENT_TYPES:
        transparency_text.insert("end",
            f"{event[0]} → Size: {event[1]}KB | Probability: {event[2]}\n"
        )

    transparency_text.insert("end",
        "\nFORMULAS USED\n\n"
        "Cloud Latency = 300 + (Data_kb / 10)\n"
        "Edge Latency = 50 + (Data_kb / 100)\n"
        "Energy = Data_kb × Energy_per_kb\n"
        "Improvement % = (Baseline − Optimized) / Baseline × 100\n\n"
        f"Simulation Duration: {SIMULATION_DURATION_MINUTES} minutes\n"
        f"Monte Carlo Runs: {MONTE_CARLO_RUNS}\n"
        "Random Seed Fixed for Reproducibility\n"
    )

    transparency_text.config(state="disabled")

    # ==========================================================
    # RUN SIMULATION
    # ==========================================================

    def run_sim():

        status_label.config(text="Status: Running Simulation...")
        root.update()

        results = run_experiment()

        baseline = results["baseline"]
        optimized = results["optimized"]

        base_lat = statistics.mean([x[0] for x in baseline])
        opt_lat = statistics.mean([x[0] for x in optimized])

        base_bw = statistics.mean([x[1] for x in baseline])
        opt_bw = statistics.mean([x[1] for x in optimized])

        base_en = statistics.mean([x[2] for x in baseline])
        opt_en = statistics.mean([x[2] for x in optimized])

        lat_improve = ((base_lat - opt_lat) / base_lat) * 100
        bw_improve = ((base_bw - opt_bw) / base_bw) * 100
        en_improve = ((base_en - opt_en) / base_en) * 100

        results_table.delete(*results_table.get_children())

        results_table.insert("", "end", values=(
            "Latency", f"{base_lat:.2f}", f"{opt_lat:.2f}",
            f"{lat_improve:.2f}%", "Edge reduces WAN delay"
        ))

        results_table.insert("", "end", values=(
            "Bandwidth", f"{base_bw:.2f}", f"{opt_bw:.2f}",
            f"{bw_improve:.2f}%", "Edge filtering reduces WAN traffic"
        ))

        results_table.insert("", "end", values=(
            "Energy", f"{base_en:.2f}", f"{opt_en:.2f}",
            f"{en_improve:.2f}%", "Edge transmission uses less power"
        ))

        ax1.clear()
        ax2.clear()
        ax3.clear()

        ax1.bar(["Baseline", "Edge + GA"], [base_lat, opt_lat])
        ax1.set_title("Latency")

        ax2.bar(["Baseline", "Edge + GA"], [base_bw, opt_bw])
        ax2.set_title("Bandwidth")

        ax3.bar(["Baseline", "Edge + GA"], [base_en, opt_en])
        ax3.set_title("Energy")

        fig.tight_layout()
        canvas.draw()

        status_label.config(text="Status: Simulation Complete")

        run_sim.results = results

    run_button.config(command=run_sim)

    def export_results():
        try:
            export_pdf(run_sim.results)
            messagebox.showinfo("Success", "PDF exported successfully.")
        except:
            messagebox.showerror("Error", "Run simulation first.")

    export_button.config(command=export_results)

    root.mainloop()

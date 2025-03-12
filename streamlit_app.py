import glob
import os
import re

import pandas as pd
import plotly.express as px
import streamlit as st

RESULTS_DIR = "results"

st.title("📊 Backend Framework Performance Comparison")


def parse_wrk_output(file_path):
    with open(file_path, "r") as file:
        content = file.read()

    latency = re.search(r"Latency\s+([\d\.]+)ms", content)
    req_per_sec = re.search(r"Requests/sec:\s+([\d\.]+)", content)
    transfer_per_sec = re.search(r"Transfer/sec:\s+([\d\.]+)([K|M]B)", content)

    transfer_value = 0
    if transfer_per_sec:
        transfer_value = float(transfer_per_sec.group(1))
        if transfer_per_sec.group(2) == "MB":
            transfer_value *= 1024

    return (
        float(latency.group(1)) if latency else None,
        float(req_per_sec.group(1)) if req_per_sec else None,
        transfer_value,
    )


frameworks = {}
for csv_file in glob.glob(os.path.join(RESULTS_DIR, "*_results.csv")):
    language = os.path.basename(csv_file).split("_")[0]
    name = os.path.basename(csv_file).split("_")[1]
    text_file = csv_file.replace("csv", "txt")

    if not os.path.exists(text_file):
        st.warning(f"⚠️ Missing wrk result file for {name}")
        continue

    csv_data = pd.read_csv(csv_file)

    csv_data = csv_data.sort_values("Timestamp")
    csv_data["Seconds"] = csv_data["Timestamp"] - csv_data["Timestamp"].iloc[0]
    csv_data["Relative_Seconds"] = csv_data["Seconds"].diff().fillna(0).cumsum()

    latency, req_per_sec, transfer_per_sec = parse_wrk_output(text_file)

    if latency is None or req_per_sec is None:
        st.warning(f"⚠️ Failed to extract wrk data for {name}")
        continue

    frameworks[name] = {
        "Language": language,
        "CSV Data": csv_data,
        "Latency (ms)": latency,
        "Requests/sec": req_per_sec,
        "Transfer/sec (KB)": transfer_per_sec,
    }

if frameworks:
    comparison_df = pd.DataFrame(
        [
            {
                "Language": data["Language"],
                "Framework": name,
                "Latency (ms)": data["Latency (ms)"],
                "Requests/sec": data["Requests/sec"],
                "Transfer/sec (KB)": data["Transfer/sec (KB)"],
            }
            for name, data in sorted(
                frameworks.items(), key=lambda x: -x[1]["Requests/sec"]
            )
        ]
    )

    st.header("📈 Requests/sec and Latency Comparison")
    st.dataframe(comparison_df)

    st.subheader("🚀 Requests/sec Comparison")
    st.bar_chart(comparison_df.set_index("Framework")["Requests/sec"])

    st.subheader("⏱️ Latency Comparison")
    st.bar_chart(comparison_df.set_index("Framework")["Latency (ms)"])

    st.subheader("🔄 Transfer/sec Comparison")
    st.bar_chart(comparison_df.set_index("Framework")["Transfer/sec (KB)"])

    st.header("📊 Resource Usage Over Time - Combined View")

    y_axis_labels = {
        "CPU_Usage": "CPU Usage (%)",
        "Memory_Usage": "Memory Usage (%)",
        "Network_IO": "Network Throughput (MB/s)",
    }

    for resource in ["CPU_Usage", "Memory_Usage", "Network_IO"]:
        combined_df = pd.DataFrame()

        for name, data in frameworks.items():
            df = data["CSV Data"].copy()
            df["Framework"] = name
            combined_df = pd.concat([combined_df, df], ignore_index=True)

        fig = px.line(
            combined_df,
            x="Relative_Seconds",
            y=resource,
            color="Framework",
            title=f'{resource.replace("_", " ")} Comparison Across Frameworks',
            labels={"Relative_Seconds": "Seconds", resource: y_axis_labels[resource]},
        )
        st.plotly_chart(fig, use_container_width=True)

else:
    st.error("🚨 No valid results found in the results folder.")

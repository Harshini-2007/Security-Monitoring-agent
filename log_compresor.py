import csv
from collections import defaultdict
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt

# -----------------------------
# Step 1: Compress logs
# -----------------------------
compressed_logs = defaultdict(lambda: {"count": 0, "timestamps": []})

with open("logs.csv", newline='') as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        if not row or len(row) < 4:
            continue

        timestamp, user, event, ip = row[:4]
        key = (user, event, ip)
        compressed_logs[key]["count"] += 1
        compressed_logs[key]["timestamps"].append(timestamp)

# -----------------------------
# Step 2: Create DataFrame from compressed logs
# -----------------------------
data = []

for (user, event, ip), info in compressed_logs.items():
    # take the FIRST timestamp for that compressed event
    ts = pd.to_datetime(info["timestamps"][0], format="%H:%M", errors="coerce")
    data.append([user, event, ip, info["count"], ts])

df = pd.DataFrame(
    data,
    columns=["user", "event", "ip", "count", "timestamp"]
)

df = df.dropna(subset=["timestamp"])

# -----------------------------
# Step 3: Encode categorical columns
# -----------------------------
le_user = LabelEncoder()
le_event = LabelEncoder()
le_ip = LabelEncoder()

df["user_enc"] = le_user.fit_transform(df["user"])
df["event_enc"] = le_event.fit_transform(df["event"])
df["ip_enc"] = le_ip.fit_transform(df["ip"])

# -----------------------------
# Step 4: Train Isolation Forest
# -----------------------------
model = IsolationForest(
    n_estimators=100,
    contamination=0.3,   # increased to force visible anomalies
    random_state=42
)

df["anomaly"] = model.fit_predict(
    df[["user_enc", "event_enc", "ip_enc", "count"]]
)

# -----------------------------
# Step 5: Filter anomalies
# -----------------------------
anomalies = df[df["anomaly"] == -1].copy()

# -----------------------------
# Step 6: Human-readable anomalies
# -----------------------------
anomalies = anomalies[["user", "event", "ip", "count", "timestamp"]]

print("\nHuman-readable Anomalies Detected:")
print(anomalies)

# -----------------------------
# Step 7: Hour-wise analysis
# -----------------------------
anomalies["hour"] = anomalies["timestamp"].dt.hour
hourly_anomalies = anomalies.groupby("hour")["count"].sum()

print("\nAnomalies per Hour:")
print(hourly_anomalies)

# -----------------------------
# Step 8: Plot
# -----------------------------
hourly_anomalies.plot(kind="bar", title="Anomalies by Hour")
plt.xlabel("Hour of Day")
plt.ylabel("Number of Anomalies")
plt.show()

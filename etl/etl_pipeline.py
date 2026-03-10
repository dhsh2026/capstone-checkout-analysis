import pandas as pd
import numpy as np

print("Starting ETL pipeline...")

# Load raw datasets
sessions = pd.read_csv("data/sessions.csv")
events = pd.read_csv("data/events.csv")
orders = pd.read_csv("data/orders.csv")
users = pd.read_csv("data/users.csv")

print("Datasets loaded")

# Data Cleaning

sessions = sessions.drop_duplicates("session_id")
sessions["channel"] = sessions["channel"].str.lower()
sessions["device"] = sessions["device"].fillna("unknown")

events["event_ts"] = pd.to_datetime(events["event_ts"], errors="coerce")
orders["net_amount"] = pd.to_numeric(orders["net_amount"], errors="coerce")

print("Data cleaning complete")

# Build Funnel Flags

funnel = events.pivot_table(
    index="session_id",
    columns="event_type",
    aggfunc="size",
    fill_value=0
)

funnel = (funnel > 0).reset_index()

rename_map = {
    "product_view": "has_productview",
    "add_to_cart": "has_addtocart",
    "begin_checkout": "has_begincheckout",
    "payment_attempt": "has_paymentattempt",
    "purchase": "has_purchase"
}

funnel = funnel.rename(columns=rename_map)

for col in rename_map.values():
    if col not in funnel.columns:
        funnel[col] = False

print("Funnel indicators created")

# Revenue Per Session

session_revenue = (
    orders.groupby("session_id")["net_amount"]
    .sum()
    .reset_index()
)

# Build fact_sessions table

fact_sessions = (
    sessions
    .merge(funnel, on="session_id", how="left")
    .merge(session_revenue, on="session_id", how="left")
)

funnel_cols = list(rename_map.values())

fact_sessions[funnel_cols] = fact_sessions[funnel_cols].fillna(False)
fact_sessions["net_amount"] = fact_sessions["net_amount"].fillna(0)

fact_sessions[funnel_cols] = fact_sessions[funnel_cols].astype(bool)

print("fact_sessions table built")

# Eligible Experiment Population

eligible = fact_sessions[
    (fact_sessions["device"] == "web") &
    (fact_sessions["user_id"].notna()) &
    (fact_sessions["variant"].isin(["A","B"]))
].copy()

print("Eligible sessions:", eligible.shape[0])

# Add User Segments

eligible = eligible.merge(
    users[["user_id","segment"]],
    on="user_id",
    how="left"
)

# Export Tableau Dataset

export_columns = [
    "session_id",
    "session_start_ts",
    "variant",
    "device",
    "channel",
    "segment",
    "is_new_user",
    "has_productview",
    "has_addtocart",
    "has_begincheckout",
    "has_paymentattempt",
    "has_purchase",
    "net_amount"
]

export_df = eligible[export_columns]

export_df.to_csv("tableau_analysis_dataset.csv", index=False)

print("Export complete: tableau_analysis_dataset.csv")
print("ETL pipeline finished successfully.")
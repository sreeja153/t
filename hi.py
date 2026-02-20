# ============================================
# 📊 Task 5: Data Analysis on CSV Files
# Python Developer Internship
# ============================================

import pandas as pd
import matplotlib.pyplot as plt

def analyze_sales_data(csv_file):
    print("\n✨ WELCOME TO SALES DATA ANALYSIS ✨\n")

    # -----------------------------
    # 1️⃣ Load Dataset
    # -----------------------------
    try:
        df = pd.read_csv(csv_file)
        print("✅ CSV file loaded successfully!\n")
    except FileNotFoundError:
        print("❌ CSV file not found. Please check the file name.")
        return

    # -----------------------------
    # 2️⃣ Basic Data Overview
    # -----------------------------
    print("📌 Dataset Preview:")
    print(df.head(), "\n")

    print("📌 Dataset Shape (Rows, Columns):", df.shape, "\n")

    print("📌 Column Information:")
    print(df.info(), "\n")

    # -----------------------------
    # 3️⃣ Handle Missing Values
    # -----------------------------
    if df.isnull().sum().any():
        print("⚠️ Missing values found. Filling with 0...\n")
        df.fillna(0, inplace=True)
    else:
        print("✅ No missing values found.\n")

    # -----------------------------
    # 4️⃣ Sales Analysis using groupby()
    # -----------------------------
    print("📈 Total Sales by Category:\n")
    sales_by_category = df.groupby("Category")["Sales"].sum()
    print(sales_by_category, "\n")

    # -----------------------------
    # 5️⃣ Data Visualization
    # -----------------------------
    plt.figure(figsize=(8, 5))
    sales_by_category.plot(
        kind="bar",
        color="cornflowerblue",
        edgecolor="black"
    )

    plt.title("💰 Total Sales by Category", fontsize=14)
    plt.xlabel("Category", fontsize=12)
    plt.ylabel("Total Sales", fontsize=12)
    plt.xticks(rotation=0)
    plt.grid(axis="y", linestyle="--", alpha=0.6)

    plt.tight_layout()
    plt.show()

    # -----------------------------
    # 6️⃣ Insights
    # -----------------------------
    top_category = sales_by_category.idxmax()
    top_value = sales_by_category.max()

    print("🔍 Key Insight:")
    print(f"🏆 Highest selling category: {top_category}")
    print(f"💵 Total sales: {top_value}")

    print("\n🎉 Analysis Completed Successfully!")

# -----------------------------
# Program Execution
# -----------------------------
if __name__ == "__main__":
    analyze_sales_data("sales.csv")
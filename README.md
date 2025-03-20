# 📊 AI-Powered Sales Dashboard

An interactive and intelligent **Sales Dashboard** built with **Streamlit**, powered by a custom AI agent, and designed for KPI reporting and data-driven decision-making.

This project helps sales teams and analysts visualize trends, revenue, and returns efficiently, with smart filters and a built-in assistant to answer business queries.

---
## 🎥 Demo Video (click to watch ⬇)  
[![Watch the video](https://github.com/user-attachments/assets/edc9e9e5-a134-4197-b4e4-7da46e6f49fa)](https://youtu.be/W1dqJ8m9B1k)


## 🚀 Features

- 🎯 **KPI Highlights**: No. of Sales, Returns, Revenue, and Loss.
- 📈 **Visual Insights**: Line chart, Stacked Bar Graph, and Treemap to explore monthly and category-wise sales.
- 🤖 **AI Assistant Manager**: Ask questions about your data using a conversational interface (RAG-based agent).
- 🔎 **Interactive Filters**: Filter by year and product category for dynamic updates across all visualizations.
- 💡 **ETL Optimization**: Backend pipeline engineered with **Azure Data Factory** for high-volume data handling (1M+ rows).

## 🧠 Tech Stack

- MongoDB (via `pymongo`)  
- Python: Streamlit, Plotly, Pandas
- LangChain: RAG-based AI Agent  


---

## ⚙️ Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/munas-git/AI-powered-sales-dashboard.git
cd sales-dashboard-ai
```

### 2. Install dependencies
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 4. Run the application
```
streamlit run app.py
```

## 💬 AI Assistant Capabilities

The built-in assistant can answer business queries like:

- "What's the highest-selling category in 2024?"
- "Show total return losses for the last two years."
- "Which month had peak revenue?"
- "How many returns were recorded in Q1?"
- "What was the average revenue per category in 2023?"
- "Compare sales vs returns for Capsicum."

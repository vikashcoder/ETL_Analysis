
# 🚧 SafeRoads India: Road Accident Analysis Dashboard

An end-to-end data analysis project built with **Python**, **SQLite**, and **Streamlit** using Indian road accident data. The project performs data cleaning, ETL (Extract, Transform, Load), and builds an interactive dashboard to visualize accident trends across Indian states.

---

## 📊 Project Overview

This dashboard lets you explore road accident data collected from across India. It answers key questions such as:

- Which states/districts have the highest accident rates?
- Trends across different road types and locations
- Year-wise fatality counts (2016–2018)

---

## 🧱 Tech Stack

| Tool          | Purpose                            |
|---------------|------------------------------------|
| Python        | Core scripting & ETL logic         |
| Pandas        | Data cleaning and manipulation     |
| SQLite        | Lightweight database               |
| Plotly        | Interactive charts and visuals     |
| Streamlit     | Web-based interactive dashboard    |

---

## 📁 Project Structure

```
etl_analysis/
├── app/
│   └── streamlit_app.py           # Streamlit dashboard app
├── data/
│   └── road_accidents_raw.csv     # Raw dataset (2020)
├── etl/
│   └── etl_script.py              # Cleans and loads data to SQLite
├── db/
│   └── accidents.db               # SQLite DB with processed data
├── requirements.txt               # Python dependencies
└── README.md                      # Project documentation
```

---

## 🚀 How to Run the Project

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/safe-roads-india.git
cd safe-roads-india
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the ETL Script (this creates the database)
```bash
python etl/etl_script.py
```

### 5. Launch the Dashboard
```bash
streamlit run app/streamlit_app.py
```

---



## 📌 Features

- Filter by state, district, police station
- Interactive bar, line, and pie charts using Plotly
- Lightweight backend using SQLite
- Fast deployment-ready Streamlit UI

---

## 🛠️ Customization

- **Add new visualizations**: Modify `streamlit_app.py`
- **Change DB structure**: Update `etl_script.py`
- **Use other datasets**: Drop your CSV into `data/` and update accordingly

---

## 📦 requirements.txt (example)

```txt
pandas==2.2.1
streamlit==1.44.1
plotly==6.0.1
```

---

## 🧑‍💻 Author

Made with ❤️ by Vikash Raj

---

## 📜 License

This project is licensed under the MIT License.
```




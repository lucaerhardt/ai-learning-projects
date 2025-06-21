# Day 7 – Data Cleaning & Exploration

## 📊 Dataset
A small dataset with 5 students including their study hours, attendance, and scores. Some values were missing (NaN), representing real-world messy data.

## 🚀 What I Did
- Created a pandas DataFrame manually
- Identified and filled missing values with column means
- Filtered for students who studied more than 4 hours
- Sorted the dataset by Score in descending order
- Exported the cleaned dataset for future ML use

## 🧠 Skills Practiced
- Real-world data preprocessing
- pandas basics (`read_csv`, `isnull`, `fillna`, filtering)
- DataFrame manipulation and saving cleaned data

## 📁 Output
Final cleaned table:

| Name | Hours_Studied | Attendance (%) | Score |
|------|----------------|----------------|--------|
| John | 6.0 | 95.0 | 91.0 |
| Gerd | 5.0 | 90.0 | 88.0 |
| Anna | 3.0 | 80.0 | 80.0 |
| Lara | 4.0 | 85.0 | 76.0 |
| Mike | 2.0 | 87.5 | 65.0 |

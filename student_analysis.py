import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('student_data.csv')

# Calculate average score
df['Total_Score'] = df[['Math', 'Science', 'English']].mean(axis=1)

# Basic stats
print("Summary Statistics:\n", df.describe())

# Heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(df[['Math', 'Science', 'English', 'Attendance', 'Activities', 'Total_Score']].corr(), annot=True, cmap='Blues')
plt.title("Correlation Heatmap")
plt.show()

# Attendance vs Total Score
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='Attendance', y='Total_Score', hue='Activities', size='Activities', palette='viridis')
plt.title("Attendance vs Total Score")
plt.xlabel("Attendance (%)")
plt.ylabel("Average Score")
plt.show()

# Average scores
subjects = ['Math', 'Science', 'English']
avg_scores = [df[subject].mean() for subject in subjects]

plt.figure(figsize=(7, 5))
sns.barplot(x=subjects, y=avg_scores)
plt.title("Average Scores by Subject")
plt.ylabel("Average Score")
plt.show()

# Activities distribution
plt.figure(figsize=(7, 5))
sns.countplot(x='Activities', data=df)
plt.title("Activities Participation Distribution")
plt.xlabel("Activities")
plt.ylabel("Number of Students")
plt.show()

# Top students
top_students = df.sort_values(by='Total_Score', ascending=False).head(5)
print("Top Students:\n", top_students[['Name', 'Total_Score']])

      

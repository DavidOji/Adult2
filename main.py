import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Aufgabe 1
df = pd.read_csv('adult 2.csv')

# Die ersten 5 Zeilen ausgeben
print("Die ersten 5 Zeilen des DatenFrames: ")
print(df.head())

# Die letzten 5 Zeilen ausgeben
print("\n Die letzten 5 Zeilen des DatenFrames: ")
print(df.tail())

# Zusammenfassung des DatenFrames
print("\n Zusammenfassung des DatenFrames: ")
print(df.info())

# Aufgabe 2
# Spalten auswählen
selected_columns = ['age', 'occupation', 'income']
selected_data = df[selected_columns].head(10)
print("\n Zeige die ersten 10 Zeilen an: ")
print(selected_data)

# Bedingte Daten ausgeben
high_income_data = df[df['income'] == '>50K']
print("\n Zeilen bei denen das Einkommen '>50K' ist: ")
print(high_income_data.head())

# Mehrere Bedingungen
filtered_data = df[(df['age'] > 30) & (df['education'] == 'Bachelors')]
print("\n Zeilen, bei denen das Alter größer als 30 ist und die Bildung 'Bachelors' ist: ")
print(filtered_data.head())

# Aufgabe 3
# 1. Neue Spalte hinzufügen
df['age_decade'] = df['age'] // 10

# 2. Werte ändern
df['income'] = df['income'].map({'>50K': 'high', '<=50K': 'low'})

# 3. Zeilen löschen
df = df[df['occupation'] != 'Unknown']

# Ergebnisse anzeigen
print("\n DatenFrame nach den Änderungen: ")
print(df.head())

# Aufgabe 4

# Deskriptive Statistiken für die 'age'-Spalte
age_statistics = df['age'].describe()[['min', 'max']]
print("\n Deskriptive Statistiken für die 'age'-Spalte: ")
print(age_statistics)

# Gruppieren und Aggregieren (Durchschnitt von 'age' nach 'income')
average_age_by_income = df.groupby('income')['age'].mean()
print("\n Durchschnittliches Alter nach Einkommen: ")
print(average_age_by_income)

# Einzigartige Werte in der 'education'-Spalte
unique_education_values = df['education'].unique()
print("\n Einzigartige Werte in der 'education'-Spalte: ")
print(unique_education_values)

# Aufgabe 5

# 1. Boxplot: Erstelle Boxplots für `age`, gruppiert nach `income`.
plt.figure(figsize=(10, 6))
sns.boxplot(x='income', y='age', data=df)
plt.title('Boxplot für Alter, gruppiert nach Einkommen')
plt.show()

# 2. Scatter Plot: Erstelle einen Scatter Plot von `age` gegen `hours-per-week`, farbkodiert nach `income`.
plt.figure(figsize=(10, 6))
sns.scatterplot(x='age', y='hours-per-week', hue='income', data=df)
plt.title('Scatter Plot von Alter gegen Arbeitsstunden pro Woche, farbkodiert nach Einkommen')
plt.show()



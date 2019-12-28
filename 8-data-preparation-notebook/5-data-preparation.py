import pandas as pd
import numpy as np

np.warnings.filterwarnings('ignore')

titanic = pd.read_csv('data/titanic/train.csv')

# Overall exploration before cleanup
print('\n\n********************************** Dataset BEFORE Cleanup ***************************************')
print(titanic.head(8).to_string())

# Filling up the missing data with the most common values
titanic['Age'] = titanic['Age'].fillna(value=titanic['Age'].mean())
titanic['Embarked'] = titanic['Embarked'].fillna(value='S')

# Encoding categorical variables using dummy variables
encoded_sex = pd.get_dummies(titanic['Sex'], drop_first=True)
encoded_embarked = pd.get_dummies(titanic['Embarked'], drop_first=True)
titanic = pd.concat([titanic, encoded_sex, encoded_embarked], axis=1)

# Transforming the Cabin field information in numerical information
titanic['MarkedCabin'] = titanic['Cabin'].apply(lambda x: 0 if type(x) != str else 1)

# Extracting title from passenger name
titanic['IsMaster'] = titanic['Name'].apply(lambda name: 1 if 'master.' in name.lower() else 0)
titanic['IsReverend'] = titanic['Name'].apply(lambda name: 1 if 'rev.' in name.lower() else 0)
titanic['IsDoctor'] = titanic['Name'].apply(lambda name: 1 if 'dr.' in name.lower() else 0)

# Removing non numerical and 'noise' columns
titanic.drop(['PassengerId', 'Sex', 'Embarked', 'Name', 'Ticket', 'Cabin'], axis=1, inplace=True)

# Prepared dataset overall exploration
print('\n\n********************************** Dataset AFTER Cleanup ***************************************')
print(titanic.head(8).to_string())

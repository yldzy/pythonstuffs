 1/1:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
 1/2:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('finalset.csv')

#exploring the dataset
print("Original Data Shape:", df.shape)
print("\nColumn Names:", df.columns.tolist())
print("\nData Types:\n", df.dtypes)

#data preview
print("\nFirst 5 rows:\n", df.head())
print("\nLast 5 rows:\n", df.tail())
print("\nRandom 5 Rows:\n", df.sample(5))

#checking for unique values
print("\nUnique Values per Column:\n", df.nunique())

#counting per column
categorical_cols = df.select_dtypes(include='object').columns
for col in categorical_cols:
    print(f"\nValue Counts for {col}:\n", df[col].value_counts())

#checking for duplicates
print("\nDuplicate Rows:", df.duplicated().sum())
 1/3:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

#exploring the dataset
print("Original Data Shape:", df.shape)
print("\nColumn Names:", df.columns.tolist())
print("\nData Types:\n", df.dtypes)

#data preview
print("\nFirst 5 rows:\n", df.head())
print("\nLast 5 rows:\n", df.tail())
print("\nRandom 5 Rows:\n", df.sample(5))

#checking for unique values
print("\nUnique Values per Column:\n", df.nunique())

#counting per column
categorical_cols = df.select_dtypes(include='object').columns
for col in categorical_cols:
    print(f"\nValue Counts for {col}:\n", df[col].value_counts())

#checking for duplicates
print("\nDuplicate Rows:", df.duplicated().sum())
 1/4:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

#exploring the dataset
print("Original Data Shape:", df.shape)
print("\nColumn Names:", df.columns.tolist())
print("\nData Types:\n", df.dtypes)

#data preview
print("\nFirst 5 rows:\n", df.head())
print("\nLast 5 rows:\n", df.tail())
print("\nRandom 5 Rows:\n", df.sample(5))

#checking for unique values
print("\nUnique Values per Column:\n", df.nunique())

#counting per column
categorical_cols = df.select_dtypes(include='object').columns
for col in categorical_cols:
    print(f"\nValue Counts for {col}:\n", df[col].value_counts())

#checking for duplicates
print("\nDuplicate Rows:", df.duplicated().sum())
 1/5:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

#csv data set
data = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

#initials 

#exploring the dataset
print("\nColumn Names:", data.columns.tolist())
print("\nData Types:\n", data.dtypes)

#data preview
print("\nFirst 5 rows:\n", data.head())
print("\nLast 5 rows:\n", data.tail())
print("\nRandom 5 Rows:\n", data.sample(5))

#checking for unique values
print("\nUnique Values per Column:\n", data.nunique())

#counting per column
categorical_cols = data.select_dtypes(include='object').columns
for col in categorical_cols:
    print(f"\nValue Counts for {col}:\n", data[col].value_counts())

#checking for duplicates
print("\nDuplicate Rows:", data.duplicated().sum())
 1/6:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

#csv data set
data = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

#initials 

#exploring the dataset
print("\nColumn Names:", data.columns.tolist())
print("\nData Types:\n", data.dtypes)

#data preview
print("\nFirst 5 rows:\n", data.head())
print("\nLast 5 rows:\n", data.tail())
print("\nRandom 5 Rows:\n", data.sample(5))

#checking for unique values
print("\nUnique Values per Column:\n", data.nunique())

#counting per column
categorical_cols = data.select_dtypes(include='object').columns
for col in categorical_cols:
    print(f"\nValue Counts for {col}:\n", data[col].value_counts())

#checking for duplicates
print("\nDuplicate Rows:", data.duplicated().sum())
 1/7:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

#csv data set
data = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

#initials 
col_title = data.columns.tolist()
col_cat = ['Name', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']


for i in range(col_cat.len()):
    print(col_cat[i], col_title[i])
    
#exploring the dataset
print("\nColumn Names:", data.columns.tolist())
print("\nData Types:\n", data.dtypes)

#data preview
print("\nFirst 5 rows:\n", data.head())
print("\nLast 5 rows:\n", data.tail())
print("\nRandom 5 Rows:\n", data.sample(5))

#checking for unique values
print("\nUnique Values per Column:\n", data.nunique())

#counting per column
categorical_cols = data.select_dtypes(include='object').columns
for col in categorical_cols:
    print(f"\nValue Counts for {col}:\n", data[col].value_counts())

#checking for duplicates
print("\nDuplicate Rows:", data.duplicated().sum())
 1/8:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

#csv data set
data = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

#initials 
col_title = data.columns.tolist()
col_cat = ['Name', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']


for i in range(len(col_cat)):
    print(col_cat[i], col_title[i])
    
#exploring the dataset
print("\nColumn Names:", data.columns.tolist())
print("\nData Types:\n", data.dtypes)

#data preview
print("\nFirst 5 rows:\n", data.head())
print("\nLast 5 rows:\n", data.tail())
print("\nRandom 5 Rows:\n", data.sample(5))

#checking for unique values
print("\nUnique Values per Column:\n", data.nunique())

#counting per column
categorical_cols = data.select_dtypes(include='object').columns
for col in categorical_cols:
    print(f"\nValue Counts for {col}:\n", data[col].value_counts())

#checking for duplicates
print("\nDuplicate Rows:", data.duplicated().sum())
 1/9:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

#csv data set
data = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

#initials 
col_title = data.columns.tolist()
col_cat = ['Name', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']

print("\nColumn Names:")
for i in range(len(col_cat)):
    print(col_title[i], col_cat[i])
    

#data preview
print("\nFirst 5 rows:\n", data.head())
print("\nLast 5 rows:\n", data.tail())
print("\nRandom 5 Rows:\n", data.sample(5))

#checking for unique values
print("\nUnique Values per Column:\n", data.nunique())

#counting per column
categorical_cols = data.select_dtypes(include='object').columns
for col in categorical_cols:
    print(f"\nValue Counts for {col}:\n", data[col].value_counts())

#checking for duplicates
print("\nDuplicate Rows:", data.duplicated().sum())
1/10:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

#csv data set
data = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

#initials 
col_title = data.columns.tolist()
col_cat = ['Name', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']

print("\nCOLUMNS:")
for i in range(len(col_cat)):
    print(col_title[i], col_cat[i])
    

#data preview
print("\nFirst 5 rows:\n", data.head())
print("\nLast 5 rows:\n", data.tail())
print("\nRandom 5 Rows:\n", data.sample(5))

#checking for unique values
print("\nUnique Values per Column:\n", data.nunique())

#counting per column
categorical_cols = data.select_dtypes(include='object').columns
for col in categorical_cols:
    print(f"\nValue Counts for {col}:\n", data[col].value_counts())

#checking for duplicates
print("\nDuplicate Rows:", data.duplicated().sum())
1/11:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

#csv data set
data = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

#initials 
col_title = data.columns.tolist()
col_cat = ['Name', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']

print("\nCOLUMNS:")
for i in range(len(col_cat)):
    print(i, col_cat[i], col_title[i])
    

#data preview
print("\nFirst 5 rows:\n", data.head())
print("\nLast 5 rows:\n", data.tail())
print("\nRandom 5 Rows:\n", data.sample(5))

#checking for unique values
print("\nUnique Values per Column:\n", data.nunique())

#counting per column
categorical_cols = data.select_dtypes(include='object').columns
for col in categorical_cols:
    print(f"\nValue Counts for {col}:\n", data[col].value_counts())

#checking for duplicates
print("\nDuplicate Rows:", data.duplicated().sum())
1/12:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

#csv data set
data = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

#initials 
col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']

print("\nCOLUMNS:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    

#data preview
print("\nFirst 5 rows:\n", data.head())
print("\nLast 5 rows:\n", data.tail())
print("\nRandom 5 Rows:\n", data.sample(5))

#checking for unique values
print("\nUnique Values per Column:\n", data.nunique())

#counting per column
categorical_cols = data.select_dtypes(include='object').columns
for col in categorical_cols:
    print(f"\nValue Counts for {col}:\n", data[col].value_counts())

#checking for duplicates
print("\nDuplicate Rows:", data.duplicated().sum())
1/13:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

#csv data set
data = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')
ds = np.loadtxt(r'/Users/lydrenjess/Downloads/finalset.csv')

#initials 
col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']

print("\nCOLUMNS:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    

#data preview
print("\nFirst 5 rows:\n", data.head())
print("\nLast 5 rows:\n", data.tail())
print("\nRandom 5 Rows:\n", data.sample(5))

#checking for unique values
print("\nUnique Values per Column:\n", data.nunique())

#counting per column
categorical_cols = data.select_dtypes(include='object').columns
for col in categorical_cols:
    print(f"\nValue Counts for {col}:\n", data[col].value_counts())

#checking for duplicates
print("\nDuplicate Rows:", data.duplicated().sum())
1/14:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

#csv data set
data = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')
ds = np.genfromtxt(r'/Users/lydrenjess/Downloads/finalset.csv')

#initials 
col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']

print("\nCOLUMNS:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    

#data preview
print("\nFirst 5 rows:\n", data.head())
print("\nLast 5 rows:\n", data.tail())
print("\nRandom 5 Rows:\n", data.sample(5))

#checking for unique values
print("\nUnique Values per Column:\n", data.nunique())

#counting per column
categorical_cols = data.select_dtypes(include='object').columns
for col in categorical_cols:
    print(f"\nValue Counts for {col}:\n", data[col].value_counts())

#checking for duplicates
print("\nDuplicate Rows:", data.duplicated().sum())
1/15:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

#csv data set
data = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')
ds = np.genfromtxt(r'/Users/lydrenjess/Downloads/finalset.csv', skip_header)

#initials 
col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']

print("\nCOLUMNS:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    

#data preview
print("\nFirst 5 rows:\n", data.head())
print("\nLast 5 rows:\n", data.tail())
print("\nRandom 5 Rows:\n", data.sample(5))

#checking for unique values
print("\nUnique Values per Column:\n", data.nunique())

#counting per column
categorical_cols = data.select_dtypes(include='object').columns
for col in categorical_cols:
    print(f"\nValue Counts for {col}:\n", data[col].value_counts())

#checking for duplicates
print("\nDuplicate Rows:", data.duplicated().sum())
1/16:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

#csv data set
data = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')
ds = np.genfromtxt(r'/Users/lydrenjess/Downloads/finalset.csv', skip_header = 1)

#initials 
col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']

print("\nCOLUMNS:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    

#data preview
print("\nFirst 5 rows:\n", data.head())
print("\nLast 5 rows:\n", data.tail())
print("\nRandom 5 Rows:\n", data.sample(5))

#checking for unique values
print("\nUnique Values per Column:\n", data.nunique())

#counting per column
categorical_cols = data.select_dtypes(include='object').columns
for col in categorical_cols:
    print(f"\nValue Counts for {col}:\n", data[col].value_counts())

#checking for duplicates
print("\nDuplicate Rows:", data.duplicated().sum())
1/17:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

#csv data set
data = pd.read_csv(r'/Users/lydrenjess/Downloads/finalsetwname.csv')
ds = np.loadtxt(r'/Users/lydrenjess/Downloads/finalsetwoname.csv', )

#initials 
col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']

print("\nCOLUMNS:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    

#data preview
print("\nFirst 5 rows:\n", data.head())
print("\nLast 5 rows:\n", data.tail())
print("\nRandom 5 Rows:\n", data.sample(5))

#checking for unique values
print("\nUnique Values per Column:\n", data.nunique())

#counting per column
categorical_cols = data.select_dtypes(include='object').columns
for col in categorical_cols:
    print(f"\nValue Counts for {col}:\n", data[col].value_counts())

#checking for duplicates
print("\nDuplicate Rows:", data.duplicated().sum())
1/18:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

#csv data set
data = pd.read_csv(r'/Users/lydrenjess/Downloads/finalsetwname.csv')
ds = np.loadtxt(r'/Users/lydrenjess/Downloads/finalsetwoname.csv', )

#initials 
col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']

print("\nCOLUMNS:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    

#data preview
print("\nFirst 5 rows:\n", data.head())
print("\nLast 5 rows:\n", data.tail())
print("\nRandom 5 Rows:\n", data.sample(5))

#checking for unique values
print("\nUnique Values per Column:\n", data.nunique())

#counting per column
categorical_cols = data.select_dtypes(include='object').columns
for col in categorical_cols:
    print(f"\nValue Counts for {col}:\n", data[col].value_counts())

#checking for duplicates
print("\nDuplicate Rows:", data.duplicated().sum())
1/19:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

#csv data set
data = pd.read_csv(r'/Users/lydrenjess/Downloads/finalsetwname.csv')
ds = np.loadtxt(r'/Users/lydrenjess/Downloads/finalsetwoname.csv', delimiter=',' )

#initials 
col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']

print("\nCOLUMNS:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    

#data preview
print("\nFirst 5 rows:\n", data.head())
print("\nLast 5 rows:\n", data.tail())
print("\nRandom 5 Rows:\n", data.sample(5))

#checking for unique values
print("\nUnique Values per Column:\n", data.nunique())

#counting per column
categorical_cols = data.select_dtypes(include='object').columns
for col in categorical_cols:
    print(f"\nValue Counts for {col}:\n", data[col].value_counts())

#checking for duplicates
print("\nDuplicate Rows:", data.duplicated().sum())
1/20:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

#csv data set
data = pd.read_csv(r'/Users/lydrenjess/Downloads/finalsetwname.csv')
ds = np.loadtxt(r'/Users/lydrenjess/Downloads/finalsetwoname.csv', delimiter=',')
df = np.genfromtxt(r'/Users/lydrenjess/Downloads/finalsetwname.csv', delimiter=',')

#initials 
col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']

print("\nCOLUMNS:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    

#data preview
print("\nFirst 5 rows:\n", data.head())
print("\nLast 5 rows:\n", data.tail())
print("\nRandom 5 Rows:\n", data.sample(5))

#checking for unique values
print("\nUnique Values per Column:\n", data.nunique())

#counting per column
categorical_cols = data.select_dtypes(include='object').columns
for col in categorical_cols:
    print(f"\nValue Counts for {col}:\n", data[col].value_counts())

#checking for duplicates
print("\nDuplicate Rows:", data.duplicated().sum())
1/21:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

#csv data set
data = pd.read_csv(r'/Users/lydrenjess/Downloads/finalsetwname.csv')
ds = np.loadtxt(r'/Users/lydrenjess/Downloads/finalsetwname.csv', delimiter=',')

#initials 
col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']

print("\nCOLUMNS:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    

#data preview
print("\nFirst 5 rows:\n", data.head())
print("\nLast 5 rows:\n", data.tail())
print("\nRandom 5 Rows:\n", data.sample(5))

#checking for unique values
print("\nUnique Values per Column:\n", data.nunique())

#counting per column
categorical_cols = data.select_dtypes(include='object').columns
for col in categorical_cols:
    print(f"\nValue Counts for {col}:\n", data[col].value_counts())

#checking for duplicates
print("\nDuplicate Rows:", data.duplicated().sum())
1/22:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

#csv data set
data = pd.read_csv(r'/Users/lydrenjess/Downloads/finalsetwname.csv')
ds = np.loadtxt(r'/Users/lydrenjess/Downloads/finalsetwname.csv', delimiter=',', skip_header=1)

#initials 
col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']

print("\nCOLUMNS:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    

#data preview
print("\nFirst 5 rows:\n", data.head())
print("\nLast 5 rows:\n", data.tail())
print("\nRandom 5 Rows:\n", data.sample(5))

#checking for unique values
print("\nUnique Values per Column:\n", data.nunique())

#counting per column
categorical_cols = data.select_dtypes(include='object').columns
for col in categorical_cols:
    print(f"\nValue Counts for {col}:\n", data[col].value_counts())

#checking for duplicates
print("\nDuplicate Rows:", data.duplicated().sum())
1/23:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

#csv data set
data = pd.read_csv(r'/Users/lydrenjess/Downloads/finalsetwname.csv')
ds = np.genfromtxt(r'/Users/lydrenjess/Downloads/finalsetwname.csv', delimiter=',')

#initials 
col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']

print("\nCOLUMNS:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    

#data preview
print("\nFirst 5 rows:\n", data.head())
print("\nLast 5 rows:\n", data.tail())
print("\nRandom 5 Rows:\n", data.sample(5))

#checking for unique values
print("\nUnique Values per Column:\n", data.nunique())

#counting per column
categorical_cols = data.select_dtypes(include='object').columns
for col in categorical_cols:
    print(f"\nValue Counts for {col}:\n", data[col].value_counts())

#checking for duplicates
print("\nDuplicate Rows:", data.duplicated().sum())
1/24:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

#csv data set
data = pd.read_csv(r'/Users/lydrenjess/Downloads/finalsetwname.csv')
ds = np.genfromtxt(r'/Users/lydrenjess/Downloads/finalsetwname.csv', delimiter=',')

print(ds)

#initials 
col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']

print("\nCOLUMNS:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    

#data preview
print("\nFirst 5 rows:\n", data.head())
print("\nLast 5 rows:\n", data.tail())
print("\nRandom 5 Rows:\n", data.sample(5))

#checking for unique values
print("\nUnique Values per Column:\n", data.nunique())

#counting per column
categorical_cols = data.select_dtypes(include='object').columns
for col in categorical_cols:
    print(f"\nValue Counts for {col}:\n", data[col].value_counts())

#checking for duplicates
print("\nDuplicate Rows:", data.duplicated().sum())
1/25:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

#csv data set
data = pd.read_csv(r'/Users/lydrenjess/Downloads/finalsetwname.csv')
ds = np.loadtxt(r'/Users/lydrenjess/Downloads/finalsetwoname.csv')

print(ds)

#initials 
col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']

print("\nCOLUMNS:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    

#data preview
print("\nFirst 5 rows:\n", data.head())
print("\nLast 5 rows:\n", data.tail())
print("\nRandom 5 Rows:\n", data.sample(5))

#checking for unique values
print("\nUnique Values per Column:\n", data.nunique())

#counting per column
categorical_cols = data.select_dtypes(include='object').columns
for col in categorical_cols:
    print(f"\nValue Counts for {col}:\n", data[col].value_counts())

#checking for duplicates
print("\nDuplicate Rows:", data.duplicated().sum())
1/26:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

#csv data set
data = pd.read_csv(r'/Users/lydrenjess/Downloads/finalsetwname.csv')
ds = np.loadtxt(r'/Users/lydrenjess/Downloads/finalsetwoname.csv', delimiter=',')

print(ds)

#initials 
col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']

print("\nCOLUMNS:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    

#data preview
print("\nFirst 5 rows:\n", data.head())
print("\nLast 5 rows:\n", data.tail())
print("\nRandom 5 Rows:\n", data.sample(5))

#checking for unique values
print("\nUnique Values per Column:\n", data.nunique())

#counting per column
categorical_cols = data.select_dtypes(include='object').columns
for col in categorical_cols:
    print(f"\nValue Counts for {col}:\n", data[col].value_counts())

#checking for duplicates
print("\nDuplicate Rows:", data.duplicated().sum())
1/27:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

#csv data set

data = pd.read_csv(r'/Users/lydrenjess/Downloads/finalsetwname.csv')
ds = np.loadtxt(r'/Users/lydrenjess/Downloads/finalsetwoname.csv', delimiter=',')

#initials 

col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']

#outputs

print("\nCOLUMNS:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    

#data preview
print("\nFirst 5 rows:\n", data.head())
print("\nLast 5 rows:\n", data.tail())
print("\nRandom 5 Rows:\n", data.sample(5))

#checking for unique values
print("\nUnique Values per Column:\n", data.nunique())

#counting per column
categorical_cols = data.select_dtypes(include='object').columns
for col in categorical_cols:
    print(f"\nValue Counts for {col}:\n", data[col].value_counts())

#checking for duplicates
print("\nDuplicate Rows:", data.duplicated().sum())
1/28:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

#csv data set

data = pd.read_csv(r'/Users/lydrenjess/Downloads/finalsetwname.csv')
ds = np.loadtxt(r'/Users/lydrenjess/Downloads/finalsetwoname.csv', delimiter=',')

#initials 

col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']

#outputs

print("NATIONAL BASKETBALL ASSOCIATION (NBA)")
print("\nDATA SET COLUMNS:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    
print("\nTop 5 Scorers rows:\n", data.head())
print("\nLast 5 rows:\n", data.tail())
print("\nRandom 5 Rows:\n", data.sample(5))

#checking for unique values
print("\nUnique Values per Column:\n", data.nunique())

#counting per column
categorical_cols = data.select_dtypes(include='object').columns
for col in categorical_cols:
    print(f"\nValue Counts for {col}:\n", data[col].value_counts())

#checking for duplicates
print("\nDuplicate Rows:", data.duplicated().sum())
1/29:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

#csv data set

df = pd.read_csv(r'/Users/lydrenjess/Downloads/finalsetwname.csv')
ds = np.loadtxt(r'/Users/lydrenjess/Downloads/finalsetwoname.csv', delimiter=',')

#initials 

col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']

#outputs

print("NATIONAL BASKETBALL ASSOCIATION (NBA)")
print("\nDATA SET COLUMNS:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    
print("\nTop 5 Scorers:\n", df.head())
1/30:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

#csv data set

df = pd.read_csv(r'/Users/lydrenjess/Downloads/finalsetwname.csv')
ds = np.loadtxt(r'/Users/lydrenjess/Downloads/finalsetwoname.csv', delimiter=',')

#initials 

col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']

#outputs

print("TOP SCORERS IN THE NATIONAL BASKETBALL ASSOCIATION (NBA)")
print("\nDATA SET COLUMNS:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    
print("\nTop 5 Scorers:\n", df.head())
1/31:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

#csv data set

df = pd.read_csv(r'/Users/lydrenjess/Downloads/finalsetwname.csv')
ds = np.loadtxt(r'/Users/lydrenjess/Downloads/finalsetwoname.csv', delimiter=',')

#initials 

col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']

#outputs

print("SCORERS DATA IN THE NATIONAL BASKETBALL ASSOCIATION (NBA)")
print("\nDATA SET COLUMNS:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    
print("\nTop 5 Scorers:\n", df.head())
1/32: print(ds)
1/33:
print(ds)

a = ds.split()
1/34:
print(ds)

a = ds.split()
print(a)
1/35:
print(ds)

a = np.split(ds)
print(a)
1/36:
print(ds)

a = np.split(ds, 4)
print(a)
1/37: print(ds)
1/38: print(ds[0][0][1])
1/39: print(ds[1][1][1])
1/40:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import csv

#csv data set

df = pd.read_csv(r'/Users/lydrenjess/Downloads/finalsetwname.csv')
ds = np.loadtxt(r'/Users/lydrenjess/Downloads/finalsetwoname.csv', delimiter=',')

#initials

col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']

#outputs

print("SCORERS DATA IN THE NATIONAL BASKETBALL ASSOCIATION (NBA)")
print("\nDATA SET COLUMNS:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    
print("\nTop 5 Scorers:\n", df.head())
1/41:
def csv_to_array(file_path):
    data_array = []
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data_array.append(row)
    return data_array

# Example usage
file_path = 'your_file.csv'
array_data = csv_to_array(file_path)
print(array_data)
1/42:
def csv_to_array(file_path):
    data_array = []
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data_array.append(row)
    return data_array

# Example usage
file_path = '/Users/lydrenjess/Downloads/finalsetwoname.csv'
array_data = csv_to_array(file_path)
print(array_data)
1/43:
def csv_to_array(file_path):
    dfs = []
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            dfs.append(row)
    return dfs

file_path = '/Users/lydrenjess/Downloads/finalsetwoname.csv'
array_data = csv_to_array(file_path)
print(dfs)
1/44:
def csv_to_array(file_path):
    data_array = []
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data_array.append(row)
    return data_array

file_path = '/Users/lydrenjess/Downloads/finalsetwoname.csv'
array_data = csv_to_array(file_path)
print(array_data[0][0][0])
1/45:
def csv_to_array(file_path):
    data_array = []
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data_array.append(row)
    return data_array

file_path = '/Users/lydrenjess/Downloads/finalsetwoname.csv'
array_data = csv_to_array(file_path)

print(array_data[0][0][0])
print(array_data)
1/46:
def csv_to_array(file_path):
    data_array = np.array[]
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data_array.append(row)
    return data_array

file_path = '/Users/lydrenjess/Downloads/finalsetwoname.csv'
array_data = csv_to_array(file_path)

print(array_data[0][0][0])
print(array_data)
1/47:
def csv_to_array(file_path):
    data_array = np.array([])
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data_array.append(row)
    return data_array

file_path = '/Users/lydrenjess/Downloads/finalsetwoname.csv'
array_data = csv_to_array(file_path)

print(array_data[0][0][0])
print(array_data)
1/48:
def csv_to_array(file_path):
    data_array = []
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data_array.append(row)
    return data_array

file_path = '/Users/lydrenjess/Downloads/finalsetwoname.csv'
array_data = csv_to_array(file_path)

print(array_data[0][1][0])
print(array_data)
1/49:
def csv_to_array(file_path):
    data_array = []
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data_array.append(row)
    return int(data_array)

file_path = '/Users/lydrenjess/Downloads/finalsetwoname.csv'
array_data = csv_to_array(file_path)

print(array_data[0][1][0])
print(array_data)
1/50:
def csv_to_array(file_path):
    data_array = []
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data_array.append(int(row))
    return data_array

file_path = '/Users/lydrenjess/Downloads/finalsetwoname.csv'
array_data = csv_to_array(file_path)

print(array_data[0][1][0])
print(array_data)
1/51:
ppg = df['ppg'].to_numpy()

print(ppg)
1/52:
ppg = df['PPG'].to_numpy()

print(ppg)
1/53:
ppg = df['PPG'].to_numpy()

print(ppg[0])
1/54:
for i in range(len(ds)):
    print(ds[i])
1/55:
a = df
b = df['PPG'].to_np()

print(b[0])
1/56:
a = df['Name'].to_numpy()
b = df['PPG'].to_numpy()
b = df['PPG'].to_numpy()
b = df['PPG'].to_numpy()

print(a[0])
1/57:
a = df['Name'].to_numpy()
b = df['PPG'].to_numpy()
c = df['FG%'].to_numpy()
d = df['FT%'].to_numpy()

print(d[0])
1/58:
a = df['Name'].to_numpy()
b = df['PPG'].to_numpy()
c = df['FG%'].to_numpy()
d = df['FT%'].to_numpy()


print(np.max(b))
1/59:
a = df['Name'].to_numpy()
b = df['PPG'].to_numpy()
c = df['FG%'].to_numpy()
d = df['FT%'].to_numpy()


print(np.max(d))
1/60:
a = df['Name'].to_numpy()
b = df['PPG'].to_numpy()
c = df['FG%'].to_numpy()
d = df['FT%'].to_numpy()


print(np.max(c))
1/61:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import csv

#csv data set

df = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

a = df['Name'].to_numpy()
b = df['PPG'].to_numpy()
c = df['FG%'].to_numpy()
d = df['FT%'].to_numpy()


#initials

col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']

#outputs

print("SCORERS DATA IN THE NATIONAL BASKETBALL ASSOCIATION (NBA)")
print("\nDATA SET COLUMNS:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    
print("\nTop 5 Scorers:\n", df.head())
1/62:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import csv

#csv data set

df = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

a = df['Name'].to_numpy()
b = df['PPG'].to_numpy()
c = df['FG%'].to_numpy()
d = df['FT%'].to_numpy()


#initials

col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']

#outputs

print("Data Shape:", df.shape)
print("SCORERS DATA IN THE NATIONAL BASKETBALL ASSOCIATION (NBA)")
print("\nDATA SET COLUMNS:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    
print("\nTop 5 Scorers:\n", df.head())
1/63:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import csv

#csv data set

df = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

a = df['Name'].to_numpy()
b = df['PPG'].to_numpy()
c = df['FG%'].to_numpy()
d = df['FT%'].to_numpy()


#initials

col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']

#outputs


print("SCORERS DATA IN THE NATIONAL BASKETBALL ASSOCIATION (NBA)\n")
print("Data Shape:", df.shape)
print("\nDATA SET COLUMNS:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    
print("\nTop 5 Scorers:\n", df.head())
1/64:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import csv

#csv data set

df = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

a = df['Name'].to_numpy()
b = df['PPG'].to_numpy()
c = df['FG%'].to_numpy()
d = df['FT%'].to_numpy()


#initials

col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']

#outputs


print("SCORERS DATA IN THE NATIONAL BASKETBALL ASSOCIATION (NBA)\n")
print("Data Shape:", df.shape)
print("\nData set columns:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    
print("\nTop 5 Scorers:\n", df.head())
1/65:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import csv

#DATA SET

df = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

a = df['Name'].to_numpy()
b = df['PPG'].to_numpy()
c = df['FG%'].to_numpy()
d = df['FT%'].to_numpy()


#INITIALS

col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']

#OUTPUTS

print("SCORERS DATA IN THE NATIONAL BASKETBALL ASSOCIATION (NBA)\n")

#proof of clean data set
print("Original Data Shape:", df.shape)
print("\nMissing Values:\n", df.isnull().sum())

print("\nData set columns:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    
print("\nTop 5 Scorers:\n", df.head())
1/66:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import csv

#DATA SET

df = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

a = df['Name'].to_numpy()
b = df['PPG'].to_numpy()
c = df['FG%'].to_numpy()
d = df['FT%'].to_numpy()


#INITIALS

col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']

#OUTPUTS

print("SCORERS DATA IN THE NATIONAL BASKETBALL ASSOCIATION (NBA)\n")

#proof of clean data set
print("Original Data Shape:", df.shape)
print("\nMissing Values:\n", end='', df.isnull().sum())

print("\nData set columns:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    
print("\nTop 5 Scorers:\n", df.head())
1/67:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import csv

#DATA SET

df = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

a = df['Name'].to_numpy()
b = df['PPG'].to_numpy()
c = df['FG%'].to_numpy()
d = df['FT%'].to_numpy()


#INITIALS

col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']

#OUTPUTS

print("SCORERS DATA IN THE NATIONAL BASKETBALL ASSOCIATION (NBA)\n")

#proof of clean data set
print("Original Data Shape:", df.shape)
print("\nMissing Values:\n", df.isnull().sum())

print("\nData set columns:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    
print("\nTop 5 Scorers:\n", df.head())
1/68:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import csv

#DATA SET

df = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

a = df['Name'].to_numpy()
b = df['PPG'].to_numpy()
c = df['FG%'].to_numpy()
d = df['FT%'].to_numpy()


#INITIALS

col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']

#OUTPUTS

print("SCORERS DATA IN THE NATIONAL BASKETBALL ASSOCIATION (NBA)\n")

#proof of clean data set
print("Original Data Shape:", df.shape)
print("\nMissing Values:\n", end='', df.isnull().sum())

print("\nData set columns:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    
print("\nTop 5 Scorers:\n", df.head())
1/69:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import csv

#DATA SET

df = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

a = df['Name'].to_numpy()
b = df['PPG'].to_numpy()
c = df['FG%'].to_numpy()
d = df['FT%'].to_numpy()


#INITIALS

col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']

#OUTPUTS

print("SCORERS DATA IN THE NATIONAL BASKETBALL ASSOCIATION (NBA)\n")

#proof of clean data set
print("Original Data Shape:", df.shape)
print("\nMissing Values:\n") 
print(df.isnull().sum())

print("\nData set columns:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    
print("\nTop 5 Scorers:\n", df.head())
1/70:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import csv

#DATA SET

df = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

a = df['Name'].to_numpy()
b = df['PPG'].to_numpy()
c = df['FG%'].to_numpy()
d = df['FT%'].to_numpy()


#INITIALS

col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']

#OUTPUTS

print("SCORERS DATA IN THE NATIONAL BASKETBALL ASSOCIATION (NBA)\n")

#proof of clean data set
print("Original Data Shape:", df.shape)
print("Missing Values:\n") 
print(df.isnull().sum())

print("\nData set columns:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    
print("\nTop 5 Scorers:\n", df.head())
1/71:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import csv

#DATA SET

df = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

a = df['Name'].to_numpy()
b = df['PPG'].to_numpy()
c = df['FG%'].to_numpy()
d = df['FT%'].to_numpy()


#INITIALS

col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']

#OUTPUTS

print("SCORERS DATA IN THE NATIONAL BASKETBALL ASSOCIATION (NBA)\n")

#proof of clean data set
print("Original Data Shape:", df.shape)
print("Missing Values:") 
print(df.isnull().sum())

print("\nData set columns:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    
print("\nTop 5 Scorers:\n", df.head())
1/72:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import csv

#DATA SET

df = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

a = df['Name'].to_numpy()
b = df['PPG'].to_numpy()
c = df['FG%'].to_numpy()
d = df['FT%'].to_numpy()


#INITIALS

col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']

#OUTPUTS

print("SCORERS DATA IN THE NATIONAL BASKETBALL ASSOCIATION (NBA)\n")

print("\nData set columns:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    
#proof of clean data set
print("Original Data Shape:", df.shape)
print("Missing Values:") 
print(df.isnull().sum())


print("\nTop 5 Scorers:\n", df.head())
1/73:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import csv

#DATA SET

df = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

a = df['Name'].to_numpy()
b = df['PPG'].to_numpy()
c = df['FG%'].to_numpy()
d = df['FT%'].to_numpy()


#INITIALS

col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']

#OUTPUTS

print("SCORERS DATA IN THE NATIONAL BASKETBALL ASSOCIATION (NBA)\n")

print("\nData set columns:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    
#proof of clean data set
print("\nOriginal Data Shape:", df.shape)
print("Missing Values:") 
print(df.isnull().sum())


print("\nTop 5 Scorers:\n", df.head())
1/74:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import csv

#DATA SET

df = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

a = df['Name'].to_numpy()
b = df['PPG'].to_numpy()
c = df['FG%'].to_numpy()
d = df['FT%'].to_numpy()


#INITIALS

col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']

#OUTPUTS

print("SCORERS DATA IN THE NATIONAL BASKETBALL ASSOCIATION (NBA)\n")

print("Data set columns:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    
#proof of clean data set
print("\nOriginal Data Shape:", df.shape)
print("Missing Values:") 
print(df.isnull().sum())


print("\nTop 5 Scorers:\n", df.head())
1/75:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import csv

#DATA SET

df = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

a = df['Name'].to_numpy()
b = df['PPG'].to_numpy()
c = df['FG%'].to_numpy()
d = df['FT%'].to_numpy()


#INITIALS

col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']

#OUTPUTS

print("TOP 200 SCORERS DATA IN THE NATIONAL BASKETBALL ASSOCIATION (NBA)\n")

print("Data set columns:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    
#proof of clean data set
print("\nOriginal Data Shape:", df.shape)
print("Missing Values:") 
print(df.isnull().sum())


print("\nTop Scorer:\n")
x = np.max()
1/76:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import csv

#DATA SET

df = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

a = df['Name'].to_numpy()
b = df['PPG'].to_numpy()
c = df['FG%'].to_numpy()
d = df['FT%'].to_numpy()


#INITIALS

col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']

#OUTPUTS

print("TOP 200 SCORERS DATA IN THE NATIONAL BASKETBALL ASSOCIATION (NBA)\n")

print("Data set columns:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    
#proof of clean data set
print("\nOriginal Data Shape:", df.shape)
print("Missing Values:") 
print(df.isnull().sum())

#top,least, and average scorer
m = np.array([])
n = np.array([])
x = np.max(b)
y = np.min(b)

print("\nTop Scorer:\n")
for i in range(len(b)):
    if b[i] == x:
        m = np.append(i + 1)

    if b[i] == y:
        n = np.append(i + 1)

for i in range(len(m)):
    print(a[m[i]], b[m[i]])
1/77:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import csv

#DATA SET

df = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

a = df['Name'].to_numpy()
b = df['PPG'].to_numpy()
c = df['FG%'].to_numpy()
d = df['FT%'].to_numpy()


#INITIALS

col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']

#OUTPUTS

print("TOP 200 SCORERS DATA IN THE NATIONAL BASKETBALL ASSOCIATION (NBA)\n")

print("Data set columns:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    
#proof of clean data set
print("\nOriginal Data Shape:", df.shape)
print("Missing Values:") 
print(df.isnull().sum())

#top,least, and average scorer
m = np.array([])
n = np.array([])
x = np.max(b)
y = np.min(b)

print("\nTop Scorer:\n")
for i in range(len(b)):
    if b[i] == x:
        m = np.append(i + 1, axis=0)

    if b[i] == y:
        n = np.append(i + 1, axis=0)

for i in range(len(m)):
    print(a[m[i]], b[m[i]])
1/78:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import csv

#DATA SET

df = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

a = df['Name'].to_numpy()
b = df['PPG'].to_numpy()
c = df['FG%'].to_numpy()
d = df['FT%'].to_numpy()


#INITIALS

col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']

#OUTPUTS

print("TOP 200 SCORERS DATA IN THE NATIONAL BASKETBALL ASSOCIATION (NBA)\n")

print("Data set columns:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    
#proof of clean data set
print("\nOriginal Data Shape:", df.shape)
print("Missing Values:") 
print(df.isnull().sum())

#top,least, and average scorer
m = []
n = []
x = np.max(b)
y = np.min(b)

print("\nTop Scorer:\n")
for i in range(len(b)):
    if b[i] == x:
        m.append(i)

    if b[i] == y:
        n.append(i)

for i in range(len(m)):
    print(a[m[i]], b[m[i]])
1/79:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import csv

#DATA SET

df = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

a = df['Name'].to_numpy()
b = df['PPG'].to_numpy()
c = df['FG%'].to_numpy()
d = df['FT%'].to_numpy()


#INITIALS

col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']

#OUTPUTS

print("TOP 200 SCORERS DATA IN THE NATIONAL BASKETBALL ASSOCIATION (NBA)\n")

print("Data set columns:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    
#proof of clean data set
print("\nOriginal Data Shape:", df.shape)
print("Missing Values:") 
print(df.isnull().sum())

#top,least, and average scorer
m = []
n = []
x = np.max(b)
y = np.min(b)

print("\nTop Scorer:")
for i in range(len(b)):
    if b[i] == x:
        m.append(i)

    if b[i] == y:
        n.append(i)

for i in range(len(m)):
    print(a[m[i]], b[m[i]])
1/80:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import csv

#DATA SET

df = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

a = df['Name'].to_numpy()
b = df['PPG'].to_numpy()
c = df['FG%'].to_numpy()
d = df['FT%'].to_numpy()


#INITIALS

col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']

#OUTPUTS

print("TOP 200 SCORERS DATA IN THE NATIONAL BASKETBALL ASSOCIATION (NBA)\n")

print("Data set columns:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    
#proof of clean data set
print("\nOriginal Data Shape:", df.shape)
print("Missing Values:") 
print(df.isnull().sum())

#top,least, and average scorer
m = []
n = []
o = np.empty()
x = np.max(b)
y = np.min(b)

print("\nTop Scorer:")
for i in range(len(b)):
    if b[i] == x:
        m.append(i)

    if b[i] == y:
        n.append(i)

for i in range(len(m)):
    print(a[m[i]], b[m[i]])
1/81:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import csv

#DATA SET

df = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

a = df['Name'].to_numpy()
b = df['PPG'].to_numpy()
c = df['FG%'].to_numpy()
d = df['FT%'].to_numpy()


#INITIALS

col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']

#OUTPUTS

print("TOP 200 SCORERS DATA IN THE NATIONAL BASKETBALL ASSOCIATION (NBA)\n")

print("Data set columns:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    
#proof of clean data set
print("\nOriginal Data Shape:", df.shape)
print("Missing Values:") 
print(df.isnull().sum())

#top,least, and average scorer
m = []
n = []
o = np.empty(4)
x = np.max(b)
y = np.min(b)

print("\nTop Scorer:")
for i in range(len(b)):
    if b[i] == x:
        m.append(i)

    if b[i] == y:
        n.append(i)

for i in range(len(m)):
    print(a[m[i]], b[m[i]])
1/82:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import csv

#DATA SET

df = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

a = df['Name'].to_numpy()
b = df['PPG'].to_numpy()
c = df['FG%'].to_numpy()
d = df['FT%'].to_numpy()


#INITIALS

col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']

#OUTPUTS

print("TOP 200 SCORERS DATA IN THE NATIONAL BASKETBALL ASSOCIATION (NBA)\n")

print("Data set columns:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    
#proof of clean data set
print("\nOriginal Data Shape:", df.shape)
print("Missing Values:") 
print(df.isnull().sum())

#top,least, and average scorer
m = 0
n = 0
x = np.max(b)
y = np.min(b)
z = np.empty(4)

for i in range(len(b)):
    if b[i] == x:
        m = i
    
    if b[i] == y:
        n = i
print("\nTop Scorer:")
print(a[m], b[m], c[m], d[m])
1/83:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import csv

#DATA SET

df = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

a = df['Name'].to_numpy()
b = df['PPG'].to_numpy()
c = df['FG%'].to_numpy()
d = df['FT%'].to_numpy()


#INITIALS

col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']
pos = ['Top', 'Least', 'Average']

#OUTPUTS

print("TOP 200 SCORERS DATA IN THE NATIONAL BASKETBALL ASSOCIATION (NBA)\n")

print("Data set columns:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    
#proof of clean data set
print("\nOriginal Data Shape:", df.shape)
print("Missing Values:") 
print(df.isnull().sum())

#top,least, and average scorer
m = 0
n = 0
o = 0
x = np.max(b)
y = np.min(b)

for i in range(len(b)):
    if b[i] == x:
        m = i
    
    if b[i] == y:
        n = i

    if b[i] == z:
        o = i
print(pos[j], col_cat[j+1])
print(a[m], b[m])
1/84:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import csv

#DATA SET

df = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

a = df['Name'].to_numpy()
b = df['PPG'].to_numpy()
c = df['FG%'].to_numpy()
d = df['FT%'].to_numpy()


#INITIALS

col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']
pos = ['Top', 'Least', 'Average']

#OUTPUTS

print("TOP 200 SCORERS DATA IN THE NATIONAL BASKETBALL ASSOCIATION (NBA)\n")

print("Data set columns:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    
#proof of clean data set
print("\nOriginal Data Shape:", df.shape)
print("Missing Values:") 
print(df.isnull().sum())

#top,least, and average scorer
m = 0
n = 0
o = 0
x = np.max(b)
y = np.min(b)
z = np.mean(b)
for i in range(len(b)):
    if b[i] == x:
        m = i
    
    if b[i] == y:
        n = i

    if b[i] == z:
        o = i
print(pos[j], col_cat[j+1])
print(a[m], b[m])
1/85:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import csv

#DATA SET

df = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

a = df['Name'].to_numpy()
b = df['PPG'].to_numpy()
c = df['FG%'].to_numpy()
d = df['FT%'].to_numpy()


#INITIALS

col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']
pos = ['Top', 'Least', 'Average']

#OUTPUTS

print("TOP 200 SCORERS DATA IN THE NATIONAL BASKETBALL ASSOCIATION (NBA)\n")

print("Data set columns:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    
#proof of clean data set
print("\nOriginal Data Shape:", df.shape)
print("Missing Values:") 
print(df.isnull().sum())

#top,least, and average scorer
for j in range (len(pos)):
    m = 0
    n = 0
    o = 0
    x = np.max(b)
    y = np.min(b)
    z = np.mean(b)
    
    for i in range(len(b)):
        if b[i] == x:
            m = i
    
        if b[i] == y:
            n = i

        if b[i] == z:
            o = i
    print(pos[j], col_cat[j+1])
    print(a[m], b[m])
1/86:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import csv

#DATA SET

df = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

a = df['Name'].to_numpy()
b = df['PPG'].to_numpy()
c = df['FG%'].to_numpy()
d = df['FT%'].to_numpy()


#INITIALS

col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']
pos = ['Top', 'Least', 'Average']

#OUTPUTS

print("TOP 200 SCORERS DATA IN THE NATIONAL BASKETBALL ASSOCIATION (NBA)\n")

print("Data set columns:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    
#proof of clean data set
print("\nOriginal Data Shape:", df.shape)
print("Missing Values:") 
print(df.isnull().sum())

#top,least, and average scorer
for j in range (len(pos)):
    m = 0
    n = 0
    o = 0
    x = np.max(b)
    y = np.min(b)
    z = np.mean(b)
    q = np.empty(3)
    
    for i in range(len(b)):
        if b[i] == x:
            m = i
    
        if b[i] == y:
            n = i

        if b[i] == z:
            o = i
    q.append(m, n, i)
    print(pos[j], col_cat[j+1])
    print(a[m], b[m])
1/87:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import csv

#DATA SET

df = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

a = df['Name'].to_numpy()
b = df['PPG'].to_numpy()
c = df['FG%'].to_numpy()
d = df['FT%'].to_numpy()


#INITIALS

col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']
pos = ['Top', 'Least', 'Average']

#OUTPUTS

print("TOP 200 SCORERS DATA IN THE NATIONAL BASKETBALL ASSOCIATION (NBA)\n")

print("Data set columns:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    
#proof of clean data set
print("\nOriginal Data Shape:", df.shape)
print("Missing Values:") 
print(df.isnull().sum())

#top,least, and average scorer
for j in range (len(pos)):
    m = 0
    n = 0
    o = 0
    x = np.max(b)
    y = np.min(b)
    z = np.mean(b)
    q = np.empty(3)
    
    for i in range(len(b)):
        if b[i] == x:
            m = i
    
        if b[i] == y:
            n = i

        if b[i] == z:
            o = i
    q.np.append(m, n, i)
    print(pos[j], col_cat[j+1])
    print(a[m], b[m])
1/88:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import csv

#DATA SET

df = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

a = df['Name'].to_numpy()
b = df['PPG'].to_numpy()
c = df['FG%'].to_numpy()
d = df['FT%'].to_numpy()


#INITIALS

col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']
pos = ['Top', 'Least', 'Average']

#OUTPUTS

print("TOP 200 SCORERS DATA IN THE NATIONAL BASKETBALL ASSOCIATION (NBA)\n")

print("Data set columns:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    
#proof of clean data set
print("\nOriginal Data Shape:", df.shape)
print("Missing Values:") 
print(df.isnull().sum())

#top,least, and average scorer
for j in range (len(pos)):
    m = 0
    n = 0
    o = 0
    x = np.max(b)
    y = np.min(b)
    z = np.mean(b)
    q = np.empty(3)
    
    for i in range(len(b)):
        if b[i] == x:
            m = i
    
        if b[i] == y:
            n = i

        if b[i] == z:
            o = i
    q = np.append(m, n, i)
    print(pos[j], col_cat[j+1])
    print(a[m], b[m])
1/89:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import csv

#DATA SET

df = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

a = df['Name'].to_numpy()
b = df['PPG'].to_numpy()
c = df['FG%'].to_numpy()
d = df['FT%'].to_numpy()


#INITIALS

col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']
pos = ['Top', 'Least', 'Average']

#OUTPUTS

print("TOP 200 SCORERS DATA IN THE NATIONAL BASKETBALL ASSOCIATION (NBA)\n")

print("Data set columns:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    
#proof of clean data set
print("\nOriginal Data Shape:", df.shape)
print("Missing Values:") 
print(df.isnull().sum())

#top,least, and average scorer
for j in range (len(pos)):
    m = 0
    n = 0
    o = 0
    x = np.max(b)
    y = np.min(b)
    z = np.mean(b)
    q = np.empty(3)
    
    for i in range(len(b)):
        if b[i] == x:
            m = i
    
        if b[i] == y:
            n = i

        if b[i] == z:
            o = i
    q = np.append(m, n, i)
    print(pos[j], col_cat[j+1])
    if q[j] == 0:
        print(a[m], b[m])

    if q[j] == 1:
        print(a[n], b[n])

    if q[j] == 2:
        print(a[o], b[o])
1/90:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import csv

#DATA SET

df = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

a = df['Name'].to_numpy()
b = df['PPG'].to_numpy()
c = df['FG%'].to_numpy()
d = df['FT%'].to_numpy()


#INITIALS

col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']
pos = ['Top', 'Least', 'Average']

#OUTPUTS

print("TOP 200 SCORERS DATA IN THE NATIONAL BASKETBALL ASSOCIATION (NBA)\n")

print("Data set columns:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    
#proof of clean data set
print("\nOriginal Data Shape:", df.shape)
print("Missing Values:") 
print(df.isnull().sum())

#top,least, and average scorer
for j in range (len(pos)):
    m = 0
    n = 0
    o = 0
    x = np.max(b)
    y = np.min(b)
    z = np.mean(b)
    q = []
    
    for i in range(len(b)):
        if b[i] == x:
            m = i
    
        if b[i] == y:
            n = i

        if b[i] == z:
            o = i
    q = np.append(m, n, i)
    print(pos[j], col_cat[j+1])
    if q[j] == 0:
        print(a[m], b[m])

    if q[j] == 1:
        print(a[n], b[n])

    if q[j] == 2:
        print(a[o], b[o])
1/91:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import csv

#DATA SET

df = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

a = df['Name'].to_numpy()
b = df['PPG'].to_numpy()
c = df['FG%'].to_numpy()
d = df['FT%'].to_numpy()


#INITIALS

col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']
pos = ['Top', 'Least', 'Average']

#OUTPUTS

print("TOP 200 SCORERS DATA IN THE NATIONAL BASKETBALL ASSOCIATION (NBA)\n")

print("Data set columns:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    
#proof of clean data set
print("\nOriginal Data Shape:", df.shape)
print("Missing Values:") 
print(df.isnull().sum())

#top,least, and average scorer
for j in range (len(pos)):
    m = 0
    n = 0
    o = 0
    x = np.max(b)
    y = np.min(b)
    z = np.mean(b)
    q = np.empty(3)
    
    for i in range(len(b)):
        if b[i] == x:
            q = np.insert(0, i)
    
        if b[i] == y:
            q = np.insert(1, i)

        if b[i] == z:
            q = np.insert(2, i)
    
    print(pos[j], col_cat[j+1])
    if q[j] == 0:
        print(a[m], b[m])

    if q[j] == 1:
        print(a[n], b[n])

    if q[j] == 2:
        print(a[o], b[o])
1/92:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import csv

#DATA SET

df = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

a = df['Name'].to_numpy()
b = df['PPG'].to_numpy()
c = df['FG%'].to_numpy()
d = df['FT%'].to_numpy()


#INITIALS

col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']
pos = ['Top', 'Least', 'Average']

#OUTPUTS

print("TOP 200 SCORERS DATA IN THE NATIONAL BASKETBALL ASSOCIATION (NBA)\n")

print("Data set columns:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    
#proof of clean data set
print("\nOriginal Data Shape:", df.shape)
print("Missing Values:") 
print(df.isnull().sum())

#top,least, and average scorer
for j in range (len(pos)):
    m = 0
    n = 0
    o = 0
    x = np.max(b)
    y = np.min(b)
    z = np.mean(b)
    q = np.empty(3)
    
    for i in range(len(b)):
        if b[i] == x:
            q.insert(0, i)
    
        if b[i] == y:
            q.insert(1, i)

        if b[i] == z:
            q.insert(2, i)
    
    print(pos[j], col_cat[j+1])
    if q[j] == 0:
        print(a[m], b[m])

    if q[j] == 1:
        print(a[n], b[n])

    if q[j] == 2:
        print(a[o], b[o])
1/93:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import csv

#DATA SET

df = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

a = df['Name'].to_numpy()
b = df['PPG'].to_numpy()
c = df['FG%'].to_numpy()
d = df['FT%'].to_numpy()


#INITIALS

col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']
pos = ['Top', 'Least', 'Average']

#OUTPUTS

print("TOP 200 SCORERS DATA IN THE NATIONAL BASKETBALL ASSOCIATION (NBA)\n")

print("Data set columns:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    
#proof of clean data set
print("\nOriginal Data Shape:", df.shape)
print("Missing Values:") 
print(df.isnull().sum())

#top,least, and average scorer
for j in range (len(pos)):
    m = 0
    n = 0
    o = 0
    x = np.max(b)
    y = np.min(b)
    z = np.mean(b)
    q = []
    
    for i in range(len(b)):
        if b[i] == x:
            q.insert(0, i)
    
        if b[i] == y:
            q.insert(1, i)

        if b[i] == z:
            q.insert(2, i)
    
    print(pos[j], col_cat[j+1])
    if q[j] == 0:
        print(a[m], b[m])

    if q[j] == 1:
        print(a[n], b[n])

    if q[j] == 2:
        print(a[o], b[o])
1/94:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import csv

#DATA SET

df = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

a = df['Name'].to_numpy()
b = df['PPG'].to_numpy()
c = df['FG%'].to_numpy()
d = df['FT%'].to_numpy()


#INITIALS

col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']
pos = ['Top', 'Least', 'Average']

#OUTPUTS

print("TOP 200 SCORERS DATA IN THE NATIONAL BASKETBALL ASSOCIATION (NBA)\n")

print("Data set columns:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    
#proof of clean data set
print("\nOriginal Data Shape:", df.shape)
print("Missing Values:") 
print(df.isnull().sum())

#top,least, and average scorer
for j in range (len(pos)):
    m = 0
    n = 0
    o = 0
    x = np.max(b)
    y = np.min(b)
    z = np.mean(b)
    q = []
    
    for i in range(len(b)):
        if b[i] == x:
            q.insert(0, i)
    
        if b[i] == y:
            q.insert(1, i)

        if b[i] == z:
            q.insert(2, i)
    
    print(pos[j], col_cat[j+1])
    if j == 0:
        print(a[m], b[m])

    if j == 1:
        print(a[n], b[n])

    if j == 2:
        print(a[o], b[o])
1/95:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import csv

#DATA SET

df = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

a = df['Name'].to_numpy()
b = df['PPG'].to_numpy()
c = df['FG%'].to_numpy()
d = df['FT%'].to_numpy()


#INITIALS

col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']
pos = ['Top', 'Least', 'Average']

#OUTPUTS

print("TOP 200 SCORERS DATA IN THE NATIONAL BASKETBALL ASSOCIATION (NBA)\n")

print("Data set columns:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    
#proof of clean data set
print("\nOriginal Data Shape:", df.shape)
print("Missing Values:") 
print(df.isnull().sum())

#top,least, and average scorer
for j in range (len(pos)):
    m = 0
    n = 0
    o = 0
    x = np.max(b)
    y = np.min(b)
    z = np.mean(b)
    q = []
    
    for i in range(len(b)):
        if b[i] == x:
            q.insert(0, i)
    
        if b[i] == y:
            q.insert(1, i)

        if b[i] == z:
            q.insert(2, i)
    
    print(pos[j], col_cat[j+1])
    print(a[q[j]], b[q[j]])
1/96:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import csv

#DATA SET

df = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

a = df['Name'].to_numpy()
b = df['PPG'].to_numpy()
c = df['FG%'].to_numpy()
d = df['FT%'].to_numpy()


#INITIALS

col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']
pos = ['Top', 'Least', 'Average']

#OUTPUTS

print("TOP 200 SCORERS DATA IN THE NATIONAL BASKETBALL ASSOCIATION (NBA)\n")

print("Data set columns:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    
#proof of clean data set
print("\nOriginal Data Shape:", df.shape)
print("Missing Values:") 
print(df.isnull().sum())

#top,least, and average scorer
for j in range (len(pos)):
    m = 0
    n = 0
    o = 0
    x = np.max(b)
    y = np.min(b)
    z = np.mean(b)
    q = []
    
    for i in range(len(b)):
        if b[i] == x:
            q.insert(0, i)
    
        if b[i] == y:
            q.insert(1, i)

    print(pos[j], col_cat[j+1])
    print(a[q[j]], b[q[j]])
    if j == 2:
        print("An Average Top 200 NBA Scorer has a PPG of", z)
1/97:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import csv

#DATA SET

df = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

a = df['Name'].to_numpy()
b = df['PPG'].to_numpy()
c = df['FG%'].to_numpy()
d = df['FT%'].to_numpy()


#INITIALS

col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']
pos = ['Top', 'Least', 'Average']

#OUTPUTS

print("TOP 200 SCORERS DATA IN THE NATIONAL BASKETBALL ASSOCIATION (NBA)\n")

print("Data set columns:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    
#proof of clean data set
print("\nOriginal Data Shape:", df.shape)
print("Missing Values:") 
print(df.isnull().sum())

#top,least, and average scorer
for j in range (len(pos)):
    m = 0
    n = 0
    o = 0
    x = np.max(b)
    y = np.min(b)
    z = np.mean(b)
    q = []
    
    for i in range(len(b)):
        if b[i] == x:
            q.insert(0, i)
    
        if b[i] == y:
            q.insert(1, i)

    print(pos[j], col_cat[j+1])
    if j < 2:
    print(a[q[j]], b[q[j]])
    if j == 2:
        print("An Average Top 200 NBA Scorer has a PPG of", z)
1/98:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import csv

#DATA SET

df = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

a = df['Name'].to_numpy()
b = df['PPG'].to_numpy()
c = df['FG%'].to_numpy()
d = df['FT%'].to_numpy()


#INITIALS

col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']
pos = ['Top', 'Least', 'Average']

#OUTPUTS

print("TOP 200 SCORERS DATA IN THE NATIONAL BASKETBALL ASSOCIATION (NBA)\n")

print("Data set columns:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    
#proof of clean data set
print("\nOriginal Data Shape:", df.shape)
print("Missing Values:") 
print(df.isnull().sum())

#top,least, and average scorer
for j in range (len(pos)):
    m = 0
    n = 0
    o = 0
    x = np.max(b)
    y = np.min(b)
    z = np.mean(b)
    q = []
    
    for i in range(len(b)):
        if b[i] == x:
            q.insert(0, i)
    
        if b[i] == y:
            q.insert(1, i)

    print(pos[j], col_cat[j+1])
    if j < 2:
        print(a[q[j]], b[q[j]])
    if j == 2:
        print("An Average Top 200 NBA Scorer has a PPG of", z)
1/99:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import csv

#DATA SET

df = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

a = df['Name'].to_numpy()
b = df['PPG'].to_numpy()
c = df['FG%'].to_numpy()
d = df['FT%'].to_numpy()


#INITIALS

col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']
pos = ['Top', 'Least', 'Average']

#OUTPUTS

print("TOP 200 SCORERS DATA IN THE NATIONAL BASKETBALL ASSOCIATION (NBA)\n")

print("Data set columns:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    
#proof of clean data set
print("\nOriginal Data Shape:", df.shape)
print("Missing Values:") 
print(df.isnull().sum())

#top,least, and average scorer
for j in range (len(pos)):
    m = 0
    n = 0
    o = 0
    x = np.max(b)
    y = np.min(b)
    z = np.mean(b)
    q = []
    
    for i in range(len(b)):
        if b[i] == x:
            q.insert(0, i)
    
        if b[i] == y:
            q.insert(1, i)

    print(pos[j], col_cat[1])
    if j < 2:
        print(a[q[j]], b[q[j]])
    if j == 2:
        print("An Average Top 200 NBA Scorer has a PPG of", z)
1/100:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import csv

#DATA SET

df = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

a = df['Name'].to_numpy()
b = df['PPG'].to_numpy()
c = df['FG%'].to_numpy()
d = df['FT%'].to_numpy()


#INITIALS

col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']
pos = ['Top', 'Least', 'TOP 200 Average']

#OUTPUTS

print("TOP 200 SCORERS DATA IN THE NATIONAL BASKETBALL ASSOCIATION (NBA)\n")

print("Data set columns:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    
#proof of clean data set
print("\nOriginal Data Shape:", df.shape)
print("Missing Values:") 
print(df.isnull().sum())

#top,least, and average scorer
for j in range (len(pos)):
    m = 0
    n = 0
    o = 0
    x = np.max(b)
    y = np.min(b)
    z = np.mean(b)
    q = []
    
    for i in range(len(b)):
        if b[i] == x:
            q.insert(0, i)
    
        if b[i] == y:
            q.insert(1, i)

    print(pos[j], col_cat[1])
    if j < 2:
        print(a[q[j]], b[q[j]])
    if j == 2:
        print(z)
1/101:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import csv

#DATA SET

df = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

a = df['Name'].to_numpy()
b = df['PPG'].to_numpy()
c = df['FG%'].to_numpy()
d = df['FT%'].to_numpy()


#INITIALS

col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']
pos = ['Top', 'Least', 'TOP 200 Average']

#OUTPUTS

print("TOP 200 SCORERS DATA IN THE NATIONAL BASKETBALL ASSOCIATION (NBA)\n")

print("Data set columns:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    
#proof of clean data set
print("\nOriginal Data Shape:", df.shape)
print("Missing Values:") 
print(df.isnull().sum())

#top,least, and average scorer
for j in range (len(pos)):
    m = 0
    n = 0
    o = 0
    x = np.max(b)
    y = np.min(b)
    z = np.mean(b)
    q = []
    
    for i in range(len(b)):
        if b[i] == x:
            q.insert(0, i)
    
        if b[i] == y:
            q.insert(1, i)

    print()
    print(pos[j], col_cat[1])
    if j < 2:
        print(a[q[j]], b[q[j]])
    if j == 2:
        print(z)
1/102:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import csv

#DATA SET

df = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

a = df['Name'].to_numpy()
b = df['PPG'].to_numpy()
c = df['FG%'].to_numpy()
d = df['FT%'].to_numpy()


#INITIALS

col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']
pos = ['Top', 'Least', 'Top 200 Average']

#OUTPUTS

print("TOP 200 SCORERS DATA IN THE NATIONAL BASKETBALL ASSOCIATION (NBA)\n")

print("Data set columns:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    
#proof of clean data set
print("\nOriginal Data Shape:", df.shape)
print("Missing Values:") 
print(df.isnull().sum())

#top,least, and average scorer
for j in range (len(pos)):
    m = 0
    n = 0
    o = 0
    x = np.max(b)
    y = np.min(b)
    z = np.mean(b)
    q = []
    
    for i in range(len(b)):
        if b[i] == x:
            q.insert(0, i)
    
        if b[i] == y:
            q.insert(1, i)

    print()
    print(pos[j], col_cat[1])
    if j < 2:
        print(a[q[j]], b[q[j]])
    if j == 2:
        print(z)
1/103:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import csv

#DATA SET

df = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

a = df['Name'].to_numpy()
b = df['PPG'].to_numpy()
c = df['FG%'].to_numpy()
d = df['FT%'].to_numpy()


#INITIALS

col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']
pos = ['Top', 'Least', 'Mean']

#OUTPUTS

print("TOP 200 SCORERS DATA IN THE NATIONAL BASKETBALL ASSOCIATION (NBA)\n")

print("Data set columns:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    
#proof of clean data set
print("\nOriginal Data Shape:", df.shape)
print("Missing Values:") 
print(df.isnull().sum())

#top,least, and average scorer
for j in range (len(pos)):
    m = 0
    n = 0
    o = 0
    x = np.max(b)
    y = np.min(b)
    z = np.mean(b)
    q = []
    
    for i in range(len(b)):
        if b[i] == x:
            q.insert(0, i)
    
        if b[i] == y:
            q.insert(1, i)

    print()
    print(pos[j], col_cat[1])
    if j < 2:
        print(a[q[j]], b[q[j]])
    if j == 2:
        print(z)
1/104:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import csv

#DATA SET

df = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

a = df['Name'].to_numpy()
b = df['PPG'].to_numpy()
c = df['FG%'].to_numpy()
d = df['FT%'].to_numpy()


#INITIALS

col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']
pos = ['Top', 'Least', 'Mean']

#OUTPUTS

print("TOP 200 SCORERS DATA IN THE NATIONAL BASKETBALL ASSOCIATION (NBA)\n")

print("Data set columns:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    
#proof of clean data set
print("\nOriginal Data Shape:", df.shape)
print("Missing Values:") 
print(df.isnull().sum())

#top,least, and average scorer
for p in range(3):
    for j in range (len(pos)):
        m = 0
        n = 0
        o = 0
        x = np.max(b)
        y = np.min(b)
        z = np.mean(b)
        q = []
    
        for i in range(len(b)):
            if b[i] == x:
                q.insert(0, i)
    
            if b[i] == y:
                q.insert(1, i)

        print()
        print(pos[j], col_cat[p+1])
        if j < 2:
            print(a[q[j]], b[q[j]])
        if j == 2:
            print(z)
1/105:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import csv

#DATA SET

df = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

a = df['Name'].to_numpy()
b = df['PPG'].to_numpy()
c = df['FG%'].to_numpy()
d = df['FT%'].to_numpy()


#INITIALS

col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']
pos = ['Top', 'Least', 'Mean']

#OUTPUTS

print("TOP 200 SCORERS DATA IN THE NATIONAL BASKETBALL ASSOCIATION (NBA)\n")

print("Data set columns:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    
#proof of clean data set
print("\nOriginal Data Shape:", df.shape)
print("Missing Values:") 
print(df.isnull().sum())

#top,least, and average scorer
for p in range(3):
    for j in range (len(pos)):
        m = 0
        n = 0
        o = 0
        x = np.max(b)
        y = np.min(b)
        z = np.mean(b)
        q = []
    
        for i in range(len(b)):
            if b[i] == x:
                q.insert(0, i)
    
            if b[i] == y:
                q.insert(1, i)

        print()
        print(pos[j], col_cat[1])
        if j < 2:
            print(a[q[j]], b[q[j]])
        if j == 2:
            print(z)
1/106:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import csv

#DATA SET

df = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

a = df['Name'].to_numpy()
b = df['PPG'].to_numpy()
c = df['FG%'].to_numpy()
d = df['FT%'].to_numpy()


#INITIALS

col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']
pos = ['Top', 'Least', 'Mean']

#OUTPUTS

print("TOP 200 SCORERS DATA IN THE NATIONAL BASKETBALL ASSOCIATION (NBA)\n")

print("Data set columns:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    
#proof of clean data set
print("\nOriginal Data Shape:", df.shape)
print("Missing Values:") 
print(df.isnull().sum())

#top,least, and average scorer
for p in range(3):
    for j in range (len(pos)):
        m = 0
        n = 0
        o = 0
        x = np.max(b)
        y = np.min(b)
        z = np.mean(b)
        q = []
    
        for i in range(len(b)):
            if b[i] == x:
                q.insert(0, i)
    
            if b[i] == y:
                q.insert(1, i)

        print()
        print(pos[j], col_cat[1])
        if j < 2:
            print(a[q[j]], b[q[j]])
        if j == 2:
            print(z)
1/107:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import csv

#DATA SET

df = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

a = df['Name'].to_numpy()
b = df['PPG'].to_numpy()
c = df['FG%'].to_numpy()
d = df['FT%'].to_numpy()


#INITIALS

col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']
pos = ['Top', 'Least', 'Mean']

#OUTPUTS

print("TOP 200 SCORERS DATA IN THE NATIONAL BASKETBALL ASSOCIATION (NBA)\n")

print("Data set columns:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    
#proof of clean data set
print("\nOriginal Data Shape:", df.shape)
print("Missing Values:") 
print(df.isnull().sum())

#top,least, and average scorer
for j in range (len(pos)):
    m = 0
    n = 0
    o = 0
    x = np.max(b)
    y = np.min(b)
    z = np.mean(b)
    q = []
    
    for i in range(len(b)):
        if b[i] == x:
            q.insert(0, i)
    
        if b[i] == y:
            q.insert(1, i)

    print()
    print(pos[j], col_cat[1])
    if j < 2:
        print(a[q[j]], b[q[j]])
    if j == 2:
        print(z)
1/108:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import csv

#DATA SET

df = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

a = df['Name'].to_numpy()
b = df['PPG'].to_numpy()
c = df['FG%'].to_numpy()
d = df['FT%'].to_numpy()


#INITIALS

col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']
pos = ['Top', 'Least', 'Mean']

#OUTPUTS

print("TOP 200 SCORERS DATA IN THE NATIONAL BASKETBALL ASSOCIATION (NBA)\n")

print("Data set columns:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    
#proof of clean data set
print("\nOriginal Data Shape:", df.shape)
print("Missing Values:") 
print(df.isnull().sum())

#top,least, and average scorer
for j in range (len(pos)):
    m = 0
    n = 0
    o = 0
    x = np.max(b)
    y = np.min(b)
    z = np.mean(b)
    q = []
    
    for i in range(len(b)):
        if b[i] == x:
            q.insert(0, i)
    
        if b[i] == y:
            q.insert(1, i)

    print()
    print(pos[j], col_cat[1])
    if j < 2:
        print(a[q[j]], b[q[j]])
    if j == 2:
        print(z)
1/109:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import csv

#DATA SET

df = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

a = df['Name'].to_numpy()
b = df['PPG'].to_numpy()
c = df['FG%'].to_numpy()
d = df['FT%'].to_numpy()


#INITIALS

col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']
pos = ['Top', 'Least', 'Mean']

#OUTPUTS

print("TOP 200 SCORERS DATA IN THE NATIONAL BASKETBALL ASSOCIATION (NBA)\n")

print("Data set columns:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    
#proof of clean data set
print("\nOriginal Data Shape:", df.shape)
print("Missing Values:") 
print(df.isnull().sum())

#top,least, and average scorer
for j in range (len(pos)):
    m = 0
    n = 0
    o = 0
    x = np.max(b)
    y = np.min(b)
    z = np.mean(b)
    q = []
    
    for i in range(len(b)):
        if b[i] == x:
            q.insert(0, i)
    
        if b[i] == y:
            q.insert(1, i)

    print()
    print(pos[j], col_cat[1])
    if j < 2:
        print(a[q[j]], b[q[j]])
    if j == 2:
        print(z)
1/110:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import csv

#DATA SET

df = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

a = df['Name'].to_numpy()
b = df['PPG'].to_numpy()
c = df['FG%'].to_numpy()
d = df['FT%'].to_numpy()


#INITIALS

col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']
pos = ['Top', 'Least', 'Mean']

#OUTPUTS

print("TOP 200 SCORERS DATA IN THE NATIONAL BASKETBALL ASSOCIATION (NBA)\n")

print("Data set columns:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    
#proof of clean data set
print("\nOriginal Data Shape:", df.shape)
print("Missing Values:") 
print(df.isnull().sum())
print("\nFirst 5 rows:\n", df.head())
#top,least, and average scorer
for j in range (len(pos)):
    m = 0
    n = 0
    o = 0
    x = np.max(b)
    y = np.min(b)
    z = np.mean(b)
    q = []
    
    for i in range(len(b)):
        if b[i] == x:
            q.insert(0, i)
    
        if b[i] == y:
            q.insert(1, i)

    print()
    print(pos[j], col_cat[1])
    if j < 2:
        print(a[q[j]], b[q[j]])
    if j == 2:
        print(z)
1/111:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import csv

#DATA SET

df = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

a = df['Name'].to_numpy()
b = df['PPG'].to_numpy()
c = df['FG%'].to_numpy()
d = df['FT%'].to_numpy()


#INITIALS

col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']
pos = ['Top', 'Least', 'Mean']

#OUTPUTS

print("TOP 200 SCORERS DATA IN THE NATIONAL BASKETBALL ASSOCIATION (NBA)\n")

print("Data set columns:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    
#proof of clean data set
print("\nOriginal Data Shape:", df.shape)
print("Missing Values:") 
print(df.isnull().sum())
print("\nTop 5 scorers:\n", df.head())
#top,least, and average scorer
for j in range (len(pos)):
    m = 0
    n = 0
    o = 0
    x = np.max(b)
    y = np.min(b)
    z = np.mean(b)
    q = []
    
    for i in range(len(b)):
        if b[i] == x:
            q.insert(0, i)
    
        if b[i] == y:
            q.insert(1, i)

    print()
    print(pos[j], col_cat[1])
    if j < 2:
        print(a[q[j]], b[q[j]])
    if j == 2:
        print(z)
1/112:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import csv

#DATA SET

df = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

a = df['Name'].to_numpy()
b = df['PPG'].to_numpy()
c = df['FG%'].to_numpy()
d = df['FT%'].to_numpy()


#INITIALS

col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']
pos = ['Top', 'Least', 'Mean']

#OUTPUTS

print("TOP 200 SCORERS DATA IN THE NATIONAL BASKETBALL ASSOCIATION (NBA)\n")

print("Data set columns:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    
#proof of clean data set
print("\nOriginal Data Shape:", df.shape)
print("Missing Values:") 
print(df.isnull().sum())
print("\nTop 5 scorers:\n", df.head())
1/113:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import csv

#DATA SET

df = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

a = df['Name'].to_numpy()
b = df['PPG'].to_numpy()
c = df['FG%'].to_numpy()
d = df['FT%'].to_numpy()


#INITIALS

col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']

#OUTPUTS

print("TOP 200 SCORERS DATA IN THE NATIONAL BASKETBALL ASSOCIATION (NBA)\n")

print("Data set columns:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    
#proof of clean data set
print("\nOriginal Data Shape:", df.shape)
print("Missing Values:") 
print(df.isnull().sum())
print("\nTop 5 scorers:\n", df.head())

sumppg = np.sum(b)
maxppg = np.max(b)
minppg = np.min(b)
meanfg = np.mean(c)
medianfg = np.median(c)
perfg = np.percentile(c, [90, 95, 99])
stdft = np.std(d)
varft = np.var(d)
rangeft = np.ptp(d)

print("\nPPG Statistics:")
print(f"Sum of PPG: {sumppg:.1f}")
print(f"Maximum of PPG: {maxppg:.1f}")
print(f"Minimum of PPG: {minppg:.1f}")

print("\nFG% Statistics:")
print(f"Mean of FG%: {meanfg:.1f}")
print(f"Median of FG%: {medianfg:.1f}")
print(f"90th, 95th, and 99th Percentile of FG%: {perfg:.1f}")

print("\nFT% Statistics:")
print(f"Standard Deviation of FT%: {stdft:.1f}")
print(f"Variance of FT%: {varft:.1f}")
print(f"Range of FT%: {rangeft:.1f}")
1/114:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import csv

#DATA SET

df = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

a = df['Name'].to_numpy()
b = df['PPG'].to_numpy()
c = df['FG%'].to_numpy()
d = df['FT%'].to_numpy()


#INITIALS

col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']

#OUTPUTS

print("TOP 200 SCORERS DATA IN THE NATIONAL BASKETBALL ASSOCIATION (NBA)\n")

print("Data set columns:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    
#proof of clean data set
print("\nOriginal Data Shape:", df.shape)
print("Missing Values:") 
print(df.isnull().sum())
print("\nTop 5 scorers:\n", df.head())

sumppg = np.sum(b)
maxppg = np.max(b)
minppg = np.min(b)
meanfg = np.mean(c)
medianfg = np.median(c)
perfg = np.percentile(c, [90, 95, 99])
stdft = np.std(d)
varft = np.var(d)
rangeft = np.ptp(d)

print("\nPPG Statistics:")
print(f"Sum of PPG: {sumppg:.1f}")
print(f"Maximum of PPG: {maxppg:.1f}")
print(f"Minimum of PPG: {minppg:.1f}")

print("\nFG% Statistics:")
print(f"Mean of FG%: {meanfg:.1f}")
print(f"Median of FG%: {medianfg:.1f}")
print(f"90th, 95th, and 99th Percentile of FG%: {perfg:.1f}")

print("\nFT% Statistics:")
print(f"Standard Deviation of FT%: {stdft:.1f}")
print(f"Variance of FT%: {varft:.1f}")
print(f"Range of FT%: {rangeft:.1f}")
1/115:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import csv

#DATA SET

df = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

a = df['Name'].to_numpy()
b = df['PPG'].to_numpy()
c = df['FG%'].to_numpy()
d = df['FT%'].to_numpy()


#INITIALS

col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']

#OUTPUTS

print("TOP 200 SCORERS DATA IN THE NATIONAL BASKETBALL ASSOCIATION (NBA)\n")

print("Data set columns:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    
#proof of clean data set
print("\nOriginal Data Shape:", df.shape)
print("Missing Values:") 
print(df.isnull().sum())
print("\nTop 5 scorers:\n", df.head())

sumppg = np.sum(b)
maxppg = np.max(b)
minppg = np.min(b)
meanfg = np.mean(c)
medianfg = np.median(c)
perfg = np.percentile(c, [90, 95, 99])
stdft = np.std(d)
varft = np.var(d)
rangeft = np.ptp(d)

print("\nPPG Statistics:")
print(f"Sum of PPG: {sumppg:.1f}")
print(f"Maximum of PPG: {maxppg:.1f}")
print(f"Minimum of PPG: {minppg:.1f}")

print("\nFG% Statistics:")
print(f"Mean of FG%: {meanfg:.1f}")
print(f"Median of FG%: {medianfg:.1f}")
print(f"90th, 95th, and 99th Percentile of FG%: {perfg:.1f}")

print("\nFT% Statistics:")
print(f"Standard Deviation of FT%: {stdft:.1f}")
print(f"Variance of FT%: {varft:.1f}")
print(f"Range of FT%: {rangeft:.1f}")
1/116:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import csv

#DATA SET

df = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

a = df['Name'].to_numpy()
b = df['PPG'].to_numpy()
c = df['FG%'].to_numpy()
d = df['FT%'].to_numpy()


#INITIALS

col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']

#OUTPUTS

print("TOP 200 SCORERS DATA IN THE NATIONAL BASKETBALL ASSOCIATION (NBA)\n")

print("Data set columns:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    
#proof of clean data set
print("\nOriginal Data Shape:", df.shape)
print("Missing Values:") 
print(df.isnull().sum())
print("\nTop 5 scorers:\n", df.head())

sumppg = np.sum(b)
maxppg = np.max(b)
minppg = np.min(b)
meanfg = np.mean(c)
medianfg = np.median(c)
perfg = np.percentile(c, [90, 95, 99])
stdft = np.std(d)
varft = np.var(d)
rangeft = np.ptp(d)

print("\nPPG Statistics:")
print(f"Sum of PPG: {sumppg:.1f}")
print(f"Maximum of PPG: {maxppg:.1f}")
print(f"Minimum of PPG: {minppg:.1f}")

print("\nFG% Statistics:")
print(f"Mean of FG%: {meanfg:.1f}")
print(f"Median of FG%: {medianfg:.1f}")
print(f"The 90th, 95th, and 99th Percentile of FG%: {perfg:.1f}")

print("\nFT% Statistics:")
print(f"Standard Deviation of FT%: {stdft:.1f}")
print(f"Variance of FT%: {varft:.1f}")
print(f"Range of FT%: {rangeft:.1f}")
1/117:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import csv

#DATA SET

df = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

a = df['Name'].to_numpy()
b = df['PPG'].to_numpy()
c = df['FG%'].to_numpy()
d = df['FT%'].to_numpy()


#INITIALS

col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']

#OUTPUTS

print("TOP 200 SCORERS DATA IN THE NATIONAL BASKETBALL ASSOCIATION (NBA)\n")

print("Data set columns:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    
#proof of clean data set
print("\nOriginal Data Shape:", df.shape)
print("Missing Values:") 
print(df.isnull().sum())
print("\nTop 5 scorers:\n", df.head())

sumppg = np.sum(b)
maxppg = np.max(b)
minppg = np.min(b)
meanfg = np.mean(c)
medianfg = np.median(c)
perfg = np.percentile(c, [90, 95, 99])
stdft = np.std(d)
varft = np.var(d)
rangeft = np.ptp(d)

print("\nPPG Statistics:")
print(f"Sum of PPG: {sumppg:.1f}")
print(f"Maximum of PPG: {maxppg:.1f}")
print(f"Minimum of PPG: {minppg:.1f}")

print("\nFG% Statistics:")
print(f"Mean of FG%: {meanfg:.1f}")
print(f"Median of FG%: {medianfg:.1f}")
print(f"The 90th, 95th, and 99th Percentile of FG%: {perfg}")

print("\nFT% Statistics:")
print(f"Standard Deviation of FT%: {stdft:.1f}")
print(f"Variance of FT%: {varft:.1f}")
print(f"Range of FT%: {rangeft:.1f}")
1/118:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import csv

#DATA SET

df = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

a = df['Name'].to_numpy()
b = df['PPG'].to_numpy()
c = df['FG%'].to_numpy()
d = df['FT%'].to_numpy()


#INITIALS

col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']

#OUTPUTS

print("TOP 200 SCORERS DATA IN THE NATIONAL BASKETBALL ASSOCIATION (NBA)\n")

print("Data set columns:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    
#proof of clean data set
print("\nOriginal Data Shape:", df.shape)
print("Missing Values:") 
print(df.isnull().sum())
print("\nTop 5 scorers:\n", df.head())

sumppg = np.sum(b)
maxppg = np.max(b)
minppg = np.min(b)
meanfg = np.mean(c)
medianfg = np.median(c)
perfg = np.percentile(c, [90, 95, 99])
stdft = np.std(d)
varft = np.var(d)
rangeft = np.ptp(d)

print("\nPPG Statistics:")
print(f"Sum of PPG: {sumppg:.1f}")
print(f"Maximum of PPG: {maxppg:.1f}")
print(f"Minimum of PPG: {minppg:.1f}")

print("\nFG% Statistics:")
print(f"Mean of FG%: {meanfg:.1f}")
print(f"Median of FG%: {medianfg:.1f}")
print(f"90th, 95th, and 99th Percentile of FG%: {perfg}")

print("\nFT% Statistics:")
print(f"Standard Deviation of FT%: {stdft:.1f}")
print(f"Variance of FT%: {varft:.1f}")
print(f"Range of FT%: {rangeft:.1f}")
1/119:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import csv

#DATA SET

df = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

a = df['Name'].to_numpy()
b = df['PPG'].to_numpy()
c = df['FG%'].to_numpy()
d = df['FT%'].to_numpy()


#INITIALS
col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']

#OUTPUTS
print("TOP 200 SCORERS DATA IN THE NATIONAL BASKETBALL ASSOCIATION (NBA)\n")

print("Data set columns:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    
#proof of clean data set
print("\nOriginal Data Shape:", df.shape)
print("Missing Values:") 
print(df.isnull().sum())
print("\nTop 5 scorers:\n", df.head())
1/120:
#numpy operations
sumppg = np.sum(b)
maxppg = np.max(b)
minppg = np.min(b)
meanfg = np.mean(c)
medianfg = np.median(c)
perfg = np.percentile(c, [90, 95, 99])
stdft = np.std(d)
varft = np.var(d)
rangeft = np.ptp(d)

print("\nPPG Statistics:")
print(f"Sum of PPG: {sumppg:.1f}")
print(f"Maximum of PPG: {maxppg:.1f}")
print(f"Minimum of PPG: {minppg:.1f}")

print("\nFG% Statistics:")
print(f"Mean of FG%: {meanfg:.1f}")
print(f"Median of FG%: {medianfg:.1f}")
print(f"90th, 95th, and 99th Percentile of FG%: {perfg}")

print("\nFT% Statistics:")
print(f"Standard Deviation of FT%: {stdft:.1f}")
print(f"Variance of FT%: {varft:.1f}")
print(f"Range of FT%: {rangeft:.1f}")
1/121:
#scipy operations
sga = df[df['Name'] == 'Shai Gilgeous-Alexander']['PPG']
giannis = df[df['Name'] == 'Giannis Antetokounmpo']['PPG']
jokic = df[df['Name'] == 'Nikola Jokic']['PPG']
f_statistic, p_value = stats.f_oneway(sga, giannis, jokic)
1/122:
#scipy operations
sga = df[df['Name'] == 'Shai Gilgeous-Alexander']['PPG']['FG%']['FT%']
giannis = df[df['Name'] == 'Giannis Antetokounmpo']['PPG']['FG%']['FT%']
jokic = df[df['Name'] == 'Nikola Jokic']['PPG']['FG%']['FT%']
f_statistic, p_value = stats.f_oneway(sga, giannis, jokic)
1/123:
#scipy operations
group1 = np.array([0, 0, 0, 0, 0])

print(group1)
1/124:
#scipy operations
grp1 = np.array([0, 0, 0, 0, 0])

print(grp1)
1/125:
#scipy operations
grp1 = np.array([])
grp2 = np.array([])
grp3 = np.array([])
for i in range(15):
    if i < 5:
        grp1 = np.append(grp1, b[i])

    if i < 10 and i > 4:
        grp1 = np.append(grp2, b[i])

    if i < 15 and i > 9:
        grp1 = np.append(grp3, b[i])

print(grp1)
1/126:
#scipy operations
grp1 = np.array([])
grp2 = np.array([])
grp3 = np.array([])
for i in range(15):
    if i < 5:
        grp1 = np.append(grp1, b[i])

    if i < 10 and i > 4:
        grp1 = np.append(grp2, b[i])

    if i < 15 and i > 9:
        grp1 = np.append(grp3, b[i])

print(grp1, grp2, grp3)
1/127:
#scipy operations
grp1 = np.array([])
grp2 = np.array([])
grp3 = np.array([])
for i in range(15):
    if i < 5:
        grp1 = np.append(grp1, b[i])

    if i < 10 and i > 4:
        grp1 = np.append(grp2, b[i])

    if i < 15 and i > 9:
        grp1 = np.append(grp3, b[i])

print(grp1, grp2, grp3)
1/128:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import csv

#DATA SET

df = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

a = df['Name'].to_numpy()
b = df['PPG'].to_numpy()
c = df['FG%'].to_numpy()
d = df['FT%'].to_numpy()


#INITIALS
col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']

#OUTPUTS
print("TOP 200 SCORERS DATA IN THE NATIONAL BASKETBALL ASSOCIATION (NBA)\n")

print("Data set columns:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    
#proof of clean data set
print("\nOriginal Data Shape:", df.shape)
print("Missing Values:") 
print(df.isnull().sum())
print("\nTop 5 scorers:\n", df.head())
1/129:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import csv

#DATA SET

df = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

a = df['Name'].to_numpy()
b = df['PPG'].to_numpy()
c = df['FG%'].to_numpy()
d = df['FT%'].to_numpy()


#INITIALS
col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']

#OUTPUTS
print("TOP 200 SCORERS DATA IN THE NATIONAL BASKETBALL ASSOCIATION (NBA)\n")

print("Data set columns:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    
#proof of clean data set
print("\nOriginal Data Shape:", df.shape)
print("Missing Values:") 
print(df.isnull().sum())
print("\nTop 5 scorers:\n", df.head())
1/130:
#numpy operations
sumppg = np.sum(b)
maxppg = np.max(b)
minppg = np.min(b)
meanfg = np.mean(c)
medianfg = np.median(c)
perfg = np.percentile(c, [90, 95, 99])
stdft = np.std(d)
varft = np.var(d)
rangeft = np.ptp(d)

print("\nPPG Statistics:")
print(f"Sum of PPG: {sumppg:.1f}")
print(f"Maximum of PPG: {maxppg:.1f}")
print(f"Minimum of PPG: {minppg:.1f}")

print("\nFG% Statistics:")
print(f"Mean of FG%: {meanfg:.1f}")
print(f"Median of FG%: {medianfg:.1f}")
print(f"90th, 95th, and 99th Percentile of FG%: {perfg}")

print("\nFT% Statistics:")
print(f"Standard Deviation of FT%: {stdft:.1f}")
print(f"Variance of FT%: {varft:.1f}")
print(f"Range of FT%: {rangeft:.1f}")
1/131:
#scipy operations
grp1 = np.array([])
grp2 = np.array([])
grp3 = np.array([])
for i in range(15):
    if i < 5:
        grp1 = np.append(grp1, b[i])

    if i < 10 and i > 4:
        grp1 = np.append(grp2, b[i])

    if i < 15 and i > 9:
        grp1 = np.append(grp3, b[i])

print(grp1, grp2, grp3)
1/132:
#scipy operations
grp1 = np.array([])
grp2 = np.array([])
grp3 = np.array([])
for i in range(15):
    if i < 5:
        grp1 = np.append(grp1, b[i])

    if i < 10 and i > 4:
        grp2 = np.append(grp2, b[i])

    if i < 15 and i > 9:
        grp3 = np.append(grp3, b[i])

print(grp1, grp2, grp3)
1/133:
#scipy operations
grp1 = np.array([])
grp2 = np.array([])
grp3 = np.array([])
for i in range(15):
    if i < 5:
        grp1 = np.append(grp1, b[i])

    if i < 10 and i > 4:
        grp2 = np.append(grp2, b[i])

    if i < 15 and i > 9:
        grp3 = np.append(grp3, b[i])

print(grp1, grp2, grp3, grp3[4])
1/134:
#scipy operations
grp1 = np.array([])
grp2 = np.array([])
grp3 = np.array([])
for i in range(15):
    if i < 5:
        grp1 = np.append(grp1, b[i])

    if i < 10 and i > 4:
        grp2 = np.append(grp2, b[i])

    if i < 15 and i > 9:
        grp3 = np.append(grp3, b[i])

print(grp1, grp2, grp3, grp2[4])
1/135:
#scipy operations
grp1 = np.array([])
grp2 = np.array([])
grp3 = np.array([])
for i in range(15):
    if i < 5:
        grp1 = np.append(grp1, b[i])

    if i < 10 and i > 4:
        grp2 = np.append(grp2, b[i])

    if i < 15 and i > 9:
        grp3 = np.append(grp3, b[i])

print(grp1, grp2, grp3)
1/136:
#scipy operations

#initializing 3 arrays with 5 values each
arr1 = np.array([])
arr2 = np.array([])
arr3 = np.array([])
for i in range(15):
    if i < 5:
        arr1 = np.append(arr1, b[i])

    if i < 10 and i > 4:
        arr2 = np.append(arr2, b[i])

    if i < 15 and i > 9:
        arr3 = np.append(arr3, b[i])

print(grp1, grp2, grp3)
1/137:
#scipy operations

#initializing 3 arrays with 5 values each
arr1 = np.array([])
arr2 = np.array([])
arr3 = np.array([])
for i in range(15):
    if i < 5:
        arr1 = np.append(arr1, b[i])

    if i < 10 and i > 4:
        arr2 = np.append(arr2, b[i])

    if i < 15 and i > 9:
        arr3 = np.append(arr3, b[i])

f_statistic, p_value = stats.f_oneway(group1, group2, group3)
1/138:
#scipy operations

#initializing 3 arrays with 5 values each
arr1 = np.array([])
arr2 = np.array([])
arr3 = np.array([])
for i in range(15):
    if i < 5:
        arr1 = np.append(arr1, b[i])

    if i < 10 and i > 4:
        arr2 = np.append(arr2, b[i])

    if i < 15 and i > 9:
        arr3 = np.append(arr3, b[i])

f_statistic, p_value = stats.f_oneway(arr1, arr2, arr3)
1/139:
#scipy operations

#initializing 3 arrays with 5 values each
arr1 = np.array([])
arr2 = np.array([])
arr3 = np.array([])
for i in range(15):
    if i < 5:
        arr1 = np.append(arr1, b[i])

    if i < 10 and i > 4:
        arr2 = np.append(arr2, b[i])

    if i < 15 and i > 9:
        arr3 = np.append(arr3, b[i])

#one-way anova
f_statistic, p_value = stats.f_oneway(arr1, arr2, arr3)
print(f"F-statistic: {f_statistic:.4f}, P-value: {p_value:.4f}")
1/140:
#scipy operations

#initializing 3 arrays with 5 values each
arr1 = np.array([])
arr2 = np.array([])
arr3 = np.array([])
for i in range(15):
    if i < 5:
        arr1 = np.append(arr1, b[i])

    if i < 10 and i > 4:
        arr2 = np.append(arr2, b[i])

    if i < 15 and i > 9:
        arr3 = np.append(arr3, b[i])

#one-way anova
f_statistic, p_value = stats.f_oneway(arr1, arr2, arr3)
print(f"One-Way Anova \nF-statistic: {f_statistic:.4f}, P-value: {p_value:.4f}")
1/141:
#scipy operations

#initializing 3 arrays with 5 values each
arr1 = np.array([])
arr2 = np.array([])
arr3 = np.array([])
for i in range(15):
    if i < 5:
        arr1 = np.append(arr1, b[i])

    if i < 10 and i > 4:
        arr2 = np.append(arr2, b[i])

    if i < 15 and i > 9:
        arr3 = np.append(arr3, b[i])

print("Array 1:", arr1, "\nArray 2:", arr2, "\nArray 3:", arr3)
#one-way anova
f_statistic, p_value = stats.f_oneway(arr1, arr2, arr3)
print(f"One-Way Anova \nF-statistic: {f_statistic:.4f}, P-value: {p_value:.4f}")
1/142:
#scipy operations

#initializing 3 arrays with 5 values each
arr1 = np.array([])
arr2 = np.array([])
arr3 = np.array([])
for i in range(15):
    if i < 5:
        arr1 = np.append(arr1, b[i])

    if i < 10 and i > 4:
        arr2 = np.append(arr2, b[i])

    if i < 15 and i > 9:
        arr3 = np.append(arr3, b[i])

print("Array 1:", arr1, "\nArray 2:", arr2, "\nArray 3:", arr3)
#one-way anova
f_statistic, p_value = stats.f_oneway(arr1, arr2, arr3)
print(f"\nOne-Way Anova \nF-statistic: {f_statistic:.4f}, P-value: {p_value:.4f}")
1/143:
#scipy operations

#initializing 3 arrays with 5 values each
arr1 = np.array([])
arr2 = np.array([])
arr3 = np.array([])
for i in range(15):
    if i < 5:
        arr1 = np.append(arr1, b[i])

    if i < 10 and i > 4:
        arr2 = np.append(arr2, b[i])

    if i < 15 and i > 9:
        arr3 = np.append(arr3, b[i])

print("Array 1:", arr1, "\nArray 2:", arr2, "\nArray 3:", arr3)

#one-way anova
f_statistic, p_value = stats.f_oneway(arr1, arr2, arr3)
print(f"\nOne-Way Anova \nF-statistic: {f_statistic:.4f}, P-value: {p_value:.4f}")

#standard normal
zarr1 = zscore(arr1)
zarr2 = zscore(arr2)
1/144:
import pandas as pd
import numpy as np
from scipy import stats, zscore, norm
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import csv

#DATA SET

df = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

a = df['Name'].to_numpy()
b = df['PPG'].to_numpy()
c = df['FG%'].to_numpy()
d = df['FT%'].to_numpy()


#INITIALS
col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']

#OUTPUTS
print("TOP 200 SCORERS DATA IN THE NATIONAL BASKETBALL ASSOCIATION (NBA)\n")

print("Data set columns:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    
#proof of clean data set
print("\nOriginal Data Shape:", df.shape)
print("Missing Values:") 
print(df.isnull().sum())
print("\nTop 5 scorers:\n", df.head())
1/145:
import pandas as pd
import numpy as np
from scipy import stats, zscore, norm
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import csv

#DATA SET

df = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

a = df['Name'].to_numpy()
b = df['PPG'].to_numpy()
c = df['FG%'].to_numpy()
d = df['FT%'].to_numpy()


#INITIALS
col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']

#OUTPUTS
print("TOP 200 SCORERS DATA IN THE NATIONAL BASKETBALL ASSOCIATION (NBA)\n")

print("Data set columns:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    
#proof of clean data set
print("\nOriginal Data Shape:", df.shape)
print("Missing Values:") 
print(df.isnull().sum())
print("\nTop 5 scorers:\n", df.head())
1/146:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import csv

#DATA SET

df = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

a = df['Name'].to_numpy()
b = df['PPG'].to_numpy()
c = df['FG%'].to_numpy()
d = df['FT%'].to_numpy()


#INITIALS
col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']

#OUTPUTS
print("TOP 200 SCORERS DATA IN THE NATIONAL BASKETBALL ASSOCIATION (NBA)\n")

print("Data set columns:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    
#proof of clean data set
print("\nOriginal Data Shape:", df.shape)
print("Missing Values:") 
print(df.isnull().sum())
print("\nTop 5 scorers:\n", df.head())
1/147:
#numpy operations
sumppg = np.sum(b)
maxppg = np.max(b)
minppg = np.min(b)
meanfg = np.mean(c)
medianfg = np.median(c)
perfg = np.percentile(c, [90, 95, 99])
stdft = np.std(d)
varft = np.var(d)
rangeft = np.ptp(d)

print("\nPPG Statistics:")
print(f"Sum of PPG: {sumppg:.1f}")
print(f"Maximum of PPG: {maxppg:.1f}")
print(f"Minimum of PPG: {minppg:.1f}")

print("\nFG% Statistics:")
print(f"Mean of FG%: {meanfg:.1f}")
print(f"Median of FG%: {medianfg:.1f}")
print(f"90th, 95th, and 99th Percentile of FG%: {perfg}")

print("\nFT% Statistics:")
print(f"Standard Deviation of FT%: {stdft:.1f}")
print(f"Variance of FT%: {varft:.1f}")
print(f"Range of FT%: {rangeft:.1f}")
1/148:
#scipy operations

#initializing 3 arrays with 5 values each
arr1 = np.array([])
arr2 = np.array([])
arr3 = np.array([])
for i in range(15):
    if i < 5:
        arr1 = np.append(arr1, b[i])

    if i < 10 and i > 4:
        arr2 = np.append(arr2, b[i])

    if i < 15 and i > 9:
        arr3 = np.append(arr3, b[i])

print("Array 1:", arr1, "\nArray 2:", arr2, "\nArray 3:", arr3)

#one-way anova
f_statistic, p_value = stats.f_oneway(arr1, arr2, arr3)
print(f"\nOne-Way Anova \nF-statistic: {f_statistic:.4f}, P-value: {p_value:.4f}")

#standard normal
zarr1 = zscore(arr1)
zarr2 = zscore(arr2)
1/149:
#scipy operations

#initializing 3 arrays with 5 values each
arr1 = np.array([])
arr2 = np.array([])
arr3 = np.array([])
for i in range(15):
    if i < 5:
        arr1 = np.append(arr1, b[i])

    if i < 10 and i > 4:
        arr2 = np.append(arr2, b[i])

    if i < 15 and i > 9:
        arr3 = np.append(arr3, b[i])

print("Array 1:", arr1, "\nArray 2:", arr2, "\nArray 3:", arr3)

#one-way anova
f_statistic, p_value = stats.f_oneway(arr1, arr2, arr3)
print(f"\nOne-Way Anova \nF-statistic: {f_statistic:.4f}, P-value: {p_value:.4f}")

#standard normal
zarr1 = stats.zscore(arr1)
zarr2 = stats.zscore(arr2)
1/150:
#scipy operations

#initializing 3 arrays with 5 values each
arr1 = np.array([])
arr2 = np.array([])
arr3 = np.array([])
for i in range(15):
    if i < 5:
        arr1 = np.append(arr1, b[i])

    if i < 10 and i > 4:
        arr2 = np.append(arr2, b[i])

    if i < 15 and i > 9:
        arr3 = np.append(arr3, b[i])

print("Array 1:", arr1, "\nArray 2:", arr2, "\nArray 3:", arr3)

#one-way anova
f_statistic, p_value = stats.f_oneway(arr1, arr2, arr3)
print(f"\nOne-Way Anova \nF-statistic: {f_statistic:.4f}, P-value: {p_value:.4f}")

#standard normal
zarr1 = stats.zscore(arr1)
zarr2 = stats.zscore(arr2)
print(zarr1, zarr2)
1/151:
#scipy operations

#initializing 3 arrays with 5 values each
arr1 = np.array([])
arr2 = np.array([])
arr3 = np.array([])
for i in range(15):
    if i < 5:
        arr1 = np.append(arr1, b[i])

    if i < 10 and i > 4:
        arr2 = np.append(arr2, b[i])

    if i < 15 and i > 9:
        arr3 = np.append(arr3, b[i])

print("Array 1:", arr1, "\nArray 2:", arr2, "\nArray 3:", arr3)

#one-way anova
f_statistic, p_value = stats.f_oneway(arr1, arr2, arr3)
print(f"\nOne-Way Anova \nF-statistic: {f_statistic:.4f}, P-value: {p_value:.4f}")

#standard normal
zarr1 = stats.zscore(arr1)
print(f"\nZ-Distribution\nZ-score: {zarr1:4f}")
1/152:
#scipy operations

#initializing 3 arrays with 5 values each
arr1 = np.array([])
arr2 = np.array([])
arr3 = np.array([])
for i in range(15):
    if i < 5:
        arr1 = np.append(arr1, b[i])

    if i < 10 and i > 4:
        arr2 = np.append(arr2, b[i])

    if i < 15 and i > 9:
        arr3 = np.append(arr3, b[i])

print("Array 1:", arr1, "\nArray 2:", arr2, "\nArray 3:", arr3)

#one-way anova
f_statistic, p_value = stats.f_oneway(arr1, arr2, arr3)
print(f"\nOne-Way Anova \nF-statistic: {f_statistic:.4f}, P-value: {p_value:.4f}")

#standard normal
zarr1 = stats.zscore(arr1)
print(f"\nZ-Distribution\nZ-score:", zarr1)
1/153:
#scipy operations

#initializing 3 arrays with 5 values each
arr1 = np.array([])
arr2 = np.array([])
arr3 = np.array([])
for i in range(15):
    if i < 5:
        arr1 = np.append(arr1, b[i])

    if i < 10 and i > 4:
        arr2 = np.append(arr2, b[i])

    if i < 15 and i > 9:
        arr3 = np.append(arr3, b[i])

print("Array 1:", arr1, "\nArray 2:", arr2, "\nArray 3:", arr3)

#one-way anova
f_statistic, p_value = stats.f_oneway(arr1, arr2, arr3)
print(f"\nOne-Way Anova \nF-statistic: {f_statistic:.4f}, P-value: {p_value:.4f}")

#standard normal
zarr1 = stats.zscore(arr1)
print(f"\nZ-Distribution\nZ-score for Array 1:", zarr1)
1/154:
#scipy operations

#initializing 3 arrays with 5 values each
arr1 = np.array([])
arr2 = np.array([])
arr3 = np.array([])
for i in range(15):
    if i < 5:
        arr1 = np.append(arr1, b[i])

    if i < 10 and i > 4:
        arr2 = np.append(arr2, b[i])

    if i < 15 and i > 9:
        arr3 = np.append(arr3, b[i])

print("Array 1:", arr1, "\nArray 2:", arr2, "\nArray 3:", arr3)

#one-way anova
f_statistic, p_value = stats.f_oneway(arr1, arr2, arr3)
print(f"\nOne-Way Anova \nF-statistic: {f_statistic:.4f}, P-value: {p_value:.4f}")

#standard normal
zarr1 = stats.zscore(arr1)
print(f"\nZ-Distribution\nZ-score for Array 1:", zarr1)

#plot
z_range = np.linspace(-3, 3, 1000)
pdf = stats.norm.pdf(z_range)

plt.figure(figsize=(10, 5))
plt.plot(z_range, pdf, color='gray', linestyle='--', label='Standard Normal PDF')

plt.hist(z_group1, bins=10, density=True, alpha=0.6, label='Array 1 Z-scores', color='blue')

plt.axvline(0, color='black', linestyle='--', linewidth=1)
plt.title('Z-Score Distribution of Array 1')
plt.xlabel('Z-score')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()
1/155:
#scipy operations

#initializing 3 arrays with 5 values each
arr1 = np.array([])
arr2 = np.array([])
arr3 = np.array([])
for i in range(15):
    if i < 5:
        arr1 = np.append(arr1, b[i])

    if i < 10 and i > 4:
        arr2 = np.append(arr2, b[i])

    if i < 15 and i > 9:
        arr3 = np.append(arr3, b[i])

print("Array 1:", arr1, "\nArray 2:", arr2, "\nArray 3:", arr3)

#one-way anova
f_statistic, p_value = stats.f_oneway(arr1, arr2, arr3)
print(f"\nOne-Way Anova \nF-statistic: {f_statistic:.4f}, P-value: {p_value:.4f}")

#standard normal
zarr1 = stats.zscore(arr1)
print(f"\nZ-Distribution\nZ-score for Array 1:", zarr1)

#plot
z_range = np.linspace(-3, 3, 1000)
pdf = stats.norm.pdf(z_range)

plt.figure(figsize=(10, 5))
plt.plot(z_range, pdf, color='gray', linestyle='--', label='Standard Normal PDF')

plt.hist(zarr1, bins=10, density=True, alpha=0.6, label='Array 1 Z-scores', color='blue')

plt.axvline(0, color='black', linestyle='--', linewidth=1)
plt.title('Z-Score Distribution of Array 1')
plt.xlabel('Z-score')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()
1/156:
#scipy operations

#initializing 3 arrays with 5 values each
arr1 = np.array([])
arr2 = np.array([])
arr3 = np.array([])
for i in range(15):
    if i < 5:
        arr1 = np.append(arr1, b[i])

    if i < 10 and i > 4:
        arr2 = np.append(arr2, b[i])

    if i < 15 and i > 9:
        arr3 = np.append(arr3, b[i])

print("Array 1:", arr1, "\nArray 2:", arr2, "\nArray 3:", arr3)

#one-way anova
f_statistic, p_value = stats.f_oneway(arr1, arr2, arr3)
print(f"\nOne-Way Anova \nF-statistic: {f_statistic:.4f}, P-value: {p_value:.4f}")

#standard normal
zarr1 = stats.zscore(arr1)
print(f"\nZ-Distribution\nZ-score for Array 1:", zarr1)

#plot
z_range = np.linspace(-3, 3, 1000)
pdf = stats.norm.pdf(z_range)

plt.figure(figsize=(10, 5))
plt.plot(z_range, pdf, color='gray', linestyle='--', label='Standard Normal PDF')

plt.hist(zarr1, bins=10, density=True, alpha=0.6, label='Array 1 Z-scores', color='blue')

plt.axvline(0, color='black', linestyle='-', linewidth=1)
plt.title('Z-Score Distribution of Array 1')
plt.xlabel('Z-score')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()
1/157:
#scipy operations

#initializing 3 arrays with 5 values each
arr1 = np.array([])
arr2 = np.array([])
arr3 = np.array([])
for i in range(15):
    if i < 5:
        arr1 = np.append(arr1, b[i])

    if i < 10 and i > 4:
        arr2 = np.append(arr2, b[i])

    if i < 15 and i > 9:
        arr3 = np.append(arr3, b[i])

print("Array 1:", arr1, "\nArray 2:", arr2, "\nArray 3:", arr3)

#one-way anova
f_statistic, p_value = stats.f_oneway(arr1, arr2, arr3)
print(f"\nOne-Way Anova \nF-statistic: {f_statistic:.4f}, P-value: {p_value:.4f}")

#standard normal
zarr1 = stats.zscore(arr1)
print(f"\nZ-Distribution\nZ-score for Array 1:", zarr1)

#plot
z_range = np.linspace(-3, 3, 1000)
pdf = stats.norm.pdf(z_range)

plt.figure(figsize=(10, 5))
plt.plot(z_range, pdf, color='gray', linestyle='--', label='Standard Normal PDF')

plt.hist(zarr1, bins=10, density=True, alpha=0.5, label='Array 1 Z-scores', color='blue')

plt.axvline(0, color='black', linestyle='-', linewidth=1)
plt.title('Z-Score Distribution of Array 1')
plt.xlabel('Z-score')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()
1/158:
#scipy operations

#initializing 3 arrays with 5 values each
arr1 = np.array([])
arr2 = np.array([])
arr3 = np.array([])
for i in range(15):
    if i < 5:
        arr1 = np.append(arr1, b[i])

    if i < 10 and i > 4:
        arr2 = np.append(arr2, b[i])

    if i < 15 and i > 9:
        arr3 = np.append(arr3, b[i])

print("Array 1:", arr1, "\nArray 2:", arr2, "\nArray 3:", arr3)

#one-way anova
f_statistic, p_value = stats.f_oneway(arr1, arr2, arr3)
print(f"\nOne-Way Anova \nF-statistic: {f_statistic:.4f}, P-value: {p_value:.4f}")

#standard normal
zarr1 = stats.zscore(arr1)
print(f"\nZ-Distribution\nZ-score for Array 1:", zarr1)

#plot
z_range = np.linspace(-3, 3, 100)
pdf = stats.norm.pdf(z_range)

plt.figure(figsize=(10, 5))
plt.plot(z_range, pdf, color='gray', linestyle='--', label='Standard Normal PDF')

plt.hist(zarr1, bins=10, density=True, alpha=0.5, label='Array 1 Z-scores', color='blue')

plt.axvline(0, color='black', linestyle='-', linewidth=1)
plt.title('Z-Score Distribution of Array 1')
plt.xlabel('Z-score')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()
1/159:
#scipy operations

#initializing 3 arrays with 5 values each
arr1 = np.array([])
arr2 = np.array([])
arr3 = np.array([])
for i in range(15):
    if i < 5:
        arr1 = np.append(arr1, b[i])

    if i < 10 and i > 4:
        arr2 = np.append(arr2, b[i])

    if i < 15 and i > 9:
        arr3 = np.append(arr3, b[i])

print("Array 1:", arr1, "\nArray 2:", arr2, "\nArray 3:", arr3)

#one-way anova
f_statistic, p_value = stats.f_oneway(arr1, arr2, arr3)
print(f"\nOne-Way Anova \nF-statistic: {f_statistic:.4f}, P-value: {p_value:.4f}")

#standard normal
zarr1 = stats.zscore(arr1)
print(f"\nZ-Distribution\nZ-score for Array 1:", zarr1)

#plot
z_range = np.linspace(-3, 3, 50)
pdf = stats.norm.pdf(z_range)

plt.figure(figsize=(10, 5))
plt.plot(z_range, pdf, color='gray', linestyle='--', label='Standard Normal PDF')

plt.hist(zarr1, bins=10, density=True, alpha=0.5, label='Array 1 Z-scores', color='blue')

plt.axvline(0, color='black', linestyle='-', linewidth=1)
plt.title('Z-Score Distribution of Array 1')
plt.xlabel('Z-score')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()
1/160:
#scipy operations

#initializing 3 arrays with 5 values each
arr1 = np.array([])
arr2 = np.array([])
arr3 = np.array([])
for i in range(15):
    if i < 5:
        arr1 = np.append(arr1, b[i])

    if i < 10 and i > 4:
        arr2 = np.append(arr2, b[i])

    if i < 15 and i > 9:
        arr3 = np.append(arr3, b[i])

print("Array 1:", arr1, "\nArray 2:", arr2, "\nArray 3:", arr3)

#one-way anova
f_statistic, p_value = stats.f_oneway(arr1, arr2, arr3)
print(f"\nOne-Way Anova \nF-statistic: {f_statistic:.4f}, P-value: {p_value:.4f}")

#standard normal
zarr1 = stats.zscore(arr1)
print(f"\nZ-Distribution\nZ-score for Array 1:", zarr1)

#plot
z_range = np.linspace(-3, 3, 50)
pdf = stats.norm.pdf(z_range)

plt.figure(figsize=(10, 5))
plt.plot(z_range, pdf, color='gray', linestyle='--', label='Standard Normal PDF')

plt.hist(zarr1, bins=10, density=True, alpha=0.5, label='Array 1 Z-scores', color='blue')

plt.axvline(0, color='black', linestyle='-', linewidth=3)
plt.title('Z-Score Distribution of Array 1')
plt.xlabel('Z-score')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()
1/161:
#scipy operations

#initializing 3 arrays with 5 values each
arr1 = np.array([])
arr2 = np.array([])
arr3 = np.array([])
for i in range(15):
    if i < 5:
        arr1 = np.append(arr1, b[i])

    if i < 10 and i > 4:
        arr2 = np.append(arr2, b[i])

    if i < 15 and i > 9:
        arr3 = np.append(arr3, b[i])

print("Array 1:", arr1, "\nArray 2:", arr2, "\nArray 3:", arr3)

#one-way anova
f_statistic, p_value = stats.f_oneway(arr1, arr2, arr3)
print(f"\nOne-Way Anova \nF-statistic: {f_statistic:.4f}, P-value: {p_value:.4f}")

#standard normal
zarr1 = stats.zscore(arr1)
print(f"\nZ-Distribution\nZ-score for Array 1:", zarr1)

#plot
z_range = np.linspace(-3, 3, 50)
pdf = stats.norm.pdf(z_range)

plt.figure(figsize=(10, 5))
plt.plot(z_range, pdf, color='gray', linestyle='-', label='Standard Normal PDF')

plt.hist(zarr1, bins=10, density=True, alpha=0.5, label='Array 1 Z-scores', color='blue')

plt.axvline(0, color='black', linestyle='-', linewidth=3)
plt.title('Z-Score Distribution of Array 1')
plt.xlabel('Z-score')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()
1/162:
#scipy operations

#initializing 3 arrays with 5 values each
arr1 = np.array([])
arr2 = np.array([])
arr3 = np.array([])
for i in range(15):
    if i < 5:
        arr1 = np.append(arr1, b[i])

    if i < 10 and i > 4:
        arr2 = np.append(arr2, b[i])

    if i < 15 and i > 9:
        arr3 = np.append(arr3, b[i])

print("Array 1:", arr1, "\nArray 2:", arr2, "\nArray 3:", arr3)

#one-way anova
f_statistic, p_value = stats.f_oneway(arr1, arr2, arr3)
print(f"\nOne-Way Anova \nF-statistic: {f_statistic:.4f}, P-value: {p_value:.4f}")

#standard normal
zarr1 = stats.zscore(arr1)
print(f"\nZ-Distribution\nZ-score for Array 1:", zarr1)

#plot
z_range = np.linspace(-3, 3, 50)
pdf = stats.norm.pdf(z_range)

plt.figure(figsize=(10, 8))
plt.plot(z_range, pdf, color='gray', linestyle='-', label='Standard Normal PDF')

plt.hist(zarr1, bins=10, density=True, alpha=0.5, label='Array 1 Z-scores', color='blue')

plt.axvline(0, color='black', linestyle='-', linewidth=3)
plt.title('Z-Score Distribution of Array 1')
plt.xlabel('Z-score')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()
1/163:
#scipy operations

#initializing 3 arrays with 5 values each
arr1 = np.array([])
arr2 = np.array([])
arr3 = np.array([])
for i in range(15):
    if i < 5:
        arr1 = np.append(arr1, b[i])

    if i < 10 and i > 4:
        arr2 = np.append(arr2, b[i])

    if i < 15 and i > 9:
        arr3 = np.append(arr3, b[i])

print("Array 1:", arr1, "\nArray 2:", arr2, "\nArray 3:", arr3)

#one-way anova
f_statistic, p_value = stats.f_oneway(arr1, arr2, arr3)
print(f"\nOne-Way Anova \nF-statistic: {f_statistic:.4f}, P-value: {p_value:.4f}")

#standard normal
zarr1 = stats.zscore(arr1)
print(f"\nZ-Distribution\nZ-score for Array 1:", zarr1)

#plot
z_range = np.linspace(-3, 3, 50)
pdf = stats.norm.pdf(z_range)

plt.figure(figsize=(10, 4))
plt.plot(z_range, pdf, color='gray', linestyle='-', label='Standard Normal PDF')

plt.hist(zarr1, bins=10, density=True, alpha=0.5, label='Array 1 Z-scores', color='blue')

plt.axvline(0, color='black', linestyle='-', linewidth=3)
plt.title('Z-Score Distribution of Array 1')
plt.xlabel('Z-score')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()
1/164:
#scipy operations

#initializing 3 arrays with 5 values each
arr1 = np.array([])
arr2 = np.array([])
arr3 = np.array([])
for i in range(15):
    if i < 5:
        arr1 = np.append(arr1, b[i])

    if i < 10 and i > 4:
        arr2 = np.append(arr2, b[i])

    if i < 15 and i > 9:
        arr3 = np.append(arr3, b[i])

print("Array 1:", arr1, "\nArray 2:", arr2, "\nArray 3:", arr3)

#one-way anova
f_statistic, p_value = stats.f_oneway(arr1, arr2, arr3)
print(f"\nOne-Way Anova \nF-statistic: {f_statistic:.4f}, P-value: {p_value:.4f}")

#standard normal
zarr1 = stats.zscore(arr1)
print(f"\nZ-Distribution\nZ-score for Array 1:", zarr1)

#plot
z_range = np.linspace(-3, 3, 50)
pdf = stats.norm.pdf(z_range)

plt.figure(figsize=(10, 4))
plt.plot(z_range, pdf, color='gray', linestyle='-', label='Standard Normal PDF')

plt.hist(zarr1, bins=10, density=True, alpha=0.1, label='Array 1 Z-scores', color='blue')

plt.axvline(0, color='black', linestyle='-', linewidth=3)
plt.title('Z-Score Distribution of Array 1')
plt.xlabel('Z-score')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()
1/165:
#scipy operations

#initializing 3 arrays with 5 values each
arr1 = np.array([])
arr2 = np.array([])
arr3 = np.array([])
for i in range(15):
    if i < 5:
        arr1 = np.append(arr1, b[i])

    if i < 10 and i > 4:
        arr2 = np.append(arr2, b[i])

    if i < 15 and i > 9:
        arr3 = np.append(arr3, b[i])

print("Array 1:", arr1, "\nArray 2:", arr2, "\nArray 3:", arr3)

#one-way anova
f_statistic, p_value = stats.f_oneway(arr1, arr2, arr3)
print(f"\nOne-Way Anova \nF-statistic: {f_statistic:.4f}, P-value: {p_value:.4f}")

#standard normal
zarr1 = stats.zscore(arr1)
print(f"\nZ-Distribution\nZ-score for Array 1:", zarr1)

#plot
z_range = np.linspace(-3, 3, 50)
pdf = stats.norm.pdf(z_range)

plt.figure(figsize=(10, 4))
plt.plot(z_range, pdf, color='gray', linestyle='-', label='Standard Normal PDF')

plt.hist(zarr1, bins=4, density=True, alpha=0.5, label='Array 1 Z-scores', color='blue')

plt.axvline(0, color='black', linestyle='-', linewidth=3)
plt.title('Z-Score Distribution of Array 1')
plt.xlabel('Z-score')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()
1/166:
#scipy operations

#initializing 3 arrays with 5 values each
arr1 = np.array([])
arr2 = np.array([])
arr3 = np.array([])
for i in range(15):
    if i < 5:
        arr1 = np.append(arr1, b[i])

    if i < 10 and i > 4:
        arr2 = np.append(arr2, b[i])

    if i < 15 and i > 9:
        arr3 = np.append(arr3, b[i])

print("Array 1:", arr1, "\nArray 2:", arr2, "\nArray 3:", arr3)

#one-way anova
f_statistic, p_value = stats.f_oneway(arr1, arr2, arr3)
print(f"\nOne-Way Anova \nF-statistic: {f_statistic:.4f}, P-value: {p_value:.4f}")

#standard normal
zarr1 = stats.zscore(arr1)
print(f"\nZ-Distribution\nZ-score for Array 1:", zarr1)

#plot
z_range = np.linspace(-3, 3, 50)
pdf = stats.norm.pdf(z_range)

plt.figure(figsize=(10, 4))
plt.plot(z_range, pdf, color='gray', linestyle='-', label='Standard Normal PDF')

plt.hist(zarr1, bins=20, density=True, alpha=0.5, label='Array 1 Z-scores', color='blue')

plt.axvline(0, color='black', linestyle='-', linewidth=3)
plt.title('Z-Score Distribution of Array 1')
plt.xlabel('Z-score')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()
1/167:
#scipy operations

#initializing 3 arrays with 5 values each
arr1 = np.array([])
arr2 = np.array([])
arr3 = np.array([])
for i in range(15):
    if i < 5:
        arr1 = np.append(arr1, b[i])

    if i < 10 and i > 4:
        arr2 = np.append(arr2, b[i])

    if i < 15 and i > 9:
        arr3 = np.append(arr3, b[i])

print("Array 1:", arr1, "\nArray 2:", arr2, "\nArray 3:", arr3)

#one-way anova
f_statistic, p_value = stats.f_oneway(arr1, arr2, arr3)
print(f"\nOne-Way Anova \nF-statistic: {f_statistic:.4f}, P-value: {p_value:.4f}")

#standard normal
zarr1 = stats.zscore(arr1)
print(f"\nZ-Distribution\nZ-score for Array 1:", zarr1)

#plot
z_range = np.linspace(-3, 3, 50)
pdf = stats.norm.pdf(z_range)

plt.figure(figsize=(10, 4))
plt.plot(z_range, pdf, color='gray', linestyle='-', label='Standard Normal PDF')

plt.hist(zarr1, bins=100, density=True, alpha=0.5, label='Array 1 Z-scores', color='blue')

plt.axvline(0, color='black', linestyle='-', linewidth=3)
plt.title('Z-Score Distribution of Array 1')
plt.xlabel('Z-score')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()
1/168:
#scipy operations

#initializing 3 arrays with 5 values each
arr1 = np.array([])
arr2 = np.array([])
arr3 = np.array([])
for i in range(15):
    if i < 5:
        arr1 = np.append(arr1, b[i])

    if i < 10 and i > 4:
        arr2 = np.append(arr2, b[i])

    if i < 15 and i > 9:
        arr3 = np.append(arr3, b[i])

print("Array 1:", arr1, "\nArray 2:", arr2, "\nArray 3:", arr3)

#one-way anova
f_statistic, p_value = stats.f_oneway(arr1, arr2, arr3)
print(f"\nOne-Way Anova \nF-statistic: {f_statistic:.4f}, P-value: {p_value:.4f}")

#standard normal
zarr1 = stats.zscore(arr1)
print(f"\nZ-Distribution\nZ-score for Array 1:", zarr1)

#plot
z_range = np.linspace(-3, 3, 50)
pdf = stats.norm.pdf(z_range)

plt.figure(figsize=(10, 4))
plt.plot(z_range, pdf, color='gray', linestyle='-', label='Standard Normal PDF')

plt.hist(zarr1, bins=50, density=True, alpha=0.5, label='Array 1 Z-scores', color='blue')

plt.axvline(0, color='black', linestyle='-', linewidth=3)
plt.title('Z-Score Distribution of Array 1')
plt.xlabel('Z-score')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()
1/169:
#scipy operations

#initializing 3 arrays with 5 values each
arr1 = np.array([])
arr2 = np.array([])
arr3 = np.array([])
for i in range(15):
    if i < 5:
        arr1 = np.append(arr1, b[i])

    if i < 10 and i > 4:
        arr2 = np.append(arr2, b[i])

    if i < 15 and i > 9:
        arr3 = np.append(arr3, b[i])

print("Array 1:", arr1, "\nArray 2:", arr2, "\nArray 3:", arr3)

#one-way anova
f_statistic, p_value = stats.f_oneway(arr1, arr2, arr3)
print(f"\nOne-Way Anova \nF-statistic: {f_statistic:.4f}, P-value: {p_value:.4f}")

#standard normal
zarr1 = stats.zscore(arr1)
print(f"\nZ-Distribution\nZ-score for Array 1:", zarr1)

#plot
z_range = np.linspace(-3, 3, 50)
pdf = stats.norm.pdf(z_range)

plt.figure(figsize=(10, 4))
plt.plot(z_range, pdf, color='gray', linestyle='-', label='Standard Normal PDF')

plt.hist(zarr1, bins=25, density=True, alpha=0.5, label='Array 1 Z-scores', color='blue')

plt.axvline(0, color='black', linestyle='-', linewidth=3)
plt.title('Z-Score Distribution of Array 1')
plt.xlabel('Z-score')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()
1/170:
#scipy operations

#initializing 3 arrays with 5 values each
arr1 = np.array([])
arr2 = np.array([])
arr3 = np.array([])
for i in range(15):
    if i < 5:
        arr1 = np.append(arr1, b[i])

    if i < 10 and i > 4:
        arr2 = np.append(arr2, b[i])

    if i < 15 and i > 9:
        arr3 = np.append(arr3, b[i])

print("Array 1:", arr1, "\nArray 2:", arr2, "\nArray 3:", arr3)

#one-way anova
f_statistic, p_value = stats.f_oneway(arr1, arr2, arr3)
print(f"\nOne-Way Anova \nF-statistic: {f_statistic:.4f}, P-value: {p_value:.4f}")

#standard normal
zarr1 = stats.zscore(arr1)
print(f"\nZ-Distribution\nZ-score for Array 1:", zarr1)

#plot
z_range = np.linspace(-3, 3, 50)
pdf = stats.norm.pdf(z_range)

plt.figure(figsize=(10, 4))
plt.plot(z_range, pdf, color='gray', linestyle='-', label='Standard Normal PDF')

plt.hist(zarr1, bins=15, density=True, alpha=0.5, label='Array 1 Z-scores', color='blue')

plt.axvline(0, color='black', linestyle='-', linewidth=3)
plt.title('Z-Score Distribution of Array 1')
plt.xlabel('Z-score')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()
1/171:
#scipy operations

#initializing 3 arrays with 5 values each
arr1 = np.array([])
arr2 = np.array([])
arr3 = np.array([])
for i in range(15):
    if i < 5:
        arr1 = np.append(arr1, b[i])

    if i < 10 and i > 4:
        arr2 = np.append(arr2, b[i])

    if i < 15 and i > 9:
        arr3 = np.append(arr3, b[i])

print("Array 1:", arr1, "\nArray 2:", arr2, "\nArray 3:", arr3)

#one-way anova
f_statistic, p_value = stats.f_oneway(arr1, arr2, arr3)
print(f"\nOne-Way Anova \nF-statistic: {f_statistic:.4f}, P-value: {p_value:.4f}")

#standard normal
zarr1 = stats.zscore(arr1)
print(f"\nZ-Distribution\nZ-score for Array 1:", zarr1)

#plot
z_range = np.linspace(-3, 3, 50)
pdf = stats.norm.pdf(z_range)

plt.figure(figsize=(10, 4))
plt.plot(z_range, pdf, color='gray', linestyle='-', label='Standard Normal PDF')

plt.hist(zarr1, bins=20, density=True, alpha=0.5, label='Array 1 Z-scores', color='blue')

plt.axvline(0, color='black', linestyle='-', linewidth=3)
plt.title('Z-Score Distribution of Array 1')
plt.xlabel('Z-score')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()
1/172:
#scipy operations

#initializing 3 arrays with 5 values each
arr1 = np.array([])
arr2 = np.array([])
arr3 = np.array([])
for i in range(15):
    if i < 5:
        arr1 = np.append(arr1, b[i])

    if i < 10 and i > 4:
        arr2 = np.append(arr2, b[i])

    if i < 15 and i > 9:
        arr3 = np.append(arr3, b[i])

print("Array 1:", arr1, "\nArray 2:", arr2, "\nArray 3:", arr3)

#one-way anova
f_statistic, p_value = stats.f_oneway(arr1, arr2, arr3)
print(f"\nOne-Way Anova \nF-statistic: {f_statistic:.4f}, P-value: {p_value:.4f}")

#plot
#standard normal
zarr1 = stats.zscore(arr1)
print(f"\nZ-Distribution\nZ-score for Array 1:", zarr1)

#plot
z_range = np.linspace(-3, 3, 50)
pdf = stats.norm.pdf(z_range)

plt.figure(figsize=(10, 4))
plt.plot(z_range, pdf, color='gray', linestyle='-', label='Standard Normal PDF')

plt.hist(zarr1, bins=20, density=True, alpha=0.5, label='Array 1 Z-scores', color='blue')

plt.axvline(0, color='black', linestyle='-', linewidth=3)
plt.title('Z-Score Distribution of Array 1')
plt.xlabel('Z-score')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()
1/173:
#scipy operations

#initializing 3 arrays with 5 values each
arr1 = np.array([])
arr2 = np.array([])
arr3 = np.array([])
for i in range(15):
    if i < 5:
        arr1 = np.append(arr1, b[i])

    if i < 10 and i > 4:
        arr2 = np.append(arr2, b[i])

    if i < 15 and i > 9:
        arr3 = np.append(arr3, b[i])

print("Array 1:", arr1, "\nArray 2:", arr2, "\nArray 3:", arr3)

#one-way anova
f_statistic, p_value = stats.f_oneway(arr1, arr2, arr3)
print(f"\nOne-Way Anova \nF-statistic: {f_statistic:.4f}, P-value: {p_value:.4f}")

#plot
data = [arr1, arr2, arr3]
labels = ['Array 1', 'Array 2', 'Array 3']

plt.figure(figsize=(8, 5))
plt.boxplot(data, labels=labels)
plt.title('One-Way ANOVA: Group Comparisons')
plt.ylabel('Scores')
plt.grid(True)
plt.axhline(y=sum(arr1 + arr2 + arr3)/len(arr1 + arr2 + arr3), color='red', linestyle='--', label='Overall Mean')
plt.legend()
plt.show()

#standard normal
zarr1 = stats.zscore(arr1)
print(f"\nZ-Distribution\nZ-score for Array 1:", zarr1)

#plot
z_range = np.linspace(-3, 3, 50)
pdf = stats.norm.pdf(z_range)

plt.figure(figsize=(10, 4))
plt.plot(z_range, pdf, color='gray', linestyle='-', label='Standard Normal PDF')

plt.hist(zarr1, bins=20, density=True, alpha=0.5, label='Array 1 Z-scores', color='blue')

plt.axvline(0, color='black', linestyle='-', linewidth=3)
plt.title('Z-Score Distribution of Array 1')
plt.xlabel('Z-score')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()
1/174:
#scipy operations

#initializing 3 arrays with 5 values each
arr1 = np.array([])
arr2 = np.array([])
arr3 = np.array([])
for i in range(15):
    if i < 5:
        arr1 = np.append(arr1, b[i])

    if i < 10 and i > 4:
        arr2 = np.append(arr2, b[i])

    if i < 15 and i > 9:
        arr3 = np.append(arr3, b[i])

print("Array 1:", arr1, "\nArray 2:", arr2, "\nArray 3:", arr3)

#one-way anova
f_statistic, p_value = stats.f_oneway(arr1, arr2, arr3)
print(f"\nOne-Way Anova \nF-statistic: {f_statistic:.4f}, P-value: {p_value:.4f}")

#plot
data = [arr1, arr2, arr3]
labels = ['Array 1', 'Array 2', 'Array 3']

plt.figure(figsize=(8, 5))
plt.boxplot(data, tick_labels=labels)
plt.title('One-Way ANOVA: Group Comparisons')
plt.ylabel('Scores')
plt.grid(True)
plt.axhline(y=sum(arr1 + arr2 + arr3)/len(arr1 + arr2 + arr3), color='red', linestyle='--', label='Overall Mean')
plt.legend()
plt.show()

#standard normal
zarr1 = stats.zscore(arr1)
print(f"\nZ-Distribution\nZ-score for Array 1:", zarr1)

#plot
z_range = np.linspace(-3, 3, 50)
pdf = stats.norm.pdf(z_range)

plt.figure(figsize=(10, 4))
plt.plot(z_range, pdf, color='gray', linestyle='-', label='Standard Normal PDF')

plt.hist(zarr1, bins=20, density=True, alpha=0.5, label='Array 1 Z-scores', color='blue')

plt.axvline(0, color='black', linestyle='-', linewidth=3)
plt.title('Z-Score Distribution of Array 1')
plt.xlabel('Z-score')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()
1/175:
#scipy operations

#initializing 3 arrays with 5 values each
arr1 = np.array([])
arr2 = np.array([])
arr3 = np.array([])
for i in range(15):
    if i < 5:
        arr1 = np.append(arr1, b[i])

    if i < 10 and i > 4:
        arr2 = np.append(arr2, b[i])

    if i < 15 and i > 9:
        arr3 = np.append(arr3, b[i])

print("Array 1:", arr1, "\nArray 2:", arr2, "\nArray 3:", arr3)

#one-way anova
f_statistic, p_value = stats.f_oneway(arr1, arr2, arr3)
print(f"\nOne-Way Anova \nF-statistic: {f_statistic:.4f}, P-value: {p_value:.4f}")

#plot
data = [arr1, arr2, arr3]
labels = ['Array 1', 'Array 2', 'Array 3']

plt.figure(figsize=(8, 5))
plt.boxplot(data, tick_labels=labels)
plt.title('One-Way ANOVA: Group Comparisons')
plt.ylabel('Scores')
plt.grid(True)
plt.legend()
plt.show()

#standard normal
zarr1 = stats.zscore(arr1)
print(f"\nZ-Distribution\nZ-score for Array 1:", zarr1)

#plot
z_range = np.linspace(-3, 3, 50)
pdf = stats.norm.pdf(z_range)

plt.figure(figsize=(10, 4))
plt.plot(z_range, pdf, color='gray', linestyle='-', label='Standard Normal PDF')

plt.hist(zarr1, bins=20, density=True, alpha=0.5, label='Array 1 Z-scores', color='blue')

plt.axvline(0, color='black', linestyle='-', linewidth=3)
plt.title('Z-Score Distribution of Array 1')
plt.xlabel('Z-score')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()
1/176:
#scipy operations

#initializing 3 arrays with 5 values each
arr1 = np.array([])
arr2 = np.array([])
arr3 = np.array([])
for i in range(15):
    if i < 5:
        arr1 = np.append(arr1, b[i])

    if i < 10 and i > 4:
        arr2 = np.append(arr2, b[i])

    if i < 15 and i > 9:
        arr3 = np.append(arr3, b[i])

print("Array 1:", arr1, "\nArray 2:", arr2, "\nArray 3:", arr3)

#one-way anova
f_statistic, p_value = stats.f_oneway(arr1, arr2, arr3)
print(f"\nOne-Way Anova \nF-statistic: {f_statistic:.4f}, P-value: {p_value:.4f}")

#plot
data = [arr1, arr2, arr3]
labels = ['Array 1', 'Array 2', 'Array 3']

plt.figure(figsize=(8, 5))
plt.boxplot(data, tick_labels=labels)
plt.title('One-Way ANOVA: Group Comparisons')
plt.ylabel('Scores')
plt.grid(True)
plt.show()

#standard normal
zarr1 = stats.zscore(arr1)
print(f"\nZ-Distribution\nZ-score for Array 1:", zarr1)

#plot
z_range = np.linspace(-3, 3, 50)
pdf = stats.norm.pdf(z_range)

plt.figure(figsize=(10, 4))
plt.plot(z_range, pdf, color='gray', linestyle='-', label='Standard Normal PDF')

plt.hist(zarr1, bins=20, density=True, alpha=0.5, label='Array 1 Z-scores', color='blue')

plt.axvline(0, color='black', linestyle='-', linewidth=3)
plt.title('Z-Score Distribution of Array 1')
plt.xlabel('Z-score')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()
1/177:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import csv

#DATA SET

df = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

a = df['Name'].to_numpy()
b = df['PPG'].to_numpy()
c = df['FG%'].to_numpy()
d = df['FT%'].to_numpy()


#INITIALS
col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']

#OUTPUTS
print("TOP 200 SCORERS DATA IN THE NATIONAL BASKETBALL ASSOCIATION (NBA)\n")

print("Data set columns:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    
#proof of clean data set
print("\nOriginal Data Shape:", df.shape)
print("Missing Values:") 
print(df.isnull().sum())
print("\nTop 5 scorers:\n", df.head())
1/178:
#numpy operations
sumppg = np.sum(b)
maxppg = np.max(b)
minppg = np.min(b)
meanfg = np.mean(c)
medianfg = np.median(c)
perfg = np.percentile(c, [90, 95, 99])
stdft = np.std(d)
varft = np.var(d)
rangeft = np.ptp(d)

print("\nPPG Statistics:")
print(f"Sum of PPG: {sumppg:.1f}")
print(f"Maximum of PPG: {maxppg:.1f}")
print(f"Minimum of PPG: {minppg:.1f}")

print("\nFG% Statistics:")
print(f"Mean of FG%: {meanfg:.1f}")
print(f"Median of FG%: {medianfg:.1f}")
print(f"90th, 95th, and 99th Percentile of FG%: {perfg}")

print("\nFT% Statistics:")
print(f"Standard Deviation of FT%: {stdft:.1f}")
print(f"Variance of FT%: {varft:.1f}")
print(f"Range of FT%: {rangeft:.1f}")
1/179:
#scipy operations

#initializing 3 arrays with 5 values each
arr1 = np.array([])
arr2 = np.array([])
arr3 = np.array([])
for i in range(15):
    if i < 5:
        arr1 = np.append(arr1, b[i])

    if i < 10 and i > 4:
        arr2 = np.append(arr2, b[i])

    if i < 15 and i > 9:
        arr3 = np.append(arr3, b[i])

print("Array 1:", arr1, "\nArray 2:", arr2, "\nArray 3:", arr3)

#one-way anova
f_statistic, p_value = stats.f_oneway(arr1, arr2, arr3)
print(f"\nOne-Way Anova \nF-statistic: {f_statistic:.4f}, P-value: {p_value:.4f}")

#plot
data = [arr1, arr2, arr3]
labels = ['Array 1', 'Array 2', 'Array 3']

plt.figure(figsize=(8, 5))
plt.boxplot(data, tick_labels=labels)
plt.title('One-Way ANOVA: Array Comparisons')
plt.ylabel('Scores')
plt.grid(True)
plt.show()

#standard normal
zarr1 = stats.zscore(arr1)
print(f"\nZ-Distribution\nZ-score for Array 1:", zarr1)

#plot
z_range = np.linspace(-3, 3, 50)
pdf = stats.norm.pdf(z_range)

plt.figure(figsize=(10, 4))
plt.plot(z_range, pdf, color='gray', linestyle='-', label='Standard Normal PDF')

plt.hist(zarr1, bins=20, density=True, alpha=0.5, label='Array 1 Z-scores', color='blue')

plt.axvline(0, color='black', linestyle='-', linewidth=3)
plt.title('Z-Score Distribution of Array 1')
plt.xlabel('Z-score')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()
1/180:
#scipy operations

#initializing 4 arrays with 50 values each
arr1 = np.array([])
arr2 = np.array([])
arr3 = np.array([])
arr4 = np.array([])
for i in range(15):
    if i < 50:
        arr1 = np.append(arr1, b[i])

    if i < 100 and i > 49:
        arr2 = np.append(arr2, b[i])

    if i < 150 and i > 99:
        arr3 = np.append(arr3, b[i])

    if i < 200 and i > 149:
        arr4 = np.append(arr4, b[i])

print("Array 1:", arr1, "\nArray 2:", arr2, "\nArray 3:", arr3)

#one-way anova
f_statistic, p_value = stats.f_oneway(arr1, arr2, arr3)
print(f"\nOne-Way Anova \nF-statistic: {f_statistic:.4f}, P-value: {p_value:.4f}")

#plot
data = [arr1, arr2, arr3]
labels = ['Array 1', 'Array 2', 'Array 3']

plt.figure(figsize=(8, 5))
plt.boxplot(data, tick_labels=labels)
plt.title('One-Way ANOVA: Array Comparisons')
plt.ylabel('Scores')
plt.grid(True)
plt.show()

#standard normal
zarr1 = stats.zscore(arr1)
print(f"\nZ-Distribution\nZ-score for Array 1:", zarr1)

#plot
z_range = np.linspace(-3, 3, 50)
pdf = stats.norm.pdf(z_range)

plt.figure(figsize=(10, 4))
plt.plot(z_range, pdf, color='gray', linestyle='-', label='Standard Normal PDF')

plt.hist(zarr1, bins=20, density=True, alpha=0.5, label='Array 1 Z-scores', color='blue')

plt.axvline(0, color='black', linestyle='-', linewidth=3)
plt.title('Z-Score Distribution of Array 1')
plt.xlabel('Z-score')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()
1/181:
#scipy operations

#initializing 4 arrays with 50 values each
arr1 = np.array([])
arr2 = np.array([])
arr3 = np.array([])
arr4 = np.array([])
for i in range(200):
    if i < 50:
        arr1 = np.append(arr1, b[i])

    if i < 100 and i > 49:
        arr2 = np.append(arr2, b[i])

    if i < 150 and i > 99:
        arr3 = np.append(arr3, b[i])

    if i < 200 and i > 149:
        arr4 = np.append(arr4, b[i])

print("Array 1:", arr1, "\nArray 2:", arr2, "\nArray 3:", arr3)

#one-way anova
f_statistic, p_value = stats.f_oneway(arr1, arr2, arr3)
print(f"\nOne-Way Anova \nF-statistic: {f_statistic:.4f}, P-value: {p_value:.4f}")

#plot
data = [arr1, arr2, arr3]
labels = ['Array 1', 'Array 2', 'Array 3']

plt.figure(figsize=(8, 5))
plt.boxplot(data, tick_labels=labels)
plt.title('One-Way ANOVA: Array Comparisons')
plt.ylabel('Scores')
plt.grid(True)
plt.show()

#standard normal
zarr1 = stats.zscore(arr1)
print(f"\nZ-Distribution\nZ-score for Array 1:", zarr1)

#plot
z_range = np.linspace(-3, 3, 50)
pdf = stats.norm.pdf(z_range)

plt.figure(figsize=(10, 4))
plt.plot(z_range, pdf, color='gray', linestyle='-', label='Standard Normal PDF')

plt.hist(zarr1, bins=20, density=True, alpha=0.5, label='Array 1 Z-scores', color='blue')

plt.axvline(0, color='black', linestyle='-', linewidth=3)
plt.title('Z-Score Distribution of Array 1')
plt.xlabel('Z-score')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()
1/182:
#scipy operations

#initializing 4 arrays with 50 values each
arr1 = np.array([])
arr2 = np.array([])
arr3 = np.array([])
arr4 = np.array([])
for i in range(200):
    if i < 50:
        arr1 = np.append(arr1, b[i])

    if i < 100 and i > 49:
        arr2 = np.append(arr2, b[i])

    if i < 150 and i > 99:
        arr3 = np.append(arr3, b[i])

    if i < 200 and i > 149:
        arr4 = np.append(arr4, b[i])

#one-way anova
f_statistic, p_value = stats.f_oneway(arr1, arr2, arr3, arr4)
print(f"\nOne-Way Anova \nF-statistic: {f_statistic:.4f}, P-value: {p_value:.4f}")

#plot
data = [arr1, arr2, arr3, arr4]
labels = ['Array 1', 'Array 2', 'Array 3', 'Array 4']

plt.figure(figsize=(8, 5))
plt.boxplot(data, tick_labels=labels)
plt.title('One-Way ANOVA: Array Comparisons')
plt.ylabel('Scores')
plt.grid(True)
plt.show()

#standard normal
zval = stats.zscore(b)
print(f"\nZ-Distribution\nZ-score for Array 1:", zval)

#plot
z_range = np.linspace(-3, 3, 50)
pdf = stats.norm.pdf(z_range)

plt.figure(figsize=(10, 4))
plt.plot(z_range, pdf, color='gray', linestyle='-', label='Standard Normal PDF')

plt.hist(zval, bins=20, density=True, alpha=0.5, label='Z-scores', color='blue')

plt.axvline(0, color='black', linestyle='-', linewidth=3)
plt.title('Z-Score Distribution of Array 1')
plt.xlabel('Z-score')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()
1/183:
#scipy operations

#initializing 4 arrays with 50 values each
arr1 = np.array([])
arr2 = np.array([])
arr3 = np.array([])
arr4 = np.array([])
for i in range(200):
    if i < 50:
        arr1 = np.append(arr1, b[i])

    if i < 100 and i > 49:
        arr2 = np.append(arr2, b[i])

    if i < 150 and i > 99:
        arr3 = np.append(arr3, b[i])

    if i < 200 and i > 149:
        arr4 = np.append(arr4, b[i])

#one-way anova
f_statistic, p_value = stats.f_oneway(arr1, arr2, arr3, arr4)
print(f"\nOne-Way Anova \nF-statistic: {f_statistic:.4f}, P-value: {p_value:.4f}")

#plot
data = [arr1, arr2, arr3, arr4]
labels = ['Array 1', 'Array 2', 'Array 3', 'Array 4']

plt.figure(figsize=(8, 5))
plt.boxplot(data, tick_labels=labels)
plt.title('One-Way ANOVA: Array Comparisons')
plt.ylabel('Scores')
plt.grid(True)
plt.show()

#standard normal
zval = stats.zscore(b)

#plot
z_range = np.linspace(-3, 3, 50)
pdf = stats.norm.pdf(z_range)

plt.figure(figsize=(10, 4))
plt.plot(z_range, pdf, color='gray', linestyle='-', label='Standard Normal PDF')

plt.hist(zval, bins=20, density=True, alpha=0.5, label='Z-scores', color='blue')

plt.axvline(0, color='black', linestyle='-', linewidth=3)
plt.title('Z-Score Distribution of Array 1')
plt.xlabel('Z-score')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()
1/184:
#scipy operations

#initializing 4 arrays with 50 values each
arr1 = np.array([])
arr2 = np.array([])
arr3 = np.array([])
arr4 = np.array([])
for i in range(200):
    if i < 50:
        arr1 = np.append(arr1, b[i])

    if i < 100 and i > 49:
        arr2 = np.append(arr2, b[i])

    if i < 150 and i > 99:
        arr3 = np.append(arr3, b[i])

    if i < 200 and i > 149:
        arr4 = np.append(arr4, b[i])

#one-way anova
f_statistic, p_value = stats.f_oneway(arr1, arr2, arr3, arr4)
print(f"\nOne-Way Anova \nF-statistic: {f_statistic:.4f}, P-value: {p_value:.4f}")

#plot
data = [arr1, arr2, arr3, arr4]
labels = ['Array 1', 'Array 2', 'Array 3', 'Array 4']

plt.figure(figsize=(8, 5))
plt.boxplot(data, tick_labels=labels)
plt.title('One-Way ANOVA: Array Comparisons')
plt.ylabel('Scores')
plt.grid(True)
plt.show()

#standard normal
zval = stats.zscore(b)
print(f"\nZ-Distribution\nZ-score for first 5 values:")
for i in range(5):
    print(zval[i])

#plot
z_range = np.linspace(-3, 3, 50)
pdf = stats.norm.pdf(z_range)

plt.figure(figsize=(10, 4))
plt.plot(z_range, pdf, color='gray', linestyle='-', label='Standard Normal PDF')

plt.hist(zval, bins=20, density=True, alpha=0.5, label='Z-scores', color='blue')

plt.axvline(0, color='black', linestyle='-', linewidth=3)
plt.title('Z-Score Distribution of Array 1')
plt.xlabel('Z-score')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()
1/185:
#scipy operations

#initializing 4 arrays with 50 values each
arr1 = np.array([])
arr2 = np.array([])
arr3 = np.array([])
arr4 = np.array([])
for i in range(200):
    if i < 50:
        arr1 = np.append(arr1, b[i])

    if i < 100 and i > 49:
        arr2 = np.append(arr2, b[i])

    if i < 150 and i > 99:
        arr3 = np.append(arr3, b[i])

    if i < 200 and i > 149:
        arr4 = np.append(arr4, b[i])

#one-way anova
f_statistic, p_value = stats.f_oneway(arr1, arr2, arr3, arr4)
print(f"\nOne-Way Anova \nF-statistic: {f_statistic:.4f}, P-value: {p_value:.4f}")

#plot
data = [arr1, arr2, arr3, arr4]
labels = ['Array 1', 'Array 2', 'Array 3', 'Array 4']

plt.figure(figsize=(8, 5))
plt.boxplot(data, tick_labels=labels)
plt.title('One-Way ANOVA: Array Comparisons')
plt.ylabel('Scores')
plt.grid(True)
plt.show()

#standard normal
zval = stats.zscore(b)
print(f"\nZ-Distribution\n\nZ-score for first 5 values:")
for i in range(5):
    print(zval[i])

#plot
z_range = np.linspace(-3, 3, 50)
pdf = stats.norm.pdf(z_range)

plt.figure(figsize=(10, 4))
plt.plot(z_range, pdf, color='gray', linestyle='-', label='Standard Normal PDF')

plt.hist(zval, bins=20, density=True, alpha=0.5, label='Z-scores', color='blue')

plt.axvline(0, color='black', linestyle='-', linewidth=3)
plt.title('Z-Score Distribution of Data Set')
plt.xlabel('Z-score')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()
1/186:
#scipy operations

#initializing 4 arrays with 50 values each
arr1 = np.array([])
arr2 = np.array([])
arr3 = np.array([])
arr4 = np.array([])
for i in range(200):
    if i < 50:
        arr1 = np.append(arr1, b[i])

    if i < 100 and i > 49:
        arr2 = np.append(arr2, b[i])

    if i < 150 and i > 99:
        arr3 = np.append(arr3, b[i])

    if i < 200 and i > 149:
        arr4 = np.append(arr4, b[i])

#one-way anova
f_statistic, p_value = stats.f_oneway(arr1, arr2, arr3, arr4)
print(f"\nOne-Way Anova \nF-statistic: {f_statistic:.4f}, P-value: {p_value:.4f}")

#plot
data = [arr1, arr2, arr3, arr4]
labels = ['Array 1', 'Array 2', 'Array 3', 'Array 4']

plt.figure(figsize=(8, 5))
plt.boxplot(data, tick_labels=labels)
plt.title('One-Way ANOVA: Array Comparisons')
plt.ylabel('Scores')
plt.grid(True)
plt.show()

#standard normal
zval = stats.zscore(arr1)
print(f"\nZ-Distribution\n\nZ-score for first 5 values:")
for i in range(5):
    print(zval[i])

#plot
z_range = np.linspace(-3, 3, 50)
pdf = stats.norm.pdf(z_range)

plt.figure(figsize=(10, 4))
plt.plot(z_range, pdf, color='gray', linestyle='-', label='Standard Normal PDF')

plt.hist(zval, bins=20, density=True, alpha=0.5, label='Z-scores', color='blue')

plt.axvline(0, color='black', linestyle='-', linewidth=3)
plt.title('Z-Score Distribution of Array 1')
plt.xlabel('Z-score')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()
1/187:
#scipy operations

#initializing 4 arrays with 50 values each
arr1 = np.array([])
arr2 = np.array([])
arr3 = np.array([])
arr4 = np.array([])
for i in range(200):
    if i < 50:
        arr1 = np.append(arr1, b[i])

    if i < 100 and i > 49:
        arr2 = np.append(arr2, b[i])

    if i < 150 and i > 99:
        arr3 = np.append(arr3, b[i])

    if i < 200 and i > 149:
        arr4 = np.append(arr4, b[i])

#one-way anova
f_statistic, p_value = stats.f_oneway(arr1, arr2, arr3, arr4)
print(f"\nOne-Way Anova \n\nF-statistic: {f_statistic:.4f}, P-value: {p_value:.4f}")

#plot
data = [arr1, arr2, arr3, arr4]
labels = ['Array 1', 'Array 2', 'Array 3', 'Array 4']

plt.figure(figsize=(8, 5))
plt.boxplot(data, tick_labels=labels)
plt.title('One-Way ANOVA: Array Comparisons')
plt.ylabel('Scores')
plt.grid(True)
plt.show()

#standard normal
zval = stats.zscore(arr1)
print(f"\nZ-Distribution\n\nZ-score for first 5 values:")
for i in range(5):
    print(zval[i])

#plot
z_range = np.linspace(-3, 3, 50)
pdf = stats.norm.pdf(z_range)

plt.figure(figsize=(10, 4))
plt.plot(z_range, pdf, color='gray', linestyle='-', label='Standard Normal PDF')

plt.hist(zval, bins=20, density=True, alpha=0.5, label='Z-scores', color='blue')

plt.axvline(0, color='black', linestyle='-', linewidth=3)
plt.title('Z-Score Distribution of Array 1')
plt.xlabel('Z-score')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()
1/188:
#scipy operations

#initializing 4 arrays with 50 values each
arr1 = np.array([])
arr2 = np.array([])
arr3 = np.array([])
arr4 = np.array([])
for i in range(200):
    if i < 50:
        arr1 = np.append(arr1, b[i])

    if i < 100 and i > 49:
        arr2 = np.append(arr2, b[i])

    if i < 150 and i > 99:
        arr3 = np.append(arr3, b[i])

    if i < 200 and i > 149:
        arr4 = np.append(arr4, b[i])

#one-way anova
f_statistic, p_value = stats.f_oneway(arr1, arr2, arr3, arr4)
print(f"\nOne-Way Anova \n\nF-statistic: {f_statistic:.4f}, P-value: {p_value:.4f}")

#plot
data = [arr1, arr2, arr3, arr4]
labels = ['Array 1', 'Array 2', 'Array 3', 'Array 4']

plt.figure(figsize=(8, 5))
plt.boxplot(data, tick_labels=labels)
plt.title('One-Way ANOVA: Array Comparisons')
plt.ylabel('Scores')
plt.grid(True)
plt.show()

#standard normal
zval = stats.zscore(arr1)
print(f"\nZ-Distribution\n\nZ-score for first 5 values:")
for i in range(5):
    print(zval[i], end='')

#plot
z_range = np.linspace(-3, 3, 50)
pdf = stats.norm.pdf(z_range)

plt.figure(figsize=(10, 4))
plt.plot(z_range, pdf, color='gray', linestyle='-', label='Standard Normal PDF')

plt.hist(zval, bins=20, density=True, alpha=0.5, label='Z-scores', color='blue')

plt.axvline(0, color='black', linestyle='-', linewidth=3)
plt.title('Z-Score Distribution of Array 1')
plt.xlabel('Z-score')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()
1/189:
#scipy operations

#initializing 4 arrays with 50 values each
arr1 = np.array([])
arr2 = np.array([])
arr3 = np.array([])
arr4 = np.array([])
for i in range(200):
    if i < 50:
        arr1 = np.append(arr1, b[i])

    if i < 100 and i > 49:
        arr2 = np.append(arr2, b[i])

    if i < 150 and i > 99:
        arr3 = np.append(arr3, b[i])

    if i < 200 and i > 149:
        arr4 = np.append(arr4, b[i])

#one-way anova
f_statistic, p_value = stats.f_oneway(arr1, arr2, arr3, arr4)
print(f"\nOne-Way Anova \n\nF-statistic: {f_statistic:.4f}, P-value: {p_value:.4f}")

#plot
data = [arr1, arr2, arr3, arr4]
labels = ['Array 1', 'Array 2', 'Array 3', 'Array 4']

plt.figure(figsize=(8, 5))
plt.boxplot(data, tick_labels=labels)
plt.title('One-Way ANOVA: Array Comparisons')
plt.ylabel('Scores')
plt.grid(True)
plt.show()

#standard normal
zval = stats.zscore(arr1)
print(f"\nZ-Distribution\n\nZ-score for first 5 values:")
for i in range(5):
    print(zval[i], end=' ')

#plot
z_range = np.linspace(-3, 3, 50)
pdf = stats.norm.pdf(z_range)

plt.figure(figsize=(10, 4))
plt.plot(z_range, pdf, color='gray', linestyle='-', label='Standard Normal PDF')

plt.hist(zval, bins=20, density=True, alpha=0.5, label='Z-scores', color='blue')

plt.axvline(0, color='black', linestyle='-', linewidth=3)
plt.title('Z-Score Distribution of Array 1')
plt.xlabel('Z-score')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()
1/190:
#scipy operations

#initializing 4 arrays with 50 values each
arr1 = np.array([])
arr2 = np.array([])
arr3 = np.array([])
arr4 = np.array([])
for i in range(200):
    if i < 50:
        arr1 = np.append(arr1, b[i])

    if i < 100 and i > 49:
        arr2 = np.append(arr2, b[i])

    if i < 150 and i > 99:
        arr3 = np.append(arr3, b[i])

    if i < 200 and i > 149:
        arr4 = np.append(arr4, b[i])

#one-way anova
f_statistic, p_value = stats.f_oneway(arr1, arr2, arr3, arr4)
print(f"\nOne-Way Anova \n\nF-statistic: {f_statistic:.4f}, P-value: {p_value:.4f}")

#plot
data = [arr1, arr2, arr3, arr4]
labels = ['Array 1', 'Array 2', 'Array 3', 'Array 4']

plt.figure(figsize=(8, 5))
plt.boxplot(data, tick_labels=labels)
plt.title('One-Way ANOVA: Array Comparisons')
plt.ylabel('Scores')
plt.grid(True)
plt.show()

#standard normal
zval = stats.zscore(arr1)
print(f"\nZ-Distribution\n\nZ-score for first 5 values:")
for i in range(5):
    print(zval[i], end=' ')

#plot
z_range = np.linspace(-3, 3, 50)
pdf = stats.norm.pdf(z_range)

plt.figure(figsize=(10, 4))
plt.plot(z_range, pdf, color='gray', linestyle='-', label='Standard Normal PDF')

plt.hist(zval, bins=20, density=True, alpha=0.5, label='Z-scores', color='blue')

plt.axvline(0, color='black', linestyle='-', linewidth=3)
plt.title('Z-Score Distribution of Array 1')
plt.xlabel('Z-score')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()

#t-test
t_stat, p_value = stats.ttest_ind(arr3, arr4)
print(f"T-test between North and South Sales: t={t_stat:.2f}, p={p_value:.3f}")
1/191:
#scipy operations

#initializing 4 arrays with 25 values each
arr1 = np.array([])
arr2 = np.array([])
arr3 = np.array([])
arr4 = np.array([])
for i in range(200):
    if i < 25:
        arr1 = np.append(arr1, b[i])

    if i < 50 and i > 24:
        arr2 = np.append(arr2, b[i])

    if i < 75 and i > 49:
        arr3 = np.append(arr3, b[i])

    if i < 100 and i > 74:
        arr4 = np.append(arr4, b[i])

#one-way anova
f_statistic, p_value = stats.f_oneway(arr1, arr2, arr3, arr4)
print(f"\nOne-Way Anova \n\nF-statistic: {f_statistic:.4f}, P-value: {p_value:.4f}")

#plot
data = [arr1, arr2, arr3, arr4]
labels = ['Array 1', 'Array 2', 'Array 3', 'Array 4']

plt.figure(figsize=(8, 5))
plt.boxplot(data, tick_labels=labels)
plt.title('One-Way ANOVA: Array Comparisons')
plt.ylabel('Scores')
plt.grid(True)
plt.show()

#standard normal
zval = stats.zscore(arr1)
print(f"\nZ-Distribution\n\nZ-score for first 5 values:")
for i in range(5):
    print(zval[i], end=' ')

#plot
z_range = np.linspace(-3, 3, 50)
pdf = stats.norm.pdf(z_range)

plt.figure(figsize=(10, 4))
plt.plot(z_range, pdf, color='gray', linestyle='-', label='Standard Normal PDF')

plt.hist(zval, bins=20, density=True, alpha=0.5, label='Z-scores', color='blue')

plt.axvline(0, color='black', linestyle='-', linewidth=3)
plt.title('Z-Score Distribution of Array 1')
plt.xlabel('Z-score')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()

#t-test
t_stat, p_value = stats.ttest_ind(arr3, arr4)
print(f"T-test between North and South Sales: t={t_stat:.2f}, p={p_value:.3f}")
1/192:
#scipy operations

#initializing 4 arrays with 25 values each
arr1 = np.array([])
arr2 = np.array([])
arr3 = np.array([])
arr4 = np.array([])
for i in range(100):
    if i < 25:
        arr1 = np.append(arr1, b[i])

    if i < 50 and i > 24:
        arr2 = np.append(arr2, b[i])

    if i < 75 and i > 49:
        arr3 = np.append(arr3, b[i])

    if i < 100 and i > 74:
        arr4 = np.append(arr4, b[i])

#one-way anova
f_statistic, p_value = stats.f_oneway(arr1, arr2, arr3, arr4)
print(f"\nOne-Way Anova \n\nF-statistic: {f_statistic:.4f}, P-value: {p_value:.4f}")

#plot
data = [arr1, arr2, arr3, arr4]
labels = ['Array 1', 'Array 2', 'Array 3', 'Array 4']

plt.figure(figsize=(8, 5))
plt.boxplot(data, tick_labels=labels)
plt.title('One-Way ANOVA: Array Comparisons')
plt.ylabel('Scores')
plt.grid(True)
plt.show()

#standard normal
zval = stats.zscore(arr1)
print(f"\nZ-Distribution\n\nZ-score for first 5 values:")
for i in range(5):
    print(zval[i], end=' ')

#plot
z_range = np.linspace(-3, 3, 50)
pdf = stats.norm.pdf(z_range)

plt.figure(figsize=(10, 4))
plt.plot(z_range, pdf, color='gray', linestyle='-', label='Standard Normal PDF')

plt.hist(zval, bins=20, density=True, alpha=0.5, label='Z-scores', color='blue')

plt.axvline(0, color='black', linestyle='-', linewidth=3)
plt.title('Z-Score Distribution of Array 1')
plt.xlabel('Z-score')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()

#t-test
t_stat, p_value = stats.ttest_ind(arr3, arr4)
print(f"T-test between North and South Sales: t={t_stat:.2f}, p={p_value:.3f}")
1/193:
#scipy operations

#initializing 4 arrays with 5 values each
arr1 = np.array([])
arr2 = np.array([])
arr3 = np.array([])
arr4 = np.array([])
for i in range(100):
    if i < 5:
        arr1 = np.append(arr1, b[i])

    if i < 10 and i > 4:
        arr2 = np.append(arr2, b[i])

    if i < 15 and i > 9:
        arr3 = np.append(arr3, b[i])

    if i < 20 and i > 14:
        arr4 = np.append(arr4, b[i])

#one-way anova
f_statistic, p_value = stats.f_oneway(arr1, arr2, arr3, arr4)
print(f"\nOne-Way Anova \n\nF-statistic: {f_statistic:.4f}, P-value: {p_value:.4f}")

#plot
data = [arr1, arr2, arr3, arr4]
labels = ['Array 1', 'Array 2', 'Array 3', 'Array 4']

plt.figure(figsize=(8, 5))
plt.boxplot(data, tick_labels=labels)
plt.title('One-Way ANOVA: Array Comparisons')
plt.ylabel('Scores')
plt.grid(True)
plt.show()

#standard normal
zval = stats.zscore(arr1)
print(f"\nZ-Distribution\n\nZ-score for first 5 values:")
for i in range(5):
    print(zval[i], end=' ')

#plot
z_range = np.linspace(-3, 3, 50)
pdf = stats.norm.pdf(z_range)

plt.figure(figsize=(10, 4))
plt.plot(z_range, pdf, color='gray', linestyle='-', label='Standard Normal PDF')

plt.hist(zval, bins=20, density=True, alpha=0.5, label='Z-scores', color='blue')

plt.axvline(0, color='black', linestyle='-', linewidth=3)
plt.title('Z-Score Distribution of Array 1')
plt.xlabel('Z-score')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()

#t-test
t_stat, p_value = stats.ttest_ind(arr3, arr4)
print(f"T-test between North and South Sales: t={t_stat:.2f}, p={p_value:.3f}")
1/194:
#scipy operations

#initializing 4 arrays with 5 values each
arr1 = np.array([])
arr2 = np.array([])
arr3 = np.array([])
arr4 = np.array([])
for i in range(100):
    if i < 5:
        arr1 = np.append(arr1, b[i])

    if i < 10 and i > 4:
        arr2 = np.append(arr2, b[i])

    if i < 15 and i > 9:
        arr3 = np.append(arr3, b[i])

    if i < 20 and i > 14:
        arr4 = np.append(arr4, b[i])

#one-way anova
f_statistic, p_value = stats.f_oneway(arr1, arr2, arr3, arr4)
print(f"\nOne-Way Anova \n\nF-statistic: {f_statistic:.4f}, P-value: {p_value:.8f}")

#plot
data = [arr1, arr2, arr3, arr4]
labels = ['Array 1', 'Array 2', 'Array 3', 'Array 4']

plt.figure(figsize=(8, 5))
plt.boxplot(data, tick_labels=labels)
plt.title('One-Way ANOVA: Array Comparisons')
plt.ylabel('Scores')
plt.grid(True)
plt.show()

#standard normal
zval = stats.zscore(arr1)
print(f"\nZ-Distribution\n\nZ-score for first 5 values:")
for i in range(5):
    print(zval[i], end=' ')

#plot
z_range = np.linspace(-3, 3, 50)
pdf = stats.norm.pdf(z_range)

plt.figure(figsize=(10, 4))
plt.plot(z_range, pdf, color='gray', linestyle='-', label='Standard Normal PDF')

plt.hist(zval, bins=20, density=True, alpha=0.5, label='Z-scores', color='blue')

plt.axvline(0, color='black', linestyle='-', linewidth=3)
plt.title('Z-Score Distribution of Array 1')
plt.xlabel('Z-score')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()

#t-test
t_stat, p_value = stats.ttest_ind(arr3, arr4)
print(f"T-test between North and South Sales: t={t_stat:.2f}, p={p_value:.3f}")
1/195:
#scipy operations

#initializing 4 arrays with 5 values each
arr1 = np.array([])
arr2 = np.array([])
arr3 = np.array([])
arr4 = np.array([])
for i in range(100):
    if i < 5:
        arr1 = np.append(arr1, b[i])

    if i < 10 and i > 4:
        arr2 = np.append(arr2, b[i])

    if i < 15 and i > 9:
        arr3 = np.append(arr3, b[i])

    if i < 20 and i > 14:
        arr4 = np.append(arr4, b[i])

#one-way anova
f_statistic, p_value = stats.f_oneway(arr1, arr2, arr3, arr4)
print(f"\nOne-Way Anova \n\nF-statistic: {f_statistic:.4f}, P-value: {p_value:.8f}")

#plot
data = [arr1, arr2, arr3, arr4]
labels = ['Array 1', 'Array 2', 'Array 3', 'Array 4']

plt.figure(figsize=(8, 5))
plt.boxplot(data, tick_labels=labels)
plt.title('One-Way ANOVA: Array Comparisons')
plt.ylabel('Scores')
plt.grid(True)
plt.show()

#standard normal
zval = stats.zscore(arr1)
print(f"\nZ-Distribution\n\nZ-score for first 5 values:")
for i in range(5):
    print(zval[i], end=' ')

#plot
z_range = np.linspace(-3, 3, 50)
pdf = stats.norm.pdf(z_range)

plt.figure(figsize=(10, 4))
plt.plot(z_range, pdf, color='gray', linestyle='-', label='Standard Normal PDF')

plt.hist(zval, bins=20, density=True, alpha=0.5, label='Z-scores', color='blue')

plt.axvline(0, color='black', linestyle='-', linewidth=3)
plt.title('Z-Score Distribution of Array 1')
plt.xlabel('Z-score')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()

#t-test
t_stat, p_value = stats.ttest_ind(arr3, arr4)
print(f"T-test between Array 3 and Array 4: t={t_stat:.2f}, p={p_value:.3f}")
1/196:
#scipy operations

#initializing 4 arrays with 5 values each
arr1 = np.array([])
arr2 = np.array([])
arr3 = np.array([])
arr4 = np.array([])
for i in range(100):
    if i < 5:
        arr1 = np.append(arr1, b[i])

    if i < 10 and i > 4:
        arr2 = np.append(arr2, b[i])

    if i < 15 and i > 9:
        arr3 = np.append(arr3, b[i])

    if i < 20 and i > 14:
        arr4 = np.append(arr4, b[i])

print("Array 1", arr1,"Array 2", arr2, "Array 3",arr3, "Array 4",arr4)
#one-way anova
f_statistic, p_value = stats.f_oneway(arr1, arr2, arr3, arr4)
print(f"\nOne-Way Anova \n\nF-statistic: {f_statistic:.4f}, P-value: {p_value:.8f}")

#plot
data = [arr1, arr2, arr3, arr4]
labels = ['Array 1', 'Array 2', 'Array 3', 'Array 4']

plt.figure(figsize=(8, 5))
plt.boxplot(data, tick_labels=labels)
plt.title('One-Way ANOVA: Array Comparisons')
plt.ylabel('Scores')
plt.grid(True)
plt.show()

#standard normal
zval = stats.zscore(arr1)
print(f"\nZ-Distribution\n\nZ-score for first 5 values:")
for i in range(5):
    print(zval[i], end=' ')

#plot
z_range = np.linspace(-3, 3, 50)
pdf = stats.norm.pdf(z_range)

plt.figure(figsize=(10, 4))
plt.plot(z_range, pdf, color='gray', linestyle='-', label='Standard Normal PDF')

plt.hist(zval, bins=20, density=True, alpha=0.5, label='Z-scores', color='blue')

plt.axvline(0, color='black', linestyle='-', linewidth=3)
plt.title('Z-Score Distribution of Array 1')
plt.xlabel('Z-score')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()

#t-test
t_stat, p_value = stats.ttest_ind(arr3, arr4)
print(f"T-test between Array 3 and Array 4: t={t_stat:.2f}, p={p_value:.3f}")
1/197:
#scipy operations

#initializing 4 arrays with 5 values each
arr1 = np.array([])
arr2 = np.array([])
arr3 = np.array([])
arr4 = np.array([])
for i in range(100):
    if i < 5:
        arr1 = np.append(arr1, b[i])

    if i < 10 and i > 4:
        arr2 = np.append(arr2, b[i])

    if i < 15 and i > 9:
        arr3 = np.append(arr3, b[i])

    if i < 20 and i > 14:
        arr4 = np.append(arr4, b[i])

print("Array 1", arr1,"\nArray 2", arr2, "\nArray 3",arr3, "\nArray 4",arr4)
#one-way anova
f_statistic, p_value = stats.f_oneway(arr1, arr2, arr3, arr4)
print(f"\nOne-Way Anova \n\nF-statistic: {f_statistic:.4f}, P-value: {p_value:.8f}")

#plot
data = [arr1, arr2, arr3, arr4]
labels = ['Array 1', 'Array 2', 'Array 3', 'Array 4']

plt.figure(figsize=(8, 5))
plt.boxplot(data, tick_labels=labels)
plt.title('One-Way ANOVA: Array Comparisons')
plt.ylabel('Scores')
plt.grid(True)
plt.show()

#standard normal
zval = stats.zscore(arr1)
print(f"\nZ-Distribution\n\nZ-score for first 5 values:")
for i in range(5):
    print(zval[i], end=' ')

#plot
z_range = np.linspace(-3, 3, 50)
pdf = stats.norm.pdf(z_range)

plt.figure(figsize=(10, 4))
plt.plot(z_range, pdf, color='gray', linestyle='-', label='Standard Normal PDF')

plt.hist(zval, bins=20, density=True, alpha=0.5, label='Z-scores', color='blue')

plt.axvline(0, color='black', linestyle='-', linewidth=3)
plt.title('Z-Score Distribution of Array 1')
plt.xlabel('Z-score')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()

#t-test
t_stat, p_value = stats.ttest_ind(arr3, arr4)
print(f"T-test between Array 3 and Array 4: t={t_stat:.2f}, p={p_value:.3f}")
1/198:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import csv

#DATA SET

df = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

a = df['Name'].to_numpy()
b = df['PPG'].to_numpy()
c = df['FG%'].to_numpy()
d = df['FT%'].to_numpy()


#INITIALS
col_title = data.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']

#OUTPUTS
print("TOP 200 SCORERS DATA IN THE NATIONAL BASKETBALL ASSOCIATION (NBA)\n")

print("Data set columns:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    
#proof of clean data set
print("\nOriginal Data Shape:", df.shape)
print("Missing Values:") 
print(df.isnull().sum())
print("\nTop 5 scorers:\n", df.head())
1/199:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import csv

#DATA SET

df = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

a = df['Name'].to_numpy()
b = df['PPG'].to_numpy()
c = df['FG%'].to_numpy()
d = df['FT%'].to_numpy()


#INITIALS
col_title = df.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']

#OUTPUTS
print("TOP 200 SCORERS DATA IN THE NATIONAL BASKETBALL ASSOCIATION (NBA)\n")

print("Data set columns:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    
#proof of clean data set
print("\nOriginal Data Shape:", df.shape)
print("Missing Values:") 
print(df.isnull().sum())
print("\nTop 5 scorers:\n", df.head())
1/200:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import csv

#DATA SET

df = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

a = df['Name'].to_numpy()
b = df['PPG'].to_numpy()
c = df['FG%'].to_numpy()
d = df['FT%'].to_numpy()


#INITIALS
col_title = df.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']

#OUTPUTS
print("TOP 200 SCORERS DATA IN THE NATIONAL BASKETBALL ASSOCIATION (NBA)\n")

print("Data set columns:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    
#proof of clean data set
print("\nOriginal Data Shape:", df.shape)
print("Missing Values:") 
print(df.isnull().sum())
print("\nTop 5 scorers:\n", df.head())
1/201:
#numpy operations
sumppg = np.sum(b)
maxppg = np.max(b)
minppg = np.min(b)
meanfg = np.mean(c)
medianfg = np.median(c)
perfg = np.percentile(c, [90, 95, 99])
stdft = np.std(d)
varft = np.var(d)
rangeft = np.ptp(d)

print("\nPPG Statistics:")
print(f"Sum of PPG: {sumppg:.1f}")
print(f"Maximum of PPG: {maxppg:.1f}")
print(f"Minimum of PPG: {minppg:.1f}")

print("\nFG% Statistics:")
print(f"Mean of FG%: {meanfg:.1f}")
print(f"Median of FG%: {medianfg:.1f}")
print(f"90th, 95th, and 99th Percentile of FG%: {perfg}")

print("\nFT% Statistics:")
print(f"Standard Deviation of FT%: {stdft:.1f}")
print(f"Variance of FT%: {varft:.1f}")
print(f"Range of FT%: {rangeft:.1f}")
1/202:
#scipy operations

#initializing 4 arrays with 5 values each
arr1 = np.array([])
arr2 = np.array([])
arr3 = np.array([])
arr4 = np.array([])
for i in range(100):
    if i < 5:
        arr1 = np.append(arr1, b[i])

    if i < 10 and i > 4:
        arr2 = np.append(arr2, b[i])

    if i < 15 and i > 9:
        arr3 = np.append(arr3, b[i])

    if i < 20 and i > 14:
        arr4 = np.append(arr4, b[i])

print("Array 1", arr1,"\nArray 2", arr2, "\nArray 3",arr3, "\nArray 4",arr4)
#one-way anova
f_statistic, p_value = stats.f_oneway(arr1, arr2, arr3, arr4)
print(f"\nOne-Way Anova \n\nF-statistic: {f_statistic:.4f}, P-value: {p_value:.8f}")

#plot
data = [arr1, arr2, arr3, arr4]
labels = ['Array 1', 'Array 2', 'Array 3', 'Array 4']

plt.figure(figsize=(8, 5))
plt.boxplot(data, tick_labels=labels)
plt.title('One-Way ANOVA: Array Comparisons')
plt.ylabel('Scores')
plt.grid(True)
plt.show()

#standard normal
zval = stats.zscore(arr1)
print(f"\nZ-Distribution\n\nZ-score for first 5 values:")
for i in range(5):
    print(zval[i], end=' ')

#plot
z_range = np.linspace(-3, 3, 50)
pdf = stats.norm.pdf(z_range)

plt.figure(figsize=(10, 4))
plt.plot(z_range, pdf, color='gray', linestyle='-', label='Standard Normal PDF')

plt.hist(zval, bins=20, density=True, alpha=0.5, label='Z-scores', color='blue')

plt.axvline(0, color='black', linestyle='-', linewidth=3)
plt.title('Z-Score Distribution of Array 1')
plt.xlabel('Z-score')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()

#t-test
t_stat, p_value = stats.ttest_ind(arr3, arr4)
print(f"T-test between Array 3 and Array 4: t={t_stat:.2f}, p={p_value:.3f}")
1/203:
#Statsmodels
x = sm.add_constant(df['FG%'])
model = sm.OLS(df['PPG'], x).fit()
print("\nLinear Regression Summary:")
print(model.summary())
1/204:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

#DATA SET

df = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

a = df['Name'].to_numpy()
b = df['PPG'].to_numpy()
c = df['FG%'].to_numpy()
d = df['FT%'].to_numpy()


#INITIALS
col_title = df.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']

#OUTPUTS
print("TOP 200 SCORERS DATA IN THE NATIONAL BASKETBALL ASSOCIATION (NBA)\n")

print("Data set columns:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    
#proof of clean data set
print("\nOriginal Data Shape:", df.shape)
print("Missing Values:") 
print(df.isnull().sum())
print("\nTop 5 scorers:\n", df.head())
1/205:
#scipy operations

#initializing 4 arrays with 5 values each
arr1 = np.array([])
arr2 = np.array([])
arr3 = np.array([])
arr4 = np.array([])
for i in range(100):
    if i < 5:
        arr1 = np.append(arr1, b[i])

    if i < 10 and i > 4:
        arr2 = np.append(arr2, b[i])

    if i < 15 and i > 9:
        arr3 = np.append(arr3, b[i])

    if i < 20 and i > 14:
        arr4 = np.append(arr4, b[i])

print("Array 1", arr1,"\nArray 2", arr2, "\nArray 3",arr3, "\nArray 4",arr4)
#one-way anova
f_statistic, p_value = stats.f_oneway(arr1, arr2, arr3, arr4)
print(f"\nOne-Way Anova \n\nF-statistic: {f_statistic:.4f}, P-value: {p_value:.8f}")

#plot
data = [arr1, arr2, arr3, arr4]
labels = ['Array 1', 'Array 2', 'Array 3', 'Array 4']

plt.figure(figsize=(8, 5))
plt.boxplot(data, tick_labels=labels)
plt.title('One-Way ANOVA: Array Comparisons')
plt.ylabel('Scores')
plt.grid(True)
plt.show()

#standard normal
zval = stats.zscore(arr1)
print(f"\nZ-Distribution\n\nZ-score for first 5 values:")
for i in range(5):
    print(zval[i], end=' ')

#plot
z_range = np.linspace(-3, 3, 50)
pdf = stats.norm.pdf(z_range)

plt.figure(figsize=(10, 4))
plt.plot(z_range, pdf, color='gray', linestyle='-', label='Standard Normal PDF')

plt.hist(zval, bins=20, density=True, alpha=0.5, label='Z-scores', color='blue')

plt.axvline(0, color='black', linestyle='-', linewidth=3)
plt.title('Z-Score Distribution of Array 1')
plt.xlabel('Z-score')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()

#t-test
t_stat, p_value = stats.ttest_ind(arr3, arr4)
print(f"T-test between Array 3 and Array 4: t={t_stat:.2f}, p={p_value:.3f}")
1/206:
#Statsmodels
x = sm.add_constant(df['FG%'])
model = sm.OLS(df['PPG'], x).fit()
print("\nLinear Regression Summary:")
print(model.summary())
1/207:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

#DATA SET
df = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

a = df['Name'].to_numpy()
b = df['PPG'].to_numpy()
c = df['FG%'].to_numpy()
d = df['FT%'].to_numpy()


#INITIALS
col_title = df.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']

#OUTPUTS
print("TOP 200 SCORERS DATA IN THE NATIONAL BASKETBALL ASSOCIATION (NBA)\n")

print("Data set columns:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    
#proof of clean data set
print("\nOriginal Data Shape:", df.shape)
print("Missing Values:") 
print(df.isnull().sum())
print("\nTop 5 scorers:\n", df.head())
1/208:
#scipy operations

#sampling the data set into 4 arrays (samples) with 5 values each
arr1 = np.array([])
arr2 = np.array([])
arr3 = np.array([])
arr4 = np.array([])
for i in range(20):
    if i < 5:
        arr1 = np.append(arr1, b[i])

    if i < 10 and i > 4:
        arr2 = np.append(arr2, b[i])

    if i < 15 and i > 9:
        arr3 = np.append(arr3, b[i])

    if i < 20 and i > 14:
        arr4 = np.append(arr4, b[i])

print("Array 1", arr1,"\nArray 2", arr2, "\nArray 3",arr3, "\nArray 4",arr4)
#one-way anova
f_statistic, p_value = stats.f_oneway(arr1, arr2, arr3, arr4)
print(f"\nOne-Way Anova \n\nF-statistic: {f_statistic:.4f}, P-value: {p_value:.8f}")

#plot
data = [arr1, arr2, arr3, arr4]
labels = ['Array 1', 'Array 2', 'Array 3', 'Array 4']

plt.figure(figsize=(8, 5))
plt.boxplot(data, tick_labels=labels)
plt.title('One-Way ANOVA: Array Comparisons')
plt.ylabel('Scores')
plt.grid(True)
plt.show()

#standard normal
zval = stats.zscore(arr1)
print(f"\nZ-Distribution\n\nZ-score for first 5 values:")
for i in range(5):
    print(zval[i], end=' ')

#plot
z_range = np.linspace(-3, 3, 50)
pdf = stats.norm.pdf(z_range)

plt.figure(figsize=(10, 4))
plt.plot(z_range, pdf, color='gray', linestyle='-', label='Standard Normal PDF')

plt.hist(zval, bins=20, density=True, alpha=0.5, label='Z-scores', color='blue')

plt.axvline(0, color='black', linestyle='-', linewidth=3)
plt.title('Z-Score Distribution of Array 1')
plt.xlabel('Z-score')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()

#t-test
t_stat, p_value = stats.ttest_ind(arr3, arr4)
print(f"T-test between Array 3 and Array 4: t={t_stat:.2f}, p={p_value:.3f}")
1/209:
#scipy operations

#sampling the data set into 4 arrays (samples) with 5 values each
arr1 = np.array([])
arr2 = np.array([])
arr3 = np.array([])
arr4 = np.array([])
for i in range(20):
    if i < 5:
        arr1 = np.append(arr1, b[i])

    if i < 10 and i > 4:
        arr2 = np.append(arr2, b[i])

    if i < 15 and i > 9:
        arr3 = np.append(arr3, b[i])

    if i < 20 and i > 14:
        arr4 = np.append(arr4, b[i])

print("Array 1", arr1,"\nArray 2", arr2, "\nArray 3",arr3, "\nArray 4",arr4)
#one-way anova
f_statistic, p_value = stats.f_oneway(arr1, arr2, arr3, arr4)
print(f"\nOne-Way Anova \n\nF-statistic: {f_statistic:.4f}, P-value: {p_value:.8f}")

#plot
data = [arr1, arr2, arr3, arr4]
labels = ['Array 1', 'Array 2', 'Array 3', 'Array 4']

plt.figure(figsize=(8, 5))
plt.boxplot(data, tick_labels=labels)
plt.title('One-Way ANOVA: Array Comparisons')
plt.ylabel('Scores')
plt.grid(True)
plt.show()

#standard normal
zval = stats.zscore(arr1)
print(f"\nZ-Distribution\n\nZ-score for first 5 values:")
for i in range(5):
    print(zval[i], end=' ')

#plot
z_range = np.linspace(-3, 3, 50)
pdf = stats.norm.pdf(z_range)

plt.figure(figsize=(10, 4))
plt.plot(z_range, pdf, color='gray', linestyle='-', label='Standard Normal PDF')

plt.hist(zval, bins=20, density=True, alpha=0.5, label='Z-scores', color='blue')

plt.axvline(0, color='black', linestyle='-', linewidth=3)
plt.title('Z-Score Distribution of Array 1')
plt.xlabel('Z-score')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()

#t-test
t_stat, p_value = stats.ttest_ind(arr3, arr4)
print(f"T-test between Array 3 and Array 4: t={t_stat:.2f}, p={p_value:.3f}")

#plot
plt.figure(figsize=(8, 5))
plt.boxplot([group1, group2], labels=['Group 1', 'Group 2'])
plt.title('T-Test: Group Comparison')
plt.ylabel('Values')
plt.grid(True)

# Annotate with p-value
plt.text(1.5, max(max(group1), max(group2)), f'p = {p_val:.4f}', 
         ha='center', va='bottom', fontsize=12, color='blue')

plt.show()
1/210:
#scipy operations

#sampling the data set into 4 arrays (samples) with 5 values each
arr1 = np.array([])
arr2 = np.array([])
arr3 = np.array([])
arr4 = np.array([])
for i in range(20):
    if i < 5:
        arr1 = np.append(arr1, b[i])

    if i < 10 and i > 4:
        arr2 = np.append(arr2, b[i])

    if i < 15 and i > 9:
        arr3 = np.append(arr3, b[i])

    if i < 20 and i > 14:
        arr4 = np.append(arr4, b[i])

print("Array 1", arr1,"\nArray 2", arr2, "\nArray 3",arr3, "\nArray 4",arr4)
#one-way anova
f_statistic, p_value = stats.f_oneway(arr1, arr2, arr3, arr4)
print(f"\nOne-Way Anova \n\nF-statistic: {f_statistic:.4f}, P-value: {p_value:.8f}")

#plot
data = [arr1, arr2, arr3, arr4]
labels = ['Array 1', 'Array 2', 'Array 3', 'Array 4']

plt.figure(figsize=(8, 5))
plt.boxplot(data, tick_labels=labels)
plt.title('One-Way ANOVA: Array Comparisons')
plt.ylabel('Scores')
plt.grid(True)
plt.show()

#standard normal
zval = stats.zscore(arr1)
print(f"\nZ-Distribution\n\nZ-score for first 5 values:")
for i in range(5):
    print(zval[i], end=' ')

#plot
z_range = np.linspace(-3, 3, 50)
pdf = stats.norm.pdf(z_range)

plt.figure(figsize=(10, 4))
plt.plot(z_range, pdf, color='gray', linestyle='-', label='Standard Normal PDF')

plt.hist(zval, bins=20, density=True, alpha=0.5, label='Z-scores', color='blue')

plt.axvline(0, color='black', linestyle='-', linewidth=3)
plt.title('Z-Score Distribution of Array 1')
plt.xlabel('Z-score')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()

#t-test
t_stat, p_value = stats.ttest_ind(arr3, arr4)
print(f"T-test between Array 3 and Array 4: t={t_stat:.2f}, p={p_value:.3f}")

#plot
plt.figure(figsize=(8, 5))
plt.boxplot([arr3, arr4], labels=['Array 3', 'Array 4'])
plt.title('T-Test: Array 3 & Array 4 Comparison')
plt.ylabel('Values')
plt.grid(True)

# Annotate with p-value
plt.text(1.5, max(max(arr3), max(arr4)), f'p = {p_val:.4f}', 
         ha='center', va='bottom', fontsize=12, color='blue')

plt.show()
1/211:
#scipy operations

#sampling the data set into 4 arrays (samples) with 5 values each
arr1 = np.array([])
arr2 = np.array([])
arr3 = np.array([])
arr4 = np.array([])
for i in range(20):
    if i < 5:
        arr1 = np.append(arr1, b[i])

    if i < 10 and i > 4:
        arr2 = np.append(arr2, b[i])

    if i < 15 and i > 9:
        arr3 = np.append(arr3, b[i])

    if i < 20 and i > 14:
        arr4 = np.append(arr4, b[i])

print("Array 1", arr1,"\nArray 2", arr2, "\nArray 3",arr3, "\nArray 4",arr4)
#one-way anova
f_statistic, p_value = stats.f_oneway(arr1, arr2, arr3, arr4)
print(f"\nOne-Way Anova \n\nF-statistic: {f_statistic:.4f}, P-value: {p_value:.8f}")

#plot
data = [arr1, arr2, arr3, arr4]
labels = ['Array 1', 'Array 2', 'Array 3', 'Array 4']

plt.figure(figsize=(8, 5))
plt.boxplot(data, tick_labels=labels)
plt.title('One-Way ANOVA: Array Comparisons')
plt.ylabel('Scores')
plt.grid(True)
plt.show()

#standard normal
zval = stats.zscore(arr1)
print(f"\nZ-Distribution\n\nZ-score for first 5 values:")
for i in range(5):
    print(zval[i], end=' ')

#plot
z_range = np.linspace(-3, 3, 50)
pdf = stats.norm.pdf(z_range)

plt.figure(figsize=(10, 4))
plt.plot(z_range, pdf, color='gray', linestyle='-', label='Standard Normal PDF')

plt.hist(zval, bins=20, density=True, alpha=0.5, label='Z-scores', color='blue')

plt.axvline(0, color='black', linestyle='-', linewidth=3)
plt.title('Z-Score Distribution of Array 1')
plt.xlabel('Z-score')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()

#t-test
t_stat, p_value = stats.ttest_ind(arr3, arr4)
print(f"T-test between Array 3 and Array 4: t={t_stat:.2f}, p={p_value:.3f}")

#plot
plt.figure(figsize=(8, 5))
plt.boxplot([arr3, arr4], labels=['Array 3', 'Array 4'])
plt.title('T-Test: Array 3 & Array 4 Comparison')
plt.ylabel('Values')
plt.grid(True)

# Annotate with p-value
plt.text(1.5, max(max(arr3), max(arr4)), f'p = {p_value:.4f}', 
         ha='center', va='bottom', fontsize=12, color='blue')

plt.show()
1/212:
#scipy operations

#sampling the data set into 4 arrays (samples) with 5 values each
arr1 = np.array([])
arr2 = np.array([])
arr3 = np.array([])
arr4 = np.array([])
for i in range(20):
    if i < 5:
        arr1 = np.append(arr1, b[i])

    if i < 10 and i > 4:
        arr2 = np.append(arr2, b[i])

    if i < 15 and i > 9:
        arr3 = np.append(arr3, b[i])

    if i < 20 and i > 14:
        arr4 = np.append(arr4, b[i])

print("Array 1", arr1,"\nArray 2", arr2, "\nArray 3",arr3, "\nArray 4",arr4)
#one-way anova
f_statistic, p_value = stats.f_oneway(arr1, arr2, arr3, arr4)
print(f"\nOne-Way Anova \n\nF-statistic: {f_statistic:.4f}, P-value: {p_value:.8f}")

#plot
data = [arr1, arr2, arr3, arr4]
labels = ['Array 1', 'Array 2', 'Array 3', 'Array 4']

plt.figure(figsize=(8, 5))
plt.boxplot(data, tick_labels=labels)
plt.title('One-Way ANOVA: Array Comparisons')
plt.ylabel('Scores')
plt.grid(True)
plt.show()

#standard normal
zval = stats.zscore(arr1)
print(f"\nZ-Distribution\n\nZ-score for first 5 values:")
for i in range(5):
    print(zval[i], end=' ')

#plot
z_range = np.linspace(-3, 3, 50)
pdf = stats.norm.pdf(z_range)

plt.figure(figsize=(10, 4))
plt.plot(z_range, pdf, color='gray', linestyle='-', label='Standard Normal PDF')

plt.hist(zval, bins=20, density=True, alpha=0.5, label='Z-scores', color='blue')

plt.axvline(0, color='black', linestyle='-', linewidth=3)
plt.title('Z-Score Distribution of Array 1')
plt.xlabel('Z-score')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()

#t-test
t_stat, p_value = stats.ttest_ind(arr3, arr4)
print(f"T-test between Array 3 and Array 4: t={t_stat:.2f}, p={p_value:.3f}")

#plot
plt.figure(figsize=(8, 5))
plt.boxplot([arr3, arr4], tick_labels=['Array 3', 'Array 4'])
plt.title('T-Test: Array 3 & Array 4 Comparison')
plt.ylabel('Values')
plt.grid(True)

# Annotate with p-value
plt.text(1.5, max(max(arr3), max(arr4)), f'p = {p_value:.4f}', 
         ha='center', va='bottom', fontsize=12, color='blue')

plt.show()
1/213:
#scipy operations

#sampling the data set into 4 arrays (samples) with 5 values each
arr1 = np.array([])
arr2 = np.array([])
arr3 = np.array([])
arr4 = np.array([])
for i in range(20):
    if i < 5:
        arr1 = np.append(arr1, b[i])

    if i < 10 and i > 4:
        arr2 = np.append(arr2, b[i])

    if i < 15 and i > 9:
        arr3 = np.append(arr3, b[i])

    if i < 20 and i > 14:
        arr4 = np.append(arr4, b[i])

print("Array 1", arr1,"\nArray 2", arr2, "\nArray 3",arr3, "\nArray 4",arr4)
#one-way anova
f_statistic, p_value = stats.f_oneway(arr1, arr2, arr3, arr4)
print(f"\nOne-Way Anova \n\nF-statistic: {f_statistic:.4f}, P-value: {p_value:.8f}")

#plot
data = [arr1, arr2, arr3, arr4]
labels = ['Array 1', 'Array 2', 'Array 3', 'Array 4']

plt.figure(figsize=(8, 5))
plt.boxplot(data, tick_labels=labels)
plt.title('One-Way ANOVA: Array Comparisons')
plt.ylabel('Scores')
plt.grid(True)
plt.show()

#standard normal
zval = stats.zscore(arr1)
print(f"\nZ-Distribution\n\nZ-score for first 5 values:")
for i in range(5):
    print(zval[i], end=' ')

#plot
z_range = np.linspace(-3, 3, 50)
pdf = stats.norm.pdf(z_range)

plt.figure(figsize=(10, 4))
plt.plot(z_range, pdf, color='gray', linestyle='-', label='Standard Normal PDF')

plt.hist(zval, bins=20, density=True, alpha=0.5, label='Z-scores', color='blue')

plt.axvline(0, color='black', linestyle='-', linewidth=3)
plt.title('Z-Score Distribution of Array 1')
plt.xlabel('Z-score')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()

#t-test
t_stat, p_value = stats.ttest_ind(arr3, arr4)
print(f"T - Test\n\nT-test between Array 3 and Array 4: t={t_stat:.2f}, p={p_value:.3f}")

#plot
plt.figure(figsize=(8, 5))
plt.boxplot([arr3, arr4], tick_labels=['Array 3', 'Array 4'])
plt.title('T-Test: Array 3 & Array 4 Comparison')
plt.ylabel('Values')
plt.grid(True)

# Annotate with p-value
plt.text(1.5, max(max(arr3), max(arr4)), f'p = {p_value:.4f}', 
         ha='center', va='bottom', fontsize=12, color='blue')

plt.show()
1/214:
#scipy operations

#sampling the data set into 4 arrays (samples) with 5 values each
arr1 = np.array([])
arr2 = np.array([])
arr3 = np.array([])
arr4 = np.array([])
for i in range(20):
    if i < 5:
        arr1 = np.append(arr1, b[i])

    if i < 10 and i > 4:
        arr2 = np.append(arr2, b[i])

    if i < 15 and i > 9:
        arr3 = np.append(arr3, b[i])

    if i < 20 and i > 14:
        arr4 = np.append(arr4, b[i])

print("Array 1", arr1,"\nArray 2", arr2, "\nArray 3",arr3, "\nArray 4",arr4)
#one-way anova
f_statistic, p_value = stats.f_oneway(arr1, arr2, arr3, arr4)
print(f"\nOne-Way Anova \n\nF-statistic: {f_statistic:.4f}, P-value: {p_value:.8f}")

#plot
data = [arr1, arr2, arr3, arr4]
labels = ['Array 1', 'Array 2', 'Array 3', 'Array 4']

plt.figure(figsize=(8, 5))
plt.boxplot(data, tick_labels=labels)
plt.title('One-Way ANOVA: Array Comparisons')
plt.ylabel('Scores')
plt.grid(True)
plt.show()

#standard normal
zval = stats.zscore(arr1)
print(f"\nZ-Distribution\n\nZ-score for first 5 values:")
for i in range(5):
    print(zval[i], end=' ')

#plot
z_range = np.linspace(-3, 3, 50)
pdf = stats.norm.pdf(z_range)

plt.figure(figsize=(10, 4))
plt.plot(z_range, pdf, color='gray', linestyle='-', label='Standard Normal PDF')

plt.hist(zval, bins=20, density=True, alpha=0.5, label='Z-scores', color='blue')

plt.axvline(0, color='black', linestyle='-', linewidth=3)
plt.title('Z-Score Distribution of Array 1')
plt.xlabel('Z-score')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()

#t-test
t_stat, p_value = stats.ttest_ind(arr3, arr4)
print(f"T - Test\n\nT-test between Array 3 and Array 4: \nt = {t_stat:.2f} \np = {p_value:.3f}")

#plot
plt.figure(figsize=(8, 5))
plt.boxplot([arr3, arr4], tick_labels=['Array 3', 'Array 4'])
plt.title('T-Test: Array 3 & Array 4 Comparison')
plt.ylabel('Values')
plt.grid(True)

# Annotate with p-value
plt.text(1.5, max(max(arr3), max(arr4)), f'p = {p_value:.4f}', 
         ha='center', va='bottom', fontsize=12, color='blue')

plt.show()
1/215:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

#DATA SET
df = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

a = df['Name'].to_numpy()
b = df['PPG'].to_numpy()
c = df['FG%'].to_numpy()
d = df['FT%'].to_numpy()


#INITIALS
col_title = df.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']

#OUTPUTS
print("TOP 200 SCORERS DATA IN THE NATIONAL BASKETBALL ASSOCIATION (NBA)\n")

print("Data set columns:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    
#proof of clean data set
print("\nOriginal Data Shape:", df.shape)
print("Missing Values:") 
print(df.isnull().sum())
print("\nTop 5 scorers:\n", df.head())
1/216:
#numpy operations

sumppg = np.sum(b)
maxppg = np.max(b)
minppg = np.min(b)
meanfg = np.mean(c)
medianfg = np.median(c)
perfg = np.percentile(c, [90, 95, 99])
stdft = np.std(d)
varft = np.var(d)
rangeft = np.ptp(d)

print("\nPPG Statistics:")
print(f"Sum of PPG: {sumppg:.1f}")
print(f"Maximum of PPG: {maxppg:.1f}")
print(f"Minimum of PPG: {minppg:.1f}")

print("\nFG% Statistics:")
print(f"Mean of FG%: {meanfg:.1f}")
print(f"Median of FG%: {medianfg:.1f}")
print(f"90th, 95th, and 99th Percentile of FG%: {perfg}")

print("\nFT% Statistics:")
print(f"Standard Deviation of FT%: {stdft:.1f}")
print(f"Variance of FT%: {varft:.1f}")
print(f"Range of FT%: {rangeft:.1f}")
1/217:
#scipy operations

#sampling the data set into 4 arrays (samples) with 5 values each
arr1 = np.array([])
arr2 = np.array([])
arr3 = np.array([])
arr4 = np.array([])
for i in range(20):
    if i < 5:
        arr1 = np.append(arr1, b[i])

    if i < 10 and i > 4:
        arr2 = np.append(arr2, b[i])

    if i < 15 and i > 9:
        arr3 = np.append(arr3, b[i])

    if i < 20 and i > 14:
        arr4 = np.append(arr4, b[i])

print("Array 1", arr1,"\nArray 2", arr2, "\nArray 3",arr3, "\nArray 4",arr4)
#one-way anova
f_statistic, p_value = stats.f_oneway(arr1, arr2, arr3, arr4)
print(f"\nOne-Way Anova \n\nF-statistic: {f_statistic:.4f}, P-value: {p_value:.8f}")

#plot
data = [arr1, arr2, arr3, arr4]
labels = ['Array 1', 'Array 2', 'Array 3', 'Array 4']

plt.figure(figsize=(8, 5))
plt.boxplot(data, tick_labels=labels)
plt.title('One-Way ANOVA: Array Comparisons')
plt.ylabel('Scores')
plt.grid(True)
plt.show()

#standard normal
zval = stats.zscore(arr1)
print(f"\nZ-Distribution\n\nZ-score for first 5 values:")
for i in range(5):
    print(zval[i], end=' ')

#plot
z_range = np.linspace(-3, 3, 50)
pdf = stats.norm.pdf(z_range)

plt.figure(figsize=(10, 4))
plt.plot(z_range, pdf, color='gray', linestyle='-', label='Standard Normal PDF')

plt.hist(zval, bins=20, density=True, alpha=0.5, label='Z-scores', color='blue')

plt.axvline(0, color='black', linestyle='-', linewidth=3)
plt.title('Z-Score Distribution of Array 1')
plt.xlabel('Z-score')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()

#t-test
t_stat, p_value = stats.ttest_ind(arr3, arr4)
print(f"T - Test\n\nT-test between Array 3 and Array 4: \nt = {t_stat:.2f} \np = {p_value:.3f}")

#plot
plt.figure(figsize=(8, 5))
plt.boxplot([arr3, arr4], tick_labels=['Array 3', 'Array 4'])
plt.title('T-Test: Array 3 & Array 4 Comparison')
plt.ylabel('Values')
plt.grid(True)

# Annotate with p-value
plt.text(1.5, max(max(arr3), max(arr4)), f'p = {p_value:.4f}', 
         ha='center', va='bottom', fontsize=12, color='blue')

plt.show()
1/218:
#Statsmodels

x = sm.add_constant(df['FG%'])
model = sm.OLS(df['PPG'], x).fit()
print("\nLinear Regression Summary:")
print(model.summary())
1/219:
#correlation and other visualizations

corr_matrix = np.corrcoef(arr1, arr2)

# Extract the correlation coefficient
correlation = corr_matrix[0, 1]

print("Correlation coefficient (Pearson r):", correlation)
1/220:
#correlation and other visualizations

corr_matrix = np.corrcoef(b, c)

# Extract the correlation coefficient
correlation = corr_matrix[0, 1]
print("")
print("Correlation coefficient (Pearson r):", correlation)
1/221:
#correlation and other visualizations
x = 0
y = 1

#corr1
corr_matrix = np.corrcoef(b, c)
correlation = corr_matrix[0, 1]
print(col_title[x], col_title[x], "vs", col_title[y], col_title[y], ":\n")
print("Correlation coefficient (Pearson r):", correlation)
1/222:
#correlation and other visualizations
x = 0
y = 1

#corr1
corr_matrix = np.corrcoef(b, c)
correlation = corr_matrix[0, 1]
print(col_title[x], col_cat[x], "vs", col_title[y], col_cat[y], ":\n")
print("Correlation coefficient (Pearson r):", correlation)
1/223:
#correlation and other visualizations
x = 0
y = 1

#corr1
corr_matrix = np.corrcoef(b, c)
correlation = corr_matrix[0, 1]
print(col_cat[x], col_title[x], "vs", col_cat[y], col_title[y], ":\n")
print("Correlation coefficient (Pearson r):", correlation)
1/224:
#correlation and other visualizations
x = 0
y = 1

#corr1
corr_matrix = np.corrcoef(b, c)
correlation = corr_matrix[0, 1]
print(col_cat[x], col_title[x], "vs", col_cat[y], col_title[y])
print("\nCorrelation coefficient (Pearson r):", correlation)
1/225:
#correlation and other visualizations
x = 0
y = 1

#corr1
corr_matrix = np.corrcoef(b, c)
correlation = corr_matrix[0, 1]
print(col_cat[x], col_title[x], "vs", col_cat[y], col_title[y])
print("\nCorrelation coefficient (Pearson r):", correlation)
x += 1
y += 1
print(x, y)
1/226:
#correlation and other visualizations
x = 0
y = 1

#corr1
corr_matrix = np.corrcoef(b, c)
correlation = corr_matrix[0, 1]
print(col_cat[x], col_title[x], "vs", col_cat[y], col_title[y])
print("\nCorrelation coefficient (Pearson r):", correlation)
y += 1

#corr2
corr_matrix = np.corrcoef(b, d)
correlation = corr_matrix[0, 1]
print(col_cat[x], col_title[x], "vs", col_cat[y], col_title[y])
print("\nCorrelation coefficient (Pearson r):", correlation)
x += 1

#corr3
corr_matrix = np.corrcoef(c, d)
correlation = corr_matrix[0, 1]
print(col_cat[x], col_title[x], "vs", col_cat[y], col_title[y])
print("\nCorrelation coefficient (Pearson r):", correlation)
1/227:
#correlation and other visualizations
x = 0
y = 1

#corr1
corr_matrix = np.corrcoef(b, c)
correlation = corr_matrix[0, 1]
print(col_cat[x], col_title[x], "vs", col_cat[y], col_title[y])
print("Correlation coefficient (Pearson r):", correlation)
y += 1

#corr2
corr_matrix = np.corrcoef(b, d)
correlation = corr_matrix[0, 1]
print()
print(col_cat[x], col_title[x], "vs", col_cat[y], col_title[y])
print("\nCorrelation coefficient (Pearson r):", correlation)
x += 1

#corr3
corr_matrix = np.corrcoef(c, d)
correlation = corr_matrix[0, 1]
print()
print(col_cat[x], col_title[x], "vs", col_cat[y], col_title[y])
print("\nCorrelation coefficient (Pearson r):", correlation)
1/228:
#correlation and other visualizations
x = 0
y = 1

#corr1
corr_matrix = np.corrcoef(b, c)
correlation = corr_matrix[0, 1]
print(col_cat[x], col_title[x], "vs", col_cat[y], col_title[y])
print("Correlation coefficient (Pearson r):", correlation)
y += 1

#corr2
corr_matrix = np.corrcoef(b, d)
correlation = corr_matrix[0, 1]
print()
print(col_cat[x], col_title[x], "vs", col_cat[y], col_title[y])
print("Correlation coefficient (Pearson r):", correlation)
x += 1

#corr3
corr_matrix = np.corrcoef(c, d)
correlation = corr_matrix[0, 1]
print()
print(col_cat[x], col_title[x], "vs", col_cat[y], col_title[y])
print("Correlation coefficient (Pearson r):", correlation)
1/229:
#correlation and other visualizations
x = 1
y = 2

#corr1
corr_matrix = np.corrcoef(b, c)
correlation = corr_matrix[0, 1]
print(col_cat[x], col_title[x], "vs", col_cat[y], col_title[y])
print("Correlation coefficient (Pearson r):", correlation)
y += 1

#corr2
corr_matrix = np.corrcoef(b, d)
correlation = corr_matrix[0, 1]
print()
print(col_cat[x], col_title[x], "vs", col_cat[y], col_title[y])
print("Correlation coefficient (Pearson r):", correlation)
x += 1

#corr3
corr_matrix = np.corrcoef(c, d)
correlation = corr_matrix[0, 1]
print()
print(col_cat[x], col_title[x], "vs", col_cat[y], col_title[y])
print("Correlation coefficient (Pearson r):", correlation)
1/230:
#correlation and other visualizations
x = 1
y = 2

#corr1
corr_matrix = np.corrcoef(b, c)
correlation = corr_matrix[0, 1]
print(col_cat[x], col_title[x], "vs", col_cat[y], col_title[y])
print("Correlation coefficient (Pearson r):", correlation)
y += 1

#plot for corr1
slope, intercept, r_value, p_value, std_err = linregress(b, c)

y_pred = slope * b + intercept

# Plot scatter and regression line
plt.figure(figsize=(8, 5))
plt.scatter(b, c, color='blue', label='Data Points')
plt.plot(b, y_pred, color='red', label=f'Regression Line\ny = {slope:.2f}x + {intercept:.2f}')

# Annotate correlation coefficient
plt.text(min(b), max(c), f'R = {r_value:.2f}', fontsize=12, color='green')

# Labels and legend
plt.title('Scatter Plot with Regression Line')
plt.xlabel(col_cat[x], col_title[x])
plt.ylabel(col_cat[y], col_title[y)
plt.grid(True)
plt.legend()
plt.show()

#corr2
corr_matrix = np.corrcoef(b, d)
correlation = corr_matrix[0, 1]
print()
print(col_cat[x], col_title[x], "vs", col_cat[y], col_title[y])
print("Correlation coefficient (Pearson r):", correlation)
x += 1

#corr3
corr_matrix = np.corrcoef(c, d)
correlation = corr_matrix[0, 1]
print()
print(col_cat[x], col_title[x], "vs", col_cat[y], col_title[y])
print("Correlation coefficient (Pearson r):", correlation)
1/231:
#correlation and other visualizations
x = 1
y = 2

#corr1
corr_matrix = np.corrcoef(b, c)
correlation = corr_matrix[0, 1]
print(col_cat[x], col_title[x], "vs", col_cat[y], col_title[y])
print("Correlation coefficient (Pearson r):", correlation)
y += 1

#plot for corr1
slope, intercept, r_value, p_value, std_err = linregress(b, c)

y_pred = slope * b + intercept

# Plot scatter and regression line
plt.figure(figsize=(8, 5))
plt.scatter(b, c, color='blue', label='Data Points')
plt.plot(b, y_pred, color='red', label=f'Regression Line\ny = {slope:.2f}x + {intercept:.2f}')

# Annotate correlation coefficient
plt.text(min(b), max(c), f'R = {r_value:.2f}', fontsize=12, color='green')

# Labels and legend
plt.title('Scatter Plot with Regression Line')
plt.xlabel(col_cat[x], col_title[x])
plt.ylabel(col_cat[y], col_title[y])
plt.grid(True)
plt.legend()
plt.show()

#corr2
corr_matrix = np.corrcoef(b, d)
correlation = corr_matrix[0, 1]
print()
print(col_cat[x], col_title[x], "vs", col_cat[y], col_title[y])
print("Correlation coefficient (Pearson r):", correlation)
x += 1

#corr3
corr_matrix = np.corrcoef(c, d)
correlation = corr_matrix[0, 1]
print()
print(col_cat[x], col_title[x], "vs", col_cat[y], col_title[y])
print("Correlation coefficient (Pearson r):", correlation)
1/232:
#correlation and other visualizations
x = 1
y = 2

#corr1
corr_matrix = np.corrcoef(b, c)
correlation = corr_matrix[0, 1]
print(col_cat[x], col_title[x], "vs", col_cat[y], col_title[y])
print("Correlation coefficient (Pearson r):", correlation)
y += 1

#plot for corr1
slope, intercept, r_value, p_value, std_err = stats.linregress(b, c)

y_pred = slope * b + intercept

# Plot scatter and regression line
plt.figure(figsize=(8, 5))
plt.scatter(b, c, color='blue', label='Data Points')
plt.plot(b, y_pred, color='red', label=f'Regression Line\ny = {slope:.2f}x + {intercept:.2f}')

# Annotate correlation coefficient
plt.text(min(b), max(c), f'R = {r_value:.2f}', fontsize=12, color='green')

# Labels and legend
plt.title('Scatter Plot with Regression Line')
plt.xlabel(col_cat[x], col_title[x])
plt.ylabel(col_cat[y], col_title[y])
plt.grid(True)
plt.legend()
plt.show()

#corr2
corr_matrix = np.corrcoef(b, d)
correlation = corr_matrix[0, 1]
print()
print(col_cat[x], col_title[x], "vs", col_cat[y], col_title[y])
print("Correlation coefficient (Pearson r):", correlation)
x += 1

#corr3
corr_matrix = np.corrcoef(c, d)
correlation = corr_matrix[0, 1]
print()
print(col_cat[x], col_title[x], "vs", col_cat[y], col_title[y])
print("Correlation coefficient (Pearson r):", correlation)
1/233:
#correlation and other visualizations
x = 1
y = 2

#corr1
corr_matrix = np.corrcoef(b, c)
correlation = corr_matrix[0, 1]
print(col_cat[x], col_title[x], "vs", col_cat[y], col_title[y])
print("Correlation coefficient (Pearson r):", correlation)
y += 1

#plot for corr1
slope, intercept, r_value, p_value, std_err = stats.linregress(b, c)

y_pred = slope * b + intercept

# Plot scatter and regression line
plt.figure(figsize=(8, 5))
plt.scatter(b, c, color='blue', label='Data Points')
plt.plot(b, y_pred, color='red', label=f'Regression Line\ny = {slope:.2f}x + {intercept:.2f}')

# Annotate correlation coefficient
plt.text(min(b), max(c), f'R = {r_value:.2f}', fontsize=12, color='green')

# Labels and legend
plt.title('Scatter Plot with Regression Line')
plt.xlabel('Points Per Game PPG')
plt.ylabel('Field Goal Percentage FG%')
plt.grid(True)
plt.legend()
plt.show()

#corr2
corr_matrix = np.corrcoef(b, d)
correlation = corr_matrix[0, 1]
print()
print(col_cat[x], col_title[x], "vs", col_cat[y], col_title[y])
print("Correlation coefficient (Pearson r):", correlation)
x += 1

#corr3
corr_matrix = np.corrcoef(c, d)
correlation = corr_matrix[0, 1]
print()
print(col_cat[x], col_title[x], "vs", col_cat[y], col_title[y])
print("Correlation coefficient (Pearson r):", correlation)
1/234:
#correlation and other visualizations
x = 1
y = 2

#corr1
corr_matrix = np.corrcoef(b, c)
correlation = corr_matrix[0, 1]
print(col_cat[x], col_title[x], "vs", col_cat[y], col_title[y])
print("Correlation coefficient (Pearson r):", correlation)
y += 1

#plot for corr1
slope, intercept, r_value, p_value, std_err = stats.linregress(b, c)

y_pred = slope * b + intercept

# Plot scatter and regression line
plt.figure(figsize=(8, 5))
plt.scatter(b, c, color='blue', label='Data Points')
plt.plot(b, y_pred, color='pink', label=f'Regression Line\ny = {slope:.2f}x + {intercept:.2f}')

# Annotate correlation coefficient
plt.text(min(b), max(c), f'R = {r_value:.2f}', fontsize=12, color='green')

# Labels and legend
plt.title('Scatter Plot with Regression Line')
plt.xlabel('Points Per Game PPG')
plt.ylabel('Field Goal Percentage FG%')
plt.grid(True)
plt.legend()
plt.show()

#corr2
corr_matrix = np.corrcoef(b, d)
correlation = corr_matrix[0, 1]
print()
print(col_cat[x], col_title[x], "vs", col_cat[y], col_title[y])
print("Correlation coefficient (Pearson r):", correlation)
x += 1

#corr3
corr_matrix = np.corrcoef(c, d)
correlation = corr_matrix[0, 1]
print()
print(col_cat[x], col_title[x], "vs", col_cat[y], col_title[y])
print("Correlation coefficient (Pearson r):", correlation)
1/235:
#correlation and other visualizations
x = 1
y = 2

#corr1
corr_matrix = np.corrcoef(b, c)
correlation = corr_matrix[0, 1]
print(col_cat[x], col_title[x], "vs", col_cat[y], col_title[y])
print("Correlation coefficient (Pearson r):", correlation)
y += 1

#plot for corr1
slope, intercept, r_value, p_value, std_err = stats.linregress(b, c)

y_pred = slope * b + intercept

# Plot scatter and regression line
plt.figure(figsize=(8, 5))
plt.scatter(b, c, color='pink', label='Data Points')
plt.plot(b, y_pred, color='red', label=f'Regression Line\ny = {slope:.2f}x + {intercept:.2f}')

# Annotate correlation coefficient
plt.text(min(b), max(c), f'R = {r_value:.2f}', fontsize=12, color='green')

# Labels and legend
plt.title('Scatter Plot with Regression Line')
plt.xlabel('Points Per Game PPG')
plt.ylabel('Field Goal Percentage FG%')
plt.grid(True)
plt.legend()
plt.show()

#corr2
corr_matrix = np.corrcoef(b, d)
correlation = corr_matrix[0, 1]
print()
print(col_cat[x], col_title[x], "vs", col_cat[y], col_title[y])
print("Correlation coefficient (Pearson r):", correlation)
x += 1

#corr3
corr_matrix = np.corrcoef(c, d)
correlation = corr_matrix[0, 1]
print()
print(col_cat[x], col_title[x], "vs", col_cat[y], col_title[y])
print("Correlation coefficient (Pearson r):", correlation)
1/236:
#correlation and other visualizations
x = 1
y = 2

#corr1
corr_matrix = np.corrcoef(b, c)
correlation = corr_matrix[0, 1]
print(col_cat[x], col_title[x], "vs", col_cat[y], col_title[y])
print("Correlation coefficient (Pearson r):", correlation)
y += 1

#plot for corr1
slope, intercept, r_value, p_value, std_err = stats.linregress(b, c)

y_pred = slope * b + intercept

# Plot scatter and regression line
plt.figure(figsize=(8, 5))
plt.scatter(b, c, color='pink', label='Data Points')
plt.plot(b, y_pred, color='red', label=f'Regression Line\ny = {slope:.2f}x + {intercept:.2f}')

# Annotate correlation coefficient
plt.text(min(b), max(c), f'R = {r_value:.2f}', fontsize=12, color='blue')

# Labels and legend
plt.title('Scatter Plot with Regression Line')
plt.xlabel('Points Per Game PPG')
plt.ylabel('Field Goal Percentage FG%')
plt.grid(True)
plt.legend()
plt.show()

#corr2
corr_matrix = np.corrcoef(b, d)
correlation = corr_matrix[0, 1]
print()
print(col_cat[x], col_title[x], "vs", col_cat[y], col_title[y])
print("Correlation coefficient (Pearson r):", correlation)
x += 1

#corr3
corr_matrix = np.corrcoef(c, d)
correlation = corr_matrix[0, 1]
print()
print(col_cat[x], col_title[x], "vs", col_cat[y], col_title[y])
print("Correlation coefficient (Pearson r):", correlation)
1/237:
#correlation and other visualizations
x = 1
y = 2

#corr1
corr_matrix = np.corrcoef(b, c)
correlation = corr_matrix[0, 1]
print(col_cat[x], col_title[x], "vs", col_cat[y], col_title[y])
print("Correlation coefficient (Pearson r):", correlation)
y += 1

#plot for corr1
slope, intercept, r_value, p_value, std_err = stats.linregress(b, c)

y_pred = slope * b + intercept

plt.figure(figsize=(8, 5))
plt.scatter(b, c, color='pink', label='Data Points')
plt.plot(b, y_pred, color='red', label=f'Regression Line\ny = {slope:.2f}x + {intercept:.2f}')

plt.text(min(b), max(c), f'r = {correlation:.2f}', fontsize=12, color='blue')

plt.title('Scatter Plot with Regression Line')
plt.xlabel('Points Per Game PPG')
plt.ylabel('Field Goal Percentage FG%')
plt.grid(True)
plt.legend()
plt.show()

#corr2
corr_matrix = np.corrcoef(b, d)
correlation = corr_matrix[0, 1]
print()
print(col_cat[x], col_title[x], "vs", col_cat[y], col_title[y])
print("Correlation coefficient (Pearson r):", correlation)
x += 1

#corr3
corr_matrix = np.corrcoef(c, d)
correlation = corr_matrix[0, 1]
print()
print(col_cat[x], col_title[x], "vs", col_cat[y], col_title[y])
print("Correlation coefficient (Pearson r):", correlation)
1/238:
#correlation and other visualizations
x = 1
y = 2

#corr1
corr_matrix = np.corrcoef(b, c)
correlation = corr_matrix[0, 1]
print(col_cat[x], col_title[x], "vs", col_cat[y], col_title[y])
print(f"Correlation coefficient (Pearson r): {r_value:.4f}", correlation)
y += 1

#plot for corr1
slope, intercept, r_value, p_value, std_err = stats.linregress(b, c)

y_pred = slope * b + intercept

plt.figure(figsize=(8, 5))
plt.scatter(b, c, color='pink', label='Data Points')
plt.plot(b, y_pred, color='red', label=f'Regression Line\ny = {slope:.2f}x + {intercept:.2f}')

plt.text(min(b), max(c), f'r = {r_value:.2f}', fontsize=12, color='blue')

plt.title('Scatter Plot with Regression Line')
plt.xlabel('Points Per Game PPG')
plt.ylabel('Field Goal Percentage FG%')
plt.grid(True)
plt.legend()
plt.show()

#corr2
corr_matrix = np.corrcoef(b, d)
correlation = corr_matrix[0, 1]
print()
print(col_cat[x], col_title[x], "vs", col_cat[y], col_title[y])
print("Correlation coefficient (Pearson r):", correlation)
x += 1

#corr3
corr_matrix = np.corrcoef(c, d)
correlation = corr_matrix[0, 1]
print()
print(col_cat[x], col_title[x], "vs", col_cat[y], col_title[y])
print("Correlation coefficient (Pearson r):", correlation)
1/239:
#correlation and other visualizations
x = 1
y = 2

#corr1
corr_matrix = np.corrcoef(b, c)
correlation = corr_matrix[0, 1]
print(col_cat[x], col_title[x], "vs", col_cat[y], col_title[y])
print(f"Correlation coefficient (Pearson r): {r_value:.4f}", correlation)
y += 1

#plot for corr1
slope, intercept, r_value, p_value, std_err = stats.linregress(b, c)

y_pred = slope * b + intercept

plt.figure(figsize=(8, 5))
plt.scatter(b, c, color='pink', label='Data Points')
plt.plot(b, y_pred, color='red', label=f'Regression Line\ny = {slope:.2f}x + {intercept:.2f}')

plt.text(min(b), max(c), f'r = {r_value:.2f}', fontsize=12, color='blue')

plt.title('Scatter Plot with Regression Line')
plt.xlabel('Points Per Game PPG')
plt.ylabel('Field Goal Percentage FG%')
plt.grid(True)
plt.legend()
plt.show()

#corr2
corr_matrix = np.corrcoef(b, d)
correlation = corr_matrix[0, 1]
print()
print(col_cat[x], col_title[x], "vs", col_cat[y], col_title[y])
print("Correlation coefficient (Pearson r):", correlation)
x += 1

#plot for corr2
slope, intercept, r_value, p_value, std_err = stats.linregress(b, d)

y_pred = slope * b + intercept

plt.figure(figsize=(8, 5))
plt.scatter(b, d, color='pink', label='Data Points')
plt.plot(b, y_pred, color='red', label=f'Regression Line\ny = {slope:.2f}x + {intercept:.2f}')

plt.text(min(b), max(d), f'r = {r_value:.2f}', fontsize=12, color='blue')

plt.title('Scatter Plot with Regression Line')
plt.xlabel('Points Per Game PPG')
plt.ylabel('Free Throw Percentage FT%')
plt.grid(True)
plt.legend()
plt.show()

#corr3
corr_matrix = np.corrcoef(c, d)
correlation = corr_matrix[0, 1]
print()
print(col_cat[x], col_title[x], "vs", col_cat[y], col_title[y])
print("Correlation coefficient (Pearson r):", correlation)

#plot for corr3
slope, intercept, r_value, p_value, std_err = stats.linregress(c, d)

y_pred = slope * c + intercept

plt.figure(figsize=(8, 5))
plt.scatter(c, d, color='pink', label='Data Points')
plt.plot(c, y_pred, color='red', label=f'Regression Line\ny = {slope:.2f}x + {intercept:.2f}')

plt.text(min(b), max(c), f'r = {r_value:.2f}', fontsize=12, color='blue')

plt.title('Scatter Plot with Regression Line')
plt.xlabel('Field Goal Percentage FG%')
plt.ylabel('Free Throw Percentage FT%')
plt.grid(True)
plt.legend()
plt.show()
1/240:
#correlation and other visualizations
x = 1
y = 2

#corr1
corr_matrix = np.corrcoef(b, c)
correlation = corr_matrix[0, 1]
print(col_cat[x], col_title[x], "vs", col_cat[y], col_title[y])
print(f"Correlation coefficient (Pearson r): {r_value:.4f}", correlation)
y += 1

#plot for corr1
slope, intercept, r_value, p_value, std_err = stats.linregress(b, c)

y_pred = slope * b + intercept

plt.figure(figsize=(8, 5))
plt.scatter(b, c, color='pink', label='Data Points')
plt.plot(b, y_pred, color='red', label=f'Regression Line\ny = {slope:.2f}x + {intercept:.2f}')

plt.text(min(b), max(c), f'r = {r_value:.2f}', fontsize=12, color='blue')

plt.title('Scatter Plot with Regression Line')
plt.xlabel('Points Per Game PPG')
plt.ylabel('Field Goal Percentage FG%')
plt.grid(True)
plt.legend()
plt.show()

#corr2
corr_matrix = np.corrcoef(b, d)
correlation = corr_matrix[0, 1]
print()
print(col_cat[x], col_title[x], "vs", col_cat[y], col_title[y])
print("Correlation coefficient (Pearson r):", correlation)
x += 1

#plot for corr2
slope, intercept, r_value, p_value, std_err = stats.linregress(b, d)

y_pred = slope * b + intercept

plt.figure(figsize=(8, 5))
plt.scatter(b, d, color='pink', label='Data Points')
plt.plot(b, y_pred, color='red', label=f'Regression Line\ny = {slope:.2f}x + {intercept:.2f}')

plt.text(min(b), max(d), f'r = {r_value:.2f}', fontsize=12, color='blue')

plt.title('Scatter Plot with Regression Line')
plt.xlabel('Points Per Game PPG')
plt.ylabel('Free Throw Percentage FT%')
plt.grid(True)
plt.legend()
plt.show()

#corr3
corr_matrix = np.corrcoef(c, d)
correlation = corr_matrix[0, 1]
print()
print(col_cat[x], col_title[x], "vs", col_cat[y], col_title[y])
print("Correlation coefficient (Pearson r):", correlation)

#plot for corr3
slope, intercept, r_value, p_value, std_err = stats.linregress(c, d)

y_pred = slope * c + intercept

plt.figure(figsize=(8, 5))
plt.scatter(c, d, color='pink', label='Data Points')
plt.plot(c, y_pred, color='red', label=f'Regression Line\ny = {slope:.2f}x + {intercept:.2f}')

plt.text(min(c), max(d), f'r = {r_value:.2f}', fontsize=12, color='blue')

plt.title('Scatter Plot with Regression Line')
plt.xlabel('Field Goal Percentage FG%')
plt.ylabel('Free Throw Percentage FT%')
plt.grid(True)
plt.legend()
plt.show()
1/241:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

#DATA SET
df = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

a = df['Name'].to_numpy()
b = df['PPG'].to_numpy()
c = df['FG%'].to_numpy()
d = df['FT%'].to_numpy()


#INITIALS
col_title = df.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']

#OUTPUTS
print("TOP 200 SCORERS DATA IN THE NATIONAL BASKETBALL ASSOCIATION (NBA)\n")

print("Data set columns:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    
#proof of clean data set
print("\nOriginal Data Shape:", df.shape)
print("Missing Values:") 
print(df.isnull().sum())
print("\nTop 5 scorers:\n", df.head())
1/242:
#numpy operations

sumppg = np.sum(b)
maxppg = np.max(b)
minppg = np.min(b)
meanfg = np.mean(c)
medianfg = np.median(c)
perfg = np.percentile(c, [90, 95, 99])
stdft = np.std(d)
varft = np.var(d)
rangeft = np.ptp(d)

print("\nPPG Statistics:")
print(f"Sum of PPG: {sumppg:.1f}")
print(f"Maximum of PPG: {maxppg:.1f}")
print(f"Minimum of PPG: {minppg:.1f}")

print("\nFG% Statistics:")
print(f"Mean of FG%: {meanfg:.1f}")
print(f"Median of FG%: {medianfg:.1f}")
print(f"90th, 95th, and 99th Percentile of FG%: {perfg}")

print("\nFT% Statistics:")
print(f"Standard Deviation of FT%: {stdft:.1f}")
print(f"Variance of FT%: {varft:.1f}")
print(f"Range of FT%: {rangeft:.1f}")
1/243:
#scipy operations

#sampling the data set into 4 arrays (samples) with 5 values each
arr1 = np.array([])
arr2 = np.array([])
arr3 = np.array([])
arr4 = np.array([])
for i in range(20):
    if i < 5:
        arr1 = np.append(arr1, b[i])

    if i < 10 and i > 4:
        arr2 = np.append(arr2, b[i])

    if i < 15 and i > 9:
        arr3 = np.append(arr3, b[i])

    if i < 20 and i > 14:
        arr4 = np.append(arr4, b[i])

print("Array 1", arr1,"\nArray 2", arr2, "\nArray 3",arr3, "\nArray 4",arr4)

#one-way anova
f_statistic, p_value = stats.f_oneway(arr1, arr2, arr3, arr4)
print(f"\nOne-Way Anova \n\nF-statistic: {f_statistic:.4f}, P-value: {p_value:.8f}")

#plot
data = [arr1, arr2, arr3, arr4]
labels = ['Array 1', 'Array 2', 'Array 3', 'Array 4']

plt.figure(figsize=(8, 5))
plt.boxplot(data, tick_labels=labels)
plt.title('One-Way ANOVA: Array Comparisons')
plt.ylabel('Scores')
plt.grid(True)
plt.show()

#standard normal
zval = stats.zscore(arr1)
print(f"\nZ-Distribution\n\nZ-score for first 5 values:")
for i in range(5):
    print(zval[i], end=' ')

#plot
z_range = np.linspace(-3, 3, 50)
pdf = stats.norm.pdf(z_range)

plt.figure(figsize=(10, 4))
plt.plot(z_range, pdf, color='gray', linestyle='-', label='Standard Normal PDF')

plt.hist(zval, bins=20, density=True, alpha=0.5, label='Z-scores', color='blue')

plt.axvline(0, color='black', linestyle='-', linewidth=3)
plt.title('Z-Score Distribution of Array 1')
plt.xlabel('Z-score')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()

#t-test
t_stat, p_value = stats.ttest_ind(arr3, arr4)
print(f"T - Test\n\nT-test between Array 3 and Array 4: \nt = {t_stat:.2f} \np = {p_value:.3f}")

#plot
plt.figure(figsize=(8, 5))
plt.boxplot([arr3, arr4], tick_labels=['Array 3', 'Array 4'])
plt.title('T-Test: Array 3 & Array 4 Comparison')
plt.ylabel('Values')
plt.grid(True)

plt.text(1.5, max(max(arr3), max(arr4)), f'p = {p_value:.4f}', 
         ha='center', va='bottom', fontsize=12, color='blue')

plt.show()
1/244:
#Statsmodels

x = sm.add_constant(df['FG%'])
model = sm.OLS(df['PPG'], x).fit()
print("\nLinear Regression Summary:")
print(model.summary())
1/245:
#correlation and other visualizations
x = 1
y = 2

#corr1
corr_matrix = np.corrcoef(b, c)
correlation = corr_matrix[0, 1]
print(col_cat[x], col_title[x], "vs", col_cat[y], col_title[y])
print(f"Correlation coefficient (Pearson r): {r_value:.4f}", correlation)
y += 1

#plot for corr1
slope, intercept, r_value, p_value, std_err = stats.linregress(b, c)

y_pred = slope * b + intercept

plt.figure(figsize=(8, 5))
plt.scatter(b, c, color='pink', label='Data Points')
plt.plot(b, y_pred, color='red', label=f'Regression Line\ny = {slope:.2f}x + {intercept:.2f}')

plt.text(min(b), max(c), f'r = {r_value:.2f}', fontsize=12, color='blue')

plt.title('Scatter Plot with Regression Line')
plt.xlabel('Points Per Game PPG')
plt.ylabel('Field Goal Percentage FG%')
plt.grid(True)
plt.legend()
plt.show()

#corr2
corr_matrix = np.corrcoef(b, d)
correlation = corr_matrix[0, 1]
print()
print(col_cat[x], col_title[x], "vs", col_cat[y], col_title[y])
print("Correlation coefficient (Pearson r):", correlation)
x += 1

#plot for corr2
slope, intercept, r_value, p_value, std_err = stats.linregress(b, d)

y_pred = slope * b + intercept

plt.figure(figsize=(8, 5))
plt.scatter(b, d, color='pink', label='Data Points')
plt.plot(b, y_pred, color='red', label=f'Regression Line\ny = {slope:.2f}x + {intercept:.2f}')

plt.text(min(b), max(d), f'r = {r_value:.2f}', fontsize=12, color='blue')

plt.title('Scatter Plot with Regression Line')
plt.xlabel('Points Per Game PPG')
plt.ylabel('Free Throw Percentage FT%')
plt.grid(True)
plt.legend()
plt.show()

#corr3
corr_matrix = np.corrcoef(c, d)
correlation = corr_matrix[0, 1]
print()
print(col_cat[x], col_title[x], "vs", col_cat[y], col_title[y])
print("Correlation coefficient (Pearson r):", correlation)

#plot for corr3
slope, intercept, r_value, p_value, std_err = stats.linregress(c, d)

y_pred = slope * c + intercept

plt.figure(figsize=(8, 5))
plt.scatter(c, d, color='pink', label='Data Points')
plt.plot(c, y_pred, color='red', label=f'Regression Line\ny = {slope:.2f}x + {intercept:.2f}')

plt.text(min(c), max(d), f'r = {r_value:.2f}', fontsize=12, color='blue')

plt.title('Scatter Plot with Regression Line')
plt.xlabel('Field Goal Percentage FG%')
plt.ylabel('Free Throw Percentage FT%')
plt.grid(True)
plt.legend()
plt.show()
1/246:
ds = pd.DataFrame({'X': b, 'Y': c})

# Create scatterplot with regression line
plt.figure(figsize=(8, 5))
sns.regplot(x='Points Per Game PPG', y='Field Goal Percentage FG%', data=ds, color='blue', marker='o', ci=95)

plt.title('Seaborn Scatterplot with Regression Line')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.grid(True)
plt.show()
1/247:
ds = pd.DataFrame({'X': b, 'Y': c})

# Create scatterplot with regression line
plt.figure(figsize=(8, 5))
sns.regplot(x='X', y='Y', data=ds, color='blue', marker='o', ci=95)

plt.title('Seaborn Scatterplot with Regression Line')
plt.xlabel('Points Per Game PPG')
plt.ylabel('Field Goal Percentage FG%')
plt.grid(True)
plt.show()
1/248:
ds = pd.DataFrame({'X': b, 'Y': c})

# Create scatterplot with regression line
plt.figure(figsize=(8, 5))
sns.regplot(x='X', y='Y', data=ds, color='blue', marker='o',  line_kws={'color': 'red', 'linewidth': 2})

plt.title('Seaborn Scatterplot with Regression Line')
plt.xlabel('Points Per Game PPG')
plt.ylabel('Field Goal Percentage FG%')
plt.grid(True)
plt.show()
1/249:
ds = pd.DataFrame({'X': b, 'Y': c})

# Create scatterplot with regression line
plt.figure(figsize=(8, 5))
sns.regplot(x='X', y='Y', data=ds, color='blue', marker='o', ci = 95, line_kws={'color': 'red', 'linewidth': 2})

plt.title('Seaborn Scatterplot with Regression Line')
plt.xlabel('Points Per Game PPG')
plt.ylabel('Field Goal Percentage FG%')
plt.grid(True)
plt.show()
1/250:
#correlation and other visualizations
x = 1
y = 2

#corr1
corr_matrix = np.corrcoef(b, c)
correlation = corr_matrix[0, 1]
print(col_cat[x], col_title[x], "vs", col_cat[y], col_title[y])
print(f"Correlation coefficient (Pearson r): {r_value:.4f}", correlation)
y += 1

#plot for corr1
ds = pd.DataFrame({'X': b, 'Y': c})

plt.figure(figsize=(8, 5))
sns.regplot(x='X', y='Y', data=ds, color='blue', marker='o', ci = 95, line_kws={'color': 'red', 'linewidth': 2})

plt.title('Seaborn Scatterplot with Regression Line')
plt.xlabel('Points Per Game PPG')
plt.ylabel('Field Goal Percentage FG%')
plt.grid(True)
plt.show()

#corr2
corr_matrix = np.corrcoef(b, d)
correlation = corr_matrix[0, 1]
print()
print(col_cat[x], col_title[x], "vs", col_cat[y], col_title[y])
print("Correlation coefficient (Pearson r):", correlation)
x += 1

#plot for corr2
ds = pd.DataFrame({'X': b, 'Y': d})

plt.figure(figsize=(8, 5))
sns.regplot(x='X', y='Y', data=ds, color='blue', marker='o', ci = 95, line_kws={'color': 'red', 'linewidth': 2})

plt.title('Seaborn Scatterplot with Regression Line')
plt.xlabel('Points Per Game PPG')
plt.ylabel('Field Goal Percentage FG%')
plt.grid(True)
plt.show()

#corr3
corr_matrix = np.corrcoef(c, d)
correlation = corr_matrix[0, 1]
print()
print(col_cat[x], col_title[x], "vs", col_cat[y], col_title[y])
print("Correlation coefficient (Pearson r):", correlation)

#plot for corr3
ds = pd.DataFrame({'X': c, 'Y': d})

plt.figure(figsize=(8, 5))
sns.regplot(x='X', y='Y', data=ds, color='blue', marker='o', ci = 95, line_kws={'color': 'red', 'linewidth': 2})

plt.title('Seaborn Scatterplot with Regression Line')
plt.xlabel('Points Per Game PPG')
plt.ylabel('Field Goal Percentage FG%')
plt.grid(True)
plt.show()
1/251:
#correlation and other visualizations
x = 1
y = 2

#corr1
corr_matrix = np.corrcoef(b, c)
correlation = corr_matrix[0, 1]
print(col_cat[x], col_title[x], "vs", col_cat[y], col_title[y])
print(f"Correlation coefficient (Pearson r): {r_value:.4f}", correlation)
y += 1

#plot for corr1
slope, intercept, r_value, p_value, std_err = stats.linregress(b, c)
equation = f'y = {slope:.2f}x + {intercept:.2f}'

ds = pd.DataFrame({'X': b, 'Y': c})

plt.figure(figsize=(8, 5))
sns.regplot(x='X', y='Y', data=ds, color='blue', marker='o', ci = 95, line_kws={'color': 'red', 'linewidth': 2})

plt.text(min(b), max(c), equation, fontsize=12, color='red', ha='left')
plt.title('Seaborn Scatterplot with Regression Line')
plt.xlabel('Points Per Game PPG')
plt.ylabel('Field Goal Percentage FG%')
plt.grid(True)
plt.show()

#corr2
corr_matrix = np.corrcoef(b, d)
correlation = corr_matrix[0, 1]
print()
print(col_cat[x], col_title[x], "vs", col_cat[y], col_title[y])
print("Correlation coefficient (Pearson r):", correlation)
x += 1

#plot for corr2
ds = pd.DataFrame({'X': b, 'Y': d})

plt.figure(figsize=(8, 5))
sns.regplot(x='X', y='Y', data=ds, color='blue', marker='o', ci = 95, line_kws={'color': 'red', 'linewidth': 2})

plt.title('Seaborn Scatterplot with Regression Line')
plt.xlabel('Points Per Game PPG')
plt.ylabel('Field Goal Percentage FG%')
plt.grid(True)
plt.show()

#corr3
corr_matrix = np.corrcoef(c, d)
correlation = corr_matrix[0, 1]
print()
print(col_cat[x], col_title[x], "vs", col_cat[y], col_title[y])
print("Correlation coefficient (Pearson r):", correlation)

#plot for corr3
ds = pd.DataFrame({'X': c, 'Y': d})

plt.figure(figsize=(8, 5))
sns.regplot(x='X', y='Y', data=ds, color='blue', marker='o', ci = 95, line_kws={'color': 'red', 'linewidth': 2})

plt.title('Seaborn Scatterplot with Regression Line')
plt.xlabel('Points Per Game PPG')
plt.ylabel('Field Goal Percentage FG%')
plt.grid(True)
plt.show()
1/252:
#correlation and other visualizations
x = 1
y = 2

#corr1
corr_matrix = np.corrcoef(b, c)
correlation = corr_matrix[0, 1]
print(col_cat[x], col_title[x], "vs", col_cat[y], col_title[y])
print(f"Correlation coefficient (Pearson r): {r_value:.4f}", correlation)
y += 1

#plot for corr1
ds = pd.DataFrame({'X': b, 'Y': c})

plt.figure(figsize=(8, 5))
sns.regplot(x='X', y='Y', data=ds, color='blue', marker='o', ci = 95, line_kws={'color': 'red', 'linewidth': 2})

plt.title('Seaborn Scatterplot with Regression Line')
plt.xlabel('Points Per Game PPG')
plt.ylabel('Field Goal Percentage FG%')
plt.grid(True)
plt.show()

#corr2
corr_matrix = np.corrcoef(b, d)
correlation = corr_matrix[0, 1]
print()
print(col_cat[x], col_title[x], "vs", col_cat[y], col_title[y])
print("Correlation coefficient (Pearson r):", correlation)
x += 1

#plot for corr2
ds = pd.DataFrame({'X': b, 'Y': d})

plt.figure(figsize=(8, 5))
sns.regplot(x='X', y='Y', data=ds, color='blue', marker='o', ci = 95, line_kws={'color': 'red', 'linewidth': 2})

plt.title('Seaborn Scatterplot with Regression Line')
plt.xlabel('Points Per Game PPG')
plt.ylabel('Field Goal Percentage FG%')
plt.grid(True)
plt.show()

#corr3
corr_matrix = np.corrcoef(c, d)
correlation = corr_matrix[0, 1]
print()
print(col_cat[x], col_title[x], "vs", col_cat[y], col_title[y])
print("Correlation coefficient (Pearson r):", correlation)

#plot for corr3
ds = pd.DataFrame({'X': c, 'Y': d})

plt.figure(figsize=(8, 5))
sns.regplot(x='X', y='Y', data=ds, color='blue', marker='o', ci = 95, line_kws={'color': 'red', 'linewidth': 2})

plt.title('Seaborn Scatterplot with Regression Line')
plt.xlabel('Points Per Game PPG')
plt.ylabel('Field Goal Percentage FG%')
plt.grid(True)
plt.show()
1/253:
#correlation and other visualizations
x = 1
y = 2

#corr1
corr_matrix = np.corrcoef(b, c)
correlation = corr_matrix[0, 1]
print(col_cat[x], col_title[x], "vs", col_cat[y], col_title[y])
print("Correlation coefficient (Pearson r):", correlation)
y += 1

#plot for corr1
ds = pd.DataFrame({'X': b, 'Y': c})

plt.figure(figsize=(8, 5))
sns.regplot(x='X', y='Y', data=ds, color='blue', marker='o', ci = 95, line_kws={'color': 'red', 'linewidth': 2})

plt.title('Seaborn Scatterplot with Regression Line')
plt.xlabel('Points Per Game PPG')
plt.ylabel('Field Goal Percentage FG%')
plt.grid(True)
plt.show()

#corr2
corr_matrix = np.corrcoef(b, d)
correlation = corr_matrix[0, 1]
print()
print(col_cat[x], col_title[x], "vs", col_cat[y], col_title[y])
print("Correlation coefficient (Pearson r):", correlation)
x += 1

#plot for corr2
ds = pd.DataFrame({'X': b, 'Y': d})

plt.figure(figsize=(8, 5))
sns.regplot(x='X', y='Y', data=ds, color='blue', marker='o', ci = 95, line_kws={'color': 'red', 'linewidth': 2})

plt.title('Seaborn Scatterplot with Regression Line')
plt.xlabel('Points Per Game PPG')
plt.ylabel('Field Goal Percentage FG%')
plt.grid(True)
plt.show()

#corr3
corr_matrix = np.corrcoef(c, d)
correlation = corr_matrix[0, 1]
print()
print(col_cat[x], col_title[x], "vs", col_cat[y], col_title[y])
print("Correlation coefficient (Pearson r):", correlation)

#plot for corr3
ds = pd.DataFrame({'X': c, 'Y': d})

plt.figure(figsize=(8, 5))
sns.regplot(x='X', y='Y', data=ds, color='blue', marker='o', ci = 95, line_kws={'color': 'red', 'linewidth': 2})

plt.title('Seaborn Scatterplot with Regression Line')
plt.xlabel('Points Per Game PPG')
plt.ylabel('Field Goal Percentage FG%')
plt.grid(True)
plt.show()
1/254:
#scipy operations

#sampling the data set into 4 arrays (samples) with 5 values each
arr1 = np.array([])
arr2 = np.array([])
arr3 = np.array([])
arr4 = np.array([])
for i in range(20):
    if i < 5:
        arr1 = np.append(arr1, b[i])

    if i < 10 and i > 4:
        arr2 = np.append(arr2, b[i])

    if i < 15 and i > 9:
        arr3 = np.append(arr3, b[i])

    if i < 20 and i > 14:
        arr4 = np.append(arr4, b[i])

print("Array 1", arr1,"\nArray 2", arr2, "\nArray 3",arr3, "\nArray 4",arr4)

#one-way anova
f_statistic, p_value = stats.f_oneway(arr1, arr2, arr3, arr4)
print(f"\nOne-Way Anova \n\nF-statistic: {f_statistic:.4f}, P-value: {p_value:.8f}")

#plot
data = [arr1, arr2, arr3, arr4]
labels = ['Array 1', 'Array 2', 'Array 3', 'Array 4']

plt.figure(figsize=(8, 5))
plt.boxplot(data, tick_labels=labels)
plt.title('One-Way ANOVA: Array Comparisons')
plt.ylabel('Scores')
plt.grid(True)
plt.show()

#standard normal
zval = stats.zscore(arr1)
print(f"\nZ-Distribution\n\nZ-score for first 5 values:")
for i in range(5):
    print(zval[i], end=' ')

#plot
z_range = np.linspace(-3, 3, 50)
pdf = stats.norm.pdf(z_range)

plt.figure(figsize=(10, 4))
plt.plot(z_range, pdf, color='gray', linestyle='-', label='Standard Normal PDF')

plt.hist(zval, bins=20, density=True, alpha=0.5, label='Z-scores', color='blue')

plt.axvline(0, color='black', linestyle='-', linewidth=3)
plt.title('Z-Score Distribution of Array 1')
plt.xlabel('Z-score')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()

#t-test
t_stat, p_value = stats.ttest_ind(arr3, arr4)
print(f"T - Test\n\nT-test between Array 3 and Array 4: \nt = {t_stat:.2f} \np = {p_value:.3f}")

#plot
plt.figure(figsize=(8, 5))
plt.boxplot([arr3, arr4], tick_labels=['Array 3', 'Array 4'])
plt.title('T-Test: Array 3 & Array 4 Comparison')
plt.ylabel('Values')
plt.grid(True)
plt.show()
1/255: #seaborn
1/256:
#seaborn

dx = pd.DataFrame({
    'A': b,
    'B': c,
    'C': d
})

# Compute correlation matrix
corr = df.corr()

# Plot heatmap
plt.figure(figsize=(6, 5))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', square=True)

plt.title('Correlation Heatmap of 3 Arrays')
plt.show()
1/257:
#seaborn

dx = pd.DataFrame({
    'A': b,
    'B': c,
    'C': d
})

# Compute correlation matrix
corr = dx.corr()

# Plot heatmap
plt.figure(figsize=(6, 5))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', square=True)

plt.title('Correlation Heatmap of 3 Arrays')
plt.show()
1/258:
#seaborn

dx = pd.DataFrame({
    'PPG': b,
    'FG%': c,
    'FT%': d
})

# Compute correlation matrix
corr = dx.corr()

# Plot heatmap
plt.figure(figsize=(6, 5))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', square=True)

plt.title('Correlation Heatmap of 3 Arrays')
plt.show()
1/259:
#seaborn

dx = pd.DataFrame({
    'PPG': b,
    'FG%': c,
    'FT%': d
})

# Compute correlation matrix
corr = dx.corr()

# Plot heatmap
plt.figure(figsize=(6, 5))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', square=True)

plt.title('Correlation Heatmap')
plt.show()
1/260:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

#DATA SET
df = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

a = df['Name'].to_numpy()
b = df['PPG'].to_numpy()
c = df['FG%'].to_numpy()
d = df['FT%'].to_numpy()


#INITIALS
col_title = df.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']

#OUTPUTS
print("TOP 200 SCORERS DATA IN THE NATIONAL BASKETBALL ASSOCIATION (NBA)\n")

print("Data set columns:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    
#proof of clean data set
print("\nOriginal Data Shape:", df.shape)
print("Missing Values:") 
print(df.isnull().sum())
print("\nTop 5 scorers:\n", df.head())
1/261:
#numpy operations

sumppg = np.sum(b)
maxppg = np.max(b)
minppg = np.min(b)
meanfg = np.mean(c)
medianfg = np.median(c)
perfg = np.percentile(c, [90, 95, 99])
stdft = np.std(d)
varft = np.var(d)
rangeft = np.ptp(d)

print("\nPPG Statistics:")
print(f"Sum of PPG: {sumppg:.1f}")
print(f"Maximum of PPG: {maxppg:.1f}")
print(f"Minimum of PPG: {minppg:.1f}")

print("\nFG% Statistics:")
print(f"Mean of FG%: {meanfg:.1f}")
print(f"Median of FG%: {medianfg:.1f}")
print(f"90th, 95th, and 99th Percentile of FG%: {perfg}")

print("\nFT% Statistics:")
print(f"Standard Deviation of FT%: {stdft:.1f}")
print(f"Variance of FT%: {varft:.1f}")
print(f"Range of FT%: {rangeft:.1f}")
1/262:
#scipy operations

#sampling the data set into 4 arrays (samples) with 5 values each
arr1 = np.array([])
arr2 = np.array([])
arr3 = np.array([])
arr4 = np.array([])
for i in range(20):
    if i < 5:
        arr1 = np.append(arr1, b[i])

    if i < 10 and i > 4:
        arr2 = np.append(arr2, b[i])

    if i < 15 and i > 9:
        arr3 = np.append(arr3, b[i])

    if i < 20 and i > 14:
        arr4 = np.append(arr4, b[i])

print("Array 1", arr1,"\nArray 2", arr2, "\nArray 3",arr3, "\nArray 4",arr4)

#one-way anova
f_statistic, p_value = stats.f_oneway(arr1, arr2, arr3, arr4)
print(f"\nOne-Way Anova \n\nF-statistic: {f_statistic:.4f}, P-value: {p_value:.8f}")

#plot
data = [arr1, arr2, arr3, arr4]
labels = ['Array 1', 'Array 2', 'Array 3', 'Array 4']

plt.figure(figsize=(8, 5))
plt.boxplot(data, tick_labels=labels)
plt.title('One-Way ANOVA: Array Comparisons')
plt.ylabel('Scores')
plt.grid(True)
plt.show()

#standard normal
zval = stats.zscore(arr1)
print(f"\nZ-Distribution\n\nZ-score for first 5 values:")
for i in range(5):
    print(zval[i], end=' ')

#plot
z_range = np.linspace(-3, 3, 50)
pdf = stats.norm.pdf(z_range)

plt.figure(figsize=(10, 4))
plt.plot(z_range, pdf, color='gray', linestyle='-', label='Standard Normal PDF')

plt.hist(zval, bins=20, density=True, alpha=0.5, label='Z-scores', color='blue')

plt.axvline(0, color='black', linestyle='-', linewidth=3)
plt.title('Z-Score Distribution of Array 1')
plt.xlabel('Z-score')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()

#t-test
t_stat, p_value = stats.ttest_ind(arr3, arr4)
print(f"T - Test\n\nT-test between Array 3 and Array 4: \nt = {t_stat:.2f} \np = {p_value:.3f}")

#plot
plt.figure(figsize=(8, 5))
plt.boxplot([arr3, arr4], tick_labels=['Array 3', 'Array 4'])
plt.title('T-Test: Array 3 & Array 4 Comparison')
plt.ylabel('Values')
plt.grid(True)
plt.show()
1/263:
#Statsmodels

x = sm.add_constant(df['FG%'])
model = sm.OLS(df['PPG'], x).fit()
print("\nLinear Regression Summary:")
print(model.summary())
1/264:
#correlation with visualizations
x = 1
y = 2

#corr1
corr_matrix = np.corrcoef(b, c)
correlation = corr_matrix[0, 1]
print(col_cat[x], col_title[x], "vs", col_cat[y], col_title[y])
print("Correlation coefficient (Pearson r):", correlation)
y += 1

#plot for corr1
ds = pd.DataFrame({'X': b, 'Y': c})

plt.figure(figsize=(8, 5))
sns.regplot(x='X', y='Y', data=ds, color='blue', marker='o', ci = 95, line_kws={'color': 'red', 'linewidth': 2})

plt.title('Seaborn Scatterplot with Regression Line')
plt.xlabel('Points Per Game PPG')
plt.ylabel('Field Goal Percentage FG%')
plt.grid(True)
plt.show()

#corr2
corr_matrix = np.corrcoef(b, d)
correlation = corr_matrix[0, 1]
print()
print(col_cat[x], col_title[x], "vs", col_cat[y], col_title[y])
print("Correlation coefficient (Pearson r):", correlation)
x += 1

#plot for corr2
ds = pd.DataFrame({'X': b, 'Y': d})

plt.figure(figsize=(8, 5))
sns.regplot(x='X', y='Y', data=ds, color='blue', marker='o', ci = 95, line_kws={'color': 'red', 'linewidth': 2})

plt.title('Seaborn Scatterplot with Regression Line')
plt.xlabel('Points Per Game PPG')
plt.ylabel('Field Goal Percentage FG%')
plt.grid(True)
plt.show()

#corr3
corr_matrix = np.corrcoef(c, d)
correlation = corr_matrix[0, 1]
print()
print(col_cat[x], col_title[x], "vs", col_cat[y], col_title[y])
print("Correlation coefficient (Pearson r):", correlation)

#plot for corr3
ds = pd.DataFrame({'X': c, 'Y': d})

plt.figure(figsize=(8, 5))
sns.regplot(x='X', y='Y', data=ds, color='blue', marker='o', ci = 95, line_kws={'color': 'red', 'linewidth': 2})

plt.title('Seaborn Scatterplot with Regression Line')
plt.xlabel('Points Per Game PPG')
plt.ylabel('Field Goal Percentage FG%')
plt.grid(True)
plt.show()
1/265:
#seaborn

dx = pd.DataFrame({
    'PPG': b,
    'FG%': c,
    'FT%': d
})

# Compute correlation matrix
corr = dx.corr()

# Plot heatmap
plt.figure(figsize=(6, 5))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', square=True)

plt.title('Correlation Heatmap')
plt.show()
1/266:
#seaborn

dx = pd.DataFrame({'PPG': b, 'FG%': c, 'FT%': d})
corr = dx.corr()

plt.figure(figsize=(6, 5))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', square=True)
plt.title('Correlation Heatmap')
plt.show()
   1: %history -g -f filename
   2: %history -g -f filename
   3: %history -g -f revision_history
   4: %history -g -f revision_history
   5: %history -g -f revision_history.py
   6: %history -g -f revision_history.py
   7: %history -g -f revision_history.ipynb
   8: %history -g -f revision_history.ipynb
   9: %history -g -f ranjorevision_history
  10: %history -g -f ranjorevision_history.py
  11: %history -g -f ranjorevision_history.py
  12: %history -g -f ranjorevision_history.py
  13: %history -g -f ranjorev_history.py
  14: %history -g -f ranjorev_history.py
  15: %history -g -f ranjorev_history.py
  16: %history -n 1-513
  17:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

#DATA SET
df = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

a = df['Name'].to_numpy()
b = df['PPG'].to_numpy()
c = df['FG%'].to_numpy()
d = df['FT%'].to_numpy()


#INITIALS
col_title = df.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']

#OUTPUTS
print("TOP 200 SCORERS DATA IN THE NATIONAL BASKETBALL ASSOCIATION (NBA)\n")

print("Data set columns:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    
#proof of clean data set
print("\nOriginal Data Shape:", df.shape)
print("Missing Values:") 
print(df.isnull().sum())
print("\nTop 5 scorers:\n", df.head())
  18:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

#DATA SET
df = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

a = df['Name'].to_numpy()
b = df['PPG'].to_numpy()
c = df['FG%'].to_numpy()
d = df['FT%'].to_numpy()


#INITIALS
col_title = df.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']

#OUTPUTS
print("TOP 200 SCORERS DATA IN THE NATIONAL BASKETBALL ASSOCIATION (NBA)\n")

print("Data set columns:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    
#proof of clean data set
print("\nOriginal Data Shape:", df.shape)
print("Missing Values:") 
print(df.isnull().sum())
print("\nTop 5 scorers:\n", df.head())
  19:
#numpy operations

sumppg = np.sum(b)
maxppg = np.max(b)
minppg = np.min(b)
meanfg = np.mean(c)
medianfg = np.median(c)
perfg = np.percentile(c, [90, 95, 99])
stdft = np.std(d)
varft = np.var(d)
rangeft = np.ptp(d)

print("\nPPG Statistics:")
print(f"Sum of PPG: {sumppg:.1f}")
print(f"Maximum of PPG: {maxppg:.1f}")
print(f"Minimum of PPG: {minppg:.1f}")

print("\nFG% Statistics:")
print(f"Mean of FG%: {meanfg:.1f}")
print(f"Median of FG%: {medianfg:.1f}")
print(f"90th, 95th, and 99th Percentile of FG%: {perfg}")

print("\nFT% Statistics:")
print(f"Standard Deviation of FT%: {stdft:.1f}")
print(f"Variance of FT%: {varft:.1f}")
print(f"Range of FT%: {rangeft:.1f}")
  20:
#scipy operations

#sampling the data set into 4 arrays (samples) with 5 values each
arr1 = np.array([])
arr2 = np.array([])
arr3 = np.array([])
arr4 = np.array([])
for i in range(20):
    if i < 5:
        arr1 = np.append(arr1, b[i])

    if i < 10 and i > 4:
        arr2 = np.append(arr2, b[i])

    if i < 15 and i > 9:
        arr3 = np.append(arr3, b[i])

    if i < 20 and i > 14:
        arr4 = np.append(arr4, b[i])

print("Array 1", arr1,"\nArray 2", arr2, "\nArray 3",arr3, "\nArray 4",arr4)

#one-way anova
f_statistic, p_value = stats.f_oneway(arr1, arr2, arr3, arr4)
print(f"\nOne-Way Anova \n\nF-statistic: {f_statistic:.4f}, P-value: {p_value:.8f}")

#plot
data = [arr1, arr2, arr3, arr4]
labels = ['Array 1', 'Array 2', 'Array 3', 'Array 4']

plt.figure(figsize=(8, 5))
plt.boxplot(data, tick_labels=labels)
plt.title('One-Way ANOVA: Array Comparisons')
plt.ylabel('Scores')
plt.grid(True)
plt.show()

#standard normal
zval = stats.zscore(arr1)
print(f"\nZ-Distribution\n\nZ-score for first 5 values:")
for i in range(5):
    print(zval[i], end=' ')

#plot
z_range = np.linspace(-3, 3, 50)
pdf = stats.norm.pdf(z_range)

plt.figure(figsize=(10, 4))
plt.plot(z_range, pdf, color='gray', linestyle='-', label='Standard Normal PDF')

plt.hist(zval, bins=20, density=True, alpha=0.5, label='Z-scores', color='blue')

plt.axvline(0, color='black', linestyle='-', linewidth=3)
plt.title('Z-Score Distribution of Array 1')
plt.xlabel('Z-score')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()

#t-test
t_stat, p_value = stats.ttest_ind(arr3, arr4)
print(f"T - Test\n\nT-test between Array 3 and Array 4: \nt = {t_stat:.2f} \np = {p_value:.3f}")

#plot
plt.figure(figsize=(8, 5))
plt.boxplot([arr3, arr4], tick_labels=['Array 3', 'Array 4'])
plt.title('T-Test: Array 3 & Array 4 Comparison')
plt.ylabel('Values')
plt.grid(True)
plt.show()
  21:
#scipy operations

#sampling the data set into 4 arrays (samples) with 5 values each
arr1 = np.array([])
arr2 = np.array([])
arr3 = np.array([])
arr4 = np.array([])
for i in range(20):
    if i < 5:
        arr1 = np.append(arr1, b[i])

    if i < 10 and i > 4:
        arr2 = np.append(arr2, b[i])

    if i < 15 and i > 9:
        arr3 = np.append(arr3, b[i])

    if i < 20 and i > 14:
        arr4 = np.append(arr4, b[i])

print("Array 1", arr1,"\nArray 2", arr2, "\nArray 3",arr3, "\nArray 4",arr4)

#one-way anova
f_statistic, p_value = stats.f_oneway(arr1, arr2, arr3, arr4)
print(f"\nOne-Way Anova \n\nF-statistic: {f_statistic:.4f}, P-value: {p_value:.8f}")

#plot
data = [arr1, arr2, arr3, arr4]
labels = ['Array 1', 'Array 2', 'Array 3', 'Array 4']

plt.figure(figsize=(8, 5))
plt.boxplot(data, tick_labels=labels)
plt.title('One-Way ANOVA: Array Comparisons')
plt.ylabel('Scores')
plt.grid(True)
plt.show()

#standard normal
zval = stats.zscore(arr1)
print(f"\nZ-Distribution\n\nZ-score for first 5 values:")
for i in range(5):
    print(zval[i], end=' ')

#plot
z_range = np.linspace(-3, 3, 50)
pdf = stats.norm.pdf(z_range)

plt.figure(figsize=(10, 4))
plt.plot(z_range, pdf, color='gray', linestyle='-', label='Standard Normal PDF')

plt.hist(zval, bins=20, density=True, alpha=0.5, label='Z-scores', color='blue')

plt.axvline(0, color='black', linestyle='-', linewidth=3)
plt.title('Z-Score Distribution of Array 1')
plt.xlabel('Z-score')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()

#t-test
t_stat, p_value = stats.ttest_ind(arr3, arr4)
print(f"T - Test\n\nT-test between Array 3 and Array 4: \nt = {t_stat:.2f} \np = {p_value:.3f}")

#plot
plt.figure(figsize=(8, 5))
plt.boxplot([arr3, arr4], tick_labels=['Array 3', 'Array 4'])
plt.title('T-Test: Array 3 & Array 4 Comparison')
plt.ylabel('Values')
plt.grid(True)
plt.show()
  22:
#Statsmodels

x = sm.add_constant(df['FG%'])
model = sm.OLS(df['PPG'], x).fit()
print("\nLinear Regression Summary:")
print(model.summary())
  23:
#correlation with visualizations
x = 1
y = 2

#corr1
corr_matrix = np.corrcoef(b, c)
correlation = corr_matrix[0, 1]
print(col_cat[x], col_title[x], "vs", col_cat[y], col_title[y])
print("Correlation coefficient (Pearson r):", correlation)
y += 1

#plot for corr1
ds = pd.DataFrame({'X': b, 'Y': c})

plt.figure(figsize=(8, 5))
sns.regplot(x='X', y='Y', data=ds, color='blue', marker='o', ci = 95, line_kws={'color': 'red', 'linewidth': 2})

plt.title('Seaborn Scatterplot with Regression Line')
plt.xlabel('Points Per Game PPG')
plt.ylabel('Field Goal Percentage FG%')
plt.grid(True)
plt.show()

#corr2
corr_matrix = np.corrcoef(b, d)
correlation = corr_matrix[0, 1]
print()
print(col_cat[x], col_title[x], "vs", col_cat[y], col_title[y])
print("Correlation coefficient (Pearson r):", correlation)
x += 1

#plot for corr2
ds = pd.DataFrame({'X': b, 'Y': d})

plt.figure(figsize=(8, 5))
sns.regplot(x='X', y='Y', data=ds, color='blue', marker='o', ci = 95, line_kws={'color': 'red', 'linewidth': 2})

plt.title('Seaborn Scatterplot with Regression Line')
plt.xlabel('Points Per Game PPG')
plt.ylabel('Field Goal Percentage FG%')
plt.grid(True)
plt.show()

#corr3
corr_matrix = np.corrcoef(c, d)
correlation = corr_matrix[0, 1]
print()
print(col_cat[x], col_title[x], "vs", col_cat[y], col_title[y])
print("Correlation coefficient (Pearson r):", correlation)

#plot for corr3
ds = pd.DataFrame({'X': c, 'Y': d})

plt.figure(figsize=(8, 5))
sns.regplot(x='X', y='Y', data=ds, color='blue', marker='o', ci = 95, line_kws={'color': 'red', 'linewidth': 2})

plt.title('Seaborn Scatterplot with Regression Line')
plt.xlabel('Points Per Game PPG')
plt.ylabel('Field Goal Percentage FG%')
plt.grid(True)
plt.show()
  24:
#seaborn

dx = pd.DataFrame({'PPG': b, 'FG%': c, 'FT%': d})
corr = dx.corr()

plt.figure(figsize=(6, 5))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', square=True)
plt.title('Correlation Heatmap')
plt.show()
  25: %history -n 1-513
 3/1:
#seaborn

dx = pd.DataFrame({'CRC': b, 'HSH': c, 'Height': d})
corr = dx.corr()

plt.figure(figsize=(6, 5))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', square=True)
plt.title('Correlation Heatmap')
plt.show()
 3/2:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

#DATA SET
df = pd.read_csv(r'C:\Users\hmcldryl\Desktop\cupsnheight.csv')

a = df['Person'].to_numpy()
b = df['Cups of Rice Consumed'].to_numpy()
c = df['Hours Spent on Homework'].to_numpy()
d = df['Height'].to_numpy()


#INITIALS
col_title = df.columns.tolist()
col_cat = ['Person', 'Cups of Rice Consumed', 'Hours Spent on Homework', 'Height']

#OUTPUTS
print("Synthetic Dataset of Dietary, Academic, and Physical Attributes\n")

print("Data set columns:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    
#proof of clean data set
print("\nOriginal Data Shape:", df.shape)
print("Missing Values:") 
print(df.isnull().sum())
print("\nTop 5 Person:\n", df.head())
 3/3: %history -n 1-505
 3/4: %history -n 1-505
 3/5:
#numpy operations

sumcrc = np.sum(b)
maxcrc = np.max(b)
mincrc = np.min(b)
meanhsh = np.mean(c)
medianhsh = np.median(c)
perhsh = np.percentile(c, [45, 50, 55])
stdh = np.std(d)
varh = np.var(d)
rangeh = np.ptp(d)

print("\nCup of Rice Consumed Statistics:")
print(f"Sum of Cup of Rice Consumed: {sumcrc:.1f}")
print(f"Maximum of Cup of Rice Consumed: {maxcrc:.1f}")
print(f"Minimum of Cup of Rice Consumed: {mincrc:.1f}")

print("\nHours Spent on Homework Statistics:")
print(f"Mean of Hours Spent on Homework: {meanhsh:.1f}")
print(f"Median of Hours Spent on Homework: {medianhsh:.1f}")
print(f"45th, 50th, and 55th Percentile of Hours Spent on Homework: {perhsh}")

print("\nHeight Statistics:")
print(f"Standard Deviation of Height: {stdh:.1f}")
print(f"Variance of Height: {varh:.1f}")
print(f"Range of Height: {rangeh:.1f}")
 3/6:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

#DATA SET
df = pd.read_csv(r'C:\Users\hmcldryl\Desktop\cupsnheight.csv')

a = df['Person'].to_numpy()
b = df['Cups of Rice Consumed'].to_numpy()
c = df['Hours Spent on Homework'].to_numpy()
d = df['Height'].to_numpy()


#INITIALS
col_title = df.columns.tolist()
col_cat = ['Person', 'Cups of Rice Consumed', 'Hours Spent on Homework', 'Height']

#OUTPUTS
print("Synthetic Dataset of Dietary, Academic, and Physical Attributes\n")

print("Data set columns:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    
#proof of clean data set
print("\nOriginal Data Shape:", df.shape)
print("Missing Values:") 
print(df.isnull().sum())
print("\nTop 5 Person:\n", df.head())
  26:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

#DATA SET
df = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

a = df['Name'].to_numpy()
b = df['PPG'].to_numpy()
c = df['FG%'].to_numpy()
d = df['FT%'].to_numpy()


#INITIALS
col_title = df.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']

#OUTPUTS
print("TOP 200 SCORERS DATA IN THE NATIONAL BASKETBALL ASSOCIATION (NBA)\n")

print("Data set columns:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    
#proof of clean data set
print("\nOriginal Data Shape:", df.shape)
print("Missing Values:") 
print(df.isnull().sum())
print("\nTop 5 scorers:\n", df.head())
  27:
#numpy operations

sumppg = np.sum(b)
maxppg = np.max(b)
minppg = np.min(b)
meanfg = np.mean(c)
medianfg = np.median(c)
perfg = np.percentile(c, [90, 95, 99])
stdft = np.std(d)
varft = np.var(d)
rangeft = np.ptp(d)

print("\nPPG Statistics:")
print(f"Sum of PPG: {sumppg:.1f}")
print(f"Maximum of PPG: {maxppg:.1f}")
print(f"Minimum of PPG: {minppg:.1f}")

print("\nFG% Statistics:")
print(f"Mean of FG%: {meanfg:.1f}")
print(f"Median of FG%: {medianfg:.1f}")
print(f"90th, 95th, and 99th Percentile of FG%: {perfg}")

print("\nFT% Statistics:")
print(f"Standard Deviation of FT%: {stdft:.1f}")
print(f"Variance of FT%: {varft:.1f}")
print(f"Range of FT%: {rangeft:.1f}")
  28:
#scipy operations

#sampling the data set into 4 arrays (samples) with 5 values each
arr1 = np.array([])
arr2 = np.array([])
arr3 = np.array([])
arr4 = np.array([])
for i in range(20):
    if i < 5:
        arr1 = np.append(arr1, b[i])

    if i < 10 and i > 4:
        arr2 = np.append(arr2, b[i])

    if i < 15 and i > 9:
        arr3 = np.append(arr3, b[i])

    if i < 20 and i > 14:
        arr4 = np.append(arr4, b[i])

print("Array 1", arr1,"\nArray 2", arr2, "\nArray 3",arr3, "\nArray 4",arr4)

#one-way anova
f_statistic, p_value = stats.f_oneway(arr1, arr2, arr3, arr4)
print(f"\nOne-Way Anova \n\nF-statistic: {f_statistic:.4f}, P-value: {p_value:.8f}")

#plot
data = [arr1, arr2, arr3, arr4]
labels = ['Array 1', 'Array 2', 'Array 3', 'Array 4']

plt.figure(figsize=(8, 5))
plt.boxplot(data, tick_labels=labels)
plt.title('One-Way ANOVA: Array Comparisons')
plt.ylabel('Scores')
plt.grid(True)
plt.show()

#standard normal
zval = stats.zscore(arr1)
print(f"\nZ-Distribution\n\nZ-score for first 5 values:")
for i in range(5):
    print(zval[i], end=' ')

#plot
z_range = np.linspace(-3, 3, 50)
pdf = stats.norm.pdf(z_range)

plt.figure(figsize=(10, 4))
plt.plot(z_range, pdf, color='gray', linestyle='-', label='Standard Normal PDF')

plt.hist(zval, bins=20, density=True, alpha=0.5, label='Z-scores', color='blue')

plt.axvline(0, color='black', linestyle='-', linewidth=3)
plt.title('Z-Score Distribution of Array 1')
plt.xlabel('Z-score')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()

#t-test
t_stat, p_value = stats.ttest_ind(arr3, arr4)
print(f"T - Test\n\nT-test between Array 3 and Array 4: \nt = {t_stat:.2f} \np = {p_value:.3f}")

#plot
plt.figure(figsize=(8, 5))
plt.boxplot([arr3, arr4], tick_labels=['Array 3', 'Array 4'])
plt.title('T-Test: Array 3 & Array 4 Comparison')
plt.ylabel('Values')
plt.grid(True)
plt.show()
  29:
#Statsmodels

x = sm.add_constant(df['FG%'])
model = sm.OLS(df['PPG'], x).fit()
print("\nLinear Regression Summary:")
print(model.summary())
  30:
#correlation with visualizations
x = 1
y = 2

#corr1
corr_matrix = np.corrcoef(b, c)
correlation = corr_matrix[0, 1]
print(col_cat[x], col_title[x], "vs", col_cat[y], col_title[y])
print("Correlation coefficient (Pearson r):", correlation)
y += 1

#plot for corr1
ds = pd.DataFrame({'X': b, 'Y': c})

plt.figure(figsize=(8, 5))
sns.regplot(x='X', y='Y', data=ds, color='blue', marker='o', ci = 95, line_kws={'color': 'red', 'linewidth': 2})

plt.title('Seaborn Scatterplot with Regression Line')
plt.xlabel('Points Per Game PPG')
plt.ylabel('Field Goal Percentage FG%')
plt.grid(True)
plt.show()

#corr2
corr_matrix = np.corrcoef(b, d)
correlation = corr_matrix[0, 1]
print()
print(col_cat[x], col_title[x], "vs", col_cat[y], col_title[y])
print("Correlation coefficient (Pearson r):", correlation)
x += 1

#plot for corr2
ds = pd.DataFrame({'X': b, 'Y': d})

plt.figure(figsize=(8, 5))
sns.regplot(x='X', y='Y', data=ds, color='blue', marker='o', ci = 95, line_kws={'color': 'red', 'linewidth': 2})

plt.title('Seaborn Scatterplot with Regression Line')
plt.xlabel('Points Per Game PPG')
plt.ylabel('Free Throw Percentage FT%')
plt.grid(True)
plt.show()

#corr3
corr_matrix = np.corrcoef(c, d)
correlation = corr_matrix[0, 1]
print()
print(col_cat[x], col_title[x], "vs", col_cat[y], col_title[y])
print("Correlation coefficient (Pearson r):", correlation)

#plot for corr3
ds = pd.DataFrame({'X': c, 'Y': d})

plt.figure(figsize=(8, 5))
sns.regplot(x='X', y='Y', data=ds, color='blue', marker='o', ci = 95, line_kws={'color': 'red', 'linewidth': 2})

plt.title('Seaborn Scatterplot with Regression Line')
plt.xlabel('Field Goal Percentage FG%')
plt.ylabel('Free Throw Percentage FT%')
plt.grid(True)
plt.show()
  31:
#seaborn

dx = pd.DataFrame({'PPG': b, 'FG%': c, 'FT%': d})
corr = dx.corr()

plt.figure(figsize=(6, 5))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', square=True)
plt.title('Correlation Heatmap')
plt.show()
  32: %history -n 1-513
  33:
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

#DATA SET
df = pd.read_csv(r'/Users/lydrenjess/Downloads/finalset.csv')

a = df['Name'].to_numpy()
b = df['PPG'].to_numpy()
c = df['FG%'].to_numpy()
d = df['FT%'].to_numpy()


#INITIALS
col_title = df.columns.tolist()
col_cat = ['Player', 'Points Per Game', 'Field Goal Percentage', 'Free Throw Percentage']

#OUTPUTS
print("TOP 200 SCORERS DATA IN THE NATIONAL BASKETBALL ASSOCIATION (NBA)\n")

print("Data set columns:")
for i in range(len(col_cat)):
    print(i + 1, col_cat[i], col_title[i])
    
#proof of clean data set
print("\nOriginal Data Shape:", df.shape)
print("Missing Values:") 
print(df.isnull().sum())
print("\nTop 5 scorers:\n", df.head())
  34:
#numpy operations

sumppg = np.sum(b)
maxppg = np.max(b)
minppg = np.min(b)
meanfg = np.mean(c)
medianfg = np.median(c)
perfg = np.percentile(c, [90, 95, 99])
stdft = np.std(d)
varft = np.var(d)
rangeft = np.ptp(d)

print("\nPPG Statistics:")
print(f"Sum of PPG: {sumppg:.1f}")
print(f"Maximum of PPG: {maxppg:.1f}")
print(f"Minimum of PPG: {minppg:.1f}")

print("\nFG% Statistics:")
print(f"Mean of FG%: {meanfg:.1f}")
print(f"Median of FG%: {medianfg:.1f}")
print(f"90th, 95th, and 99th Percentile of FG%: {perfg}")

print("\nFT% Statistics:")
print(f"Standard Deviation of FT%: {stdft:.1f}")
print(f"Variance of FT%: {varft:.1f}")
print(f"Range of FT%: {rangeft:.1f}")
  35:
#scipy operations

#sampling the data set into 4 arrays (samples) with 5 values each
arr1 = np.array([])
arr2 = np.array([])
arr3 = np.array([])
arr4 = np.array([])
for i in range(20):
    if i < 5:
        arr1 = np.append(arr1, b[i])

    if i < 10 and i > 4:
        arr2 = np.append(arr2, b[i])

    if i < 15 and i > 9:
        arr3 = np.append(arr3, b[i])

    if i < 20 and i > 14:
        arr4 = np.append(arr4, b[i])

print("Array 1", arr1,"\nArray 2", arr2, "\nArray 3",arr3, "\nArray 4",arr4)

#one-way anova
f_statistic, p_value = stats.f_oneway(arr1, arr2, arr3, arr4)
print(f"\nOne-Way Anova \n\nF-statistic: {f_statistic:.4f}, P-value: {p_value:.8f}")

#plot
data = [arr1, arr2, arr3, arr4]
labels = ['Array 1', 'Array 2', 'Array 3', 'Array 4']

plt.figure(figsize=(8, 5))
plt.boxplot(data, tick_labels=labels)
plt.title('One-Way ANOVA: Array Comparisons')
plt.ylabel('Scores')
plt.grid(True)
plt.show()

#standard normal
zval = stats.zscore(arr1)
print(f"\nZ-Distribution\n\nZ-score for first 5 values:")
for i in range(5):
    print(zval[i], end=' ')

#plot
z_range = np.linspace(-3, 3, 50)
pdf = stats.norm.pdf(z_range)

plt.figure(figsize=(10, 4))
plt.plot(z_range, pdf, color='gray', linestyle='-', label='Standard Normal PDF')

plt.hist(zval, bins=20, density=True, alpha=0.5, label='Z-scores', color='blue')

plt.axvline(0, color='black', linestyle='-', linewidth=3)
plt.title('Z-Score Distribution of Array 1')
plt.xlabel('Z-score')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()

#t-test
t_stat, p_value = stats.ttest_ind(arr3, arr4)
print(f"T - Test\n\nT-test between Array 3 and Array 4: \nt = {t_stat:.2f} \np = {p_value:.3f}")

#plot
plt.figure(figsize=(8, 5))
plt.boxplot([arr3, arr4], tick_labels=['Array 3', 'Array 4'])
plt.title('T-Test: Array 3 & Array 4 Comparison')
plt.ylabel('Values')
plt.grid(True)
plt.show()
  36:
#Statsmodels

x = sm.add_constant(df['FG%'])
model = sm.OLS(df['PPG'], x).fit()
print("\nLinear Regression Summary:")
print(model.summary())
  37:
#correlation with visualizations
x = 1
y = 2

#corr1
corr_matrix = np.corrcoef(b, c)
correlation = corr_matrix[0, 1]
print(col_cat[x], col_title[x], "vs", col_cat[y], col_title[y])
print("Correlation coefficient (Pearson r):", correlation)
y += 1

#plot for corr1
ds = pd.DataFrame({'X': b, 'Y': c})

plt.figure(figsize=(8, 5))
sns.regplot(x='X', y='Y', data=ds, color='blue', marker='o', ci = 95, line_kws={'color': 'red', 'linewidth': 2})

plt.title('Seaborn Scatterplot with Regression Line')
plt.xlabel('Points Per Game PPG')
plt.ylabel('Field Goal Percentage FG%')
plt.grid(True)
plt.show()

#corr2
corr_matrix = np.corrcoef(b, d)
correlation = corr_matrix[0, 1]
print()
print(col_cat[x], col_title[x], "vs", col_cat[y], col_title[y])
print("Correlation coefficient (Pearson r):", correlation)
x += 1

#plot for corr2
ds = pd.DataFrame({'X': b, 'Y': d})

plt.figure(figsize=(8, 5))
sns.regplot(x='X', y='Y', data=ds, color='blue', marker='o', ci = 95, line_kws={'color': 'red', 'linewidth': 2})

plt.title('Seaborn Scatterplot with Regression Line')
plt.xlabel('Points Per Game PPG')
plt.ylabel('Free Throw Percentage FT%')
plt.grid(True)
plt.show()

#corr3
corr_matrix = np.corrcoef(c, d)
correlation = corr_matrix[0, 1]
print()
print(col_cat[x], col_title[x], "vs", col_cat[y], col_title[y])
print("Correlation coefficient (Pearson r):", correlation)

#plot for corr3
ds = pd.DataFrame({'X': c, 'Y': d})

plt.figure(figsize=(8, 5))
sns.regplot(x='X', y='Y', data=ds, color='blue', marker='o', ci = 95, line_kws={'color': 'red', 'linewidth': 2})

plt.title('Seaborn Scatterplot with Regression Line')
plt.xlabel('Field Goal Percentage FG%')
plt.ylabel('Free Throw Percentage FT%')
plt.grid(True)
plt.show()
  38:
#seaborn

dx = pd.DataFrame({'PPG': b, 'FG%': c, 'FT%': d})
corr = dx.corr()

plt.figure(figsize=(6, 5))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', square=True)
plt.title('Correlation Heatmap')
plt.show()
  39: %history -n 1-513
  40: %history -g -f ranjo_revhis
  41: %history -g -f ranjo_revhis

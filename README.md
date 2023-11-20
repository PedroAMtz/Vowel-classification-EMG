## Vowel Classification using EMG signals :chart_with_upwards_trend:

---

### LightGBM model - extended version V1
This version of the model uses the complete data for classification, the data includes signal recorde from 8 different electrodes, data from a gyroscope (3-dimensional) and data from acceleration recordings (also 3-dimensional). With this, the composition of each recording has shape (400, 14), 400 rows of data from 14 different points ([e1	e2	e3	e4	e5	e6	e7	e8	gx	gy	gz	ax	ay	az]) corresponding to each of the data collection mechanisms described above. The classification classes are of course, the 5 vowels (A, E, I ,O, U) which were encoded to represent a numerical value in order to correctly fit the model.
The history of the experiment can be found at [gbm-extended-version-V1](https://github.com/PedroAMtz/Vowel-classification-EMG/blob/main/GBM-for-Vowel-identification.ipynb).

**Results**
Results for this version of the model (extended version-includes all data) show the well performance of the model using the testing dataset of the data. 
![Alt text](confusion_mtx_V1.png)

* Classification report:

|   | Precision | Recall | F1-Score | Support |
|---|-----------|--------|----------|---------|
| A | 1.00      | 0.92   | 0.96     | 13      |
| E | 0.89      | 0.89   | 0.89     | 9       |
| I | 0.80      | 0.80   | 0.80     | 10      |
| O | 0.80      | 1.00   | 0.89     | 4       |
| U | 0.89      | 0.89   | 0.89     | 9       |

**Accuracy:** 0.89

**Macro Avg:**
  - Precision: 0.88
  - Recall: 0.90
  - F1-Score: 0.89

**Weighted Avg:**
  - Precision: 0.89
  - Recall: 0.89
  - F1-Score: 0.89
  - Support: 45


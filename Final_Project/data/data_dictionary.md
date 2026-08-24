# Data Dictionary — Cardiovascular Disease Dataset

| Column | Meaning | Type / Encoding |
|---|---|---|
| `id` | Record identifier | Integer; removed before modeling |
| `age` | Age value in the dataset | Numeric |
| `gender` | Encoded gender variable | Binary categorical |
| `height` | Height | Numeric |
| `weight` | Weight | Numeric |
| `ap_hi` | Systolic blood-pressure field | Numeric |
| `ap_lo` | Diastolic blood-pressure field | Numeric |
| `cholesterol` | Cholesterol category | Ordinal categorical |
| `gluc` | Glucose category | Ordinal categorical |
| `smoke` | Smoking indicator | Binary |
| `alco` | Alcohol-use indicator | Binary |
| `active` | Physical-activity indicator | Binary |
| `cardio` | Target class for the classification task | Binary: 0 / 1 |

## Notes:

- The dataset is used for educational machine-learning analysis.
- `cardio` is the supervised-learning target.
- `id` is treated as an identifier rather than a predictive feature.

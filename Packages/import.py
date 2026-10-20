import kagglehub
from kagglehub import KaggleDatasetAdapter

df = kagglehub.dataset_load(
    KaggleDatasetAdapter.PANDAS,
    "karkavelrajaj/amazon-sales-dataset",
    "amazon.csv",
)

print(df.head())
print(df.shape)
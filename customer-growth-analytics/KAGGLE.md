# Run this project in Kaggle
**Ready to import; not yet executed or published on a Kaggle account.**

## Notebook route
1. Download `customer-growth-analytics.ipynb` from this project. Create a Kaggle notebook and import the `.ipynb` using the notebook import/upload option.
2. Choose one source route:
   - **Internet enabled:** the first code cell downloads the original public UCI archive automatically.
   - **Attached input:** download the original UCI ZIP, extract `Online Retail.xlsx`, and attach that file as a Kaggle input. The notebook finds a single exact-name file under `/kaggle/input`. With multiple candidates, set `DATA_PATH` explicitly in the first cell.
3. Use a Python CPU session. No GPU or paid model API is needed. The notebook uses pandas, NumPy, matplotlib and openpyxl; install any missing package before running.
4. Run every cell in order. Review the source SHA256, quality waterfall, assertions and results. Outputs are saved to `/kaggle/working/customer-growth-output`.
5. Save a private version first. Review outputs and attribution before deciding to make it public. Add the resulting Kaggle URL to this README only after it exists.

If Internet is disabled and no original file is attached, the notebook will fail at download. It deliberately does not substitute synthetic data. An arbitrary Kaggle mirror with different columns or a CSV filename is not a drop-in input.

## Optional CLI route
Use the official Kaggle CLI with your own account authentication. Keep credentials outside this repository.

Copy `kernel-metadata.example.json` to `kernel-metadata.json` in the notebook directory. Replace `YOUR_KAGGLE_USERNAME` with the actual account slug. The example defaults to private, Internet enabled, CPU and no attached dataset. Then:
```sh
kaggle kernels push -p .
```
This command uploads and runs a kernel; do it only when you want to create/update it in that account. If using an attached Kaggle dataset instead, put its actual `owner/dataset-slug` in `dataset_sources`. Do not invent a Kaggle dataset ID or assume your GitHub and Kaggle usernames match.

Official references: [Kaggle notebooks](https://www.kaggle.com/docs/notebooks), [kernel metadata](https://github.com/Kaggle/kaggle-cli/blob/main/docs/kernels_metadata.md), [kernel commands](https://github.com/Kaggle/kaggle-cli/blob/main/docs/kernels.md).

## Attribution
Preserve the notebook citation: Chen, D. (2015), Online Retail, UCI Machine Learning Repository, https://doi.org/10.24432/C5BW33, CC BY 4.0. Describe the cleaning and aggregation changes. Do not present this public dataset as proprietary customer data or these observations as business results you delivered.

[Project home](README.md)

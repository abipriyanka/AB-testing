# Email Marketing A/B Test

An intermediate data-science project analysing a **real randomised email marketing experiment**.

The dataset comes from Kevin Hillstrom's **MineThatData E-Mail Analytics and Data Mining Challenge**. It contains 64,000 customers who had purchased within the previous 12 months.

Customers were randomly assigned to one of three groups:

- Men's E-Mail
- Women's E-Mail
- No E-Mail

Their website visits, conversions and spend were then tracked for two weeks.

## Why I built this

A lot of beginner machine-learning projects focus on prediction. I wanted to work on a different question:

> Did an intervention actually change customer behaviour?

This project therefore focuses on experimentation, statistical significance, confidence intervals and business interpretation rather than training another predictive model.

## Dataset source

Original challenge:

https://blog.minethatdata.com/2008/03/minethatdata-e-mail-analytics-and-data.html

The dataset is also documented in TensorFlow Datasets:

https://www.tensorflow.org/datasets/catalog/hillstrom

The repository does not fabricate or simulate customer records. Run:

```bash
python download_data.py
```

to download the public Hillstrom dataset into:

```text
data/hillstrom.csv
```

## Dataset fields

| Column | Meaning |
|---|---|
| `recency` | Months since last purchase |
| `history_segment` | Previous 12-month spend band |
| `history` | Previous 12-month spend |
| `mens` | Previously purchased men's merchandise |
| `womens` | Previously purchased women's merchandise |
| `zip_code` | Area type |
| `newbie` | New customer indicator |
| `channel` | Previous purchase channel |
| `segment` | Randomised experiment group |
| `visit` | Visited the website after the campaign |
| `conversion` | Made a purchase after the campaign |
| `spend` | Spend during the measurement period |

## Questions answered

1. Were the randomised groups broadly balanced before treatment?
2. Did either email increase website visits?
3. Did either email increase conversion?
4. How large was the treatment effect?
5. What does the 95% confidence interval look like?
6. Did average spend improve?
7. Do the results look different across customer types or channels?

## Headline pattern in the data

The real dataset shows a clear ordering:

- the no-email group has the lowest visit and conversion rates,
- the women's email improves both,
- the men's email produces the highest visit, conversion and revenue-per-customer figures.

The notebook calculates the exact rates, confidence intervals and p-values directly from the downloaded data.

## Project structure

```text
hillstrom-email-ab-test/
│
├── README.md
├── requirements.txt
├── download_data.py
│
├── data/
│   └── README.md
│
├── notebooks/
│   └── email_campaign_ab_test.ipynb
│
├── sql/
│   ├── 01_campaign_summary.sql
│   ├── 02_results_by_channel.sql
│   └── 03_results_new_vs_existing.sql
│
├── src/
│   └── ab_test_utils.py
│
└── dashboard/
    └── app.py
```

## Analysis approach

### 1. Data checks

I check:

- shape and column types
- missing values
- duplicates
- experiment group sizes

I do not add unnecessary cleaning because the source data is already analysis-ready.

### 2. Balance check

Because this is a randomised experiment, the groups should be broadly comparable before the campaign.

I compare:

- recency
- previous spend
- previous men's/women's purchases
- new-customer rate

### 3. A/B testing

For conversion I use a two-proportion z-test and report:

- control rate
- treatment rate
- absolute difference
- relative lift
- p-value
- 95% confidence interval

### 4. Revenue

I compare average spend per customer and use Welch's t-test as an additional statistical check.

### 5. Segment analysis

Finally, I look at results by:

- new vs existing customer
- previous purchase channel

These segment results are exploratory rather than separate confirmed experiments.

## Run locally

Create a virtual environment:

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Install packages:

```bash
pip install -r requirements.txt
```

Download the real dataset:

```bash
python download_data.py
```

Then open:

```text
notebooks/email_campaign_ab_test.ipynb
```

For the dashboard:

```bash
streamlit run dashboard/app.py
```

## Skills demonstrated

- Python
- pandas
- SQL
- exploratory data analysis
- experiment design
- A/B testing
- hypothesis testing
- confidence intervals
- effect size
- customer segmentation
- business interpretation
- Streamlit

## Limitations

This is a historical marketing experiment, so the results should not be treated as evidence of how a modern campaign would perform today.

The subgroup analysis is exploratory. A subgroup looking stronger in this dataset does not automatically mean the company should target only that group without further testing.

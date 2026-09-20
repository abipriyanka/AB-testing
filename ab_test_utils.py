import math

import pandas as pd


def proportion_test(control, treatment):
    """Two-sided z-test and confidence interval for a difference in proportions."""
    n_control = len(control)
    n_treatment = len(treatment)

    p_control = control.mean()
    p_treatment = treatment.mean()

    successes = control.sum() + treatment.sum()
    pooled = successes / (n_control + n_treatment)

    pooled_se = math.sqrt(
        pooled * (1 - pooled) * (1 / n_control + 1 / n_treatment)
    )

    z_score = (p_treatment - p_control) / pooled_se

    normal_cdf = lambda x: (1 + math.erf(x / math.sqrt(2))) / 2
    p_value = 2 * (1 - normal_cdf(abs(z_score)))

    difference = p_treatment - p_control

    diff_se = math.sqrt(
        p_control * (1 - p_control) / n_control
        + p_treatment * (1 - p_treatment) / n_treatment
    )

    return {
        "control_rate": p_control,
        "treatment_rate": p_treatment,
        "absolute_difference": difference,
        "relative_lift": difference / p_control if p_control else float("nan"),
        "z_score": z_score,
        "p_value": p_value,
        "ci_low": difference - 1.96 * diff_se,
        "ci_high": difference + 1.96 * diff_se,
    }


def experiment_summary(df):
    return (
        df.groupby("segment")
        .agg(
            customers=("segment", "size"),
            visit_rate=("visit", "mean"),
            conversion_rate=("conversion", "mean"),
            revenue_per_customer=("spend", "mean"),
            total_revenue=("spend", "sum"),
        )
        .sort_values("conversion_rate", ascending=False)
    )


def balance_table(df):
    return (
        df.groupby("segment")
        .agg(
            avg_recency=("recency", "mean"),
            avg_history=("history", "mean"),
            mens_customer_rate=("mens", "mean"),
            womens_customer_rate=("womens", "mean"),
            newbie_rate=("newbie", "mean"),
        )
    )

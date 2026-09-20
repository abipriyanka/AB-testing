SELECT
    segment,
    COUNT(*) AS customers,
    ROUND(AVG(visit) * 100, 2) AS visit_rate_pct,
    ROUND(AVG(conversion) * 100, 2) AS conversion_rate_pct,
    ROUND(AVG(spend), 2) AS revenue_per_customer,
    ROUND(SUM(spend), 2) AS total_revenue
FROM hillstrom
GROUP BY segment
ORDER BY conversion_rate_pct DESC;

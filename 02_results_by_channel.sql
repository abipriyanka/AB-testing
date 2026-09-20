SELECT
    channel,
    segment,
    COUNT(*) AS customers,
    ROUND(AVG(visit) * 100, 2) AS visit_rate_pct,
    ROUND(AVG(conversion) * 100, 2) AS conversion_rate_pct,
    ROUND(AVG(spend), 2) AS revenue_per_customer
FROM hillstrom
GROUP BY channel, segment
ORDER BY channel, conversion_rate_pct DESC;

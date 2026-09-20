SELECT
    CASE
        WHEN newbie = 1 THEN 'New customer'
        ELSE 'Existing customer'
    END AS customer_type,
    segment,
    COUNT(*) AS customers,
    ROUND(AVG(conversion) * 100, 2) AS conversion_rate_pct,
    ROUND(AVG(spend), 2) AS revenue_per_customer
FROM hillstrom
GROUP BY customer_type, segment
ORDER BY customer_type, conversion_rate_pct DESC;

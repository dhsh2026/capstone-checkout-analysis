# Checkout Experiment Analysis – Variant B

## Introduction
Our company has launched a new checkout experience, **Variant B**, with the goal of reducing drop-offs during checkout and increasing revenue from online purchases.  

This document frames the business problem, key metrics, and analysis scope for evaluating Variant B against the existing checkout **Variant A**.

---

## 1. Business Objective
The objective of this experiment is to determine whether checkout Variant B delivers incremental revenue and reduced checkout drop-offs **without negatively impacting unit economics**, thereby justifying a full rollout.

---

## 2. North Star Metric
### Revenue per Eligible Session (RPS)
The North Star Metric for this experiment is **Revenue per Eligible Session** in the checkout experiment.
This metric captures both:
- How many users convert (purchase)
- How much revenue they generate per session
By focusing on revenue per eligible session, we directly measure the overall business impact of Variant B compared with Variant A, instead of looking only at conversion rate or average order value in isolation.

---

## 3. Supporting KPIs

### 1. Checkout Conversion Rate (Eligible Sessions)
Percentage of eligible sessions that result in at least one purchase.  
This shows how effectively each checkout variant converts users who are exposed to it.

---

### 2. Funnel Step Conversion Rates
Conversion rates between key steps in the purchase funnel:
- Landing view → Product view  
- Product view → Add to cart  
- Add to cart → Begin checkout  
- Begin checkout → Payment attempt  
- Payment attempt → Purchase  
These metrics help identify where the biggest drop-offs occur and whether Variant B improves specific steps.

---

### 3. Revenue per Eligible Session (RPS)
Average revenue generated per eligible session, including sessions that do not convert.  
This directly aligns with the North Star Metric and is measured separately for Variant A and Variant B.

---

### 4. Average Order Value (AOV)
Average revenue per order.  
This helps us understand whether Variant B changes how much customers spend when they do purchase.

---

### 5. Discount Rate
The average proportion of discount applied relative to list price across items or orders.  
This indicates whether any uplift in revenue is driven by heavier discounting, which might hurt profitability.

---

### 6. Margin Proxy (Revenue − Estimated Cost)
An approximate profit margin metric calculated using revenue and product cost estimates.  
This helps ensure that Variant B does not improve revenue at the expense of significantly lower margins.

---

### 7. Payment Failure / Drop-off Rate (Payment Step Proxy)
Among sessions that attempt payment, the proportion that do not complete a purchase.  
This acts as a proxy for payment failures or friction in the payment step and is especially important for understanding checkout performance.

---

## 4. Scope & Eligibility
The scope of this analysis is limited to sessions that are actually eligible for the checkout experiment and can be fairly compared across variants.

### Eligible Sessions
- Sessions on the web platform where the new checkout experience can be served  
- Sessions where the user is logged in (valid user identifier present)  
- Sessions explicitly assigned a checkout experiment variant (A or B)

### Out of Scope
- Mobile sessions  
- Anonymous sessions without a user ID  
- Sessions without an assigned experiment variant  
Restricting to eligible sessions ensures a clean comparison between Variant A and Variant B and avoids mixing in traffic that never saw the experimental checkout experience.

## 5. Stakeholder Questions and Data answers:
- 1. Should we roll out Variant B to everyone?
Compare conversion rate and revenue per eligible session between Variant A vs B using sessions.csv, events.csv, and orders.csv.

- 2. Does Variant B improve any specific funnel step?
Compute step-level funnel conversion (landing → product, product → cart, cart → checkout, checkout → payment, payment → purchase) by variant using events.csv.

- 3. Which channels benefit most from Variant B?
Segment KPIs (conversion, RPS, AOV) by channel and variant using sessions.csv and orders.csv.

- 4. Are there device or user-type differences (new vs returning users)?
Segment KPIs by device and is_new_user fields in sessions.csv and compare Variant A vs B.

- 5. Which product categories or price bands show the biggest impact?
Join orders.csv → order_items.csv → products.json to compute conversion and RPS per category by variant.

- 6. Does Variant B hurt margins?
Use order_items.csv + products.json to estimate margin per order and compare margin per session.

- 7. What revenue uplift can we expect next month?
Estimate incremental revenue per eligible session and multiply by expected sessions.

## Weekly Trends Analysis:
Variant B consistently outperforms A across all weeks, with average +6% conversion lift.
**Biggest anomaly:** Week 4 saw +30% lift (55.6% → 85.7%)
- RPS also spiked: $1909 → $2059  
- Session duration: 17s → 87s (5x longer)
- Hypothesis: Holiday surge + B checkout improvements

**Recent trend:** Weeks 45-50 show steady 5-8% lifts
Recommendation: Roll out B now – momentum building

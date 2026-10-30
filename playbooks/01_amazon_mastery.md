# Amazon Omnipresence Playbook: FBA, FBM, SFP & Vendor Central (1P)

This playbook establishes the operational standards and growth strategies across all four Amazon fulfillment models to maximize revenue, protect Buy Box ownership, and safeguard seller metrics.

---

## 1. Fulfillment Model Comparison & Strategic Allocation

```
+------------------------------------------------------------------------------------+
|                               AMAZON ENGINE MATRIX                                 |
+----------------------+--------------------+--------------------+-------------------+
| Model                | Best For           | Margin Profile     | Primary Risk      |
+----------------------+--------------------+--------------------+-------------------+
| FBA (3P)             | Fast-moving SKUs   | Medium (FBA fees)  | Storage fees, IPI |
| FBM (3P)             | Bulky, slow-movers | High gross margin  | VTR & LSR metrics |
| SFP (Seller Prime)   | High-ticket/fragile| High (Prime badge) | Strict delivery   |
| Vendor Central (1P)  | Bulk wholesale POs | Lower (wholesale)  | Chargebacks & MAP |
+----------------------+--------------------+--------------------+-------------------+
```

---

## 2. Amazon FBA (Fulfilled by Amazon) Playbook

### Core Metrics to Control:
- **IPI (Inventory Performance Index)**: Maintain score > 500 to unlock unlimited storage and lower tiered storage surcharges.
- **Sell-Through Rate**: Target a 90-day rolling sell-through rate of 2.5+. Avoid holding > 90 days of stock in FBA centers to evade aged inventory surcharges.
- **Inbound Defect Rate**: Keep under 0.05% by ensuring carton labels, FNSKU barcodes (or manufacturer barcodes where Brand Registered), and box weight limits (< 23kg / 50lbs) are strictly enforced.

### Launch & Ranking Checklist:
1. **Brand Registry Enrollment**: Upload trademark registration to unlock A+ Content, Brand Story, Brand Analytics, and Sponsored Brands video.
2. **Amazon Vine Program**: Enroll eligible new ASINs immediately to collect up to 30 honest reviews within the first 3-6 weeks.
3. **COSMO / A9 Search SEO**:
   - Title: `[Brand] + [Core Keyword / Product Name] + [Key Feature / Material] + [Pack Size / Variant] + [Use Case]`
   - Bullet Points: 5 bullets focusing on Benefit -> Feature -> Proof -> Guarantee. First 3 bullets optimized for mobile preview.
   - Backend Search Terms: 249 bytes maximum, zero punctuation, zero brand names, highly relevant long-tail search terms.
4. **PPC Architecture**:
   - Auto Campaign (Discovery)
   - Exact Match Campaign (High-intent harvest)
   - ASIN Target Campaign (Competitor defense and offensive conquesting)

---

## 3. Amazon FBM (Fulfilled by Merchant)

### Metric Thresholds:
- **Late Shipment Rate (LSR)**: Must stay below **4.0%**. Configure daily cutoff times (e.g., 2:00 PM) and accurate handling times (1-day handling for competitive Buy Box ranking).
- **Valid Tracking Rate (VTR)**: Must stay above **95%** using approved integrated carriers (Royal Mail 24/48 Tracked, DPD, DHL, UPS).
- **Pre-fulfillment Cancellation Rate**: Must stay below **2.5%**. Dynamic inventory sync with warehouse OMS is mandatory.

---

## 4. Seller Fulfilled Prime (SFP) Activation & Governance

SFP grants the coveted **Amazon Prime badge** while shipping orders from your own fulfillment warehouse or 3PL.

### Qualification Requirements:
1. **Shipping Carrier**: Must purchase shipping labels exclusively through **Amazon Buy Shipping** (or automated API integration like ShipStation/Linnworks).
2. **Speed Metrics**:
   - 1-Day Delivery Promise: Must meet strict regional or nationwide thresholds (typically > 30-50% page views for 1-day).
   - 2-Day Delivery Promise: > 70% nationwide coverage.
3. **Weekend Operations**: Carrier pickups must be scheduled on either Saturday or Sunday (or both) to satisfy Prime weekend delivery SLAs.
4. **On-Time Delivery Rate (OTDR)**: Must maintain $\ge 93.5\%$ (targeting 98%+).
5. **Cancellation Rate**: Must remain $< 0.5\%$.

---

## 5. Amazon Vendor Central (1P) Operations

If invited to or operating Vendor Central, Amazon acts as the retailer, purchasing bulk inventory via wholesale Purchase Orders (POs).

### Critical Playbooks:
1. **Purchase Order (PO) Governance**:
   - POs drop every Monday morning. Confirm, backorder, or reject PO quantities within 24 hours.
   - Never accept PO quantities you cannot fulfill within the Ship Window; unfulfilled confirmed POs incur an **8-10% cancellation chargeback**.
2. **Chargeback Defense & Operational Excellence**:
   - **Advance Shipment Notice (ASN)**: ASN must be transmitted via EDI 856 prior to the shipment arriving at the Amazon Fulfillment Center.
   - **Carton Barcodes (SSCC-18)**: Every pallet and carton must feature compliant GS1 SSCC-18 barcode labels.
   - **Prep Compliance**: Liquid seal tests, polybagging suffocation warnings, and drop-test packaging.
3. **Hybrid 1P / 3P Strategy**:
   - Maintain 3P (FBA/FBM) as a backup listing (under Seller Central) in case Amazon pauses 1P POs or marks items temporarily out of stock.
   - Avoid aggressive wholesale discounting to Amazon 1P that triggers automated price matching and crashes your DTC / Wholesale MAP (Minimum Advertised Price) pricing.

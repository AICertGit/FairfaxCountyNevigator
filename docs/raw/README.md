# Raw Source Files

This folder stores downloaded or snapshotted official Fairfax County / Fairfax-hosted source files for the Fairfax Service Navigator prototype.

## 2026-05-05 Initial Download Test

Downloaded by Codex during Phase 1 ingestion test:

| File | Source URL | Notes |
| --- | --- | --- |
| `fy2026_it_plan_section_1.pdf` | https://www.fairfaxcounty.gov/informationtechnology/sites/informationtechnology/files/assets/itplan/2026-adopted/FY-2026-IT-Plan-Section-1.pdf | Official FY 2026 Adopted IT Plan Section 1. |
| `fy2026_it_plan_section_3.pdf` | https://www.fairfaxcounty.gov/informationtechnology/sites/informationtechnology/files/assets/itplan/2026-adopted/FY-2026-IT-Plan-Section-3.pdf | Official FY 2026 Adopted IT Plan Section 3. |
| `fy2026_it_plan_section_4.pdf` | https://www.fairfaxcounty.gov/informationtechnology/sites/informationtechnology/files/assets/itplan/2026-adopted/FY-2026-IT-Plan-Section-4.pdf | Official FY 2026 Adopted IT Plan Section 4. |
| `fy2027_itpac_interim_letter.pdf` | https://www.fairfaxcounty.gov/informationtechnology/sites/informationtechnology/files/assets/itpac/pdf/ITPAC-FY27-Interim-Letter-to-CEX-Dec-2025-FINAL-A-1a.pdf | Official FY 2027 ITPAC interim letter. |
| `fy2026_itpac_budget_letter.pdf` | https://www.fairfaxcounty.gov/informationtechnology/sites/informationtechnology/files/assets/itpac/pdf/ITPAC-FY26-Letter-to-BOS-March11-2025-FINAL-A-1a.pdf | Official FY 2026 ITPAC budget letter. |
| `itpac_minutes_2026-01-22.pdf` | https://www.fairfaxcounty.gov/informationtechnology/sites/informationtechnology/files/assets/itpac/pdf/ITPAC-Minutes-for-1-22-26-A-1a.pdf | Official January 22, 2026 ITPAC meeting minutes. |
| `fy2027_advertised_budget_overview.pdf` | https://www.fairfaxcounty.gov/budget/sites/budget/files/Assets/documents/fy2027/advertised/overview.pdf | Official FY 2027 Advertised Budget Overview. |
| `fairfax_recycling_and_trash.html` | https://www.fairfaxcounty.gov/publicworks/recycling-and-trash | Official Fairfax recycling and trash page HTML snapshot. |

## 2026-05-05 Service Page Snapshot Batch

Downloaded by Codex during Phase 1 corpus setup:

| File | Source URL | Notes |
| --- | --- | --- |
| `taxes_vehicles.html` | https://www.fairfaxcounty.gov/taxes/vehicles/ | Official vehicle taxes page. |
| `taxes_real_estate.html` | https://www.fairfaxcounty.gov/taxes/real-estate/ | Official real estate taxes page. |
| `plus_overview.html` | https://www.fairfaxcounty.gov/plan2build/plus | Official PLUS overview page. |
| `land_development_services.html` | https://www.fairfaxcounty.gov/landdevelopment | Official Land Development Services page. |
| `lds_plus_support.html` | https://www.fairfaxcounty.gov/landdevelopment/your-lds-guide-plus | Official LDS PLUS support page. |
| `code_report_violation.html` | https://www.fairfaxcounty.gov/code/how-report-violation-dcc | Official code violation reporting page. |
| `code_compliance_faqs.html` | https://www.fairfaxcounty.gov/code/code-compliance-faqs | Official code compliance FAQ page. |
| `hhs_basic_needs_assistance.html` | https://www.fairfaxcounty.gov/neighborhood-community-services/basic-needs-assistance | Official basic needs assistance page. |
| `hhs_coordinated_services_planning.html` | https://www.fairfaxcounty.gov/neighborhood-community-services/coordinated-services-planning | Official Coordinated Services Planning page. |
| `foia_overview.html` | https://www.fairfaxcounty.gov/publicaffairs/foia | Official FOIA overview page. |
| `foia_request.html` | https://www.fairfaxcounty.gov/publicaffairs/vfoia-request | Official VFOIA request page. |
| `parks_home.html` | https://www.fairfaxcounty.gov/parks/ | Official Park Authority page. |
| `library_home.html` | https://www.fairfaxcounty.gov/library/ | Official Library page. |
| `transportation_home.html` | https://www.fairfaxcounty.gov/transportation/ | Official Transportation page. |
| `public_safety_calling_non_emergency.html` | https://www.fairfaxcounty.gov/911/calling-non-emergency | Official non-emergency calling guidance page. |
| `police_home.html` | https://www.fairfaxcounty.gov/police | Official Police Department page. |
| `health_home.html` | https://www.fairfaxcounty.gov/health | Official Health Department page. |
| `csb_home.html` | https://www.fairfaxcounty.gov/community-services-board | Official Community Services Board page. |
| `elections_home.html` | https://www.fairfaxcounty.gov/elections | Official Elections page, included as deferred/seasonal candidate. |

## Handling Notes

- These are public sources.
- Do not add confidential resident data to this folder.
- For dynamic pages and forms, prefer routing links unless reviewed for static ingestion.
- Future ingestion should record source URL, download date, file name, and approval status in `docs/source_inventory.md`.

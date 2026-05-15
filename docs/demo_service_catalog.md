# Demo Service Catalog Coverage

This repo includes a local Fairfax Resource Navigator demo UI for the Google ADK starter-pack app. The UI lives in `frontend/`, and the ADK-compatible deterministic agent lives in `app/agent.py`.

## Covered Domains

1. Housing and basic needs
   - CSP for emergency food, rent assistance, utility help, shelters, homelessness intake, affordable housing, LIHTC, and waitlist routing.

2. Taxes and revenue
   - DTA for car/personal property tax, vehicle tax payment, senior/disability tax relief, real estate assessments, payments, and appeals.

3. Health and human services
   - CSB for behavioral health, severe crisis, addiction recovery, and opioid support.
   - Health Department for immunizations, dental care for uninsured residents, WIC, and public health questions.
   - Older adult services for aging in place, senior centers, caregiver help, nutrition, and Meals on Wheels.
   - CCAR and Head Start for subsidized childcare and early education.

4. Parks, recreation, and youth
   - Parktakes, FCPA, and NCS camps.
   - Camp matching considers child age, interests, location, and budget.
   - Demo camp catalog includes Rec-PAC, Frying Pan Farm Hands, Lake Fairfax Adventure Camp, Spring Hill Splash & Sports, STEM Robo-Creators, Ice Hockey Prep Camp, and Fine Arts & Clay.
   - Community hub routing includes Sully, Lorton, and other NCS community centers.

5. Land use, permits, and code
   - DCC for tall grass, hoarding, illegal construction, boarding houses, and neighborhood complaints.
   - LDS and PLUS for permits, inspections, zoning, and property-line questions.

6. Public works and utilities
   - DPWES for trash, recycling, missed pickup, purple glass bins, hazardous waste, and disposal routing.
   - Water/sewer routing distinguishes DPWES, Fairfax Water, and other utility providers where possible.

7. Transportation
   - FCDOT, Fairfax Connector, Fastran, roads, parking, potholes, and commuting questions.

8. Public safety
   - 911 for emergencies.
   - Non-emergency police/fire/EMS routing, noise complaints, animal control, fire inspections, and Fire and Rescue community outreach.

## Triage Rules

- Emergency override: violence, self-harm, severe mental health crisis, overdose risk, weapons, or immediate danger routes to 911 or CSB Emergency Services at 703-573-5679.
- Privacy: the demo asks for ZIP code, age, household size, income range, interests, or general neighborhood only; it does not need full names or exact addresses.
- Grounding: responses include official Fairfax County or Fairfax-hosted source citations.
- Limits: the demo does not promise eligibility, legal outcomes, tax amounts, permit outcomes, shelter placement, or live camp seat availability.

# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import annotations

from dataclasses import dataclass
from typing import AsyncGenerator

from google.adk.agents import BaseAgent
from google.adk.agents.invocation_context import InvocationContext
from google.adk.apps import App
from google.adk.events.event import Event
from google.genai import types
from typing_extensions import override


@dataclass(frozen=True)
class SourceSnippet:
    id: str
    title: str
    url: str
    path: str
    quote: str


@dataclass(frozen=True)
class Route:
    key: str
    label: str
    urgency: str
    destination: str
    next_steps: tuple[str, ...]
    sources: tuple[str, ...]


@dataclass(frozen=True)
class CampOption:
    name: str
    focus: str
    ages: tuple[int, int]
    location: str
    keywords: tuple[str, ...]
    reason: str


CAMPS = (
    CampOption(
        "Rec-PAC",
        "General recreation",
        (6, 12),
        "Various Schools",
        ("affordable", "scholarship", "general", "recreation", "sports"),
        "it is a highly affordable 6-week general recreation program and scholarships may be available.",
    ),
    CampOption(
        "Frying Pan Farm Hands",
        "Outdoors/Animals",
        (5, 10),
        "Herndon",
        ("animals", "farm", "outdoors", "nature"),
        "it fits children who like animals, farm activities, and outdoor learning.",
    ),
    CampOption(
        "Lake Fairfax Adventure Camp",
        "Outdoors/Sports",
        (9, 15),
        "Reston",
        ("sports", "outdoors", "hiking", "biking", "adventure"),
        "it fits high-energy kids who like hiking, biking, sports, and Water Mine access.",
    ),
    CampOption(
        "Spring Hill Splash & Sports",
        "Aquatics/Sports",
        (6, 12),
        "McLean",
        ("sports", "swim", "pool", "aquatics"),
        "it combines indoor sports with pool time.",
    ),
    CampOption(
        "STEM Robo-Creators",
        "Technology",
        (8, 14),
        "Centreville (Sully Hub)",
        ("stem", "ai", "tech", "robotics", "coding", "building"),
        "it is designed for robotics and block coding.",
    ),
    CampOption(
        "Ice Hockey Prep Camp",
        "Specialty Sports",
        (7, 14),
        "Mount Vernon",
        ("hockey", "ice", "skating", "sports"),
        "it provides intensive ice time, though full gear is required.",
    ),
    CampOption(
        "Fine Arts & Clay",
        "Arts/Creative",
        (7, 13),
        "Franconia",
        ("art", "arts", "creative", "clay", "painting", "pottery"),
        "it fits creative children who prefer painting, pottery, or a quieter studio.",
    ),
)


SOURCE_SNIPPETS = {
    "vehicle_taxes": SourceSnippet(
        id="vehicle_taxes",
        title="Vehicle Taxes & Fees",
        url="https://www.fairfaxcounty.gov/taxes/vehicles/",
        path="docs/raw/taxes_vehicles.html",
        quote=(
            "DTA's Personal Property and Business License Division assesses "
            "vehicles normally garaged or parked in Fairfax County."
        ),
    ),
    "vehicle_pay": SourceSnippet(
        id="vehicle_pay",
        title="Pay Vehicle Tax",
        url="https://www.fairfaxcounty.gov/dta_mobileepay/",
        path="docs/raw/taxes_vehicles.html",
        quote="The vehicle tax page links residents to Pay Vehicle Tax.",
    ),
    "tax_relief": SourceSnippet(
        id="tax_relief",
        title="Tax Relief",
        url="https://www.fairfaxcounty.gov/taxes/relief",
        path="docs/source_inventory.md",
        quote=(
            "Fairfax County provides tax relief information for eligible "
            "seniors, people with disabilities, and other qualifying residents."
        ),
    ),
    "code_report": SourceSnippet(
        id="code_report",
        title="How to Report a Violation to DCC",
        url="https://www.fairfaxcounty.gov/code/how-report-violation-dcc",
        path="docs/raw/code_report_violation.html",
        quote=(
            "Code Compliance is the route for neighborhood complaints and "
            "potential property or zoning violations."
        ),
    ),
    "plus": SourceSnippet(
        id="plus",
        title="PLUS Portal",
        url="https://plus.fairfaxcounty.gov/CitizenAccess/Welcome.aspx",
        path="docs/source_inventory.md",
        quote=(
            "The source inventory approves plus.fairfaxcounty.gov as a "
            "Fairfax-hosted routing source."
        ),
    ),
    "csp": SourceSnippet(
        id="csp",
        title="Coordinated Services Planning",
        url=(
            "https://www.fairfaxcounty.gov/neighborhood-community-services/"
            "coordinated-services-planning"
        ),
        path="docs/raw/hhs_coordinated_services_planning.html",
        quote=(
            "CSP connects residents to services including food, shelter, "
            "employment, financial assistance, healthcare, and other needs."
        ),
    ),
    "basic_needs": SourceSnippet(
        id="basic_needs",
        title="Basic Needs and Assistance",
        url=(
            "https://www.fairfaxcounty.gov/neighborhood-community-services/"
            "basic-needs-assistance"
        ),
        path="docs/raw/hhs_basic_needs_assistance.html",
        quote=(
            "Fairfax lists 703-222-0880 for assistance with food, shelter, "
            "employment, financial assistance, healthcare, and more."
        ),
    ),
    "affordable_housing": SourceSnippet(
        id="affordable_housing",
        title="Affordable Housing",
        url="https://www.fairfaxcounty.gov/housing/",
        path="docs/source_inventory.md",
        quote=(
            "Housing questions such as affordable housing, waitlists, and "
            "income-restricted properties should route to official Fairfax "
            "housing resources before eligibility assumptions are made."
        ),
    ),
    "non_emergency": SourceSnippet(
        id="non_emergency",
        title="Calling Non-Emergency",
        url="https://www.fairfaxcounty.gov/911/calling-non-emergency",
        path="docs/raw/public_safety_calling_non_emergency.html",
        quote=(
            "The public safety taxonomy distinguishes emergencies from "
            "non-emergency police, fire, and EMS contacts."
        ),
    ),
    "parks_camps": SourceSnippet(
        id="parks_camps",
        title="Fairfax County Park Authority Camps",
        url="https://www.fairfaxcounty.gov/parks/camps",
        path="docs/source_inventory.md",
        quote=(
            "Park Authority camps include spring and summer registration, "
            "with camp categories such as sports and science."
        ),
    ),
    "ncs_camps": SourceSnippet(
        id="ncs_camps",
        title="NCS Camps",
        url="https://www.fairfaxcounty.gov/neighborhood-community-services/camps",
        path="docs/source_inventory.md",
        quote=(
            "NCS offers youth and teen camps during school breaks, including "
            "sports, games, fitness, art, and STEM activities."
        ),
    ),
    "sully_sports_camp": SourceSnippet(
        id="sully_sports_camp",
        title="Sully Summer Sports Camp",
        url=(
            "https://www.fairfaxcounty.gov/neighborhood-community-services/"
            "sully-community-center/sports-camps"
        ),
        path="docs/source_inventory.md",
        quote=(
            "Sully Summer Sports Camp serves ages 5-12 and lists options "
            "including basketball, soccer, gymnastics, dance, and STEM & Play."
        ),
    ),
    "community_hubs": SourceSnippet(
        id="community_hubs",
        title="Neighborhood and Community Services Community Centers",
        url="https://www.fairfaxcounty.gov/neighborhood-community-services/",
        path="docs/source_inventory.md",
        quote=(
            "Neighborhood and Community Services routes residents to community "
            "centers, youth programming, family supports, and neighborhood hubs."
        ),
    ),
    "real_estate_taxes": SourceSnippet(
        id="real_estate_taxes",
        title="Real Estate Taxes",
        url="https://www.fairfaxcounty.gov/taxes/real-estate/",
        path="docs/raw/taxes_real_estate.html",
        quote="DTA routes real estate assessments, payments, and appeals.",
    ),
    "recycling": SourceSnippet(
        id="recycling",
        title="Recycling and Trash",
        url="https://www.fairfaxcounty.gov/publicworks/recycling-and-trash",
        path="docs/raw/fairfax_recycling_and_trash.html",
        quote="DPWES provides recycling, trash, disposal, and collection routing information.",
    ),
    "health": SourceSnippet(
        id="health",
        title="Health Department",
        url="https://www.fairfaxcounty.gov/health",
        path="docs/raw/health_home.html",
        quote="The Health Department is the official route for public health services.",
    ),
    "older_adults": SourceSnippet(
        id="older_adults",
        title="Older Adult Services",
        url="https://www.fairfaxcounty.gov/familyservices/older-adults",
        path="docs/source_inventory.md",
        quote=(
            "Older adult services route aging support, caregiver help, senior "
            "centers, nutrition programs, and aging-in-place questions."
        ),
    ),
    "childcare": SourceSnippet(
        id="childcare",
        title="Child Care Assistance and Referral",
        url="https://www.fairfaxcounty.gov/neighborhood-community-services/ccar",
        path="docs/source_inventory.md",
        quote="CCAR is the county route for childcare assistance and referral information.",
    ),
    "head_start": SourceSnippet(
        id="head_start",
        title="Head Start",
        url="https://www.fairfaxcounty.gov/office-for-children/head-start",
        path="docs/source_inventory.md",
        quote="Head Start and early childhood programs support eligible young children and families.",
    ),
    "csb": SourceSnippet(
        id="csb",
        title="Community Services Board",
        url="https://www.fairfaxcounty.gov/community-services-board",
        path="docs/raw/csb_home.html",
        quote="CSB routes behavioral health, substance use, developmental disability, and crisis services.",
    ),
    "transportation": SourceSnippet(
        id="transportation",
        title="Transportation",
        url="https://www.fairfaxcounty.gov/transportation/",
        path="docs/raw/transportation_home.html",
        quote="FCDOT routes transportation, road, parking, transit, and commuting questions.",
    ),
    "lds": SourceSnippet(
        id="lds",
        title="Land Development Services",
        url="https://www.fairfaxcounty.gov/landdevelopment",
        path="docs/raw/land_development_services.html",
        quote="LDS and PLUS route building permits, inspections, zoning, and land development questions.",
    ),
    "water_sewer": SourceSnippet(
        id="water_sewer",
        title="Public Works and Utilities",
        url="https://www.fairfaxcounty.gov/publicworks",
        path="docs/source_inventory.md",
        quote=(
            "Public Works and Environmental Services routes public works, "
            "utilities, wastewater, and environmental service questions."
        ),
    ),
    "public_safety": SourceSnippet(
        id="public_safety",
        title="Calling Non-Emergency",
        url="https://www.fairfaxcounty.gov/911/calling-non-emergency",
        path="docs/raw/public_safety_calling_non_emergency.html",
        quote="Official guidance distinguishes emergency calls from non-emergency police, fire, and EMS contacts.",
    ),
    "fire_rescue": SourceSnippet(
        id="fire_rescue",
        title="Fire and Rescue",
        url="https://www.fairfaxcounty.gov/fire-ems",
        path="docs/source_inventory.md",
        quote="Fire and Rescue routes fire, EMS, fire prevention, inspections, and community outreach.",
    ),
}


ROUTES = {
    "car_tax": Route(
        key="car_tax",
        label="Taxes and fees: vehicle taxes",
        urgency="Routine unless there is a deadline, penalty, or account lockout.",
        destination="Fairfax County Department of Tax Administration",
        next_steps=(
            "Use the Vehicle Taxes & Fees page to confirm the correct subtopic.",
            "For payment, use the official Pay Vehicle Tax link.",
            "For senior or disability-related relief, review DTA tax relief information before assuming eligibility.",
            "For account-specific issues, route to DTA rather than estimating a bill.",
        ),
        sources=("vehicle_taxes", "vehicle_pay", "tax_relief"),
    ),
    "unpermitted_construction": Route(
        key="unpermitted_construction",
        label="Code compliance / neighborhood complaint",
        urgency=(
            "Routine for suspected unpermitted work; urgent if there is active "
            "danger, blocked access, fire, injury, or a crime in progress."
        ),
        destination="Department of Code Compliance, with PLUS as the routing portal",
        next_steps=(
            "Collect address, observed activity, timing, and photos if available.",
            "Use the Code Compliance violation-reporting page for the complaint route.",
            "Use PLUS when the user is ready to submit or track a case.",
        ),
        sources=("code_report", "plus"),
    ),
    "housing_safety": Route(
        key="housing_safety",
        label="Basic needs / housing or safety help",
        urgency=(
            "High sensitivity. If anyone is in immediate danger, call 911. "
            "For urgent shelter or basic-needs help, route to CSP."
        ),
        destination="Coordinated Services Planning at 703-222-0880",
        next_steps=(
            "Ask whether anyone is in immediate danger or needs emergency medical help.",
            "If not immediate danger, direct the resident to call CSP at 703-222-0880.",
            "For affordable housing, LIHTC, waitlists, shelters, or homelessness intake, route to official Fairfax housing/HHS resources without promising eligibility.",
            "Do not make eligibility promises; CSP can assess needs and connect resources.",
        ),
        sources=("csp", "basic_needs", "affordable_housing", "non_emergency"),
    ),
    "summer_camps": Route(
        key="summer_camps",
        label="Parks and recreation / youth camps",
        urgency=(
            "Routine, but time-sensitive because camp seats and registration "
            "windows can fill quickly."
        ),
        destination=(
            "Fairfax County Park Authority camps and Neighborhood and "
            "Community Services camps"
        ),
        next_steps=(
            "For a 9-year-old, start with Park Authority camp search filters for age, week, location, sports, and science/STEM.",
            "Also check NCS Camp Fairfax and NCS camps if the family wants school/community-center locations or reduced-fee options.",
            "For a sports plus STEM fit, review Sully Summer Sports Camp options such as STEM & Play or multi-sport offerings if the location works.",
            "For community hubs, route Sully, Lorton, and other NCS community center questions to Neighborhood and Community Services.",
            "Ask for preferred ZIP code, dates, budget, transportation needs, and whether the child wants competitive sports, casual play, coding, robotics, or science.",
        ),
        sources=("parks_camps", "ncs_camps", "sully_sports_camp", "community_hubs"),
    ),
    "real_estate_tax": Route(
        key="real_estate_tax",
        label="Taxes and revenue: real estate tax",
        urgency="Routine unless there is a payment or appeal deadline.",
        destination="Fairfax County Department of Tax Administration",
        next_steps=(
            "Use DTA real estate pages for assessments, payments, and appeals.",
            "For seniors or people with disabilities, review tax relief information before assuming eligibility.",
        ),
        sources=("real_estate_taxes", "tax_relief"),
    ),
    "trash_recycling": Route(
        key="trash_recycling",
        label="Public works and utilities: trash, recycling, disposal",
        urgency="Routine unless there is a public health, roadway, or safety hazard.",
        destination="DPWES / collection provider route",
        next_steps=(
            "Use ZIP code, neighborhood, or collection provider to determine county vs private collection.",
            "Use the Recycling and Trash page for missed pickup, purple glass bins, hazardous waste, and special item routing.",
        ),
        sources=("recycling",),
    ),
    "public_health": Route(
        key="public_health",
        label="Health and human services: public health",
        urgency="Escalate medical emergencies immediately.",
        destination="Fairfax County Health Department",
        next_steps=(
            "Route immunization clinics, dental care for uninsured, WIC, environmental health, or public health questions to the Health Department.",
            "Do not provide medical diagnosis; for emergency symptoms call emergency services.",
        ),
        sources=("health",),
    ),
    "older_adults": Route(
        key="older_adults",
        label="Health and human services: older adult services",
        urgency="Routine unless there is immediate safety, medical, neglect, or abuse risk.",
        destination="Fairfax County older adult services and Neighborhood and Community Services",
        next_steps=(
            "Use ZIP code and general age range only; do not ask for full names or exact addresses in the demo.",
            "Route aging-in-place, caregiver help, senior centers, Meals on Wheels, and nutrition questions to older adult services.",
            "Escalate immediate safety, medical, abuse, or neglect concerns to emergency or protective channels.",
        ),
        sources=("older_adults", "basic_needs"),
    ),
    "childcare": Route(
        key="childcare",
        label="Health and human services: childcare and early education",
        urgency="Routine unless there is an immediate child safety concern.",
        destination="Child Care Assistance and Referral and Head Start",
        next_steps=(
            "Use child age, household size, approximate income range, and ZIP code as non-PII routing context.",
            "Start with CCAR for subsidized childcare/referrals and Head Start for early childhood program questions.",
            "Do not promise eligibility; official program staff must confirm requirements and availability.",
        ),
        sources=("childcare", "head_start"),
    ),
    "mental_health": Route(
        key="mental_health",
        label="Health and human services: CSB behavioral health",
        urgency="For self-harm, violence, overdose, or immediate danger, call 911 or CSB Emergency Services at 703-573-5679.",
        destination="Community Services Board",
        next_steps=(
            "For crisis, self-harm, severe mental health crisis, violence, or overdose risk: call 911 or CSB Emergency Services at 703-573-5679 now.",
            "For non-emergency behavioral health, addiction recovery, opioid support, or developmental disability services, start with CSB.",
        ),
        sources=("csb",),
    ),
    "transportation": Route(
        key="transportation",
        label="Transportation: FCDOT, Fairfax Connector, Fastran, roads",
        urgency="Routine unless there is an active roadway hazard or immediate safety issue.",
        destination="FCDOT, Fairfax Connector, or Fastran depending on need",
        next_steps=(
            "Use ZIP code or nearest cross street to narrow Fairfax Connector, Fastran, road ownership, potholes, and commuter options.",
            "Clarify whether the road issue is county-maintained, VDOT, private, or another provider.",
        ),
        sources=("transportation",),
    ),
    "water_sewer": Route(
        key="water_sewer",
        label="Public works and utilities: water or sewer",
        urgency="Urgent if there is flooding, sewage backup, roadway hazard, or public health risk.",
        destination="DPWES, Fairfax Water, or the relevant utility provider",
        next_steps=(
            "Use ZIP code and nearest cross street or neighborhood to distinguish county sewer, Fairfax Water, or another provider.",
            "For sewer backups, flooding, or hazards, route to the utility or emergency channel rather than waiting for normal service navigation.",
        ),
        sources=("water_sewer",),
    ),
    "community_hubs": Route(
        key="community_hubs",
        label="Parks, recreation, and youth: community hubs",
        urgency="Routine unless there is an immediate safety or facility hazard.",
        destination="Neighborhood and Community Services community centers",
        next_steps=(
            "Ask for ZIP code, general neighborhood, age group, schedule, and program interest without collecting full names or exact addresses.",
            "Route Sully, Lorton, and other community-center questions to Neighborhood and Community Services.",
        ),
        sources=("community_hubs", "ncs_camps"),
    ),
    "permits": Route(
        key="permits",
        label="Land use, permits, and code: LDS / DCC / PLUS",
        urgency="Routine unless there is an immediate construction or safety hazard.",
        destination="Land Development Services and PLUS",
        next_steps=(
            "Use PLUS for permit, inspection, zoning, and property-line workflow routing.",
            "For code complaints, use DCC and avoid relying on this tool for code interpretation.",
        ),
        sources=("lds", "plus", "code_report"),
    ),
    "public_safety": Route(
        key="public_safety",
        label="Public safety: emergency, non-emergency, animal control, fire/rescue",
        urgency="Immediate danger, active violence, fire, or medical emergency should go to 911.",
        destination="911 for emergencies; non-emergency public safety or Fire and Rescue for routine matters",
        next_steps=(
            "For immediate danger, active crime, fire, or medical emergency: call 911.",
            "For routine police reports, noise complaints, animal control, fire inspections, or community outreach, use the official non-emergency route.",
        ),
        sources=("public_safety", "fire_rescue"),
    ),
    "general": Route(
        key="general",
        label="General Fairfax service navigation",
        urgency="Clarify the service area and whether the situation is urgent.",
        destination="Fairfax County official service pages",
        next_steps=(
            "Ask one short clarifying question if the service area is unclear.",
            "Route to an official county page before offering procedural detail.",
            "Escalate emergencies, safety risks, crisis needs, and account-specific issues.",
        ),
        sources=("csp", "vehicle_taxes", "code_report"),
    ),
}


def _content_to_text(content: types.Content | None) -> str:
    if not content or not content.parts:
        return ""
    return " ".join(part.text or "" for part in content.parts).strip()


def route_request(message: str) -> Route:
    """Routes a user message into the demo service catalog."""
    query = message.lower()
    if any(
        term in query
        for term in (
            "violence",
            "self-harm",
            "suicide",
            "kill myself",
            "immediate danger",
            "weapon",
            "overdose",
            "severe crisis",
            "mental",
            "csb",
            "addiction",
            "opioid",
        )
    ):
        return ROUTES["mental_health"]
    if any(
        term in query
        for term in (
            "childcare",
            "child care",
            "subsidized childcare",
            "head start",
            "early education",
            "preschool",
            "daycare",
        )
    ):
        return ROUTES["childcare"]
    if any(
        term in query
        for term in (
            "older adult",
            "senior center",
            "senior services",
            "aging",
            "aging in place",
            "meals on wheels",
            "caregiver",
        )
    ):
        return ROUTES["older_adults"]
    if any(
        term in query
        for term in (
            "summer camp",
            "camp",
            "sports camp",
            "stem",
            "steam",
            "robotics",
            "coding",
            "technology",
            "9 year old",
            "nine year old",
        )
    ):
        return ROUTES["summer_camps"]
    if any(
        term in query
        for term in ("real estate tax", "property tax", "assessment", "appeal assessment")
    ):
        return ROUTES["real_estate_tax"]
    if any(term in query for term in ("car tax", "vehicle tax", "vehicle taxes")):
        return ROUTES["car_tax"]
    if any(
        term in query
        for term in ("permit", "zoning", "property line", "inspection", "plus")
    ):
        return ROUTES["permits"]
    if any(
        term in query
        for term in (
            "unpermitted",
            "construction",
            "building without",
            "code violation",
            "neighbor built",
        )
    ):
        return ROUTES["unpermitted_construction"]
    if any(
        term in query
        for term in (
            "housing",
            "shelter",
            "homeless",
            "homelessness",
            "eviction",
            "unsafe",
            "danger",
            "food",
            "utility",
            "rent",
            "domestic",
            "affordable housing",
            "lihtc",
            "waitlist",
            "wait list",
        )
    ):
        return ROUTES["housing_safety"]
    if any(
        term in query
        for term in ("trash", "recycling", "missed pickup", "purple glass", "hazardous waste")
    ):
        return ROUTES["trash_recycling"]
    if any(
        term in query
        for term in (
            "water",
            "sewer",
            "sewage",
            "wastewater",
            "fairfax water",
            "sewer backup",
            "flooding",
        )
    ):
        return ROUTES["water_sewer"]
    if any(term in query for term in ("health", "clinic", "wic", "immunization", "dental")):
        return ROUTES["public_health"]
    if any(
        term in query
        for term in (
            "community hub",
            "community center",
            "sully",
            "lorton",
            "neighborhood center",
        )
    ):
        return ROUTES["community_hubs"]
    if any(
        term in query
        for term in ("transportation", "connector", "fastran", "pothole", "bus", "parking")
    ):
        return ROUTES["transportation"]
    if any(
        term in query
        for term in ("police", "noise", "animal control", "fire", "rescue", "non-emergency", "public safety")
    ):
        return ROUTES["public_safety"]
    return ROUTES["general"]


def _score_camp(camp: CampOption, query: str, child_age: int = 9) -> int:
    score = 0
    if camp.ages[0] <= child_age <= camp.ages[1]:
        score += 6
    for keyword in camp.keywords:
        if keyword in query:
            score += 3
    if "low income" in query or "affordable" in query or "budget" in query:
        if camp.name == "Rec-PAC":
            score += 4
    return score


def _camp_recommendations(message: str) -> list[CampOption]:
    query = message.lower()
    child_age = 9
    for candidate in range(3, 19):
        if f"{candidate}-year" in query or f"{candidate} year" in query:
            child_age = candidate
            break
    return sorted(CAMPS, key=lambda camp: _score_camp(camp, query, child_age), reverse=True)[
        :3
    ]


def generate_response(message: str) -> str:
    """Builds a deterministic, source-grounded navigator response."""
    route = route_request(message)
    citations = [SOURCE_SNIPPETS[source_id] for source_id in route.sources]
    camp_matches = _camp_recommendations(message) if route.key == "summer_camps" else []

    lines = [
        "I hear you. I will route this without asking for names or exact home addresses.",
        f"Route: {route.label}",
        f"Destination: {route.destination}",
        f"Urgency: {route.urgency}",
        "",
        "Recommended next steps:",
    ]
    if camp_matches:
        top = camp_matches[0]
        lines.extend(
            [
                (
                    f"- Primary camp recommendation: {top.name} ({top.focus}) in "
                    f"{top.location}. I recommend it because {top.reason}"
                ),
                (
                    "- Other good fits: "
                    + "; ".join(
                        f"{camp.name} in {camp.location}" for camp in camp_matches[1:]
                    )
                    + "."
                ),
                "- Next steps: search the camp name in Parktakes, then confirm age eligibility, dates, location, cost, extended care, gear requirements, and seat availability.",
            ]
        )
    else:
        lines.extend(f"- {step}" for step in route.next_steps)
    lines.extend(
        [
            "",
            "Citations:",
            *(
                f"- [{source.id}] {source.title}: {source.quote} "
                f"({source.url}; local snapshot: {source.path})"
                for source in citations
            ),
            "",
            "Demo prompts to try:",
            "- I need help with my Fairfax car tax bill.",
            "- My neighbor is doing unpermitted construction. What should I do?",
            "- I need urgent housing or safety help tonight.",
            "- Are there summer camps for my 9-year-old who likes sports and AI/STEM?",
        ]
    )
    return "\n".join(lines)


class FairfaxServiceNavigatorAgent(BaseAgent):
    """Mock-first ADK agent for the Fairfax Resource Navigator prototype."""

    @override
    async def _run_async_impl(
        self, ctx: InvocationContext
    ) -> AsyncGenerator[Event, None]:
        response = generate_response(_content_to_text(ctx.user_content))
        yield Event(
            invocation_id=ctx.invocation_id,
            author=self.name,
            branch=ctx.branch,
            content=types.Content(
                role="model",
                parts=[types.Part.from_text(text=response)],
            ),
        )

    @override
    async def _run_live_impl(
        self, ctx: InvocationContext
    ) -> AsyncGenerator[Event, None]:
        async for event in self._run_async_impl(ctx):
            yield event


root_agent = FairfaxServiceNavigatorAgent(
    name="fairfax_resource_navigator",
    description=(
        "Routes Fairfax County resident service questions to official sources "
        "with conservative urgency handling and citations."
    ),
)

app = App(
    root_agent=root_agent,
    name="app",
)

const sources = {
  parksCamps: {
    title: 'Fairfax County Park Authority Camps',
    url: 'https://www.fairfaxcounty.gov/parks/camps',
    quote:
      'Spring and summer camp registration is open, with categories including sports and science.',
  },
  ncsCamps: {
    title: 'NCS Camps',
    url: 'https://www.fairfaxcounty.gov/neighborhood-community-services/camps',
    quote:
      'NCS offers youth and teen camps during school breaks, including sports, games, fitness, art, and STEM activities.',
  },
  sullySports: {
    title: 'Sully Summer Sports Camp',
    url: 'https://www.fairfaxcounty.gov/neighborhood-community-services/sully-community-center/sports-camps',
    quote:
      'Sully serves ages 5-12 and lists basketball, soccer, gymnastics, dance, and STEM & Play options.',
  },
  vehicleTaxes: {
    title: 'Vehicle Taxes & Fees',
    url: 'https://www.fairfaxcounty.gov/taxes/vehicles/',
    quote:
      'DTA assesses vehicles normally garaged or parked in Fairfax County.',
  },
  codeReport: {
    title: 'How to Report a Violation to DCC',
    url: 'https://www.fairfaxcounty.gov/code/how-report-violation-dcc',
    quote:
      'Code Compliance is the route for neighborhood complaints and potential property or zoning violations.',
  },
  csp: {
    title: 'Coordinated Services Planning',
    url: 'https://www.fairfaxcounty.gov/neighborhood-community-services/coordinated-services-planning',
    quote:
      'CSP connects residents to food, shelter, employment, financial assistance, healthcare, and other needs.',
  },
  basicNeeds: {
    title: 'Basic Needs and Assistance',
    url: 'https://www.fairfaxcounty.gov/neighborhood-community-services/basic-needs-assistance',
    quote:
      'Fairfax lists assistance for food, shelter, employment, financial assistance, healthcare, and other needs.',
  },
  recycling: {
    title: 'Recycling and Trash',
    url: 'https://www.fairfaxcounty.gov/publicworks/recycling-and-trash',
    quote:
      'Public Works and Environmental Services provides Fairfax County recycling, trash, disposal, and collection routing information.',
  },
  transportation: {
    title: 'Transportation',
    url: 'https://www.fairfaxcounty.gov/transportation/',
    quote:
      'The transportation homepage routes residents to county transportation programs, projects, roads, commuting, and related services.',
  },
  health: {
    title: 'Health Department',
    url: 'https://www.fairfaxcounty.gov/health',
    quote:
      'The Health Department is the official route for public health services and health-related county information.',
  },
  realEstateTaxes: {
    title: 'Real Estate Taxes',
    url: 'https://www.fairfaxcounty.gov/taxes/real-estate/',
    quote:
      'DTA routes real estate assessments, payments, and appeals.',
  },
  taxRelief: {
    title: 'Tax Relief',
    url: 'https://www.fairfaxcounty.gov/taxes/relief',
    quote:
      'Fairfax County provides tax relief information for eligible seniors, people with disabilities, and other qualifying residents.',
  },
  csb: {
    title: 'Community Services Board',
    url: 'https://www.fairfaxcounty.gov/community-services-board',
    quote:
      'CSB routes behavioral health, developmental disability, substance use, opioid support, and crisis services.',
  },
  olderAdults: {
    title: 'Older Adult Services',
    url: 'https://www.fairfaxcounty.gov/familyservices/older-adults',
    quote:
      'Fairfax County routes older adult services such as aging support, caregiver help, senior centers, and nutrition programs.',
  },
  childcare: {
    title: 'Child Care Assistance and Referral',
    url: 'https://www.fairfaxcounty.gov/neighborhood-community-services/ccar',
    quote:
      'CCAR is the county route for childcare assistance and referral information.',
  },
  headStart: {
    title: 'Head Start',
    url: 'https://www.fairfaxcounty.gov/office-for-children/head-start',
    quote:
      'Head Start and early childhood programs support eligible young children and families.',
  },
  plus: {
    title: 'PLUS',
    url: 'https://www.fairfaxcounty.gov/plan2build/plus',
    quote:
      'PLUS is Fairfax County’s planning, permitting, inspections, and land use system.',
  },
  lds: {
    title: 'Land Development Services',
    url: 'https://www.fairfaxcounty.gov/landdevelopment',
    quote:
      'Land Development Services routes building permits, inspections, and land development questions.',
  },
  publicSafety: {
    title: 'Calling Non-Emergency',
    url: 'https://www.fairfaxcounty.gov/911/calling-non-emergency',
    quote:
      'Official public safety guidance distinguishes emergency calls from non-emergency police, fire, and EMS contacts.',
  },
  fireRescue: {
    title: 'Fire and Rescue',
    url: 'https://www.fairfaxcounty.gov/fire-ems',
    quote:
      'Fire and Rescue routes fire, EMS, fire prevention, inspections, and community outreach.',
  },
  waterSewer: {
    title: 'Public Works and Utilities',
    url: 'https://www.fairfaxcounty.gov/publicworks',
    quote:
      'Public Works and Environmental Services routes public works, utilities, wastewater, and environmental service questions.',
  },
  communityHubs: {
    title: 'Neighborhood and Community Services',
    url: 'https://www.fairfaxcounty.gov/neighborhood-community-services',
    quote:
      'NCS routes residents to neighborhood community centers, youth programming, family supports, and community hubs.',
  },
};

const campCatalog = [
  {
    name: 'Rec-PAC',
    focus: 'General recreation',
    ages: [6, 12],
    location: 'Various schools',
    bestFor: ['affordable', 'general activities', 'reduced fees', 'sports'],
    reason:
      'it is a highly affordable 6-week general recreation program and scholarships may be available.',
  },
  {
    name: 'Frying Pan Farm Hands',
    focus: 'Outdoors / animals',
    ages: [5, 10],
    location: 'Herndon',
    bestFor: ['animals', 'outdoors', 'nature', 'farm'],
    reason:
      'it fits younger children who like animals, farm activities, and outdoor learning.',
  },
  {
    name: 'Lake Fairfax Adventure Camp',
    focus: 'Outdoors / sports',
    ages: [9, 15],
    location: 'Reston',
    bestFor: ['sports', 'outdoors', 'high energy', 'biking', 'hiking'],
    reason:
      'it fits high-energy kids who like outdoor sports, hiking, biking, and Water Mine-style activities.',
  },
  {
    name: 'Spring Hill Splash & Sports',
    focus: 'Aquatics / sports',
    ages: [6, 12],
    location: 'McLean',
    bestFor: ['sports', 'aquatics', 'swimming', 'pool'],
    reason:
      'it combines indoor sports with pool time, which is a strong match for sports and swimming interests.',
  },
  {
    name: 'STEM Robo-Creators',
    focus: 'Technology',
    ages: [8, 14],
    location: 'Centreville / Sully',
    bestFor: ['stem', 'ai/tech', 'technology', 'robotics', 'coding', 'building'],
    reason:
      'it is designed for robotics and block coding, so it matches children who like building, AI, technology, or STEM.',
  },
  {
    name: 'Ice Hockey Prep Camp',
    focus: 'Specialty sports',
    ages: [7, 14],
    location: 'Mount Vernon',
    bestFor: ['hockey', 'ice hockey', 'sports', 'skating'],
    reason:
      'it is a specialty sports camp with intensive ice time, but full gear is required.',
  },
  {
    name: 'Fine Arts & Clay',
    focus: 'Arts / creative',
    ages: [7, 13],
    location: 'Franconia',
    bestFor: ['art', 'arts', 'creative', 'clay', 'painting', 'pottery'],
    reason:
      'it fits creative children who prefer painting, pottery, or a quieter studio setting.',
  },
];

function scoreCamp(camp, profile) {
  const age = Number(profile.age);
  const interests = profile.interests.map((item) => item.toLowerCase());
  let score = 0;
  if (age >= camp.ages[0] && age <= camp.ages[1]) score += 6;
  if (profile.area !== 'no area preference' && camp.location.includes(profile.area.split(' / ')[0])) {
    score += 3;
  }
  if (profile.income === 'under $35k' || profile.income === '$35k-$75k') {
    if (camp.name === 'Rec-PAC') score += 4;
  }
  for (const interest of interests) {
    if (camp.bestFor.some((fit) => interest.includes(fit) || fit.includes(interest))) {
      score += 3;
    }
  }
  return score;
}

function matchCamps(profile) {
  return [...campCatalog]
    .map((camp) => ({ ...camp, score: scoreCamp(camp, profile) }))
    .sort((a, b) => b.score - a.score)
    .slice(0, 3);
}

const routes = {
  camps: {
    title: 'Parks and recreation / youth camps',
    destination: 'Fairfax County Park Authority camps, Parktakes, and NCS camps',
    urgency: 'Routine, but time-sensitive because camp seats can fill quickly.',
    confidence: 88,
    sourceKeys: ['parksCamps', 'ncsCamps', 'sullySports', 'communityHubs'],
    steps: (profile) => {
      const matches = matchCamps(profile);
      const top = matches[0];
      return [
        `Primary recommendation: ${top.name} (${top.focus}) in ${top.location}. Because your child is ${profile.age} and likes ${profile.interests.join(', ')}, I recommend it because ${top.reason}`,
        `Other good fits: ${matches
          .slice(1)
          .map((camp) => `${camp.name} in ${camp.location}`)
          .join('; ')}.`,
        profile.zip
          ? `Use ZIP code ${profile.zip} and preferred area "${profile.area}" to narrow Parktakes results by nearby sites and transportation needs.`
          : 'Add the household ZIP code to narrow Parktakes results by nearby sites and transportation needs.',
        'For community hub programs, check Sully, Lorton, and other NCS community centers for age-appropriate neighborhood activities.',
        profile.income !== 'not shared'
          ? `Because the household income range is ${profile.income}, check Rec-PAC and NCS options for lower-cost or scholarship-supported programming.`
          : 'If cost is a concern, check Rec-PAC, NCS, and scholarship-supported options before registration.',
        'Next steps: search the camp name in Parktakes, then confirm age eligibility, dates, location, cost, extended care, gear requirements, and seat availability.',
      ];
    },
  },
  carTax: {
    title: 'Taxes and revenue / DTA',
    destination: 'Fairfax County Department of Tax Administration',
    urgency: 'Routine unless there is a deadline, penalty, or account lockout.',
    confidence: 90,
    sourceKeys: ['vehicleTaxes'],
    steps: (profile) => [
      'Use the Vehicle Taxes & Fees page to choose payment, registration, appeal, or account help.',
      profile.zip ? `Confirm the vehicle is normally garaged or parked in Fairfax County near ZIP ${profile.zip}.` : 'Confirm the vehicle is normally garaged or parked in Fairfax County.',
      'For account-specific questions, contact DTA rather than estimating the bill here.',
      'Keep the vehicle, bill, or MyFairfax account details ready before contacting the county.',
    ],
  },
  realEstateTax: {
    title: 'Taxes and revenue / real estate tax',
    destination: 'Fairfax County Department of Tax Administration',
    urgency: 'Routine unless there is a payment deadline, appeal deadline, or account issue.',
    confidence: 86,
    sourceKeys: ['realEstateTaxes', 'taxRelief'],
    steps: (profile) => [
      profile.zip ? `Use ZIP ${profile.zip} as location context; DTA will need parcel/account details in its official system.` : 'Use DTA real estate pages for assessments, payments, and appeals.',
      'For seniors or people with disabilities, review tax relief information before making assumptions about eligibility.',
    ],
  },
  code: {
    title: 'Code compliance / neighborhood complaint',
    destination: 'Department of Code Compliance',
    urgency: 'Routine unless there is active danger, injury, blocked access, fire, or crime in progress.',
    confidence: 86,
    sourceKeys: ['codeReport'],
    steps: (profile) => [
      'Use ZIP code, neighborhood, cross street, or the official complaint form. Avoid entering names or exact home addresses in this preview.',
      'Use the Code Compliance violation-reporting page or PLUS route for tall grass, hoarding, illegal construction, zoning, or unpermitted boarding house concerns.',
    ],
  },
  permits: {
    title: 'Land use, permits, and zoning',
    destination: 'Land Development Services and PLUS',
    urgency: 'Routine unless there is an immediate construction or safety hazard.',
    confidence: 84,
    sourceKeys: ['plus', 'lds'],
    steps: (profile) => [
      profile.zip ? `Use ZIP ${profile.zip}, neighborhood, or parcel context to choose the correct PLUS/LDS route.` : 'Use PLUS for permit, inspection, zoning, and property-line workflow routing.',
      'For building permits or property-line questions, start with LDS/PLUS and avoid relying on this tool for code interpretation.',
    ],
  },
  housing: {
    title: 'Basic needs / housing or safety help',
    destination: 'Coordinated Services Planning at 703-222-0880',
    urgency: 'High sensitivity. Call 911 if anyone is in immediate danger.',
    confidence: 92,
    sourceKeys: ['csp'],
    steps: (profile) => [
      'If not immediate danger, call Coordinated Services Planning at 703-222-0880.',
      `For emergency food, rent assistance, utilities, shelters, homelessness intake, affordable housing, or LIHTC/waitlist questions, share household size (${profile.householdSize}), number of kids (${profile.kids}), and income range (${profile.income}) only with county staff if comfortable.`,
    ],
  },
  communityHubs: {
    title: 'Parks, recreation, and youth / community hubs',
    destination: 'Neighborhood and Community Services community centers',
    urgency: 'Routine unless there is an immediate safety or facility hazard.',
    confidence: 78,
    sourceKeys: ['communityHubs', 'ncsCamps'],
    steps: (profile) => [
      profile.zip
        ? `Use ZIP ${profile.zip}, general neighborhood, age group, and schedule needs to find the closest Sully, Lorton, or other NCS community-center option.`
        : 'Use ZIP code, general neighborhood, age group, and schedule needs to find the closest Sully, Lorton, or other NCS community-center option.',
      'Route program availability, youth activities, family supports, and community hub questions to Neighborhood and Community Services.',
    ],
  },
  mentalHealth: {
    title: 'Health and human services / CSB behavioral health',
    destination: 'Community Services Board; emergency services at 703-573-5679',
    urgency: 'High sensitivity. For self-harm, violence, overdose, or immediate danger, call 911 or CSB Emergency Services at 703-573-5679.',
    confidence: 91,
    sourceKeys: ['csb'],
    steps: () => [
      'For crisis, self-harm, severe mental health crisis, violence, or overdose risk: call 911 or CSB Emergency Services at 703-573-5679 now.',
      'For non-emergency behavioral health, addiction recovery, opioid support, or developmental disability services, start with the CSB.',
    ],
  },
  olderAdults: {
    title: 'Health and human services / older adult services',
    destination: 'Fairfax County older adult services and Neighborhood and Community Services',
    urgency: 'Routine unless there is immediate safety, medical, neglect, or abuse risk.',
    confidence: 80,
    sourceKeys: ['olderAdults', 'basicNeeds'],
    steps: (profile) => [
      `Use adult age (${profile.parentAge}) and ZIP ${profile.zip || 'not shared'} to route aging-in-place, senior center, caregiver, or Meals on Wheels questions.`,
      'For immediate safety, medical, abuse, or neglect concerns, use emergency or adult protective routes instead of this preview.',
    ],
  },
  childcare: {
    title: 'Health and human services / childcare and early education',
    destination: 'Child Care Assistance and Referral; Head Start',
    urgency: 'Routine unless there is an immediate child safety concern.',
    confidence: 82,
    sourceKeys: ['childcare', 'headStart'],
    steps: (profile) => [
      `Use number of kids (${profile.kids}), child age (${profile.age}), household size (${profile.householdSize}), and income range (${profile.income}) as non-PII routing context.`,
      'Start with CCAR for subsidized childcare/referrals and Head Start for early childhood program questions.',
    ],
  },
  trash: {
    title: 'Public works and utilities / trash, recycling, or disposal',
    destination: 'DPWES / collection provider route',
    urgency: 'Routine unless there is a public health, roadway, or safety hazard.',
    confidence: 82,
    sourceKeys: ['recycling'],
    steps: (profile) => [
      profile.zip
        ? `Use ZIP ${profile.zip}, collection provider, or neighborhood to check whether service is county-collected or privately collected.`
        : 'Start with ZIP code, neighborhood, or collection provider to determine county vs private collection.',
      'Use the official Recycling and Trash page for missed pickup, purple glass bins, hazardous waste disposal, and special item routing.',
    ],
  },
  waterSewer: {
    title: 'Public works and utilities / water or sewer',
    destination: 'DPWES, Fairfax Water, or the relevant utility provider',
    urgency: 'Urgent if there is flooding, sewage backup, road hazard, or public health risk.',
    confidence: 72,
    sourceKeys: ['waterSewer'],
    steps: (profile) => [
      profile.zip ? `Use ZIP ${profile.zip} and nearest cross street/neighborhood to distinguish county sewer, Fairfax Water, or another utility provider.` : 'Use ZIP code and nearest cross street/neighborhood to distinguish county sewer, Fairfax Water, or another utility provider.',
      'For sewer backups, flooding, or hazards, route to the utility/emergency channel rather than waiting for normal service navigation.',
    ],
  },
  health: {
    title: 'Public health services',
    destination: 'Fairfax County Health Department',
    urgency: 'Escalate medical emergencies immediately; routine service questions can use official Health Department routes.',
    confidence: 76,
    sourceKeys: ['health'],
    steps: (profile) => [
      profile.zip ? `Use ZIP code ${profile.zip} to identify nearby public health service locations where applicable.` : 'Add ZIP code to identify nearby public health service locations where applicable.',
      'Route immunization clinics, dental care for uninsured, WIC, environmental health, or public health questions to the Health Department.',
      'Do not provide medical diagnosis. For emergency symptoms, call emergency services.',
    ],
  },
  transportation: {
    title: 'Transportation, roads, parking, or commuting',
    destination: 'FCDOT, Fairfax Connector, or Fastran depending on need',
    urgency: 'Routine unless there is an active roadway hazard or immediate safety issue.',
    confidence: 74,
    sourceKeys: ['transportation'],
    steps: (profile) => [
      profile.zip ? `Use ZIP ${profile.zip} to narrow Fairfax Connector, Fastran, road ownership, potholes, and commuter options.` : 'Add ZIP code or nearest cross street to narrow Fairfax Connector, Fastran, road ownership, potholes, and commuter options.',
      'Clarify whether the road issue is county-maintained, VDOT, private, or another provider before promising a repair path.',
    ],
  },
  publicSafety: {
    title: 'Public safety / non-emergency, animal control, fire and rescue',
    destination: '911 for emergencies; non-emergency public safety or Fire and Rescue for routine matters',
    urgency: 'Immediate danger, active violence, fire, or medical emergency should go to 911.',
    confidence: 88,
    sourceKeys: ['publicSafety', 'fireRescue'],
    steps: () => [
      'For immediate danger, active crime, fire, or medical emergency: call 911.',
      'For routine police reports, noise complaints, animal control, fire inspections, or community outreach, use the official non-emergency or Fire and Rescue route.',
    ],
  },
  general: {
    title: 'General Fairfax resource navigation',
    destination: 'Official Fairfax County service pages',
    urgency: 'Clarify the service area and whether the situation is urgent.',
    confidence: 62,
    sourceKeys: ['csp', 'basicNeeds', 'vehicleTaxes'],
    steps: (profile) => [
      profile.zip ? `Use ZIP code ${profile.zip} as location context for nearby county services.` : 'Add the household ZIP code to narrow nearby county resources.',
      profile.services.length
        ? `Requested service areas: ${profile.services.join(', ')}.`
        : 'Select service areas in the client profile to improve routing.',
      'Ask one clarifying question about the service area, location, and urgency.',
      'Route to an official county page before giving procedural details.',
      'Escalate emergencies, safety risks, crisis needs, and account-specific issues.',
    ],
  },
};

const messages = document.querySelector('#messages');
const appShell = document.querySelector('.app-shell');
const loginOverlay = document.querySelector('#loginOverlay');
const loginForm = document.querySelector('#loginForm');
const form = document.querySelector('#chatForm');
const input = document.querySelector('#questionInput');
const parentAgeInput = document.querySelector('#parentAgeInput');
const ageInput = document.querySelector('#ageInput');
const zipInput = document.querySelector('#zipInput');
const householdInput = document.querySelector('#householdInput');
const kidsInput = document.querySelector('#kidsInput');
const incomeInput = document.querySelector('#incomeInput');
const urgencyInput = document.querySelector('#urgencyInput');
const interestInput = document.querySelector('#interestInput');
const areaInput = document.querySelector('#areaInput');
const routeTitle = document.querySelector('#routeTitle');
const routeDestination = document.querySelector('#routeDestination');
const routeUrgency = document.querySelector('#routeUrgency');
const confidenceMeter = document.querySelector('#confidenceMeter span');
const confidenceText = document.querySelector('#confidenceText');
const sourceList = document.querySelector('#sourceList');
const leftResize = document.querySelector('#leftResize');
const rightResize = document.querySelector('#rightResize');

document.body.classList.add('login-open');

loginForm.addEventListener('submit', (event) => {
  event.preventDefault();
  loginOverlay.classList.add('is-hidden');
  document.body.classList.remove('login-open');
  input.focus();
});

document.querySelectorAll('.panel-toggle').forEach((button) => {
  button.addEventListener('click', () => {
    const panel = button.closest('.panel');
    const collapsed = panel.classList.toggle('is-collapsed');
    button.setAttribute('aria-expanded', String(!collapsed));
    button.querySelector('[aria-hidden="true"]').textContent = collapsed ? '+' : '−';
  });
});

function enableResize(handle, side) {
  handle.addEventListener('pointerdown', (event) => {
    event.preventDefault();
    handle.setPointerCapture(event.pointerId);
    const onMove = (moveEvent) => {
      const shellRect = appShell.getBoundingClientRect();
      if (side === 'left') {
        const width = Math.min(460, Math.max(280, moveEvent.clientX - shellRect.left));
        appShell.style.setProperty('--left-panel', `${width}px`);
      } else {
        const width = Math.min(460, Math.max(280, shellRect.right - moveEvent.clientX));
        appShell.style.setProperty('--right-panel', `${width}px`);
      }
    };
    const onUp = () => {
      handle.removeEventListener('pointermove', onMove);
      handle.removeEventListener('pointerup', onUp);
    };
    handle.addEventListener('pointermove', onMove);
    handle.addEventListener('pointerup', onUp);
  });
}

enableResize(leftResize, 'left');
enableResize(rightResize, 'right');

function getProfile() {
  const services = [...document.querySelectorAll('.interest-grid input:checked')].map(
    (item) => item.value,
  );
  const typedInterests = interestInput.value
    .split(',')
    .map((item) => item.trim())
    .filter(Boolean);
  return {
    parentAge: parentAgeInput.value || 'not shared',
    zip: zipInput.value.trim(),
    householdSize: householdInput.value || 'not shared',
    kids: kidsInput.value || 'not shared',
    income: incomeInput.value,
    urgency: urgencyInput.value,
    age: ageInput.value || 'school-age',
    area: areaInput.value,
    services,
    interests: typedInterests.length ? typedInterests : ['general activities'],
  };
}

function chooseRoute(text) {
  const query = text.toLowerCase();
  const profile = getProfile();
  const combined = `${query} ${profile.services.join(' ')}`.toLowerCase();
  if (['violence', 'self-harm', 'suicide', 'kill myself', 'immediate danger', 'weapon', 'overdose', 'severe crisis'].some((term) => combined.includes(term))) {
    return routes.mentalHealth;
  }
  if (['childcare', 'child care', 'head start', 'early education', 'subsidized childcare', 'preschool', 'daycare'].some((term) => combined.includes(term))) {
    return routes.childcare;
  }
  if (
    ['summer camp', 'camp', 'sport', 'stem', 'steam', 'tech', 'coding', 'robotics', '9-year', '9 year'].some(
      (term) => combined.includes(term),
    )
  ) {
    return routes.camps;
  }
  if (['real estate tax', 'assessment', 'property tax', 'appeal assessment'].some((term) => combined.includes(term))) {
    return routes.realEstateTax;
  }
  if (['car tax', 'vehicle tax', 'vehicle taxes', 'taxes'].some((term) => combined.includes(term))) {
    return routes.carTax;
  }
  if (['permit', 'zoning', 'property line', 'inspection', 'plus'].some((term) => combined.includes(term))) {
    return routes.permits;
  }
  if (['unpermitted', 'construction', 'code violation', 'neighbor', 'permits/code', 'tall grass', 'hoarding', 'boarding house'].some((term) => combined.includes(term))) {
    return routes.code;
  }
  if (['housing', 'shelter', 'homeless', 'homelessness', 'unsafe', 'danger', 'rent', 'eviction', 'food', 'utilities', 'basic needs', 'affordable housing', 'lihtc', 'waitlist', 'wait list'].some((term) => combined.includes(term))) {
    return routes.housing;
  }
  if (['trash', 'recycling', 'missed pickup', 'bulk', 'yard waste'].some((term) => combined.includes(term))) {
    return routes.trash;
  }
  if (['water', 'sewer', 'sewage', 'wastewater', 'backup', 'fairfax water', 'sewer backup', 'flooding'].some((term) => combined.includes(term))) {
    return routes.waterSewer;
  }
  if (['mental', 'csb', 'addiction', 'opioid', 'behavioral', 'substance'].some((term) => combined.includes(term))) {
    return routes.mentalHealth;
  }
  if (['older adult', 'senior', 'aging', 'meals on wheels', 'caregiver'].some((term) => combined.includes(term))) {
    return routes.olderAdults;
  }
  if (['community hub', 'community center', 'sully', 'lorton', 'neighborhood center'].some((term) => combined.includes(term))) {
    return routes.communityHubs;
  }
  if (['health', 'clinic', 'wic', 'immunization', 'dental', 'inspection'].some((term) => combined.includes(term))) {
    return routes.health;
  }
  if (['transportation', 'bus', 'connector', 'fastran', 'road', 'pothole', 'parking', 'commute'].some((term) => combined.includes(term))) {
    return routes.transportation;
  }
  if (['police', 'noise', 'animal control', 'fire', 'rescue', 'non-emergency', 'public safety'].some((term) => combined.includes(term))) {
    return routes.publicSafety;
  }
  return routes.general;
}

function addMessage(role, html) {
  const article = document.createElement('article');
  article.className = `message ${role}`;
  article.innerHTML = `
    <div class="avatar">${role === 'user' ? 'You' : 'FR'}</div>
    <div class="bubble">${html}</div>
  `;
  messages.append(article);
  messages.scrollTop = messages.scrollHeight;
}

function updateInspector(route) {
  routeTitle.textContent = route.title;
  routeDestination.textContent = route.destination;
  routeUrgency.textContent = route.urgency;
  confidenceMeter.style.width = `${route.confidence}%`;
  confidenceText.textContent = `${route.confidence}%`;
  sourceList.innerHTML = route.sourceKeys
    .map((key) => {
      const source = sources[key];
      return `
        <article class="source">
          <a href="${source.url}" target="_blank" rel="noreferrer">${source.title}</a>
          <p>${source.quote}</p>
        </article>
      `;
    })
    .join('');
}

function answerQuestion(question) {
  const route = chooseRoute(question);
  const profile = getProfile();
  const steps = route.steps(profile);
  const safetyNote =
    profile.urgency === 'immediate safety risk' ||
    /violence|self-harm|suicide|kill myself|immediate danger|weapon|overdose|severe crisis/i.test(question)
      ? '<p class="alert-note"><strong>Safety:</strong> If there is immediate danger, call 911. For severe mental health crisis, self-harm, or overdose risk, call 911 or CSB Emergency Services at 703-573-5679.</p>'
      : '';
  updateInspector(route);
  addMessage(
    'assistant',
    `
      <span class="route-pill">${route.title}</span>
      <p><strong>I hear you.</strong> I will keep this practical and route you to the right Fairfax County program without asking for names or exact addresses.</p>
      <h3>${route.destination}</h3>
      <p><strong>Urgency:</strong> ${route.urgency}</p>
      <p><strong>Client context:</strong> ZIP ${profile.zip || 'not shared'}, household size ${profile.householdSize}, kids ${profile.kids}, parent/guardian age ${profile.parentAge}, income ${profile.income}, selected services ${profile.services.join(', ') || 'not selected'}.</p>
      ${safetyNote}
      <ul>${steps.map((step) => `<li>${step}</li>`).join('')}</ul>
      <p><strong>Good follow-up:</strong> What ZIP code, neighborhood/cross street, timeline, and accessibility or language needs should I account for?</p>
    `,
  );
}

form.addEventListener('submit', (event) => {
  event.preventDefault();
  const question = input.value.trim();
  if (!question) return;
  addMessage('user', `<p>${question}</p>`);
  input.value = '';
  answerQuestion(question);
});

document.querySelectorAll('.prompt-chip').forEach((button) => {
  button.addEventListener('click', () => {
    input.value = button.dataset.prompt;
    input.focus();
  });
});

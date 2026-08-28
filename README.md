<div align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:00C6FF,50:0072FF,100:6A00FF&height=230&section=header&text=PataFundi&fontSize=72&fontColor=ffffff&animation=fadeIn&fontAlignY=35&desc=Find%20the%20Right%20Fundi%20%E2%80%A2%20Get%20the%20Job%20Done&descAlignY=58&descSize=20" width="100%"/><br/><img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=23&duration=2800&pause=700&color=0072FF&center=true&vCenter=true&width=950&lines=Welcome+to+PataFundi+%F0%9F%94%A7;Find+the+Right+Fundi+Near+You+%F0%9F%93%8D;Search+%E2%80%A2+Connect+%E2%80%A2+Book+%E2%80%A2+Pay+%E2%80%A2+Review;Escrow+Payments+%E2%80%A2+Verified+Fundis+%E2%80%A2+Disputes+Handled;Simple+Enough+for+Everyone+%F0%9F%91%8D;Fast%2C+Accessible+and+User-Friendly+%E2%9A%A1;Built+to+Fix+the+Failures+of+Existing+Platforms+%F0%9F%9A%80"/><br/><br/>

<img src="https://img.shields.io/badge/STATUS-UNDER%20DEVELOPMENT-yellow?style=for-the-badge"/>
<img src="https://img.shields.io/badge/BACKEND-FASTAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white"/>
<img src="https://img.shields.io/badge/DATABASE-POSTGRESQL-336791?style=for-the-badge&logo=postgresql&logoColor=white"/>
<img src="https://img.shields.io/badge/LANGUAGE-PYTHON-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/CACHE-REDIS-DC382D?style=for-the-badge&logo=redis&logoColor=white"/>
<img src="https://img.shields.io/badge/CONTAINER-DOCKER-2496ED?style=for-the-badge&logo=docker&logoColor=white"/><br/><br/>

<a href="#-about-patafundi"><img src="https://img.shields.io/badge/ABOUT-0072FF?style=for-the-badge"/></a>
<a href="#-features"><img src="https://img.shields.io/badge/FEATURES-6A00FF?style=for-the-badge"/></a>
<a href="#-architecture"><img src="https://img.shields.io/badge/ARCHITECTURE-00A896?style=for-the-badge"/></a>
<a href="#-database-design"><img src="https://img.shields.io/badge/DATABASE-FF3C78?style=for-the-badge"/></a>
<a href="#-installation"><img src="https://img.shields.io/badge/INSTALLATION-FF7A00?style=for-the-badge"/></a>

<br/><br/>

![Trophy Divider](https://capsule-render.vercel.app/api?type=rect&color=0:00C6FF,100:6A00FF&height=3&width=100%)

</div>

---

## 🔧 PataFundi

> **«Find the Right Fundi. Get the Job Done.»**

PataFundi is a modern, accessible, and intelligent skilled-service marketplace designed to connect customers with reliable fundis (skilled service providers) in a simple, fast, transparent, and accountable way.

Beyond simply connecting customers and fundis, PataFundi is specifically designed to address common failures found in existing service platforms:

- Difficult fundi discovery.
- Poor service-provider verification.
- Unclear availability.
- Lack of pricing transparency.
- No structured price negotiation.
- Poor communication.
- Complicated booking processes.
- Weak service tracking.
- Low accountability — no escrow, no formal dispute resolution.
- No damage protection or liability coverage.
- No support for urgent/emergency jobs.
- No support for team/company-based fundis.
- No offline or low-connectivity access path.
- Poor accessibility.
- Complex user interfaces.
- Slow or data-heavy experiences.

---

## 📑 Table of Contents

- [About PataFundi](#-about-patafundi)
- [Problem Statement](#-problem-statement)
- [Aim, Vision & Mission](#-aim-vision--mission)
- [Objectives](#-objectives)
- [Existing Platform Failures](#-existing-platform-failures)
- [Our Solution](#-our-solution)
- [Design Principles](#-design-principles)
- [Target Users](#-target-users)
- [Features](#-features)
- [Customer Features](#-customer-features)
- [Fundi Features](#-fundi-features)
- [Admin Features](#-admin-features)
- [Smart Fundi Matching](#-smart-fundi-matching)
- [Location Services](#-location-services)
- [Booking System](#-booking-system)
- [Quotation & Price Negotiation](#-quotation--price-negotiation)
- [Escrow Payment System](#-escrow-payment-system)
- [Cancellation & Refund Policy](#-cancellation--refund-policy)
- [Wallet & Payouts](#-wallet--payouts)
- [Emergency / Urgent Booking](#-emergency--urgent-booking)
- [Damage Protection & Liability](#-damage-protection--liability)
- [Team & Company Fundis](#-team--company-fundis)
- [Communication](#-communication)
- [Notifications](#-notifications)
- [Ratings & Multi-Criteria Reviews](#-ratings--multi-criteria-reviews)
- [Fundi Verification](#-fundi-verification)
- [Dispute Resolution](#-dispute-resolution)
- [Warranty / Service Guarantee](#-warranty--service-guarantee)
- [Referral & Loyalty Program](#-referral--loyalty-program)
- [Content Moderation](#-content-moderation)
- [Fundi Analytics Dashboard](#-fundi-analytics-dashboard)
- [Offline / USSD Access](#-offline--ussd-access)
- [Accessibility](#-accessibility)
- [Performance & Low-Bandwidth](#-performance-and-low-bandwidth)
- [Language Support](#-language-support)
- [Security](#-security)
- [Customer / Fundi / Admin Flow](#-customer-flow)
- [System Architecture](#-architecture)
- [Technology Stack](#-technology-stack)
- [Project Structure](#-project-structure)
- [Database Design (Full ERD)](#-database-design)
- [API Structure](#-api-structure)
- [Installation](#-installation)
- [Development Roadmap](#-development-roadmap)
- [Future Features](#-future-features)
- [Contribution](#-contribution)
- [Project Status](#-project-status)

---

## 📖 About PataFundi

Instead of depending entirely on:

```
Friends → Neighbours → Phone Calls → Personal Recommendations → Manual Searching
```

Customers can use PataFundi to:

```
Open App → Choose Service → Set Location → Find Suitable Fundis
   → Compare → Request Quote → Negotiate → Book → Track Job
   → Pay (Escrow) → Confirm Quality → Funds Released to Fundi → Review
```

---

## ❗ Problem Statement

### Customer Problems

Difficult to find qualified fundis, no reliable way to compare fundis, unclear fundi availability, unclear or non-negotiable pricing, lack of verified profiles, poor communication, complicated booking processes, no proper service tracking, difficulty resolving disputes, no protection against property damage, no way to book urgent/emergency help, poor visibility of previous work, platforms that are difficult for less tech-savvy users, high data usage and slow loading on poor networks, no offline access for users without smartphones.

### Fundi Problems

Difficulty finding new customers, limited online visibility, lack of professional digital profiles, poor tools for managing requests and bookings, lack of reputation-building mechanisms, difficulty communicating with customers, limited access to digital opportunities, no way to operate as a team/company, no insight into their own earnings and demand patterns.

---

## 🎯 Aim, Vision & Mission

**Aim:** To develop a smooth, accessible, reliable, and intelligent skilled-service platform that addresses the limitations of existing service platforms while making it easy for everyone to find, connect with, book, and manage skilled service providers regardless of their level of digital literacy.

**Vision:** To become a trusted and inclusive digital platform for discovering, connecting with, and accessing skilled service providers.

**Mission:** To simplify access to skilled services by connecting customers with suitable, available, and trusted fundis through a fast, transparent, secure, and user-friendly digital platform.

---

## 🎯 Objectives

- Improve fundi discovery.
- Improve fundi verification.
- Provide location-based matching.
- Improve availability visibility.
- Improve price transparency through structured quotations.
- Simplify booking.
- Improve customer-fundi communication.
- Provide service tracking.
- Improve accountability through escrow and dispute resolution.
- Provide trusted, multi-criteria ratings and reviews.
- Support secure digital payments.
- Provide a clear cancellation and refund policy.
- Provide an accessible user interface.
- Support users with different levels of digital literacy, including non-smartphone users.
- Minimize data usage.
- Provide fast response times.
- Support urgent/emergency service requests.
- Provide optional damage protection for higher-risk jobs.
- Support team and company-based fundi accounts.
- Support future intelligent fundi recommendations.
- Provide a warranty for completed services.
- Provide a referral/loyalty program to grow adoption.
- Give fundis visibility into their own performance and earnings.

---

## ❌ Existing Platform Failures

| Existing Failure | PataFundi Response |
|---|---|
| Difficult fundi discovery | Smart search |
| Wrong or irrelevant results | Intelligent matching |
| Unverified fundis | Multi-level fundi verification |
| Fake profiles | Identity/document verification |
| Unknown availability | Availability management |
| Unclear pricing | Structured quotation & negotiation flow |
| Complicated booking | Simple booking flow |
| Poor communication | In-app chat |
| No job tracking | Job status tracking + audit history |
| Unreliable reviews | Multi-criteria, verified-job reviews |
| Poor accountability | Escrow payments + dispute resolution |
| Unclear cancellation terms | Defined cancellation & refund policy engine |
| No recourse after bad work | Service warranty period |
| No cover for accidental damage | Optional damage protection / liability coverage |
| No urgent-help option | Emergency/priority booking tier |
| Individual fundis only | Team/company fundi accounts |
| Complex interface | Simple UI |
| Difficult for older/non-technical users | Accessibility-focused design |
| High data consumption | Low-bandwidth optimization |
| Slow loading | Performance optimization |
| Language barriers | English + Kiswahili |
| No access for non-smartphone users | USSD-based booking fallback |
| Limited fundi visibility | Professional profiles + portfolio |
| Poor dispute handling | Dedicated disputes module with evidence |
| No repeat-customer incentive | Favorites + loyalty/referral program |
| Unmoderated chat/reviews | Content moderation for text & images |
| No self-insight for fundis | Fundi analytics dashboard |

---

## 💡 Our Solution

```
                    PATAFUNDI
                        │
        ┌───────────────┼────────────────┐
        │               │                │
        ▼               ▼                ▼
      TRUST          SIMPLICITY       INTELLIGENCE
        │               │                │
  Verification       Easy UI        Smart Matching
  Escrow Payments    Fast UX        Recommendations
  Reviews            Accessibility  Location Scoring
  Disputes           Low Bandwidth  Response Time
  Warranty           USSD Access    Demand Analytics
  Damage Protection      │                │
        │               │                │
        └───────────────┼────────────────┘
                        │
                        ▼
               BETTER SERVICE EXPERIENCE
```

---

## 🎨 Design Principles

1. **Simple** — Users should understand what to do without training.
2. **Fast** — The platform should respond quickly and minimize unnecessary operations.
3. **Accessible** — People with different technical abilities should be able to use it.
4. **Mobile First** — The interface will prioritize smartphone users, with a fallback for feature phones.
5. **Trustworthy** — Users should have enough information to make informed decisions.
6. **Transparent** — Important information such as service details, booking status, and pricing should be clear.
7. **Inclusive** — The platform should not assume that every user is highly familiar with technology or owns a smartphone.
8. **Accountable** — Every step involving money and work should be recorded (audit trail).

---

## 👥 Target Users

👨‍🎓 Students • 👩‍💼 Professionals • 🏠 Homeowners • 🏪 Business owners • 👨‍🌾 Farmers • 👴 Older users • 👩‍🔧 Skilled professionals • 👨‍🔧 Fundis • Small businesses • Property managers • Organizations • Fundi teams/companies

---

## 🚀 Features

### 🔐 Authentication

- Registration, Login, Logout
- JWT authentication + revocable refresh tokens
- Password hashing & reset
- Account verification
- Role-based access control (real RBAC with roles/permissions tables)
- Session/token management
- Account activation/deactivation

### 👤 Customer Features

Create account • Manage profile • Search services/fundis • Find nearby fundis • Filter/sort results • View fundi profiles, ratings, reviews, skills, experience, availability, and past-work portfolio • Create service requests • Upload job images • Request and compare quotations • Negotiate price before booking • Book fundis • Track bookings (real-time status history) • Chat with fundis • Receive notifications • Pay via escrow • Purchase optional damage protection for a job • View payment history • Cancel requests within policy • Rate and review (multi-criteria) • Save fundis to Favorites • Report problems / open a dispute • View service history • Refer friends and earn loyalty rewards • Book emergency/urgent jobs • Access core booking via USSD if offline

### 👨‍🔧 Fundi Features

Register • Create professional profile + portfolio • Add skills, services, experience, certifications/documents for verification • Set location & service area (polygon, not just radius) • Set availability & working hours • Set standard rates and respond with custom quotations • Mark self as available for emergency jobs • Receive/accept/reject requests • Manage bookings • Update job status • Communicate with customers • View completed jobs, ratings, reviews • Track earnings via wallet • Request payouts (mobile money/bank) • View personal analytics dashboard (earnings trends, demand patterns, response time) • Build professional reputation • Operate as an individual or join/manage a team/company account • Enroll in referral/loyalty program

### 👨‍💼 Admin Features

Manage users/fundis • Verify fundis (documents) • Manage service categories/services • Manage bookings • Manage quotations • Manage reviews • Moderate chat messages and uploaded images • Handle disputes with evidence • Monitor payments, wallets, payouts, commissions • Manage damage-protection claims • Manage cancellation/refund rules • Manage emergency-job surcharge rules • Manage team/company fundi accounts • Manage referral/loyalty program rules • Manage blocked accounts • Monitor platform activity • View statistics/analytics • View audit logs • Manage system settings (commission %, default radius, warranty periods)

---

## 🤖 Smart Fundi Matching

```
Service + Location + Distance + Availability + Rating + Experience
   + Price + Skills + Previous Performance + Average Response Time
                            ↓
                      MATCH SCORE
```

**Example:**

```
👨‍🔧 John
Service Match     ✓
Distance          2.1 km
Availability      ✓
Rating            ⭐ 4.8
Experience        6 years
Verified          ✓ Trusted Fundi
Avg Response      12 min

Match Score: 95%
```

---

## 📍 Location Services

Current user location • Fundi location • Nearby fundis • Distance calculation • Search radius • Service area (geo-polygon for greater accuracy in urban areas) • Location-based ranking • Future map integration • Optional location sharing

---

## 📅 Booking System

```
PENDING → QUOTED → ACCEPTED → CONFIRMED → IN_PROGRESS → COMPLETED
```
Alternative states: `REJECTED` `CANCELLED` `EXPIRED` `DISPUTED`

Every status change is recorded in `booking_status_history` — who changed it, when, and why — to support disputes and accountability.

### 📩 Service Request Example

```
Service:  Electrical Repair
Problem:  Power socket is not working
Location: Mbeya
Time:     14:00
Budget:   TSh 30,000
Priority: Standard / Emergency
```

---

## 💵 Quotation & Price Negotiation

To close the pricing-transparency gap, a service request can move through a structured quote flow before any money changes hands:

```
Customer sends request → Fundi reviews job details/photos
   → Fundi submits quotation (price, estimated duration, materials cost)
   → Customer accepts, rejects, or counter-offers
   → Agreed quotation is attached to the booking
```

Tables: `quotations`, `quotation_items` (for itemized materials/labor), `quotation_negotiations` (message history of counter-offers).

---

## 💰 Escrow Payment System

This is one of the core features solving "poor accountability."

```
Booking → Customer Pays Agreed Quote (funds held in Escrow)
   ↓
Fundi Starts Job
   ↓
Job Completed
   ↓
Customer Confirms Quality
   ↓
Funds Released to Fundi's Wallet
   ↓
(If a dispute arises) → Dispute → Admin Reviews → Refund or Release
```

Payment methods: Mobile money • Bank payment • Card payment
Statuses: `PENDING` `HELD_IN_ESCROW` `PROCESSING` `RELEASED` `FAILED` `REFUNDED` `PARTIALLY_REFUNDED`

---

## 🔄 Cancellation & Refund Policy

Clear, rule-based cancellation terms replace ad-hoc handling:

| Cancellation Timing | Customer Refund | Fundi Compensation |
|---|---|---|
| More than 2 hours before job start | Full refund | None |
| Within 2 hours of job start | Partial refund (configurable %) | Partial compensation |
| After fundi has arrived on site | No refund (unless fundi fault) | Full compensation |
| Fundi cancels after acceptance | Full refund to customer | Rating/strike penalty on fundi |

Rules are configurable per service category by admins and stored in `cancellation_policies`, with every cancellation recorded in `cancellation_records` for audit purposes.

---

## 👛 Wallet & Payouts

- `wallets` — each fundi's in-app balance
- `transactions` — full ledger (payments, commissions, refunds, payouts)
- `commissions` — platform fee percentage per transaction
- `payouts` — fundi requests to withdraw funds to mobile money/bank

---

## 🚨 Emergency / Urgent Booking

For time-critical jobs (burst pipe, power outage, lockouts), customers can request an emergency booking:

- Filters to fundis who have marked themselves as available for urgent jobs
- Priority placement in fundi notification queues
- Configurable emergency surcharge, shown transparently before payment
- Shorter expected response-time SLA displayed to the customer

Table: `emergency_requests`, linked to the standard `bookings` table with a `priority` flag.

---

## 🛡️ Damage Protection & Liability

For higher-risk jobs (electrical, plumbing, structural work), customers can optionally add damage protection to a booking:

- Small protection fee added at checkout, held separately from the job escrow
- Claims process if property damage occurs during the job
- Admin-reviewed claims with evidence, similar to the dispute workflow
- Optional integration point for a third-party insurance partner in the future

Tables: `damage_protection_plans`, `damage_claims`.

---

## 🏢 Team & Company Fundis

Fundis are no longer limited to individual accounts:

- A `fundi_organization` can register and manage multiple `fundi_profile` members
- Jobs can be assigned to a specific team member or accepted by the organization and staffed internally
- Organization-level ratings roll up from individual member performance
- Organization admins manage their own team's availability, documents, and payouts

---

## 💬 Communication

Text messages • Images • Timestamps • Read status • Booking-linked conversations • Real-time messaging • Notifications • Automatic flagging of inappropriate content

## 🔔 Notifications

Triggers: New request, quotation received, accepted/rejected, booking confirmed/cancelled, job started/completed, payment success/failed, escrow released, new message, new review, dispute update, damage-claim update, referral reward earned
Channels: In-App • Push • Email • SMS • USSD alerts (for feature-phone users)

---

## ⭐ Ratings & Multi-Criteria Reviews

Instead of a single star rating, reviews are broken down across multiple criteria:

```
Fundi: John
Quality of Work   ⭐⭐⭐⭐⭐
Timeliness        ⭐⭐⭐⭐
Pricing           ⭐⭐⭐⭐⭐
Communication     ⭐⭐⭐⭐⭐

Average: 4.8 / 5   |   "Excellent service and very professional."
```

The system calculates: average rating, total reviews, rating distribution per criterion, completed jobs — and only allows reviews for completed, verified bookings. All review text passes through content moderation before publishing.

---

## 🛡️ Fundi Verification

```
Phone Verified → Profile Verified → Identity Verified
   → Skills/Certificate Verified → Trusted Fundi
```

Documents (ID, license, certificates) are stored in `fundi_documents` and reviewed by an admin. Verified profiles display `✓ VERIFIED` / `✓ Trusted Fundi`.

---

## ⚖️ Dispute Resolution

A dedicated module solving "poor dispute handling":

```
Customer/Fundi Reports an Issue
        ↓
   Dispute Opened (booking_id, reason)
        ↓
   Both Parties Upload Evidence (images/messages)
        ↓
   Admin Reviews
        ↓
   Decision: Refund / Release Escrow / Warning / Ban
```

Tables: `disputes`, `dispute_evidence`

---

## 🔧 Warranty / Service Guarantee

Each service type can have a warranty period (e.g. 7 days). If the same issue reoccurs within that period, the fundi is required to fix it at no extra charge — building far more trust than most existing East African service platforms.

---

## 🎁 Referral & Loyalty Program

To encourage adoption and repeat use:

- Unique referral code per user
- Reward credited to wallet/discount balance when a referred user completes their first booking
- Loyalty tiers based on completed bookings (e.g. Bronze/Silver/Gold) with perks like reduced commission or priority support
- Tables: `referrals`, `loyalty_tiers`, `reward_transactions`

---

## 🧹 Content Moderation

To keep chat, reviews, and uploaded images safe and trustworthy:

- Automated profanity/abuse filtering on chat messages and review text
- Automated flagging of inappropriate uploaded images before admin review
- Manual admin review queue for flagged content
- Repeat offenders tracked for warnings/bans

---

## 📊 Fundi Analytics Dashboard

Fundis get visibility into their own performance, not just admins:

- Earnings trends over time (daily/weekly/monthly)
- Peak demand hours/days for their service category and area
- Acceptance rate, average response time, completion rate
- Rating trend over time across each review criterion

---

## 📴 Offline / USSD Access

For customers and fundis without smartphones or reliable data:

- USSD menu for browsing basic service categories and requesting a fundi
- USSD-based booking confirmation and status checks
- SMS notifications as a fallback channel for booking updates
- Simplified feature-phone-friendly flow that syncs with the main platform

---

## ♿ Accessibility

Large readable text • Clear typography • High contrast • Large touch targets • Simple navigation • Descriptive buttons • Keyboard accessibility • Screen-reader compatibility • Meaningful error messages • Clear visual feedback • Reduced animations • Simple language

## 📱 Mobile-First Design

```
Small Phones → Large Phones → Tablets → Laptops → Desktop
```

## ⚡ Performance and Low-Bandwidth

Optimized images • Lazy loading • API pagination • Caching (Redis) • Minimal API requests • Compressed assets • Efficient queries • Database indexing • Lightweight UI • Background processing

> «Fast experience without requiring high-speed internet.»

## 🌐 Language Support

🇹🇿 Kiswahili • 🇬🇧 English — the architecture allows additional languages in the future.

## 🔒 Security

Password hashing • JWT + revocable refresh tokens • Role-based authorization (RBAC) • Input validation (Pydantic) • SQL injection protection • CORS configuration • File validation • Rate limiting • Secure environment variables • Audit logging (every admin action) • Content moderation safeguards • Secure production configuration

---

## 🔄 Customer Flow

```
OPEN → SELECT SERVICE → SET LOCATION → SEARCH → FILTER/SORT
  → VIEW FUNDI → CHECK VERIFICATION → CHECK RATING → CHECK AVAILABILITY
  → SEND REQUEST → RECEIVE QUOTE → NEGOTIATE (OPTIONAL) → FUNDI ACCEPTS
  → BOOKING CONFIRMED → PAY (ESCROW) → JOB STARTED → JOB COMPLETED
  → CONFIRM QUALITY → ESCROW RELEASED → RATE & REVIEW → DONE ✓
```

## 👨‍🔧 Fundi Flow

```
REGISTER → VERIFY ACCOUNT → UPLOAD DOCUMENTS → CREATE PROFILE
  → ADD SERVICES/SKILLS → SET LOCATION → SET AVAILABILITY
  → RECEIVE REQUEST → SEND QUOTATION → ACCEPT/REJECT → BOOKING → START JOB
  → COMPLETE JOB → ESCROW RELEASED → WALLET UPDATED → REVIEW RECEIVED
```

## 👨‍💼 Admin Flow

```
LOGIN → DASHBOARD → USERS → FUNDIS → VERIFICATION → SERVICES
  → BOOKINGS → QUOTATIONS → PAYMENTS/WALLETS/PAYOUTS → DISPUTES
  → DAMAGE CLAIMS → REVIEWS → MODERATION QUEUE → REPORTS → ANALYTICS
  → AUDIT LOGS
```

---

## 🏗️ Architecture

```
                         PATAFUNDI
                             │
              ┌──────────────┴──────────────┐
              │                             │
         👤 CUSTOMER                    👨‍🔧 FUNDI
              │                             │
              └──────────────┬──────────────┘
                             │
                             ▼
                    🌐 FRONTEND / APP / USSD
                             │
                             ▼
                    🔐 AUTHENTICATION
                             │
                             ▼
                      🚀 FASTAPI API
                             │
   ┌──────────┬──────────┬──────────┬──────────┬──────────┬──────────┐
   ▼          ▼          ▼          ▼          ▼          ▼          ▼
USERS      SERVICES   BOOKINGS   PAYMENTS   DISPUTES   VERIFICATION  MODERATION
   │          │          │          │          │          │          │
   └──────────┴──────────┴────┬─────┴──────────┴──────────┴──────────┘
                             │
                             ▼
                       🗄️ POSTGRESQL
                             │
   ┌──────────┬──────────┬──────────┬──────────┬──────────┐
   ▼          ▼          ▼          ▼          ▼          ▼
 CHAT      WALLETS    PAYOUTS   AUDIT LOG   REDIS CACHE  ANALYTICS
```

---

## 🧰 Technology Stack

### Backend

| Technology | Purpose |
|---|---|
| Python | Core language |
| FastAPI | REST API |
| SQLAlchemy | ORM |
| Pydantic | Validation |
| Alembic | Migrations |
| PostgreSQL | Database |
| JWT | Authentication |
| Uvicorn | ASGI server |
| Pytest | Testing |
| Celery | Background jobs (payouts, notifications, USSD/SMS dispatch) |

### Frontend

HTML5 • CSS3 • JavaScript • React • Next.js

### Infrastructure

Git • GitHub • Docker • PostgreSQL • Redis • Cloud/object storage • CI/CD (GitHub Actions) • USSD/SMS gateway integration

---

## 🗄️ Database Design

```
USERS
 │
 ├── ROLES / PERMISSIONS
 ├── REFRESH_TOKENS
 ├── DEVICE_TOKENS
 ├── CUSTOMER_PROFILE ── FAVORITES
 ├── REFERRALS / LOYALTY_TIERS / REWARD_TRANSACTIONS
 │
 └── FUNDI_PROFILE ── FUNDI_ORGANIZATION (team/company)
        │
        ├── FUNDI_DOCUMENTS ── VERIFICATION_LEVELS
        ├── FUNDI_PORTFOLIO
        ├── SKILLS / SERVICES / AVAILABILITY
        │
        BOOKINGS
        ├── BOOKING_STATUS_HISTORY
        ├── QUOTATIONS ── QUOTATION_ITEMS / QUOTATION_NEGOTIATIONS
        ├── EMERGENCY_REQUESTS
        ├── CANCELLATION_POLICIES / CANCELLATION_RECORDS
        │
        PAYMENTS
        ├── WALLETS / TRANSACTIONS / COMMISSIONS / PAYOUTS
        ├── DAMAGE_PROTECTION_PLANS / DAMAGE_CLAIMS
        │
        DISPUTES ── DISPUTE_EVIDENCE
        REVIEWS ── MODERATION_QUEUE
        NOTIFICATIONS
        AUDIT_LOGS
```

---

## 🔌 API Structure

```
/auth          - registration, login, refresh, logout
/users         - profile management
/fundis        - fundi profiles, portfolio, verification
/services      - service categories and listings
/bookings      - request, quote, accept, status, cancel
/quotations    - submit, counter-offer, accept/reject
/payments      - escrow, wallet, payouts, transactions
/disputes      - open, evidence, resolution
/reviews       - submit, moderate, fetch
/notifications - in-app, push, email, SMS, USSD
/admin         - verification, moderation, analytics, audit logs
```

---

## ⚙️ Installation

```bash
git clone https://github.com/patafundi/patafundi.git
cd patafundi

# Backend setup
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Environment variables
cp .env.example .env

# Database migrations
alembic upgrade head

# Run with Docker
docker-compose up --build

# Or run locally
uvicorn app.main:app --reload
```

---

## 🗺️ Development Roadmap

- [ ] Phase 1: Auth, user/fundi profiles, service categories
- [ ] Phase 2: Search, matching, booking flow, quotations
- [ ] Phase 3: Escrow payments, wallets, payouts
- [ ] Phase 4: Chat, notifications, reviews
- [ ] Phase 5: Disputes, warranty, damage protection
- [ ] Phase 6: Emergency bookings, team/company accounts
- [ ] Phase 7: Referral/loyalty, content moderation, fundi analytics
- [ ] Phase 8: USSD integration, additional languages, map integration

---

## 🔮 Future Features

- AI-powered fundi recommendations based on job history
- In-app map view with live fundi location tracking
- Video call support for remote diagnosis before booking
- Insurance partner integrations for damage protection
- Multi-currency support for cross-border expansion
- Additional local language support beyond English/Kiswahili

---

## 🤝 Contribution

Contributions are welcome. Please open an issue to discuss proposed changes before submitting a pull request, and follow the existing code style and commit conventions.

---

## 📌 Project Status

🚧 Under active development — core architecture and feature set are being implemented in phases as outlined in the Development Roadmap above.

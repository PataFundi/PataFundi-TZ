<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:00C6FF,50:0072FF,100:6A00FF&height=260&section=header&text=PataFundi&fontSize=78&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Find%20the%20Right%20Fundi%20%E2%80%A2%20Get%20the%20Job%20Done&descAlignY=58&descSize=22" width="100%"/>
<br/>
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=24&duration=2600&pause=800&color=0072FF&center=true&vCenter=true&width=980&lines=Welcome+to+PataFundi+%F0%9F%94%A7;Find+the+Right+Fundi+Near+You+%F0%9F%93%8D;Search+%E2%80%A2+Connect+%E2%80%A2+Book+%E2%80%A2+Pay+%E2%80%A2+Review;Escrow+Payments+%E2%80%A2+Verified+Fundis+%E2%80%A2+Disputes+Handled;Simple+Enough+for+Everyone+%F0%9F%91%8D;Fast%2C+Accessible+and+User-Friendly+%E2%9A%A1;Built+to+Fix+the+Failures+of+Existing+Platforms+%F0%9F%9A%80;Smart+Matching+%E2%80%A2+Emergency+Jobs+%E2%80%A2+Team+Accounts;USSD+Offline+Access+%E2%80%A2+Multi-Language+Support"/>
<br/><br/>

<img src="https://img.shields.io/badge/STATUS-UNDER%20DEVELOPMENT-yellow?style=for-the-badge"/>
<img src="https://img.shields.io/badge/BACKEND-FASTAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white"/>
<img src="https://img.shields.io/badge/DATABASE-POSTGRESQL-336791?style=for-the-badge&logo=postgresql&logoColor=white"/>
<img src="https://img.shields.io/badge/LANGUAGE-PYTHON-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/CACHE-REDIS-DC382D?style=for-the-badge&logo=redis&logoColor=white"/>
<img src="https://img.shields.io/badge/CONTAINER-DOCKER-2496ED?style=for-the-badge&logo=docker&logoColor=white"/>
<img src="https://img.shields.io/badge/FRONTEND-NEXT.JS-000000?style=for-the-badge&logo=nextdotjs&logoColor=white"/>
<img src="https://img.shields.io/badge/QUEUE-CELERY-37814A?style=for-the-badge&logo=celery&logoColor=white"/>
<br/><br/>

<a href="#-about-patafundi"><img src="https://img.shields.io/badge/ABOUT-0072FF?style=for-the-badge"/></a>
<a href="#-features"><img src="https://img.shields.io/badge/FEATURES-6A00FF?style=for-the-badge"/></a>
<a href="#-architecture"><img src="https://img.shields.io/badge/ARCHITECTURE-00A896?style=for-the-badge"/></a>
<a href="#-database-design"><img src="https://img.shields.io/badge/DATABASE-FF3C78?style=for-the-badge"/></a>
<a href="#-installation"><img src="https://img.shields.io/badge/INSTALLATION-FF7A00?style=for-the-badge"/></a>
<a href="#-development-roadmap"><img src="https://img.shields.io/badge/ROADMAP-FFD700?style=for-the-badge"/></a>

<br/><br/>

![Trophy Divider](https://capsule-render.vercel.app/api?type=rect&color=0:00C6FF,100:6A00FF&height=4&width=100%)

</div>

---

## 🔧 PataFundi

> **«Find the Right Fundi. Get the Job Done.»**

**PataFundi** is a modern, accessible, intelligent, and highly accountable skilled-service marketplace built to connect customers with reliable *fundis* (skilled service providers) across Tanzania and the broader East African region.  

It is engineered from the ground up to solve the real-world failures that plague existing service platforms — difficult discovery, weak verification, opaque pricing, poor communication, complicated booking, zero escrow protection, weak dispute resolution, no emergency support, no offline access, and interfaces that exclude less tech-savvy users.

Beyond simple matching, PataFundi delivers a complete end-to-end experience: smart discovery, structured quotations with negotiation, secure escrow payments, real-time job tracking, multi-criteria reviews, formal dispute handling, optional damage protection, team/company accounts, referral rewards, content moderation, fundi analytics, and a full USSD fallback for feature-phone and offline users.

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
  - [Authentication & Security](#-authentication--security)
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
- [Performance & Low-Bandwidth](#-performance--low-bandwidth)
- [Language Support](#-language-support)
- [Security](#-security)
- [Customer / Fundi / Admin Flows](#-customer--fundi--admin-flows)
- [System Architecture](#-architecture)
- [Technology Stack](#-technology-stack)
- [Project Structure](#-project-structure)
- [Database Design (Full ERD Overview)](#-database-design)
- [API Structure](#-api-structure)
- [Installation](#-installation)
- [Development Roadmap](#-development-roadmap)
- [Future Features](#-future-features)
- [Contribution](#-contribution)
- [Project Status](#-project-status)

---

## 📖 About PataFundi

Instead of relying on the traditional, unreliable chain of:

```
Friends → Neighbours → Phone Calls → Personal Recommendations → Manual Searching
```

Customers can use PataFundi to follow a clear, guided, and protected journey:

```
Open App → Choose Service → Set Location → Find Suitable Fundis
   → Compare Profiles, Ratings & Portfolios → Request Quote
   → Negotiate Price → Book → Track Job in Real Time
   → Pay via Escrow → Confirm Quality → Funds Released to Fundi → Leave Multi-Criteria Review
```

PataFundi is built with three core pillars:

- **Trust** — Multi-level verification, escrow, disputes, warranty, damage protection, and moderated reviews  
- **Simplicity** — Clean mobile-first interface, large touch targets, clear language, and USSD fallback  
- **Intelligence** — Smart matching engine, response-time scoring, demand analytics, and future AI recommendations  

---

## ❗ Problem Statement

### Customer Problems

- Extremely difficult to find qualified, available, and trustworthy fundis nearby  
- No reliable way to compare fundis on quality, price, experience, or response time  
- Unclear or completely hidden availability  
- Opaque or non-negotiable pricing  
- Widespread fake profiles and weak identity verification  
- Poor or non-existent in-app communication  
- Complicated, multi-step booking processes that frequently fail  
- Almost no real-time service tracking or status history  
- Extremely difficult and opaque dispute resolution  
- No protection against accidental property damage during a job  
- No structured way to request urgent or emergency help  
- Poor visibility of previous work (portfolios)  
- Platforms designed only for highly tech-savvy users  
- High data consumption and slow loading on poor networks  
- Complete lack of offline or feature-phone access  

### Fundi Problems

- Very difficult to find new customers consistently  
- Extremely limited online visibility and professional presence  
- No tools for creating a serious digital profile or portfolio  
- Poor or non-existent tools for managing incoming requests and bookings  
- Almost no reputation-building mechanisms that customers actually trust  
- Difficulty communicating clearly with customers  
- Limited access to digital payment and earning opportunities  
- No support for operating as a team or small company  
- Zero insight into personal earnings trends, peak demand hours, or response performance  

---

## 🎯 Aim, Vision & Mission

**Aim**  
To develop a smooth, accessible, reliable, and intelligent skilled-service platform that systematically addresses every major limitation of existing service platforms while remaining usable by people of all levels of digital literacy — including those without smartphones.

**Vision**  
To become the most trusted and inclusive digital platform in East Africa for discovering, connecting with, and accessing skilled service providers.

**Mission**  
To simplify access to skilled services by connecting customers with suitable, available, verified, and accountable fundis through a fast, transparent, secure, and genuinely user-friendly digital platform — with full offline support.

---

## 🎯 Objectives

- Dramatically improve fundi discovery through intelligent, multi-factor matching  
- Implement multi-level fundi verification (phone → profile → identity → skills/certificates)  
- Deliver precise location-based matching with service-area polygons  
- Provide clear, real-time availability visibility  
- Create full price transparency through structured, itemized quotations and negotiation  
- Simplify the entire booking flow into a guided, low-friction experience  
- Enable reliable customer–fundi communication via in-app chat  
- Provide complete service tracking with full status history and audit trail  
- Guarantee accountability through escrow payments and formal dispute resolution  
- Deliver trusted, multi-criteria ratings and reviews (only from completed jobs)  
- Support secure digital payments (mobile money, bank, card)  
- Offer a clear, rule-based, and configurable cancellation & refund policy  
- Design an accessible interface that works for older and less technical users  
- Support users without smartphones through a full USSD booking path  
- Minimize data usage and deliver fast performance on low-bandwidth networks  
- Support urgent and emergency service requests with priority handling  
- Provide optional damage protection / liability coverage for higher-risk jobs  
- Enable team and company-based fundi accounts  
- Lay the foundation for future intelligent AI recommendations  
- Offer a service warranty / guarantee period after job completion  
- Grow adoption through a referral and loyalty program  
- Give fundis full visibility into their own performance and earnings via analytics  

---

## ❌ Existing Platform Failures vs PataFundi Response

| Existing Failure                        | PataFundi Response                                      |
|-----------------------------------------|---------------------------------------------------------|
| Difficult fundi discovery               | Smart multi-factor search & matching engine             |
| Wrong or irrelevant results             | Intelligent scoring (distance + rating + response time) |
| Unverified fundis                       | Multi-level verification workflow                       |
| Fake profiles                           | Identity + document verification by admins              |
| Unknown availability                    | Real-time availability & working-hours management       |
| Unclear pricing                         | Structured quotation + itemized negotiation flow        |
| Complicated booking                     | Simple, guided, status-driven booking flow              |
| Poor communication                      | In-app real-time chat linked to every booking           |
| No job tracking                         | Full job status history + audit trail                   |
| Unreliable reviews                      | Multi-criteria reviews only from verified completed jobs|
| Poor accountability                     | Escrow payments + formal dispute module                 |
| Unclear cancellation terms              | Configurable cancellation & refund policy engine        |
| No recourse after bad work              | Service warranty period per category                    |
| No cover for accidental damage          | Optional damage protection with claims workflow         |
| No urgent-help option                   | Emergency / priority booking tier                       |
| Individual fundis only                  | Full team / company fundi organization accounts         |
| Complex interface                       | Clean, mobile-first, accessibility-focused UI           |
| Difficult for older / non-technical users | Large text, clear language, simple navigation         |
| High data consumption                   | Aggressive low-bandwidth optimization                   |
| Slow loading                            | Caching, pagination, lazy loading, efficient queries    |
| Language barriers                       | Full English + Kiswahili support (extensible)           |
| No access for non-smartphone users      | Complete USSD-based booking & status system             |
| Limited fundi visibility                | Professional profiles + rich portfolio                  |
| Poor dispute handling                   | Dedicated disputes module with evidence upload          |
| No repeat-customer incentive            | Favorites + referral & loyalty program                  |
| Unmoderated chat / reviews              | Automated + manual content moderation                   |
| No self-insight for fundis              | Full fundi analytics dashboard                          |

---

## 💡 Our Solution

```
                         PATAFUNDI
                             │
           ┌─────────────────┼─────────────────┐
           │                 │                 │
           ▼                 ▼                 ▼
         TRUST           SIMPLICITY        INTELLIGENCE
           │                 │                 │
   Verification          Easy UI         Smart Matching
   Escrow Payments       Fast UX         Recommendations
   Reviews & Ratings     Accessibility   Location Scoring
   Disputes              Low Bandwidth   Response Time
   Warranty              USSD Access     Demand Analytics
   Damage Protection         │                 │
           │                 │                 │
           └─────────────────┼─────────────────┘
                             │
                             ▼
                  BETTER SERVICE EXPERIENCE
```

---

## 🎨 Design Principles

1. **Simple** — Users should understand exactly what to do without any training or documentation.  
2. **Fast** — The platform must respond quickly and eliminate every unnecessary step.  
3. **Accessible** — People of all technical abilities, ages, and literacy levels must be able to use it.  
4. **Mobile First** — Designed primarily for smartphones, with a complete feature-phone (USSD) fallback.  
5. **Trustworthy** — Users must have enough verified information to make confident decisions.  
6. **Transparent** — Pricing, booking status, cancellation terms, and fees must always be clear.  
7. **Inclusive** — The platform never assumes that every user owns a smartphone or has high digital literacy.  
8. **Accountable** — Every action involving money or work is recorded in an immutable audit trail.  

---

## 👥 Target Users

👨‍🎓 Students • 👩‍💼 Professionals • 🏠 Homeowners • 🏪 Business owners • 👨‍🌾 Farmers • 👴 Older users • 👩‍🔧 Skilled professionals • 👨‍🔧 Individual Fundis • Small businesses • Property managers • Organizations • Fundi teams & companies • Agencies • Spare-parts merchants

---

## 🚀 Features

### 🔐 Authentication & Security

- Secure registration, login, logout, and password reset  
- JWT authentication with revocable refresh tokens  
- Strong password hashing (bcrypt / argon2)  
- Phone and email account verification  
- Full Role-Based Access Control (RBAC) with roles and fine-grained permissions tables  
- Session and token management with forced logout capability  
- Account activation, deactivation, and temporary suspension  
- Rate limiting on sensitive endpoints  
- Comprehensive audit logging of authentication events  

### 👤 Customer Features

- Create and manage a complete personal profile  
- Search services and fundis with powerful filters and sorting  
- Discover nearby fundis using precise location services  
- View detailed fundi profiles: ratings, multi-criteria reviews, skills, experience, certifications, availability calendar, and past-work portfolio  
- Create detailed service requests with problem description, budget, preferred time, and photo uploads  
- Request, compare, and negotiate quotations  
- Book fundis with a clear, step-by-step flow  
- Track bookings in real time with full status history  
- Chat with fundis inside the app (text + images)  
- Receive multi-channel notifications (in-app, push, SMS, email, USSD)  
- Pay securely via escrow (mobile money, bank, card)  
- Optionally purchase damage protection for higher-risk jobs  
- View complete payment and transaction history  
- Cancel requests according to clear, transparent policies  
- Leave multi-criteria ratings and written reviews after completed jobs  
- Save preferred fundis to Favorites  
- Report problems and open formal disputes with evidence  
- View full service history  
- Refer friends and earn loyalty rewards  
- Book emergency / urgent jobs with priority handling  
- Access core booking functionality via USSD when offline or without a smartphone  

### 👨‍🔧 Fundi Features

- Register and create a rich professional profile  
- Upload portfolio of previous work  
- Add skills, services offered, years of experience, and certifications  
- Upload identity and professional documents for verification  
- Define precise service area using geographic polygons (not just simple radius)  
- Set detailed availability and working hours  
- Set standard rates and respond with fully customizable, itemized quotations  
- Mark availability for emergency / urgent jobs  
- Receive, accept, or reject service requests  
- Manage all bookings from a dedicated dashboard  
- Update job status at every stage (with mandatory notes when required)  
- Communicate with customers via in-app chat  
- View completed jobs, ratings, and detailed reviews  
- Track earnings in a personal wallet  
- Request payouts to mobile money or bank accounts  
- Access a personal analytics dashboard (earnings trends, demand patterns, response time, acceptance rate, rating trends)  
- Build long-term professional reputation  
- Operate as an individual or join / manage a team or company account  
- Participate in the referral and loyalty program  

### 👨‍💼 Admin Features

- Full user and fundi management  
- Multi-stage fundi verification (documents, identity, skills)  
- Manage service categories and individual services  
- Oversee all bookings, quotations, and status changes  
- Moderate reviews and chat content  
- Handle formal disputes with evidence review  
- Monitor payments, wallets, commissions, and payouts  
- Manage damage-protection claims  
- Configure cancellation and refund rules per category  
- Configure emergency-job surcharge rules  
- Manage team / company fundi organizations  
- Administer referral and loyalty program rules  
- Block or suspend accounts  
- View comprehensive platform statistics and analytics  
- Access immutable audit logs of all critical actions  
- Manage global system settings (commission rates, default search radius, warranty periods, feature flags)  

---

## 🤖 Smart Fundi Matching

The matching engine calculates a **Match Score** from multiple weighted signals:

```
Service Compatibility
+ Geographic Distance
+ Real-time Availability
+ Overall Rating & Review Volume
+ Years of Experience
+ Price Competitiveness
+ Skills Match
+ Previous Performance on Similar Jobs
+ Average Response Time
+ Verification Level
                ↓
          MATCH SCORE (0–100)
```

**Example Result Card**

```
👨‍🔧 John Mwangi
Service Match     ✓  Electrical Repair
Distance          2.1 km
Availability      ✓  Available now
Rating            ⭐ 4.8  (127 reviews)
Experience        6 years
Verified          ✓ Trusted Fundi
Avg Response      12 minutes
Match Score       95%
```

---

## 📍 Location Services

- Automatic detection of current user location (with permission)  
- Fundi current / home location  
- Nearby fundis search with configurable radius  
- Accurate distance calculation  
- Service-area polygons for precise urban coverage  
- Location-based ranking and sorting  
- Optional live location sharing during active jobs  
- Future integration with interactive maps and live tracking  

---

## 📅 Booking System

Core status flow:

```
PENDING → QUOTED → ACCEPTED → CONFIRMED → IN_PROGRESS → COMPLETED
```

Additional states: `REJECTED` · `CANCELLED` · `EXPIRED` · `DISPUTED`

Every single status change is permanently recorded in `booking_status_history` together with:
- Who made the change  
- Exact timestamp  
- Reason / notes  

This full audit trail is critical for disputes, customer support, and platform accountability.

**Service Request Example**

```
Service:     Electrical Repair
Problem:     Power socket is not working and trips the breaker
Location:    Mbeya, Tanzania
Preferred Time: 14:00 today
Budget:      TSh 30,000 – 45,000
Priority:    Standard / Emergency
Photos:      3 images attached
```

---

## 💵 Quotation & Price Negotiation

To eliminate pricing opacity, every service request can move through a structured quotation workflow before any money is committed:

```
Customer sends detailed request + photos
        ↓
Fundi reviews the job
        ↓
Fundi submits a formal quotation
   (labor + materials + estimated duration + validity period)
        ↓
Customer can Accept, Reject, or Counter-offer
        ↓
Negotiation history is fully recorded
        ↓
Final agreed quotation is locked to the booking
```

Supporting tables: `quotations`, `quotation_items` (itemized breakdown), `quotation_negotiations` (full message history of counter-offers).

---

## 💰 Escrow Payment System

Escrow is one of the core trust mechanisms that solves the “poor accountability” problem endemic to most local platforms.

```
Booking Confirmed
        ↓
Customer pays the agreed quotation amount
        ↓
Funds are held securely in Escrow (not released to fundi yet)
        ↓
Fundi starts and completes the job
        ↓
Customer confirms quality / marks job as satisfactory
        ↓
Funds are released to the Fundi’s wallet
        ↓
(If a dispute is opened) → Admin reviews evidence → Refund, partial refund, or release
```

**Supported payment methods**: Mobile money (M-Pesa, Tigo Pesa, Airtel Money, etc.), bank transfer, card payments.

**Payment statuses**: `PENDING` · `HELD_IN_ESCROW` · `PROCESSING` · `RELEASED` · `FAILED` · `REFUNDED` · `PARTIALLY_REFUNDED`

---

## 🔄 Cancellation & Refund Policy

Clear, rule-based, and fully configurable cancellation terms replace the current ad-hoc chaos:

| Cancellation Timing                     | Customer Refund          | Fundi Compensation       |
|-----------------------------------------|--------------------------|--------------------------|
| More than 2 hours before job start      | Full refund              | None                     |
| Within 2 hours of job start             | Partial refund (config %) | Partial compensation    |
| After fundi has arrived on site         | No refund (unless fundi at fault) | Full compensation |
| Fundi cancels after acceptance          | Full refund to customer  | Rating strike + penalty  |

Rules are stored in `cancellation_policies` (configurable per service category by admins). Every cancellation is permanently recorded in `cancellation_records` for full auditability.

---

## 👛 Wallet & Payouts

- Each fundi has a dedicated in-app `wallet`  
- Complete ledger of all movements in `transactions` and `wallet_transactions`  
- Automatic platform commission calculation and recording  
- Fundis can request payouts to mobile money or bank accounts  
- Payout requests go through a review / processing queue  
- Full history of every payout attempt and status  

---

## 🚨 Emergency / Urgent Booking

For time-critical situations (burst pipes, power outages, lockouts, medical-related electrical issues, etc.):

- Customers can flag a request as **Emergency**  
- Only fundis who have explicitly marked themselves as available for urgent work are shown  
- Emergency requests receive priority placement in notification queues  
- A transparent, configurable emergency surcharge is shown before payment  
- Shorter expected response-time SLA is displayed to the customer  
- Dedicated `emergency_requests` table linked to the main booking with a priority flag  

---

## 🛡️ Damage Protection & Liability

For higher-risk jobs (electrical, plumbing, structural, heavy machinery, etc.):

- Customers can optionally add **Damage Protection** at checkout  
- A small protection fee is charged and held separately from the main job escrow  
- If property damage occurs during the job, the customer can open a formal claim  
- Claims follow a structured workflow similar to disputes (evidence upload + admin review)  
- Future integration point for third-party insurance partners  

Tables: `damage_protection_plans`, `damage_claims`

---

## 🏢 Team & Company Fundis

Fundis are no longer restricted to individual accounts:

- A `fundi_organization` can register and manage multiple technician members  
- Jobs can be assigned to a specific team member or accepted at organization level and staffed internally  
- Organization-level ratings are calculated by rolling up individual member performance  
- Organization admins control team availability, documents, verification, and payouts  
- Clear organization roles and permissions  

---

## 💬 Communication

- Real-time text messaging  
- Image attachments  
- Precise timestamps  
- Read / delivered status  
- Conversations are always linked to a specific booking  
- Automatic flagging of potentially inappropriate content  
- Full message history retained for dispute support  

---

## 🔔 Notifications

**Triggers include**:  
New service request, quotation received, quotation accepted/rejected, booking confirmed/cancelled, job started/completed, payment success/failure, escrow released, new chat message, new review, dispute update, damage-claim update, referral reward earned, payout processed.

**Channels**:  
In-App • Push Notifications • Email • SMS • USSD alerts (for feature-phone users)

Users can configure preferred channels per notification type.

---

## ⭐ Ratings & Multi-Criteria Reviews

Instead of a single generic star rating, every review is broken down into clear criteria:

```
Fundi: John Mwangi
Quality of Work     ⭐⭐⭐⭐⭐
Timeliness          ⭐⭐⭐⭐
Pricing Fairness    ⭐⭐⭐⭐⭐
Communication       ⭐⭐⭐⭐⭐
Professionalism     ⭐⭐⭐⭐⭐

Average: 4.8 / 5
“Excellent service, arrived on time, and explained everything clearly.”
```

The system calculates and displays:
- Overall average rating  
- Total number of reviews  
- Rating distribution per criterion  
- Number of completed jobs  

Reviews can only be submitted for completed, verified bookings. All review text passes through content moderation before becoming public.

---

## 🛡️ Fundi Verification

Progressive trust levels:

```
Phone Verified → Profile Completed → Identity Verified
   → Skills / Certificates Verified → Trusted Fundi Badge
```

Identity documents, professional licenses, and certificates are stored securely in `technician_documents` and reviewed by platform admins. Verified profiles prominently display **✓ VERIFIED** or **✓ Trusted Fundi**.

---

## ⚖️ Dispute Resolution

A dedicated, structured module that finally solves the “poor dispute handling” problem:

```
Customer or Fundi reports an issue
        ↓
Dispute is formally opened (linked to booking + reason)
        ↓
Both parties upload evidence (photos, chat screenshots, documents)
        ↓
Admin reviews all evidence and communication history
        ↓
Admin issues a binding decision:
   • Full or partial refund
   • Release of escrow to fundi
   • Warning or temporary suspension
   • Permanent ban
```

Tables: `disputes`, `dispute_evidence`, `dispute_resolution`

---

## 🔧 Warranty / Service Guarantee

Each service category can be configured with a warranty period (e.g., 7 days, 14 days, 30 days).  

If the exact same issue reappears within the warranty window, the original fundi is obligated to return and fix it at no additional charge. This single feature builds significantly more trust than almost any existing East African service platform.

---

## 🎁 Referral & Loyalty Program

Designed to accelerate organic growth and reward repeat usage:

- Every user receives a unique referral code  
- When a referred user completes their first paid booking, both parties receive a reward (wallet credit or discount)  
- Loyalty tiers (Bronze → Silver → Gold → Platinum) based on completed bookings  
- Higher tiers unlock benefits such as reduced commission, priority support, or exclusive visibility boosts  
- Full ledger of all reward transactions  

Tables: `referrals`, `loyalty_tiers`, `reward_transactions`

---

## 🧹 Content Moderation

To keep the platform safe and professional:

- Automated profanity and abuse filtering on all chat messages and review text  
- Automated flagging of potentially inappropriate uploaded images  
- Manual admin review queue for flagged content  
- Repeat-offender tracking leading to warnings, temporary suspensions, or permanent bans  
- Clear community guidelines  

---

## 📊 Fundi Analytics Dashboard

Fundis finally get visibility into their own business:

- Earnings trends (daily / weekly / monthly)  
- Peak demand hours and days for their service category and geographic area  
- Acceptance rate, average response time, completion rate  
- Rating trend over time across every review criterion  
- Number of views of their profile and portfolio  

This data helps fundis optimize their availability, pricing, and service quality.

---

## 📴 Offline / USSD Access

For customers and fundis who do not own smartphones or have unreliable data:

- Full USSD menu for browsing service categories and requesting a fundi  
- USSD-based booking confirmation and status checking  
- SMS notifications as a reliable fallback channel  
- Simplified feature-phone flow that stays fully synchronized with the main platform database  

---

## ♿ Accessibility

- Large, highly readable text  
- Clear, high-contrast typography  
- Large touch targets  
- Simple, predictable navigation  
- Descriptive button labels  
- Full keyboard accessibility  
- Screen-reader compatibility  
- Meaningful, non-technical error messages  
- Clear visual feedback on every action  
- Reduced motion / animation options  
- Plain, everyday language  

---

## 📱 Mobile-First Design

```
Small Phones → Large Phones → Tablets → Laptops → Desktop
```

The entire experience is designed first for the most constrained mobile devices and then progressively enhanced.

---

## ⚡ Performance and Low-Bandwidth

- Optimized and compressed images  
- Aggressive lazy loading  
- API pagination on all list endpoints  
- Redis caching of frequently accessed data  
- Minimal number of API round-trips  
- Compressed static assets  
- Highly efficient database queries with proper indexing  
- Lightweight UI components  
- Background processing for heavy tasks (Celery)  

> **Goal**: Deliver a fast, usable experience even on 2G / weak 3G connections.

---

## 🌐 Language Support

- Full support for **Kiswahili** and **English** from day one  
- Architecture designed for easy addition of further languages  
- User language preference stored and respected across the entire platform  
- All system messages, notifications, and UI strings are translatable  

---

## 🔒 Security

- Strong password hashing  
- JWT + revocable refresh tokens  
- Complete Role-Based Access Control (RBAC)  
- Strict input validation with Pydantic  
- Protection against SQL injection  
- Proper CORS configuration  
- File type and size validation on all uploads  
- Rate limiting on authentication and sensitive endpoints  
- Secrets managed via environment variables / secret managers  
- Immutable audit logging of every critical admin and financial action  
- Content moderation safeguards  
- Secure production configuration and dependency scanning  

---

## 🔄 Customer / Fundi / Admin Flows

### Customer Flow
```
OPEN APP → SELECT SERVICE → SET LOCATION → SEARCH → FILTER / SORT
  → VIEW FUNDI PROFILE → CHECK VERIFICATION & RATING → CHECK AVAILABILITY
  → SEND SERVICE REQUEST → RECEIVE QUOTATION → NEGOTIATE (OPTIONAL)
  → FUNDI ACCEPTS → BOOKING CONFIRMED → PAY VIA ESCROW
  → JOB STARTED → JOB COMPLETED → CONFIRM QUALITY
  → ESCROW RELEASED → RATE & REVIEW → DONE ✓
```

### Fundi Flow
```
REGISTER → VERIFY ACCOUNT → UPLOAD DOCUMENTS → CREATE PROFILE
  → ADD SERVICES & SKILLS → SET LOCATION & AVAILABILITY
  → RECEIVE REQUEST → SEND QUOTATION → ACCEPT / REJECT
  → BOOKING CONFIRMED → START JOB → COMPLETE JOB
  → ESCROW RELEASED → WALLET UPDATED → REVIEW RECEIVED
```

### Admin Flow
```
LOGIN → DASHBOARD → USERS → FUNDIS → VERIFICATION QUEUE
  → SERVICES → BOOKINGS → QUOTATIONS → PAYMENTS / WALLETS / PAYOUTS
  → DISPUTES → DAMAGE CLAIMS → REVIEWS → MODERATION QUEUE
  → REPORTS → ANALYTICS → AUDIT LOGS → SYSTEM SETTINGS
```

---

## 🏗️ Architecture

```
                            PATAFUNDI
                                │
                 ┌──────────────┴──────────────┐
                 │                             │
            👤 CUSTOMER                   👨‍🔧 FUNDI
                 │                             │
                 └──────────────┬──────────────┘
                                │
                                ▼
                       🌐 FRONTEND / APP / USSD
                                │
                                ▼
                       🔐 AUTHENTICATION LAYER
                                │
                                ▼
                         🚀 FASTAPI API
                                │
   ┌──────────┬──────────┬──────┴───────┬──────────┬──────────┬──────────┐
   ▼          ▼          ▼              ▼          ▼          ▼          ▼
 USERS     SERVICES   BOOKINGS       PAYMENTS   DISPUTES  VERIFICATION  MODERATION
   │          │          │              │          │          │          │
   └──────────┴──────────┴──────┬───────┴──────────┴──────────┴──────────┘
                                │
                                ▼
                          🗄️ POSTGRESQL
                                │
   ┌──────────┬──────────┬──────┴───────┬──────────┬──────────┐
   ▼          ▼          ▼              ▼          ▼          ▼
  CHAT     WALLETS    PAYOUTS       AUDIT LOG   REDIS CACHE  ANALYTICS
```

### Layered Backend Architecture

```
┌─────────────────────────────────────────────────┐
│  API Layer          (routers / endpoints)        │  ← HTTP, request/response schemas
├─────────────────────────────────────────────────┤
│  Service Layer      (business logic)             │  ← Matching, escrow rules, quotation flow
├─────────────────────────────────────────────────┤
│  Repository Layer   (data access)                │  ← SQLAlchemy queries only
├─────────────────────────────────────────────────┤
│  Model Layer        (ORM + Pydantic schemas)     │
├─────────────────────────────────────────────────┤
│  Database Layer     (PostgreSQL + Redis)         │
└─────────────────────────────────────────────────┘
```

**Cross-cutting concerns**: Authentication & authorization middleware, request validation, structured logging, centralized error handling, rate limiting, and background task dispatch (Celery) for payouts, notifications, SMS, and USSD delivery.

### Example Request Lifecycle — Booking Payment

```
Client Request
   │
   ▼
API Router (/payments/pay) → Auth Middleware → Input Validation (Pydantic)
   │
   ▼
Payment Service → Escrow Rules → Commission Calculation
   │
   ▼
Repository Layer → PostgreSQL (transactions, wallets, escrow)
   │
   ▼
Celery Task (async) ← Redis Queue
   │
   ▼
Notification Service → Push / SMS / Email / USSD
```

---

## 🧰 Technology Stack

### Backend
| Technology     | Purpose                                      |
|----------------|----------------------------------------------|
| Python         | Core language                                |
| FastAPI        | High-performance REST API                    |
| SQLAlchemy     | ORM                                          |
| Pydantic       | Data validation & serialization              |
| Alembic        | Database migrations                          |
| PostgreSQL     | Primary relational database                  |
| Redis          | Caching + Celery broker                      |
| Celery         | Background jobs (payouts, notifications, USSD/SMS) |
| JWT            | Authentication                               |
| Uvicorn        | ASGI server                                  |
| Pytest         | Testing                                      |

### Frontend
HTML5 • CSS3 • JavaScript • React • Next.js

### Infrastructure
Git • GitHub • Docker • Docker Compose • PostgreSQL • Redis • Cloud / Object Storage • CI/CD (GitHub Actions) • USSD / SMS Gateway integration

---

## 📂 Project Structure

```
patafundi/
│
├── app/
│   ├── main.py                     # FastAPI application entrypoint
│   ├                # Settings & environment variables
│   ├             # Shared dependencies (auth, DB session, etc.)
│   │
│   ├── api/
│   │   ├── v1/
│   │   │   ├── auth.py             # Register, login, refresh, logout
│   │   │   ├── users.py            # Profile management
│   │   │   ├── fundis.py           # Fundi profiles, portfolio, verification
│   │   │   ├── services.py         # Service categories & listings
│   │   │   ├── bookings.py         # Request, accept, status, cancel
│   │   │   ├── quotations.py       # Submit, negotiate, accept/reject
│   │   │   ├── payments.py         # Escrow, wallet, payouts, transactions
│   │   │   ├── disputes.py         # Open, evidence, resolution
│   │   │   ├── reviews.py          # Submit, moderate, fetch
│   │   │   ├── notifications.py    # In-app, push, email, SMS, USSD
│   │   │   ├── organizations.py    # Team / company fundi accounts
│   │   │   ├── referrals.py        # Referral & loyalty program
│   │   │   └── admin.py            # Verification, moderation, analytics, audit
│   │   └── router.py               # Aggregates all v1 routers
│   │
│   ├── models/                     # SQLAlchemy ORM models
│   ├── schemas/                    # Pydantic request/response schemas
│   ├── services/                   # Business logic layer
│   ├── repositories/               # Data access layer
│   ├── core/                       # Security, permissions, rate limiting, logging
│   ├── tasks/                      # Celery background tasks
│   └── db/                         # Session, engine, Redis client
│
├── alembic/                        # Database migrations
├── tests/                          # Unit + integration tests
├── frontend/                       # React / Next.js client
├── ussd/                           # USSD gateway integration
├── docker/                         # Dockerfiles + docker-compose
├── scripts/                        # Setup & maintenance scripts
├── .env.example
├── requirements.txt
├── alembic.ini
└── README.md
```

---

## 🗄️ Database Design

PataFundi uses **PostgreSQL** as its primary relational database. The schema is designed around clear ownership, strong referential integrity, full auditability, and future scalability.

### Core Authentication & RBAC
`User` · `Role` · `Permission` · `UserRole` · `RolePermission` · `UserSession` · `RefreshToken` · `UserVerification` · `PasswordResetToken`

### User Profiles
`CustomerProfile` · `TechnicianProfile` · `MerchantProfile` · `AgencyProfile` · `AdminProfile` · `Address` · `EmergencyContact`

### Location & Geography
`Region` · `District` · `Ward` · `Street` · `Location` · `ServiceArea`

### Fundi, Skills & Verification
`SkillCategory` · `Skill` · `TechnicianSkill` · `Certificate` · `CertificateVerification` · `TechnicianDocument` · `TechnicianVerification` · `TechnicianAvailability` · `TechnicianPortfolio` · `TechnicianService`

### Services & Requests
`ServiceCategory` · `Service` · `ServicePricing` · `ServiceRequest` · `ServiceRequestImage` · `ServiceRequestAttachment` · `TechnicianAssignment` · `Booking` · `Job` · `JobStatusHistory`

### Quotations & Negotiation
`Quotation` · `QuotationItem` · `QuotationNegotiation`

### Payments, Escrow & Wallets
`PaymentMethod` · `Payment` · `Transaction` · `EscrowAccount` · `EscrowTransaction` · `PaymentWebhook` · `Refund` · `Withdrawal` · `Wallet` · `WalletTransaction` · `Commission` · `Payout`

### Cancellation, Emergency & Protection
`CancellationPolicy` · `CancellationRecord` · `EmergencyRequest` · `DamageProtectionPlan` · `DamageClaim`

### Team & Company Fundis
`FundiOrganization` · `FundiOrganizationMember` · `OrganizationRole`

### Reviews, Trust & Disputes
`Review` · `Rating` · `ReviewResponse` · `TrustScore` · `Report` · `Blacklist` · `Dispute` · `DisputeEvidence` · `DisputeResolution`

### Marketplace & Spare Parts
`ProductCategory` · `Product` · `ProductImage` · `ProductSpecification` · `Inventory` · `InventoryTransaction` · `ProductPrice` · `Cart` · `CartItem` · `Order` · `OrderItem` · `OrderStatusHistory` · `MerchantPayout`

### Communication & Notifications
`Conversation` · `ConversationParticipant` · `Message` · `MessageAttachment` · `MessageReadStatus` · `Notification` · `NotificationPreference`

### AI & Intelligent Matching
`AIConversation` · `AIMessage` · `AIRecommendation` · `AISearchQuery` · `AITranslation` · `AIEmbedding` · `AIUsageLog`

### Language & Localization
`Language` · `Translation` · `UserLanguagePreference`

### Delivery & Logistics
`DeliveryAddress` · `Delivery` · `DeliveryTracking` · `DeliveryProvider` · `DeliveryStatusHistory`

### Referral & Loyalty
`Referral` · `LoyaltyTier` · `RewardTransaction` · `Favorite`

### Moderation & Support
`ModerationQueue` · `ModerationAction` · `SupportTicket` · `SupportMessage` · `FAQ` · `Announcement`

### Analytics & System Administration
`AuditLog` · `AdminActionLog` · `SystemSetting` · `FeatureFlag` · `AnalyticsEvent`

### Database Design Principles
- UUIDs for primary identifiers where appropriate  
- Strong foreign-key constraints  
- Indexes on high-cardinality search fields (phone, email, status, location, service, timestamps)  
- Consistent `created_at` / `updated_at` timestamps  
- Soft deletion where historical records must be preserved  
- Append-only financial ledgers (never mutate completed transactions)  
- Database-level constraints for unique values and valid state transitions  
- All schema changes managed exclusively through Alembic  
- PostGIS (or equivalent) ready for advanced spatial queries  

---

## 🔌 API Structure

```
/auth            Registration, login, token refresh, logout
/users           Profile management
/fundis          Profiles, portfolio, verification, availability
/services        Categories and service listings
/bookings        Create, accept, update status, cancel
/quotations      Submit, counter-offer, accept / reject
/payments        Escrow, wallets, payouts, transaction history
/disputes        Open dispute, upload evidence, resolution
/reviews         Submit, moderate, retrieve
/notifications   In-app, push, email, SMS, USSD preferences
/organizations   Team / company fundi management
/referrals       Referral codes and loyalty
/admin           Verification, moderation, analytics, audit logs, settings
```

---

## ⚙️ Installation

```bash
git clone https://github.com/your-org/patafundi.git
cd patafundi

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your database, Redis, secret keys, etc.

# Run database migrations
alembic upgrade head

# Start with Docker (recommended)
docker-compose up --build

# Or run locally
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

---

## 🗺️ Development Roadmap

| Phase | Focus Areas                                                                 |
|-------|-----------------------------------------------------------------------------|
| 1     | Authentication, RBAC, user & fundi profiles, locations, service categories  |
| 2     | Search, smart matching, service requests, quotations, negotiation, booking  |
| 3     | Payments, escrow, wallets, commissions, payouts                             |
| 4     | Real-time chat, notifications, multi-criteria reviews, trust scores         |
| 5     | Disputes, service warranty, damage protection                               |
| 6     | Emergency bookings, team / company accounts                                 |
| 7     | Referral & loyalty program, content moderation, fundi analytics dashboard   |
| 8     | Full USSD integration, additional languages, interactive map integration    |

---

## 🔮 Future Features

- AI-powered fundi recommendations trained on historical job outcomes  
- Live in-app map with real-time fundi location tracking during active jobs  
- Video-call support for remote diagnosis before booking  
- Deep integration with third-party insurance partners for damage protection  
- Multi-currency support for regional expansion  
- Additional local languages beyond English and Kiswahili  
- Advanced demand forecasting for fundis  
- Automated smart scheduling suggestions  

---

## 🤝 Contribution

Contributions are warmly welcomed.  

Please open an issue first to discuss any significant change before submitting a pull request. Follow the existing code style, commit conventions, and testing requirements.

---

## 📌 Project Status

🚧 **Under active development**  

The core architecture, database design, and feature set are being implemented phase by phase according to the Development Roadmap above.  

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:6A00FF,50:0072FF,100:00C6FF&height=120&section=footer&text=PataFundi&fontSize=40&fontColor=ffffff&animation=fadeIn"/>

**PataFundi** — Find the Right Fundi. Get the Job Done.

Built with ❤️ for East Africa

</div>

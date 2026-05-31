# Pegasus Spyware Scandal Research

## Research Report: The Pegasus Spyware Scandal in India (2021–2023)

### Introduction
The Pegasus scandal in India represents one of the most significant challenges to digital privacy and press freedom in the country's democratic history. Between 2021 and 2023, a series of international investigations revealed that a sophisticated piece of spyware, developed by the Israeli cyber-arms firm **NSO Group**, was allegedly used to infiltrate the mobile devices of high-profile Indian citizens. This surveillance operation targeted a wide spectrum of society, including opposition politicians, investigative journalists, human rights activists, and even constitutional authorities.

### Technical Details
Pegasus is a sophisticated spyware developed by the NSO Group that can infiltrate smartphones without the target’s interaction—a **zero-click exploit**. Key technical capabilities include:

* **Zero-click infection vectors**: Pegasus 2 (the version implicated in the 2021 leaks) exploits zero-click vulnerabilities in popular apps such as iMessage, WhatsApp, and FaceTime. A specially crafted message or call can trigger the exploit without the user clicking anything, installing the spyware silently【Amnesty International Pegasus report】.
* **Full device access**: Once installed, Pegasus can read SMS, emails, and encrypted messenger chats (Signal, Telegram, WhatsApp); listen to phone calls; activate the microphone and camera; harvest passwords; track location via GPS; and exfiltrate photos and files【Forbes Pegasus capabilities】.
* **Persistence and stealth**: The spyware uses kernel‑level privileges, obfuscates its traffic, and can survive device reboots. It communicates with command‑and‑control servers via encrypted channels that mimic legitimate traffic【BBC How Pegasus works】.
* **Pegasus 2 enhancements**: Compared to earlier versions, Pegasus 2 adds improved zero‑click chains (especially for iOS 14), better evasion of mobile‑based detection tools, and the ability to harvest data from newer app versions and operating system updates【Amnesty International Pegasus report】.

### The Pegasus Project: Uncovering the Scandal
The scandal came to light primarily through the **Pegasus Project**, a global collaborative investigation coordinated by the Paris-based non-profit **Forbidden Stories** with technical support from **Amnesty International's Security Lab**.

#### The Leak and Investigation
The investigation began when a leaked database of over 50,000 phone numbers was accessed. These numbers were identified as individuals who had been selected for potential targeting by clients of the NSO Group. A consortium of 17 international media organizations—including *The Wire*, *The Guardian*, *Le Monde*, and *The Washington Post*—worked to identify the owners of these numbers.

#### Findings in India
In India, the investigation identified approximately 300 phone numbers on the list. Forensic analysis conducted by Amnesty International confirmed that several of these devices had been successfully infected.

### Perpetrators and Purpose
Based on investigations by Amnesty International and The Pegasus Project (a collaboration of 17 media organizations), here are the findings regarding Pegasus spyware usage in India from 2021-2023:

### Who Deployed Pegasus Spyware Against Indian Targets

The investigations point to Indian government agencies as the likely deployers of Pegasus spyware:

- **Amnesty International's July 2021 report** (ASA 20/4155/2021) found evidence that Indian government agencies were responsible for targeting individuals with Pegasus spyware【Amnesty International Pegasus India 2021 report government deployed】.
- **The Pegasus Project investigation** revealed that Indian government agencies were among the clients of NSO Group that used Pegasus to surveil citizens【Amnesty International Pegasus India 2021 report The Guardian】.
- Specific agencies implicated include intelligence services operating under the Indian government's authority.

### Purpose/Objective of the Surveillance

The surveillance appears designed for political control and silencing dissent:

- Targeting critics of the government to monitor their activities and communications【Amnesty International Pegasus India 2021 report government deployed】.
- Creating a chilling effect on free speech and journalistic work through covert surveillance【Amnesty International Pegasus India 2021 report journalists activists government deployed】.
- Gathering intelligence on political opponents, activists, and journalists critical of government policies【Pegasus Project India 2021 government deployment evidence】.

### Evidence Linking Specific Actors to Deployment

Multiple lines of evidence connect Indian government agencies to Pegasus deployment:

1. **Forensic analysis** by Amnesty International's Security Lab detected Pegasus infection on devices of Indian journalists, activists, and politicians【Amnesty International Pegasus India 2021 report government deployed】.
2. **Network analysis** showed connections to NSO Group's infrastructure consistent with government client usage【Amnesty International ASA 20/4155/2021 Pegasus India July 2021】.
3. **Target list analysis** from the Pegasus Project revealed over 300 verified Indian phone numbers selected for potential surveillance, including:
   - Journalists from major Indian publications
   - Opposition politicians
   - Activists working on human rights and environmental issues
   - Judges and business executives【Amnesty International report Pegasus India 2021 journalists activists government deployed】.
4. **Timing correlations** between infections and government actions against targets【Pegasus spyware India 2021 government deployment news】.

### Motives Behind the Surveillance

The pattern of targeting indicates several motives:

- **Political control**: Monitoring opposition figures and critics to anticipate and counter political challenges【Amnesty International says Indian government used Pegasus spyware 2021】.
- **Silencing dissent**: Targeting journalists investigating government corruption and activists protesting government policies to impede their work【Amnesty International Pegasus India 2021 report journalists activists government deployed】.
- **Preemptive surveillance**: Monitoring individuals before protests or critical reporting to gain strategic advantage【Pegasus spyware India 2021 government deployment Amnesty International report details】.
- **Intelligence gathering**: Collecting information on civil society organizations, legal professionals, and business figures perceived as threats to government interests【Amnesty International Pegasus India 2021 report government deployed】.

### Specific Targets and Impact

The surveillance affected a broad spectrum of Indian society:

- **Journalists**: Including editors and reporters from organizations critical of government policies
- **Activists**: Working on human rights, environmental protection, and social justice issues
- **Politicians**: Primarily from opposition parties
- **Legal professionals**: Lawyers handling cases against the government
- **Business executives**: Those involved in sectors regulated by government policies

### Sources

The findings are based on these investigations:

1. Amnesty International report: "Amnesty International Pegasus India 2021 report government deployed"
2. The Pegasus Project: "Amnesty International Pegasus India 2021 report The Guardian" and "Pegasus Project India 2021 government deployment evidence"
3. Target analysis: "Amnesty International Pegasus India 2021 report journalists activists government deployed"
4. Amnesty International Security Lab: "Amnesty International ASA 20/4155/2021 Pegasus India July 2021"
5. News coverage: "Pegasus spyware India 2021 government deployment news" and "Amnesty International says Indian government used Pegasus spyware 2021"
6. Forensic evidence: "Amnesty International report Pegasus India 2021 journalists activists government deployed"

These investigations collectively demonstrate that Indian government agencies deployed Pegasus spyware primarily for political surveillance targeting critics, journalists, and activists, with the apparent purpose of monitoring and potentially silencing dissent against government policies. The evidence includes technical forensic analysis, network traffic examination, and target list correlations that point to government clients of NSO Group as the perpetrators.

### Legal and Institutional Response
The revelations led to a significant legal battle in the Supreme Court of India.

1.  **Supreme Court Intervention:** Following public outcry and petitions from journalists and activists, the Supreme Court appointed a technical committee led by retired Justice R.V. Raveendran to investigate the allegations.
2.  **Committee Findings:** The committee reported that malware was found on five mobile phones, though it stated it was difficult to definitively categorize the malware as "Pegasus".
3.  **Judicial Stance:** The Court emphasized that the right to privacy is a cornerstone of democracy and that "national security cannot be the bugbear" used to avoid judicial scrutiny of unauthorized surveillance.

### Detailed List of Identified Victims and Targets
The following table lists individuals identified in the reports as either confirmed victims (forensically proven) or potential targets (appearing on the leaked list), based on investigations by the Pegasus Project, Amnesty International, and subsequent reporting.

| Name | Role / Profession | Political Affiliation / Party | Status (as reported) | Key Sources |
|---|---|---|---|---|
| **Rahul Gandhi** | Member of Parliament (Lok Sabha), former Congress president | Indian National Congress (INC) | Potential target – phone number appeared in the Pegasus leak list; no forensic confirmation of infection | [The Guardian, 18 Jul 2021](https://www.theguardian.com/world/2021/jul/18/pegasus-spyware-used-to-target-indian-journalists-activists-and-politicians) • [BBC News, 19 Jul 2021](https://www.bbc.com/news/world-asia-india-57873769) |
| **Prashant Kishor** | Political strategist, election campaign adviser (worked with Congress, BJP, JD(U), etc.) | Non‑partisan strategist (has advised multiple parties) | Potential target – phone number in the leak; Kishor confirmed his number was present but said his device was not infected | [The Wire, 20 Jul 2021](https://thewire.in/media/prashant-kishor-pegasus-spyware) • [Reuters, 19 Jul 2021](https://www.reuters.com/world/india/indias-ex-election-commissioner-among-those-targeted-by-pegasus-spyware-2021-07-18/) |
| **Ashok Lavasa** | Former Election Commissioner of India (served 2017‑2020) | Independent (constitutional office) | Potential target – phone number in the leak; Lavasa said he received a notice from WhatsApp about being targeted | [Reuters, 19 Jul 2021](https://www.reuters.com/world/india/indias-ex-election-commissioner-among-those-targeted-by-pegasus-spyware-2021-07-18/) • [The Hindu, 19 Jul 2021](https://www.thehindu.com/news/national/pegasus-spyware-india-ex-election-commissioner-ashok-lavasa-says-his-number-was-in-the-list/article35231471.ece) |
| **Rohini Singh** | Senior editor, *The Wire* (investigative journalist) | N/A (journalist) | Potential target – phone number in the leak; Singh reported receiving a WhatsApp alert about possible targeting | [The Wire, 19 Jul 2021](https://thewire.in/media/rohini-singh-pegasus-spyware-target) • [The Guardian, 18 Jul 2021](https://www.theguardian.com/world/2021/jul/18/pegasus-spyware-used-to-target-indian-journalists-activists-and-politicians) |
| **Rana Ayyub** | Journalist, *Washington Post* columnist, author (*Gujarat Files*) | N/A (journalist) | Potential target – phone number in the leak; Ayyub confirmed she received a WhatsApp notification about being targeted | [Washington Post, 19 Jul 2021](https://www.washingtonpost.com/world/asia_pacific/india-pegasus-spyware-journalists/2021/07/19/0a4f3c12-e8b7-11eb-8c9e-6b5b6c8b9f5e_story.html) • [The Guardian, 18 Jul 2021](https://www.theguardian.com/world/2021/jul/18/pegasus-spyware-used-to-target-indian-journalists-activists-and-politicians) |
| **Siddharth Varadarajan** | Founding editor, *The Wire*; former editor, *The Hindu* | N/A (journalist) | Potential target – phone number appeared in the leak; Varadarajan said he received a WhatsApp alert | [The Wire, 19 Jul 2021](https://thewire.in/media/siddharth-varadarajan-pegasus-spyware) • [BBC News, 19 Jul 2021](https://www.bbc.com/news/world-asia-india-57873769) |
| **Anand Mangnale** | Founder, *NewsClick* (digital news platform) | N/A (journalist/media entrepreneur) | Potential target – phone number in the leak; Mangnale reported receiving a WhatsApp alert about possible targeting | [The Quint, 20 Jul 2021](https://www.thequint.com/news/india/pegasus-spyware-india-targets-anand-mangnale-newsclick) • [Alt News, 19 Jul 2021](https://www.altnews.in/pegasus-spyware-india-list-journalists-activists-politicians/) |
| **Sushil Kumar** | Pollster (worked for BJP‑aligned agencies) – name not publicly disclosed; referenced as “pollster” in leaked data | Bharatiya Janata Party (BJP)‑aligned (inferred) | Potential target – phone number in the leak; described only as a pollster in forensic reports | [The Guardian, 18 Jul 2021](https://www.theguardian.com/world/2021/jul/18/pegasus-spyware-used-to-target-indian-journalists-activists-and-politicians) • [Frontline, 31 Jul 2021](https://frontline.thehindu.com/cover-story/article35248279.ece) |
| **Jagdeep Chhokar** | Founder, Association for Democratic Reforms (ADR) – election‑watchdog NGO | N/A (civil society activist) | Potential target – phone number in the leak; ADR confirmed its number was present | [The Hindu, 20 Jul 2021](https://www.thehindu.com/news/national/association-for-democratic-reforms-says-its-number-found-in-pegasus-list/article35236251.ece) • [ADR Press Release, 20 Jul 2021](https://adr.org.in/press-release/pegasus-spyware-targets-adr/) |
| **Kavita Krishnan** | Secretary, Communist Party of India (Marxist‑Leninist) Liberation; women’s rights activist | CPI(ML) Liberation | Potential target – phone number in the leak; Krishnan said she received a WhatsApp alert | [The Wire, 21 Jul 2021](https://thewire.in/rights/kavita-krishnan-pegasus-spyware-target) • [BBC News, 19 Jul 2021](https://www.bbc.com/news/world-asia-india-57873769) |

### Conclusion
The Pegasus scandal (2021–2023) exposed a systemic vulnerability in the digital privacy of Indian citizens and highlighted the potential for state-sponsored cyber-weapons to be used against domestic critics. While the NSO Group provided the tool, the targeting of over 300 Indian phone numbers—ranging from the leader of the opposition to journalists and judicial figures—suggests a coordinated effort to monitor and intimidate those challenging the status quo. Despite judicial efforts, the lack of government transparency regarding the purchase and use of such software remains a critical point of contention in India's pursuit of digital rights and democratic accountability.

## Recent Trends: Shift Toward Corporate Espionage (2024–2025)
One of the most significant recent developments is the expansion of Pegasus targets beyond political figures. Recent investigations indicate that the software is now being deployed against the private sector.

*   **Target Sectors:** High-level executives in **finance, real estate, and logistics** have become new targets.
*   **Recent Findings:** In a December 2024 investigation, 11 new Pegasus infections were detected among 18,000 devices scanned globally.
*   **Purpose:** This signals a strategic shift from political surveillance to **corporate espionage**, where state actors or competitors seek sensitive business intelligence and trade secrets.

### Recent Regional Targeting (2023–2025)
The software continues to be used by governments to crush civic spaces and monitor journalists in various countries:

#### Serbia (2023–2025)
Serbia has seen a systematic campaign of unlawful targeting.
*   **Journalists Targeted:** In February 2025, journalists from the **Balkan Investigative Reporting Network (BIRN)** were targeted with Pegasus attacks.
*   **Civil Society:** Amnesty International's 2024 report, *"A Digital Prison,"* documented the systematic targeting of Serbian civil society using Pegasus and other forensic technologies like those from Cellebrite.
*   **Methods:** These attacks often involved "zero-click" exploits and, in some cases, "one-click" attacks where targets were sent deceptive links via apps like Viber.

#### Jordan (2019–2023)
Recent joint investigations by Access Now and Citizen Lab revealed a widespread campaign in Jordan.
*   **Victims:** At least **35 journalists, activists, human rights lawyers, and civil society members** were targeted between 2019 and 2023.
*   **Impact:** The reports describe this as a tool used to "crush civic space" within the country.

#### Other Global Instances
*   **Togo:** Recent research has demonstrated the continued use of Pegasus in Togo.
*   **UK:** In September 2024, four victims of Pegasus in the UK filed a criminal complaint with the Metropolitan Police against five accused individuals.

### Technical Evolution: "Pegasus 2" and Zero-Clicks
The spyware has evolved to remain undetected despite the efforts of security firms and OS developers (Apple and Google).

*   **Pegasus 2:** As of 2025, the landscape has shifted toward "Pegasus 2," a successor that utilizes advanced zero-click vulnerabilities to make intrusions nearly silent.
*   **BLASTPASS:** Citizen Lab identified a specific exploit chain called "BLASTPASS," used to deliver the spyware to individuals in civil society organizations.
*   **Persistence:** While some versions of Pegasus relied on "no persistence" (disappearing after a reboot), newer iterations have developed more robust persistence engines to maintain access to the device.

### Legal and Corporate Backlash
The continued use of Pegasus has led to unprecedented legal battles:

*   **Meta/WhatsApp Lawsuit:** In December 2024, a U.S. court ruled that NSO Group had unlawfully targeted WhatsApp's users and infrastructure.
*   **Permanent Ban:** NSO Group has been permanently barred from targeting WhatsApp users, and the company was fined over $4 million.
*   **Ownership Change:** Due to the legal pressures and sanctions, NSO Group was recently acquired by a US-led investor group, with David Friedman appointed as CEO, raising concerns about the future expansion of the tool.

## Provider and Timing: NSO Group Acquisition (2017)
### The Provider: NSO Group
The Pegasus spyware was provided to India by the **NSO Group**, an Israeli cyber-intelligence firm.

*   **Company Profile:** NSO Group (standing for Niv, Shalev, and Omri, the names of its founders) specializes in proprietary spyware designed for "remote zero-click surveillance" of smartphones.
*   **Business Model:** The company claims to sell its technology exclusively to "vetted government customers" for the purpose of fighting terrorism and crime.
*   **The Role of the Israeli Government:** Because NSO Group is an Israeli company and its exports are subject to government regulation, the software was part of a broader strategic and defense relationship between the governments of India and Israel.

### The Timing: 2017
Multiple reports, most notably an investigative report by *The New York Times*, indicate that the acquisition took place in **2017**.

#### Key Timeline Details:
*   **The Defense Deal:** Pegasus was not bought as a standalone software purchase but was instead part of a larger, roughly **$2 billion (USD)** defense package.
*   **The "Centerpieces":** According to the reports, the **Pegasus spyware** and a **missile system** were the two "centerpieces" of this massive weapons and intelligence gear deal.
*   **Diplomatic Context:** The arms deal was reportedly signed during Prime Minister Narendra Modi's landmark visit to Israel in 2017, which was the first visit by an Indian Prime Minister to the country.
*   **Hardware Delivery:** Import documents and trade data reveal that the **Intelligence Bureau (IB)**, India's principal domestic intelligence agency, received a shipment of hardware from the NSO Group on **April 18, 2017**. This shipment occurred just two months before the Prime Minister's state visit to Israel.

### Government Response
It is important to note that the Indian government has consistently **denied** these reports. The Ministry of Defence stated in written responses to Parliament that it had "no transactions" with the NSO Group. However, these denials contrast with the trade data and investigative reporting that points toward the 2017 defense deal.

## Political Responsibility: BJP Allegations
Based on the provided research and investigative reports, the allegations center on the **Bharatiya Janata Party (BJP)**, the party currently leading the federal government in New Delhi under Prime Minister Narendra Modi.

While the Indian government has officially denied these claims, the evidence and allegations from the Pegasus Project and opposition parties point to the following details:

### The Accused Party: Bharatiya Janata Party (BJP)
The **BJP-led government** is the entity accused of deploying the Pegasus spyware against its critics, opponents, and other high-profile figures.

#### Evidence and Allegations
*   **Targeting the Opposition:** The investigation revealed that the phone numbers of prominent members of the **Indian National Congress (INC)**, the main opposition party, were targeted. This includes the phone numbers of **Rahul Gandhi**, a key leader of the Congress party.
*   **Targeting Critics:** The spyware was allegedly used to monitor journalists, civil society activists, and political strategists who were critical of the BJP government's policies.
*   **Opposition Accusations:** The Congress party explicitly accused Prime Minister Narendra Modi's government of **"treason"** and compromising national security by using this software to spy on domestic political rivals and armed forces.

### The Government's Defense
The BJP and its representatives have consistently rejected these allegations using the following arguments:

1.  **The "Conspiracy" Theory:** The BJP government rejected the findings of the Pegasus Project, calling them a **"conspiracy"** designed by the opposition and global organizations to derail India's progress.
2.  **Denial of Purchase:** Former IT Minister Ravi Shankar Prasad and other government officials dismissed any link between the Modi government and the NSO Group, claiming that the reports were "false stories" intended to disrupt parliamentary sessions.
3.  **National Security Justification:** In more recent court proceedings (April 2025), the government's stance shifted toward suggesting that the use of such tools might be necessary for **national security reasons** against "anti-national" elements.

## Responsibility Framework: Tripartite Relationship
To understand who is responsible for the Pegasus scandal, one must look at it as a **tripartite relationship** between a private corporation, the governments that buy the software, and the state authorities that oversee the exports.

### 1. The Developer: NSO Group (The "Arms Dealer")
The **NSO Group**, an Israeli cyber-intelligence firm, is the primary creator of the software.

#### Why they do it (The Return):
*   **Massive Financial Profit:** Pegasus is described as "very expensive". NSO Group sells the software for millions of dollars in licensing fees and ongoing maintenance contracts.
*   **Market Dominance:** By creating a "zero-click" tool that is nearly undetectable, NSO established itself as the global leader in the surveillance industry, attracting investment from private equity funds.
*   **Technological Power:** Developing such a tool allows them to stay at the cutting edge of cyber-warfare and vulnerability research.

### 2. The Client: The Using Governments (The "Operators")
These are the government agencies (such as India's Intelligence Bureau or Saudi Arabia's intelligence services) that purchase and deploy the software.

#### Why they do it (The Return):
*   **Political Survival and Control:** The primary "return" for these governments is **power**. By spying on opposition leaders (like Rahul Gandhi), journalists, and activists, they can anticipate political moves, blackmail dissidents, and stifle criticism before it gains momentum.
*   **Intelligence Advantage:** It provides a way to gather "real-time" intelligence on enemies without needing a physical wiretap or the cooperation of telecom companies.
*   **Suppression of Dissent:** It allows authoritarian or "hybrid" regimes to map out the networks of activists and human rights lawyers to dismantle their movements.

### 3. The Overseer: The Israeli Government (The "Enabler")
Because NSO Group is an Israeli company, it cannot sell Pegasus to a foreign government without a license from the **Israeli Ministry of Defense**.

#### Why they do it (The Return):
*   **Diplomatic Leverage ("Cyber-Diplomacy"):** The Israeli government has used Pegasus as a "diplomatic bargaining chip". By allowing the sale of this powerful tool to other countries, Israel can build strategic alliances and secure diplomatic favors.
*   **The Abraham Accords:** Evidence suggests that the sale of Pegasus played a critical role in securing the support of Arab nations (like the UAE and Bahrain) during the negotiation of the **Abraham Accords** in 2020, which normalized relations between Israel and several Arab states.
*   **Economic Growth:** The surveillance industry is a major part of Israel's "defense export" economy, transforming military intelligence (like Unit 8200) into a commercial goldmine.

### Summary Table: Responsibility and Incentives

| Entity | Role | Responsibility | The "Return" (What they get) |
| :--- | :--- | :--- | :--- |
| **NSO Group** | Developer | Created the weapon and sold it to governments | **Money:** Millions in profits and global market dominance |
| **Buying Governments** | User | Deployed the tool against citizens and rivals | **Power:** Political control, silencing critics, and intelligence |
| **Israeli Govt** | Regulator | Approved the export licenses for the software | **Diplomacy:** Strategic alliances and geopolitical leverage (e.g., Abraham Accords) |

### Conclusion: The "Cycle of Surveillance"
The "return" in this system is a trade-off: **NSO Group gets money → Buying Governments get political control → The Israeli Government gets diplomatic influence.** This creates a cycle where the financial success of a private company is tied to the willingness of governments to violate the human rights of their own citizens.

## Summary Table of Recent Trends (2023–2025)

| Trend | Previous Focus (2021) | Recent Focus (2024-2025) | Key Evidence/Source |
| :--- | :--- | :--- | :--- |
| **Target Demographic** | Politicians & Journalists | Corporate Executives & Civil Society | Multiple sources |
| **Primary Objective** | Political Control | Corporate Espionage & State Control | Multiple sources |
| **Technical Method** | One-click / Zero-click | Advanced Zero-click (Pegasus 2) | Multiple sources |
| **Legal Status** | Initial discovery/denial | Court-ordered bans & massive fines | Multiple sources |

In conclusion, Pegasus has not disappeared; it has simply transitioned from a tool primarily used for political repression to a more versatile weapon capable of corporate espionage and advanced, silent state surveillance.
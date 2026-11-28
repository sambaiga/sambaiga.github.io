In Part 1, we explained why most AI strategies fail, highlighting that the issue goes beyond poor planning. AI presents three challenges: it reverses the typical diagnostic process, causes guiding policies to become outdated quickly, and creates value that standard measurement tools often overlook. As a result, many strategies lack an honest diagnosis and a real guiding policy, leaving only a list of initiatives that resemble a strategy but are not one.

We also demonstrated that integrating Rumelt’s strategic kernel with a structured technology roadmap creates a framework tailored to these challenges, rather than replicating outdated approaches. However, understanding the framework is only the beginning. The real challenge lies in applying it within an organisation’s constraints. This post addresses that challenge by presenting a five-step process for building an AI roadmap around the kernel and providing practical guidance for identifying when a strategy is lacking.

This post is intended for leaders already engaged with AI, such as CDOs, strategy leads, and senior executives who have invested in AI but have yet to see clear results. If your organisation is still considering AI investment, begin with Part 1. If you have invested and are struggling to achieve results, this post will help.

### Putting the Kernel to Work: A Five-Step AI Roadmapping Process

The five-step process here is based on Phaal’s [\[1\]](#ref-Phaal2010) roadmapping framework and the author’s research with organisations using AI. These five steps form the core of a broader seven-stage process from that research. Each step answers a key strategic question from the kernel, as shown in [Figure 1](#fig-roadmap-process). These are questions that most AI strategies rarely address.

Step 01 Diagnosis

Find the Crux

Know-Why

Step 02 Diagnosis

Honest Starting Point

Know-Why

Step 03 Guiding Policy

Diagnosis into Direction

Know-What

Step 04 Coherent Actions

Coherent Actions

Know-How

Step 05 Know-When

How Well From Day One

Know-When

Figure 1: Five-step AI roadmapping process — each step maps to a kernel element and planning layer, from crux identification through to measurement.

#### Step 1: Find the Crux Before You Build the Roadmap

This is the first part of Rumelt’s Diagnosis, the core element that everything else relies on. In roadmapping, this is your Know-Why: the market need, the value gap, and the reason for your AI initiative. Without this, every next step heads in the wrong direction.

Most organisations skip this step, or think they have done it when they have not. The reason is structural: as [\[2\]](#ref-Agrawal2022) explain, AI flips the usual diagnostic process. A capability appears, and the organisation then looks for a problem to solve. Diagnosis happens after the solution is chosen, so the crux is rarely found before the budget is set. Defining the value opportunity is not about writing a vision statement. It means finding the crux [\[3\]](#ref-Rumelt2022): the single most important obstacle that, if solved, unlocks the most value for the business. It is not the most urgent or the easiest problem, but the one that matters most.

This creates a tension that needs to be addressed. If AI flips the diagnostic process and a capability appears before the problem is clear, should technology come first? Not exactly. The key is how you use that awareness. If you use it to search for a problem, that is capability searching. If you use it to refine a diagnosis you already have, that is different. The crux does not replace value analysis; it grounds it. When you know the crux, you have a way to judge what AI can really do for you: not just a list of ideas, but a clear test of whether a capability solves the most important obstacle. Without this, a list of AI opportunities is just a wishlist based on excitement, not strategy.

Rumelt illustrates this with SpaceX. Making space travel economically viable involved dozens of obstacles: propulsion, materials, regulation, funding. But Musk did not treat them as equally urgent. He stopped and asked which one, if resolved, would make everything else tractable. The answer was clear: rockets were single-use. You built an enormously expensive machine, flew it once, and it was gone. That single diagnosis, not a list of priorities, not a vision statement, became the crux around which the entire SpaceX strategy was built.

This is where most AI strategies go wrong. They start executing before finishing the diagnosis, treating data quality, talent gaps, and tooling choices as equally urgent, instead of asking which one, if solved, would change everything else. Without answering that question, there is no crux. And without the crux, the roadmap has no anchor, as [Figure 2](#fig-crux-avoidance) shows.

Without a Crux

↖ HR AI ↗ Vision ← Chatbot ↙ Analytics ↘ Gen AI

15 pilots · no clear learning

VS

With a Crux

Forecast accuracy Data quality Pipeline gaps Model drift

3 coherent experiments · measurable progress

Figure 2: Without a crux, AI initiatives scatter — many pilots, no shared obstacle. With a diagnosed crux, every experiment points at the same thing.

This requires a shift in the question you are asking. Instead of “How can we apply AI?” ask “What is the one obstacle that, if resolved, gives us a position no competitor can easily copy?” That answer is your Know-Why, the foundation of the entire roadmap [\[4\]](#ref-verdin2015you), [\[5\]](#ref-burstrom2021ai).

Organisations that skip this step do not fail because of poor execution; they fail due to a lack of direction. They may create impressive roadmaps, but these are aimed at the wrong goal. Step 1 identifies the crux—the most important obstacle. This step builds a complete picture: an honest assessment of the organisation’s actual position, grounding your Know-Why in reality rather than aspiration.

#### Step 2: Build an Honest Starting Point

An honest diagnosis may sound simple, but it is challenging. This step requires a clear assessment of your starting point: data maturity, technical infrastructure, organisational skills, and regulatory environment. Begin from your actual situation, not where you wish you were [\[6\]](#ref-Kerr2022). Overestimating data maturity is a primary cause of AI pilot failure. Organisations often assume their data is cleaner, more complete, and better governed than it is. This leads to a “Data Poverty” problem that emerges only after budgets are committed and timelines are set. The gap is rarely visible to senior leaders, who see only aggregated dashboards and summaries, not the raw pipelines, inconsistent schemas, and governance gaps that determine AI’s true potential. This overconfidence stems from structural distance, not carelessness.

Dimension What Leaders See What AI Exposes

Data Quality

Governance

Pipelines

Integration

The Maturity Gap — the distance between the executive dashboard and the actual data pipelines is where AI pilots fail

Figure 3: The data maturity gap: aggregated dashboards give leaders a high-confidence picture that the underlying infrastructure rarely supports.

This matters beyond data quality alone. The current-state assessment must treat data as a strategic dimension in its own right, not just an input to clean up, but a capability to map: what data exists, how it is governed, how it can be integrated, and what value it can generate [\[7\]](#ref-Phaal2004), [\[8\]](#ref-Komssi2013). In Helmer’s [\[9\]](#ref-Helmer2016) framework, proprietary data is a Cornered Resource: an asset competitors cannot easily buy or replicate. Honest diagnosis of data capability is therefore not an IT assessment. It is a strategic one: are you building, protecting, and governing the one asset that compounds into a durable position, or treating it as infrastructure to be cleaned up later? An AI strategy built on an incomplete picture of data capabilities will hit walls that were never mapped and forfeit the cornered-resource position it did not know it was squandering.

A precise AI-native example is Google’s deployment of a deep learning system for diabetic retinopathy screening in Thai clinics [\[10\]](#ref-Beede2020). In laboratory conditions, the model matched or exceeded specialist ophthalmologists. The organisation’s current-state assessment was built on that result. In practice, nurses in the clinics could not consistently produce images of the quality the model required. Connectivity was too slow to run the software reliably. The system had not been designed into the clinical workflow. The gap between laboratory performance and operational reality was not a technology failure. It was a diagnosis failure: the current-state assessment had been built on controlled test data, not on the actual conditions of deployment. The crux, reliable performance at the point of care, had never been honestly assessed. It surfaced only after the system was live.

This step also brings up the “How Well” question early [\[11\]](#ref-burtonshaw2008essential): does the organisation truly have the capacity to execute? Not just in theory, but in reality. If you get this wrong at step two, every step after that is based on fiction.

#### Step 3: Turn Your Diagnosis Into a Direction

With Diagnosis complete, the crux identified, and the current state honestly assessed, the kernel’s second element comes into view: the Guiding Policy. This is the bridge between where you are and where you are choosing to go [\[12\]](#ref-sjodin2020value). In roadmapping terms, it is the Know-What layer: the tangible AI offerings, platforms, and initiatives that will deliver stakeholder value, clearly defined enough to enable trade-offs.

But here is what most strategy processes miss: a guiding policy is not just a list of priorities. It is a filter. It tells you what to say yes to, and even more importantly, what to say no to [\[13\]](#ref-FRitala2013).

A guiding policy is not just one decision. It covers short-term investments, medium-term capability bets, and long-term positions on markets and partnerships. What makes it strategic is the filter it applies at each stage: does this choice move you closer to the crux, or does it distract from it? Without this test, every initiative seems equally important. With it, you have a clear way to make tough decisions and a reason to say no.

Rumelt gives the clearest example of this in Good Strategy/Bad Strategy [\[14\]](#ref-Rumelt2011) through Steve Jobs at Apple. When Jobs returned in 1997, Apple had dozens of products, computers, printers, peripherals, and servers, each with its own team and roadmap. His diagnosis: the company was spreading itself into irrelevance. His guiding policy was not a new list of priorities. It was a decision to cut everything that did not fit a single matrix: consumer or professional, desktop or portable. Four products. Everything else is gone. That choice made every subsequent decision simpler, not because it reduced complexity, but because it created a basis for saying no.

All AI Opportunities

GenAI Vision HR AI Analytics Chatbots Forecasting LLMs NLP

→

Guiding Policy Solves the crux?

→

Crux-Aligned Only Demand Forecasting AI Supply Chain Intelligence

Figure 4: The guiding policy works as a filter: many AI opportunities enter, only those that address the diagnosed crux pass through. Everything else is deferred or dropped.

Without a clear filter, the roadmap fills with what seems reasonable rather than what the strategy requires. [\[8\]](#ref-Komssi2013) highlights a common failure: teams create detailed quarterly plans but do not explain how these choices support a clear position. When the guiding policy is missing, the roadmap becomes a schedule with ambitious goals but no strategic direction. As capabilities advance faster than most planning cycles, what [\[15\]](#ref-Mollick2024) calls the “jagged frontier,” a fixed guiding policy quickly becomes outdated [\[16\]](#ref-Suleyman2023). The discipline is not only to build a filter, but to include explicit review points in the roadmap: moments to test the guiding policy against current technology capabilities. In practice, this involves scenario analysis to map how capability shifts affect the policy, sensitivity testing of key assumptions, and formal evaluation of alternative strategies as new information emerges. This approach helps avoid the Counter-Positioning trap described in Part 1 [\[9\]](#ref-Helmer2016), where incumbents cannot adopt superior new capabilities without undermining prior investments. Review points are not just good planning; they are essential for defending against unexpected shifts in the capability frontier.

#### Step 4: Take Coherent Actions, Not Scattered Pilots

A guiding policy tells you what to pursue. The next step is Coherent Actions, the third part of the kernel. In AI, many organisations discover that knowing what to pursue and knowing how to achieve it are different. This step involves intentionally designing your approach through the Know-How layer: building the skills, partnerships, and capabilities needed for the specific paths you are taking, not for every possible path. Every hire and initiative should connect back to the crux identified in Step 1 and the guiding policy from Step 3. Coherent actions focus resources on the most important obstacle. For example, if the crux is unreliable demand forecasting, the organisation should not run unrelated pilots in HR automation, customer service chatbots, or contract review. All resources should address the single obstacle that, if solved, changes the organisation’s position.

Coherent actions cluster around four domains that conventional technology roadmaps rarely name explicitly: data quality and governance, talent development, ethical and regulatory compliance, and AI lifecycle management. Each one is a class of crux-adjacent obstacles that only becomes visible once the diagnosis has been made honestly. These are not simultaneous workstreams. They are diagnostic categories: places to look for the obstacle that is quietly blocking value. Which one is your crux depends entirely on the diagnosis. Scattered pilots typically avoid finding out.

In practice, coherent actions in AI take the form of deliberate experiments, each one designed to test a specific assumption about the crux or validate a path toward the guiding policy. Two failure modes get in the way. The first is deploying a capability before the diagnosis is complete and hoping value follows. The second is waiting for perfect certainty before committing to any path. Neither is coherent. Coherent actions are question-driven: what do we need to learn, and what is the smallest experiment that answers it [\[17\]](#ref-opresnik2015value), [\[18\]](#ref-shollo2022shifting)? The roadmap adapts as the answers come in. That is not agile for its own sake. It is the only rational response to a technology whose right path is rarely visible in advance.

#### Step 5: Build in the “How Well” From the Start

The last step is often treated as an afterthought, but it should not be. This step keeps the kernel honest over time. As markets change, diagnoses can become outdated, guiding policies can lose relevance, and actions can turn into routine. The Know-When / How Well layer is there to catch this: regular reviews that check if the crux has changed, if the guiding policy still fits, and if actions are still truly coherent.

Keeping the roadmap flexible is not just an administrative job [\[7\]](#ref-Phaal2004). It is a strategic discipline. Since AI ROI usually takes two to four years to show up [\[19\]](#ref-Deloitte2025), and the landscape changes faster than most planning cycles, regular reviews are essential. This is how the kernel stays honest.

The measurement challenge in AI is structural, not operational. Most organisations reach for the metrics that are easiest to count: models deployed, pilots completed, costs saved in individual workflows. These are the wrong instruments for a technology whose value is systemic and emergent. As [\[20\]](#ref-Iansiti2020) shows, AI value accumulates through embedded workflows and improved decision-making at scale, not at the point of model deployment. Helmer’s [\[9\]](#ref-Helmer2016) concept of Process Power explains why: the value that matters is the kind competitors cannot easily replicate because it is built into proprietary ways of working, compounding decisions, and organisational capabilities that took time to build. It shows up in outcomes, not in deployment counts.

In practice, the “How Well” layer should track outcomes such as faster decisions, fewer errors, and frontline problems solved, even if these are difficult to measure or attribute to a specific model. If a metric is easy to present to the board, it likely measures activity rather than impact. Metrics that are harder to measure but indicate progress on the crux are more valuable. Build accountability from the outset, not after a failed pilot. If the crux identified in Step 1 is no longer the main obstacle, update the roadmap accordingly. Being honest at this stage is not a failure; it demonstrates that the process is working [\[6\]](#ref-Kerr2022).

Taken together, the five steps produce a recognisable pattern. GitHub Copilot is the clearest recent example of what that pattern looks like when it holds. The team identified the crux: the bottleneck in software development is not architecture or planning. It is the gap between intent and working code at the keystroke level. That diagnosis produced a filter: one product, one user, one constraint. Coherent actions pointed every resource at that single obstacle. Measurement was outcome-linked from the start: a 2023 peer-reviewed study found developers completed tasks 55.8% faster [\[21\]](#ref-Peng2023), and by 2024 GitHub reported adoption across 90% of Fortune 100 companies [\[22\]](#ref-GitHub2024). No \$4 billion platform. No scattered pilots. A diagnosed crux and a roadmap built around it.

[Table 1](#tbl-five-steps) summarises how the five steps map onto the kernel elements, the AI-specific challenge each one addresses, and the question that step is designed to force.

| Step | Kernel Element | AI-Specific Challenge | The Question to Answer |
|----|----|----|----|
| 1: Find the Crux | Diagnosis | Inverted diagnostic sequence | What is the one obstacle that, if removed, changes everything? |
| 2: Honest Starting Point | Diagnosis | Data maturity overconfidence | Where do we actually stand? |
| 3: Diagnosis into Direction | Guiding Policy | Policy decay and the jagged frontier | What do we say no to, and when do we revisit that decision? |
| 4: Coherent Actions | Coherent Actions | Scattered pilots without learning | What specific question does each experiment answer? |
| 5: How Well From Day One | Know-When / How Well | Emergent, indirect value | Are we tracking outcomes or counting activity? |

Table 1: The Five-Step AI Roadmapping Framework: Kernel Elements, AI-Specific Challenges, and the Questions Each Step Forces

[Figure 5](#fig-ai-roadmap) illustrates what the output looks like when all five steps are completed: a layered roadmap with AI and data components aligned across market needs, product direction, and technology capability, anchored by a diagnosed crux and structured around the kernel’s three elements.

Now

6–12 Months

1–3 Years

Know-Why Market

Identify market gap

What crux blocks value?

Map value opportunity

Validate crux with stakeholders

Cornered resource position

Durable competitive advantage

Know-What Product / AI

AI prototype

Smallest testable product

Pilots targeting the crux

Question-driven experiments

AI platform scaled

Embedded in core workflows

Know-How Technology

Data governance audit

Honest current-state picture

ML team + partnerships

Capabilities for the chosen path

End-to-end ML pipeline

Production-grade infrastructure

Crux Anchor — every layer and time horizon points back to the single most important obstacle

Figure 5: AI strategy roadmap with three planning layers (Know-Why, Know-What, Know-How) across three time horizons, anchored to a single diagnosed crux.

The five steps also serve as a diagnostic instrument. Run them against any AI strategy and the gaps become visible. Run them against IBM Watson Health, and the picture is unambiguous.

### The Kernel in Practice: What IBM Watson Health Got Wrong

Between 2015 and 2022, IBM invested over \$4 billion in building Watson Health into what it called the future of AI-driven medicine [\[23\]](#ref-Strickland2022). It never made a profit. In January 2022, IBM sold the assets to a private equity firm for approximately \$1 billion. The most telling detail: its flagship partnership with MD Anderson Cancer Centre ran for five years, cost \$62 million, and was terminated before Watson was ever used on a real patient [\[24\]](#ref-Mukherjee2017), [\[25\]](#ref-Ross2017).

This was not primarily a technology failure. It was a strategy failure, and it maps precisely onto all three structural AI properties identified in Part 1.

The diagnosis was inverted from the start. IBM did not begin with a diagnosed crux in oncology. It began with Watson, a natural language processing system that had won Jeopardy! in 2011, and went looking for the most ambitious problem it could apply it to. Healthcare was chosen for its scale and prestige, not because IBM had identified a specific obstacle that Watson uniquely solved. As [\[2\]](#ref-Agrawal2022) argue, this is the structural failure mode that AI invites: a capability becomes visible, and the organisation goes looking for a problem it might solve. At IBM, diagnosis happened after the solution was chosen, which meant the crux, the specific, solvable obstacle that would have unlocked genuine clinical value, was never found. IBM did not build a strategy around a problem. It built a marketing campaign around a capability [\[26\]](#ref-Davenport2019).

The guiding policy had no filter and no review mechanism. With no real crux to anchor it, IBM’s guiding policy expanded rather than narrowed. Watson was applied to oncology, radiology, genomics, and clinical trial recruitment simultaneously. Every initiative looked equally important because nothing had been ruled out. When the LLM era arrived and the underlying capability frontier shifted, there was no mechanism to review whether Watson’s architecture still served its original intent. A guiding policy built to be revised would have recognised the structural shift early. IBM’s was not. It was tied to an approach that was becoming obsolete faster than the roadmap could keep up with [\[25\]](#ref-Ross2017).

The value was measured at the wrong layer. IBM cited Watson’s agreement rate with oncologists’ treatment recommendations as evidence of progress, at one point claiming over 90% concordance in lung cancer cases. But agreement on training data is not a clinical outcome [\[24\]](#ref-Mukherjee2017). No survival rates. No improvements in treatment accuracy at the point of care. No measurable reduction in diagnostic error. IBM was counting the wrong thing entirely, exactly the failure mode that Helmer’s [\[9\]](#ref-Helmer2016) concept of Process Power illuminates: the value that matters accumulates in embedded clinical workflows and improved decisions, not in model agreement metrics. As [\[20\]](#ref-Iansiti2020) shows, the value of AI is systemic and indirect. IBM’s measurement layer was designed for activity, not for the outcomes the organisation had originally promised.

Each of the five steps exposes a specific point of failure. Step 1 was skipped: no crux was identified before the budget was committed. Step 2 was inflated: IBM overestimated the maturity of clinical data, which turned out to be unstructured, full of shorthand and abbreviations, and deeply inconsistent across hospital systems [\[25\]](#ref-Ross2017). Step 3 produced no real filter: without a guiding policy grounded in a specific crux, Watson was pointed at too many problems simultaneously. Step 4 scattered pilots globally before any single experiment had answered a specific question about the crux. Step 5 tracked activity instead of outcomes. When value failed to materialise, there was no honest measurement layer to indicate as much.

The \$4 billion question was never “was Watson capable?” It was “Was there a real crux at the centre of the strategy?” There was not. And without it, the roadmap had no anchor, exactly as the framework predicts.

### How to Spot a Bad AI Strategy

Most AI strategies fail for the same reasons. Here are the five that are particular to this technology [\[3\]](#ref-Rumelt2022), [\[14\]](#ref-Rumelt2011).

Technology-led diagnosis. The roadmap starts from a capability and works backwards to find a problem. A language model is available, so the organisation goes looking for something it might solve. This is the structural failure mode that Part 1 identified: AI inverts the diagnostic sequence, and organisations that do not actively resist it will build strategies anchored to a capability rather than a crux. IBM Watson Health is the most expensive known example, but the pattern is far more common than the price tag. If the answer to “why are we using AI for this?” is “because we have the platform,” the diagnosis was never completed.

The platform fallacy. The organisation builds a data infrastructure, a governance layer, and a capability framework before identifying the crux. The logic is sound in isolation: you need clean data before AI can work. But a data platform is not a strategy. It is a prerequisite, and a prerequisite without a destination is just cost. Amazon spent over \$25 billion building Alexa into a world-class voice AI platform, assuming users would transact by voice. Instead, users used it almost entirely for free tasks: timers, weather, music. By 2022, the division was estimated to be losing \$10 billion annually [\[27\]](#ref-AmazonAlexa2022). In 2023, Amazon restructured and laid off hundreds of engineers, acknowledging the platform had no coherent path to monetisation. The question that was never seriously asked: what specific, diagnosed obstacle would voice AI uniquely resolve? Organisations that invest eighteen months in data infrastructure before running a single experiment are making the same error at a smaller scale.

Pilot proliferation without learning. Fifteen pilots running simultaneously, none designed to answer a specific question about the crux. Each one is too small to fail visibly and too scattered to compound. The organisation reports progress by counting pilots. MIT Sloan research found that 95% of enterprise generative AI pilots fail to deliver measurable business impact, and S&P Global data shows 42% of companies have abandoned most of their AI initiatives [\[28\]](#ref-MIT2025), [\[29\]](#ref-MLQ2025). The consistent finding is not that AI does not work. It is that pilots without a hypothesis do not produce learning. A pilot that does not test a specific assumption about a specific obstacle is a demonstration project. When none of them produces measurable value, the conclusion drawn is usually that AI is not ready, rather than that the experiments were never coherent.

Measuring the wrong layer. Model accuracy, agreement rates with human experts, and deployment counts are metrics of the technology layer, not the strategy layer. As the Watson case showed, 90% concordance with oncologists is not clinically valuable. If the measurement layer cannot answer whether the crux has been resolved, it is not a strategic instrument. It is a reporting mechanism that can declare success independently of whether anything has actually changed.

The fixed roadmap in a moving landscape. A three-year AI roadmap with no designated review points for the capability frontier is not a planning failure. It is a design failure [\[30\]](#ref-o2021agile). Google’s Bard launch in February 2023 is the clearest illustration. Google’s guiding assumption was that its search infrastructure gave it a durable moat against conversational AI. When ChatGPT went viral, Google rushed Bard to market, bypassing its own safety protocols. In the first public demo, Bard stated that the James Webb Space Telescope had taken the first images of an exoplanet. That was factually wrong. Alphabet lost \$100 billion in market cap in a single day [\[31\]](#ref-GoogleBard2023). The underlying failure was not the hallucination. It was that Google’s guiding policy was calibrated to a search-era threat model and lacked a mechanism to evaluate the different failure modes of generative AI. Bard was deprecated entirely and replaced by Gemini in 2024. The discipline is not just to build the filter. It is to schedule the moment when the filter is examined, before the frontier passes it.

These five failure modes are connected and build on each other. Starting with a technology-led diagnosis leads to a platform with no clear goal. That platform results in scattered pilots that do not produce learning. These pilots are measured at the wrong level, which delays honest evaluation. Since the guiding policy was not designed to be updated, the organisation reaches a new capability frontier with a strategy it cannot change. The kernel is missing at every stage, and each missing step makes the next one harder to fix.

### Conclusion

The gap between the 80% of organisations running AI pilots and the 5% getting real value is not about technology. It is about the missing kernel. There is no honest diagnosis, no guiding policy that acts as a filter, and no coherent actions that build toward a clear result. Instead, there is just a list of initiatives that look like strategy, measured by activity rather than real progress.

The organisations that closed this gap did not do it with better technology. GitHub Copilot did not succeed because of better models, and Klarna’s AI assistant did not win because of more advanced infrastructure. They succeeded because they identified a specific crux, built a guiding policy around it, and measured outcomes instead of just activity [\[21\]](#ref-Peng2023), [\[32\]](#ref-Klarna2024). The technology was good enough. The strategy was clear. That combination is still rare.

If there is one thing that would improve most AI strategies, it is not launching another pilot. It is holding a real diagnostic workshop with the people who understand the true obstacles. One room. One question: what is the single challenge that, if solved, changes everything for this organisation? That answer is the crux. The roadmap begins there. Everything else is execution.

## References

\[1\]

R. Phaal, C. J. P. Farrukh, and D. R. Probert, *Roadmapping for strategy and innovation: Aligning technology and markets in a dynamic world*. Cambridge, UK: University of Cambridge, Institute for Manufacturing, 2010.

\[2\]

A. Agrawal, J. Gans, and A. Goldfarb, *Power and prediction: The disruptive economics of artificial intelligence*. Boston, MA: Harvard Business Review Press, 2022.

\[3\]

R. P. Rumelt, *The crux: High-stakes problems and the art of strategy*. New York, NY: PublicAffairs, 2022.

\[4\]

P. Verdin and K. Tackx, “Are you creating or capturing value? A dynamic framework for sustainable strategy,” *SOLVAY Brussels School of Economics and Management Research Paper*, 2015.

\[5\]

T. Burstrom, V. Parida, T. Lahti, and J. Wincent, “AI-enabled business-model innovation and transformation in industrial ecosystems: A framework, model and outline for further research,” *Journal of Business Research*, vol. 128, pp. 586–595, 2021, doi: [10.1016/j.jbusres.2020.10.016](https://doi.org/10.1016/j.jbusres.2020.10.016).

\[6\]

C. Kerr and R. Phaal, “Roadmapping and roadmaps: Definition and underpinning concepts,” *IEEE Transactions on Engineering Management*, vol. 69, no. 1, pp. 6–16, 2022, doi: [10.1109/TEM.2021.3096012](https://doi.org/10.1109/TEM.2021.3096012).

\[7\]

R. Phaal, C. J. P. Farrukh, and D. Probert, “Technology roadmapping – A planning framework for evolution and revolution,” *Technological Forecasting and Social Change*, vol. 71, pp. 5–26, 2004, doi: [10.1016/S0040-1625(03)00072-6](https://doi.org/10.1016/S0040-1625(03)00072-6).

\[8\]

M. Komssi, J. Kauppinen, H. Lakkala, and C. Lassenius, “Roadmapping problems in practice: Value creation and challenges,” *Journal of Software: Evolution and Process*, vol. 26, no. 4, pp. 1899–1916, 2013, doi: [10.1002/smr.1628](https://doi.org/10.1002/smr.1628).

\[9\]

H. Helmer, *7 powers: The foundations of business strategy*. Deep Strategy LLC, 2016.

\[10\]

E. Beede *et al.*, “A human-centered evaluation of a deep learning system deployed in clinics for the detection of diabetic retinopathy,” in *Proceedings of the 2020 CHI conference on human factors in computing systems*, 2020. doi: [10.1145/3313831.3376718](https://doi.org/10.1145/3313831.3376718).

\[11\]

S. A. Burtonshaw-Gunn, *The essential management toolbox: Tools, models and notes for managers and consultants*. Chichester, UK: John Wiley & Sons, 2008.

\[12\]

D. Sjodin, V. Parida, M. Leksell, and A. Petrovic, “Smart factory implementation and process innovation: A framework for capturing value from digitalization in manufacturing,” *Research-Technology Management*, vol. 61, no. 5, pp. 22–31, 2020, doi: [10.1080/08956308.2018.1471277](https://doi.org/10.1080/08956308.2018.1471277).

\[13\]

P. Ritala, A. Pohle, and P. Hurmelinna-Laukkanen, “Intangible assets boost value capture ability in ecosystems: A systemic perspective,” *Journal of Intellectual Capital*, vol. 14, no. 4, pp. 549–569, 2013, doi: [10.1108/JIC-05-2013-0051](https://doi.org/10.1108/JIC-05-2013-0051).

\[14\]

R. P. Rumelt, *Good strategy/bad strategy: The difference and why it matters*. New York, NY: Crown Business, 2011.

\[15\]

E. Mollick, *Co-intelligence: Living and working with AI*. New York, NY: Portfolio/Penguin, 2024.

\[16\]

M. Suleyman and M. Bhaskar, *The coming wave: Technology, power, and the twenty-first century’s greatest dilemma*. New York, NY: Crown, 2023.

\[17\]

D. Opresnik and M. Taisch, “The value of Big Data in servitization,” *International Journal of Production Economics*, vol. 165, pp. 174–184, 2015, doi: [10.1016/j.ijpe.2014.12.036](https://doi.org/10.1016/j.ijpe.2014.12.036).

\[18\]

A. Shollo, A. Karpovsky, and R. D. Galliers, “How does (big) data change organizations?” *Journal of Organizational Change Management*, vol. 35, no. 1, pp. 171–191, 2022, doi: [10.1108/JOCM-07-2020-0201](https://doi.org/10.1108/JOCM-07-2020-0201).

\[19\]

Deloitte Consulting, “AI ROI: The paradox of rising investment and elusive returns,” *Deloitte Articles*, 2025, Available: <https://www.deloitte.com/ie/en/issues/generative-ai/ai-roi-the-paradox-of-rising-investment-and-elusive-returns.html>

\[20\]

M. Iansiti and K. R. Lakhani, *Competing in the age of AI: Strategy and leadership when algorithms and networks run the world*. Boston, MA: Harvard Business Review Press, 2020.

\[21\]

S. Peng, E. Kalliamvakou, P. Cihon, and M. Demirer, “The impact of AI on developer productivity: Evidence from GitHub Copilot,” *arXiv preprint arXiv:2302.06590*, 2023, Available: <https://arxiv.org/abs/2302.06590>

\[22\]

GitHub, “GitHub Copilot is now available to all companies on GitHub Enterprise.” \[Online\]. Available: <https://github.blog/news-insights/product-news/github-copilot-is-now-available-to-all-companies-on-github-enterprise/>

\[23\]

E. Strickland, “How IBM’s Watson went from the future of health care to sold off for parts,” *Slate*, 2022, Available: <https://slate.com/technology/2022/01/ibm-watson-health-failure-artificial-intelligence.html>

\[24\]

S. Mukherjee, “M. D. Anderson breaks with IBM Watson, raising questions about artificial intelligence in oncology,” *Journal of the National Cancer Institute*, vol. 109, no. 5, 2017, doi: [10.1093/jnci/djx113](https://doi.org/10.1093/jnci/djx113).

\[25\]

C. Ross and I. Swetlitz, “IBM pitched its Watson supercomputer as a revolution in cancer care. It’s nowhere close,” *STAT News*, 2017, Available: <https://www.statnews.com/2017/09/05/watson-ibm-cancer/>

\[26\]

T. Davenport and R. Kalakota, “The potential for artificial intelligence in healthcare,” *Future Healthcare Journal*, vol. 6, no. 2, pp. 94–98, 2019, doi: [10.7861/futurehosp.6-2-94](https://doi.org/10.7861/futurehosp.6-2-94).

\[27\]

E. Kim and A. Palmer, “Amazon’s Alexa is on track to lose \$10 billion this year.” \[Online\]. Available: <https://www.businessinsider.com/amazon-alexa-losing-10-billion-year-2022-11>

\[28\]

MIT Sloan Management Review, “The state of AI in the enterprise: Why GenAI pilots fail to scale,” MIT Sloan Management Review, 2025. Available: <https://sloanreview.mit.edu/>

\[29\]

MLQ.ai, “State of AI in business 2025 report: Bridging the GenAI divide,” MLQ.ai, 2025. Available: <https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf>

\[30\]

E. O’Sullivan, R. Phaal, and Ch. Featherston, “Agile roadmapping: An adaptive approach to technology foresight,” *Foresight and STI Governance*, vol. 15, no. 2, pp. 65–81, 2021, doi: [10.17323/25002597.2021.2.65.81](https://doi.org/10.17323/25002597.2021.2.65.81).

\[31\]

B. Allyn, “Google’s AI chatbot, Bard, sparks a \$100 billion loss in Alphabet shares.” \[Online\]. Available: <https://www.npr.org/2023/02/09/1155650909/google-chatbot--error-bard-shares>

\[32\]

Klarna, “Klarna AI assistant handles two-thirds of customer service chats in its first month.” \[Online\]. Available: <https://www.klarna.com/international/press/klarna-ai-assistant-handles-two-thirds-of-customer-service-chats-in-its-first-month/>

## Citation

BibTeX citation:

``` quarto-appendix-bibtex
@online{faustine2026,
  author = {Faustine, Anthony},
  title = {From {Framework} to {Practice:} {A} {Five-Step} {AI}
    {Roadmapping} {Process}},
  date = {2026-03-29},
  url = {https://sambaiga.github.io/pages/blog/posts/2026/04/},
  langid = {en}
}
```

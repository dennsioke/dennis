"""
generate_dataset.py - Generates synthetic news articles with reference summaries.
Output: dataset/news_articles.csv
"""

import csv
import os
import random
from datetime import date, timedelta

random.seed(42)

TOPIC_TEMPLATES = {
    "politics": {
        "headlines": [
            "Congress Passes {bill} Act Amid {adj} Debate",
            "President Signs {topic} Reform Legislation",
            "Senate Committee Approves {topic} Budget Plan",
            "{party} Party Announces {adj} Policy on {topic}",
            "Election Results Show {adj} Shift in {region} Voters",
        ],
        "articles": [
            "The {body} passed the {bill} Act on {day} after months of {adj} negotiations. Supporters argue the legislation will {benefit}, while critics contend it may {risk}. The bill, which garnered {n} votes in favor and {n2} against, now moves to the {chamber} for final consideration. Analysts say the outcome will have significant implications for {topic} policy heading into the upcoming electoral cycle. Several key amendments were added during floor debate, including provisions for {detail}. The {party} leadership praised the result as a historic step, while opposition members vowed to challenge the legislation in committee. Stakeholders from the {sector} sector have been closely monitoring the proceedings, with trade groups issuing statements both supporting and opposing specific clauses. The timeline for implementation remains unclear pending regulatory guidance.",
        ],
        "summaries": [
            "The {body} passed the {bill} Act with {n} votes, advancing {topic} reform after {adj} debate.",
            "Lawmakers approved the {bill} Act, sending it to the {chamber} with provisions for {detail}.",
        ],
        "vars": {"bill": ["Infrastructure", "Healthcare", "Education Funding", "Climate", "Defense"],
                 "adj": ["contentious", "bipartisan", "heated", "lengthy", "landmark"],
                 "topic": ["healthcare", "immigration", "climate", "trade", "taxation"],
                 "party": ["Democratic", "Republican", "Progressive", "Conservative"],
                 "region": ["suburban", "rural", "urban", "swing-state"],
                 "body": ["Congress", "The Senate", "The House", "The legislature"],
                 "chamber": ["Senate", "House", "President", "committee"],
                 "benefit": ["reduce costs", "expand access", "create jobs", "improve safety"],
                 "risk": ["increase debt", "limit freedoms", "harm small businesses", "raise taxes"],
                 "detail": ["tax credits", "funding allocations", "oversight provisions"],
                 "sector": ["energy", "healthcare", "finance", "agriculture"],
                 "day": ["Tuesday", "Wednesday", "Thursday", "Friday"],
                 "n": list(range(50, 80)), "n2": list(range(30, 55))},
    },
    "technology": {
        "headlines": [
            "{company} Unveils {adj} {product} at Annual Conference",
            "New {tech} Model Achieves {adj} Performance on Benchmarks",
            "{company} Acquires {startup} for ${amount} Billion",
            "Researchers Develop {adj} {tech} for {application}",
            "{company} Faces Regulatory Scrutiny Over {issue}",
        ],
        "articles": [
            "{company} announced its latest {product} on {day}, claiming it delivers {adj} performance improvements over previous generations. The new system leverages {tech} architecture to achieve {metric} on standard benchmarks, outperforming rivals by approximately {n}%. Chief technology officer {name} stated the development took {n2} months of intensive research. The product targets both enterprise customers and individual developers, with pricing starting at ${price} per month for the cloud tier. Industry analysts from {firm} rated the announcement positively, noting strong demand for {application} solutions. However, concerns were raised about energy consumption and the availability of training data. The company also revealed a partnership with {partner} to expand deployment in the {sector} sector. Beta access opens next quarter with general availability planned for {season}.",
        ],
        "summaries": [
            "{company} launched its {product} featuring {tech} architecture with {n}% performance gains over previous versions.",
            "The new {product} from {company} targets {application} workloads with {adj} efficiency improvements, priced from ${price}/month.",
        ],
        "vars": {"company": ["OpenAI", "Google", "Microsoft", "Nvidia", "Apple", "Meta", "Amazon"],
                 "product": ["AI model", "chip architecture", "developer platform", "cloud service", "language model"],
                 "tech": ["transformer", "diffusion-based", "multimodal", "edge AI", "quantum-enhanced"],
                 "adj": ["groundbreaking", "efficient", "scalable", "cost-effective", "next-generation"],
                 "application": ["image generation", "code completion", "natural language processing", "robotics"],
                 "startup": ["DeepMind spinoff", "AI safety firm", "data infrastructure company"],
                 "issue": ["data privacy", "antitrust concerns", "content moderation", "algorithmic bias"],
                 "name": ["Dr. Sarah Chen", "James Park", "Maria Lopez", "Alex Kumar"],
                 "firm": ["Gartner", "IDC", "Forrester", "Bernstein"],
                 "partner": ["AWS", "Azure", "Oracle", "SAP"],
                 "sector": ["healthcare", "finance", "education", "logistics"],
                 "season": ["spring", "summer", "fall", "Q4"],
                 "metric": ["state-of-the-art results", "near-human accuracy", "record throughput"],
                 "day": ["Monday", "Tuesday", "Wednesday"],
                 "amount": ["1.2", "3.5", "8.0", "12.0", "25.0"],
                 "price": ["49", "99", "199", "499"],
                 "n": list(range(15, 60)), "n2": list(range(12, 36))},
    },
    "sports": {
        "headlines": [
            "{team} Defeats {team2} {score} in {adj} {event}",
            "{player} Sets {adj} Record in {sport} Championship",
            "{team} Signs {player} in ${amount}M Deal",
            "{sport} Season Kicks Off with {adj} Performances",
            "{team} Coach {name} Reacts to {adj} Win",
        ],
        "articles": [
            "The {team} secured a {adj} victory over {team2} with a final score of {score} on {day} night at {venue}. Star player {player} led the performance with {stat1} and {stat2}, earning praise from head coach {name}. The game was decided in the {period} after a pivotal moment involving {event2}. Analysts credited the team's {strategy} as the key differentiator. {team2} struggled with {weakness} throughout the contest, with head coach {name2} acknowledging the gap in the post-game presser. The win moves {team} to {record} on the season, {position} in the {conference}. Next up, {team} faces {team3} on {day2} in an anticipated rematch. Ticket sales for the upcoming fixture surpassed expectations within hours of the announcement.",
        ],
        "summaries": [
            "{team} beat {team2} {score} with {player} contributing {stat1} in a {adj} performance.",
            "{player}'s {stat1} powered {team} past {team2}, improving their record to {record} in the {conference}.",
        ],
        "vars": {"team": ["Lakers", "Yankees", "Warriors", "Chiefs", "Manchester City", "Real Madrid"],
                 "team2": ["Celtics", "Red Sox", "Suns", "Eagles", "Arsenal", "Barcelona"],
                 "team3": ["Bulls", "Mets", "Clippers", "49ers", "Chelsea", "Atletico"],
                 "player": ["Marcus Johnson", "Tyler Williams", "Sophia Davis", "Carlos Reyes"],
                 "sport": ["basketball", "baseball", "football", "soccer", "tennis"],
                 "event": ["playoff game", "championship match", "rivalry clash", "finals contest"],
                 "score": ["112-98", "4-1", "7-3", "2-0", "31-17", "3-2"],
                 "adj": ["stunning", "decisive", "dominant", "thrilling", "hard-fought"],
                 "name": ["Coach Rivera", "Coach Thompson", "Coach Okafor"],
                 "name2": ["Coach Miller", "Coach Jackson", "Coach Lee"],
                 "venue": ["the arena", "home stadium", "Madison Square Garden", "the field"],
                 "period": ["fourth quarter", "second half", "final inning", "overtime"],
                 "event2": ["a crucial turnover", "an injury timeout", "a penalty kick", "a home run"],
                 "strategy": ["defensive scheme", "offensive line play", "pressing game", "transition offense"],
                 "weakness": ["turnovers", "defensive lapses", "missed set pieces", "poor shooting"],
                 "stat1": ["28 points", "2 goals", "a hat trick", "14 assists", "3 home runs"],
                 "stat2": ["10 rebounds", "6 tackles", "2 assists", "5 saves"],
                 "record": ["18-7", "22-12", "35-20", "14-5"],
                 "conference": ["Eastern Conference", "Western Division", "Premier League", "AFC"],
                 "position": ["first", "second", "third"],
                 "day": ["Saturday", "Sunday", "Monday"],
                 "day2": ["Thursday", "Friday", "Saturday"],
                 "amount": ["45", "120", "85", "200"]},
    },
    "health": {
        "headlines": [
            "Study Finds {adj} Link Between {factor} and {outcome}",
            "New {drug} Treatment Shows {adj} Results for {disease}",
            "WHO Reports {adj} Decline in {disease} Cases Globally",
            "Researchers Develop {adj} Vaccine Candidate for {disease}",
            "Health Experts Warn of {adj} Rise in {condition} Among {group}",
        ],
        "articles": [
            "A new study published in the {journal} found a {adj} correlation between {factor} and {outcome} in a cohort of {n} participants studied over {n2} years. The research, led by Dr. {name} at {institution}, suggests that individuals with {condition} are {n3}% more likely to experience {outcome}. The findings build on prior work indicating that {lifestyle} can significantly affect {metric}. However, the authors cautioned that the study relies on observational data and does not establish causation. Critics from the {organization} questioned the methodology, particularly the reliance on {method}. The research team plans a follow-up randomized controlled trial starting next year with {n4} participants across {n5} sites. Public health officials have taken note of the findings, with the {agency} issuing updated guidelines recommending {recommendation}. Reactions from patient advocacy groups were mixed.",
        ],
        "summaries": [
            "A study of {n} participants found {factor} linked to {n3}% higher risk of {outcome}, though causation was not established.",
            "Researchers at {institution} identified a {adj} association between {factor} and {outcome} over {n2} years of observation.",
        ],
        "vars": {"factor": ["diet quality", "sleep duration", "physical activity", "air pollution", "stress levels"],
                 "outcome": ["cardiovascular disease", "cognitive decline", "Type 2 diabetes", "depression", "longevity"],
                 "disease": ["cancer", "Alzheimer's", "influenza", "COVID-19", "tuberculosis"],
                 "drug": ["mRNA-based", "monoclonal antibody", "small molecule", "gene therapy"],
                 "condition": ["hypertension", "obesity", "chronic stress", "sleep apnea"],
                 "group": ["adolescents", "adults over 50", "women in their 40s", "working professionals"],
                 "adj": ["significant", "surprising", "alarming", "promising", "concerning"],
                 "journal": ["The Lancet", "NEJM", "JAMA", "Nature Medicine"],
                 "name": ["Dr. Emily Carter", "Dr. Raj Singh", "Dr. Amara Osei"],
                 "institution": ["Johns Hopkins", "Harvard Medical School", "Stanford Medicine", "Mayo Clinic"],
                 "lifestyle": ["regular exercise", "plant-based diet", "stress management", "adequate sleep"],
                 "metric": ["inflammation markers", "cardiovascular health", "cognitive performance"],
                 "organization": ["AMA", "WHO", "CDC", "NIH"],
                 "method": ["self-reported data", "retrospective analysis", "short follow-up periods"],
                 "agency": ["CDC", "WHO", "NHS", "FDA"],
                 "recommendation": ["increased screening", "lifestyle modifications", "annual checkups"],
                 "n": list(range(2000, 50000, 1000)),
                 "n2": list(range(3, 15)), "n3": list(range(15, 70)),
                 "n4": list(range(500, 3000, 100)), "n5": list(range(5, 25))},
    },
    "finance": {
        "headlines": [
            "{company} Reports {adj} Q{q} Earnings, {trend} Expectations",
            "Federal Reserve {action} Interest Rates by {n} Basis Points",
            "{index} Closes at {adj} High Amid {factor}",
            "{company} Announces ${amount}B {action2} Plan",
            "Inflation Data Shows {adj} {trend2} in {month}",
        ],
        "articles": [
            "{company} reported {adj} earnings for Q{q}, with revenue of ${revenue}B and net income of ${income}B, {trend} analyst consensus by {n}%. CEO {name} attributed the performance to {driver}, noting strong demand in the {segment} segment. The results triggered a {pct}% {move} in after-hours trading. Operating margins came in at {margin}%, compared to {margin2}% in the prior year period. The company issued guidance for the next quarter projecting revenue between ${lo}B and ${hi}B, slightly {dir} market expectations. Analysts from {firm} upgraded the stock following the report, citing {reason}. However, concerns remain about {risk} which could weigh on future performance. The {sector} sector broadly reacted {adv} to the results, with several peer companies also seeing share price movements.",
        ],
        "summaries": [
            "{company} beat Q{q} estimates by {n}% with ${revenue}B in revenue, driven by {driver} strength.",
            "{company}'s Q{q} earnings surpassed expectations on revenues of ${revenue}B, sending shares {move} {pct}% after hours.",
        ],
        "vars": {"company": ["Apple", "Microsoft", "Tesla", "Amazon", "JPMorgan", "Goldman Sachs", "Meta"],
                 "q": ["1", "2", "3", "4"],
                 "adj": ["strong", "mixed", "record", "disappointing", "solid"],
                 "trend": ["beating", "missing", "meeting", "exceeding"],
                 "trend2": ["slowdown", "acceleration", "moderation", "uptick"],
                 "action": ["raises", "cuts", "holds"],
                 "action2": ["buyback", "investment", "acquisition", "restructuring"],
                 "index": ["S&P 500", "Nasdaq", "Dow Jones", "Russell 2000"],
                 "factor": ["earnings optimism", "Fed signals", "strong jobs data", "tech rally"],
                 "month": ["January", "March", "June", "September"],
                 "name": ["Tim Cook", "Satya Nadella", "Elon Musk", "Andy Jassy"],
                 "driver": ["cloud growth", "consumer demand", "AI adoption", "international expansion"],
                 "segment": ["enterprise", "consumer", "cloud", "advertising"],
                 "reason": ["margin expansion", "strong guidance", "market share gains"],
                 "risk": ["macroeconomic headwinds", "regulatory uncertainty", "rising costs"],
                 "firm": ["Goldman Sachs", "Morgan Stanley", "Deutsche Bank", "BofA"],
                 "sector": ["technology", "financial", "consumer", "healthcare"],
                 "adv": ["positively", "negatively", "cautiously"],
                 "dir": ["above", "below", "in line with"],
                 "move": ["rise", "fall", "jump", "drop"],
                 "n": list(range(2, 20)), "pct": list(range(1, 12)),
                 "revenue": [f"{x/10:.1f}" for x in range(10, 200, 5)],
                 "income": [f"{x/10:.1f}" for x in range(5, 80, 5)],
                 "margin": list(range(15, 45)), "margin2": list(range(12, 42)),
                 "lo": [f"{x/10:.1f}" for x in range(8, 100, 3)],
                 "hi": [f"{x/10:.1f}" for x in range(12, 120, 3)],
                 "amount": list(range(2, 50))},
    },
}


def pick(vals):
    if isinstance(vals, list):
        return random.choice(vals)
    return vals


def fill_template(template, vars_dict):
    result = template
    for key, options in vars_dict.items():
        holder = "{" + key + "}"
        if holder in result:
            result = result.replace(holder, str(pick(options)))
    return result


def generate():
    os.makedirs("dataset", exist_ok=True)
    rows = []
    article_id = 1
    base_date = date(2023, 1, 1)

    COUNTS = {"politics": 3500, "technology": 3000, "sports": 2500, "health": 3000, "finance": 3000}

    for topic, count in COUNTS.items():
        tmpl = TOPIC_TEMPLATES[topic]
        for _ in range(count):
            headline = fill_template(random.choice(tmpl["headlines"]), tmpl["vars"])
            article = fill_template(random.choice(tmpl["articles"]), tmpl["vars"])
            summary = fill_template(random.choice(tmpl["summaries"]), tmpl["vars"])
            pub_date = base_date + timedelta(days=random.randint(0, 365))
            aws = len(article.split())
            sws = len(summary.split())
            rows.append({
                "article_id": article_id,
                "topic": topic,
                "headline": headline,
                "article_text": article,
                "summary": summary,
                "article_word_count": aws,
                "summary_word_count": sws,
                "compression_ratio": round(sws / max(aws, 1), 4),
                "publish_date": pub_date.isoformat(),
            })
            article_id += 1

    random.shuffle(rows)
    fields = ["article_id", "topic", "headline", "article_text", "summary",
              "article_word_count", "summary_word_count", "compression_ratio", "publish_date"]

    with open("dataset/news_articles.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)

    print(f"Generated {len(rows)} articles -> dataset/news_articles.csv")


if __name__ == "__main__":
    generate()

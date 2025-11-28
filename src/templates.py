from string import Template

SUBJECT_TPL = Template("Interested in Contributing to ${company}’s Tech Team")

BODY_TPL = Template("""Hi ${name},

I hope you’re doing well.

I’m reaching out to explore potential Entry-Level / Internship opportunities at ${company}, particularly in Full Stack Development, Software Development, or Data/Backend Engineering. I am flexible across roles within software development and always eager to learn and contribute.

My technical experience includes:
• Python, FastAPI, SQL
• HTML, CSS, JavaScript, React.js
• Building and deploying real-world applications
• Currently developing a SaaS product for liquor retailers to simplify inventory & billing workflows

I enjoy solving practical problems with clean, maintainable code and I’m highly motivated to work in a professional environment where I can contribute meaningfully while continuing to grow.

I would appreciate the opportunity to interview or have a brief discussion to understand how I could add value to your team.

Please find my resume attached for your consideration.

Thank you for your time — I genuinely appreciate it.

Warm regards,
Tanmay Jain
tnmy4903@gmail.com
8858314903
linkedin.com/in/tnmy4903/
""")

def render_subject(name: str, company: str) -> str:
    return SUBJECT_TPL.substitute(company=company.strip())

def render_body(name: str, company: str) -> str:
    return BODY_TPL.substitute(name=name.strip(), company=company.strip())

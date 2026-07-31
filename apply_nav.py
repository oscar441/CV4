from pathlib import Path
import re

root = Path(r'c:\Sites\CV4')

styles = '''* {
    box-sizing: border-box;
}

html {
    scroll-behavior: smooth;
}

body {
    margin: 0;
    font-family: 'Segoe UI', Arial, sans-serif;
    background: #f4f7fb;
    color: #243447;
    line-height: 1.55;
}

body, p, li, td, th {
    font-size: 0.96rem;
}

h1, h2, h3 {
    margin: 0 0 0.6rem;
    line-height: 1.25;
    font-weight: 600;
}

h1 {
    font-size: 1.7rem;
    color: #0f172a;
}

h2 {
    font-size: 1.2rem;
    color: #0f172a;
}

h3 {
    font-size: 1.02rem;
    color: #0f172a;
}

p {
    margin: 0 0 0.75rem;
    color: #475569;
}

a {
    color: #2563eb;
    text-decoration: none;
}

a:hover {
    text-decoration: underline;
}

.site-header {
    background: #ffffff;
    border-bottom: 1px solid #e2e8f0;
    position: sticky;
    top: 0;
    z-index: 1000;
}

.site-nav {
    max-width: 1100px;
    margin: 0 auto;
    padding: 0.7rem 1.1rem;
    display: flex;
    flex-wrap: wrap;
    gap: 0.35rem;
}

.site-nav a {
    padding: 0.5rem 0.8rem;
    border-radius: 999px;
    color: #475569;
    font-size: 0.92rem;
    font-weight: 500;
}

.site-nav a:hover,
.site-nav a.active {
    background: #eef2ff;
    color: #1d4ed8;
    text-decoration: none;
}

.site-nav a.active {
    box-shadow: inset 0 -2px 0 #2563eb;
}

main {
    max-width: 1100px;
    margin: 0 auto;
    padding: 1.35rem 1.1rem 3rem;
}

.homepage, .page-content {
    display: grid;
    gap: 1rem;
}

.hero, .content-card, .highlight-card, .intro-card, .project-card, .publication-card {
    background: #174a7c;
    border: 1px solid #2c6fb3;
    border-radius: 12px;
    padding: 1.1rem 1.2rem;
    box-shadow: 0 6px 18px rgba(15, 23, 42, 0.06);
    color: #f8fbff;
}

.hero h1, .content-card h1, .content-card h2, .content-card h3, .highlight-card h3, .intro-card h2, .project-card h3, .publication-card h3 {
    color: #ffffff;
    margin-bottom: 0.45rem;
}

.hero p, .content-card p, .content-card li, .highlight-card p, .intro-card p, .project-card p, .publication-card p {
    color: #e8f4ff;
    margin-bottom: 0.6rem;
}

.hero-actions, .resume-actions, .project-actions {
    display: flex;
    flex-wrap: wrap;
    gap: 0.6rem;
    margin-top: 0.8rem;
}

.button {
    display: inline-block;
    padding: 0.55rem 0.9rem;
    border-radius: 8px;
    text-decoration: none;
    font-weight: 600;
    font-size: 0.92rem;
}

.button.primary {
    background: #ffffff;
    color: #174a7c;
}

.button.secondary {
    background: #e2e8f0;
    color: #0f172a;
}

.highlight-grid, .projects-grid, .publications-grid {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 0.9rem;
}

.bullet-list {
    padding-left: 1rem;
    margin: 0.4rem 0 0;
}

.bullet-list li {
    margin-bottom: 0.45rem;
}

.content-card a, .highlight-card a, .hero a, .intro-card a, .project-card a, .publication-card a {
    color: #dcecff;
    text-decoration: underline;
}

table {
    width: 100%;
    border-collapse: collapse;
    margin: 0.5rem 0 0;
}

th, td {
    padding: 0.7rem;
    border: 1px solid #dbeafe;
    text-align: left;
    vertical-align: top;
}

th {
    background: #174a7c;
    color: #ffffff;
}

tr:nth-child(even) td {
    background: #f8fbff;
}

@media (max-width: 768px) {
    .highlight-grid, .projects-grid, .publications-grid {
        grid-template-columns: 1fr;
    }

    .site-nav {
        padding: 0.6rem 0.8rem;
    }

    .hero, .content-card, .highlight-card, .intro-card, .project-card, .publication-card {
        padding: 1rem;
    }
}
'''

(root / 'styles.css').write_text(styles, encoding='utf-8')

nav_js = '''(function () {
  const path = window.location.pathname;
  const base = path.includes('/research/') ? '../' : '';
  const fileName = path.split('/').pop() || 'index.html';
  const items = [
    { label: 'Home', href: 'index.html', key: 'home' },
    { label: 'Summary', href: 'Summary.html', key: 'summary' },
    { label: 'Projects', href: 'Projects.html', key: 'projects' },
    { label: 'Research', href: 'research/index.html', key: 'research' },
    { label: 'Personal Information', href: 'Education.html', key: 'personal' },
    { label: 'Contact', href: 'Contact.html', key: 'contact' }
  ];

  let activeKey = 'home';
  if (fileName === 'Summary.html') activeKey = 'summary';
  else if (fileName === 'Projects.html') activeKey = 'projects';
  else if (fileName === 'Contact.html') activeKey = 'contact';
  else if (['Education.html', 'Work Experience.html', 'ProfessionalSkillsandLanguages.html', 'ObjetivesHobbiesInterests.html', 'References.html'].includes(fileName)) activeKey = 'personal';
  else if (path.includes('/research/')) activeKey = 'research';

  const nav = document.getElementById('site-nav');
  if (!nav) return;
  nav.innerHTML = items.map((item) => {
    const href = `${base}${item.href}`;
    const isActive = item.key === activeKey;
    return `<a href="${href}" class="${isActive ? 'active' : ''}" ${isActive ? 'aria-current="page"' : ''}>${item.label}</a>`;
  }).join('');
})();
'''
(root / 'nav.js').write_text(nav_js, encoding='utf-8')

html_files = [
    'index.html',
    'Summary.html',
    'Contact.html',
    'Education.html',
    'Work Experience.html',
    'ProfessionalSkillsandLanguages.html',
    'StockMarketPricePrediction.html',
    'SelfAssessedQuestionnaires.html',
    'GoogleSheetTemplate.html',
    'ObjetivesHobbiesInterests.html',
    'References.html',
    'Projects.html',
    'research/index.html',
    'research/publication-1.html',
    'research/publication-2.html',
    'research/publication-3.html',
    'research/publication-4.html',
    'research/publication-5.html',
]

for rel in html_files:
    path = root / rel
    if not path.exists():
        continue
    text = path.read_text(encoding='utf-8')
    if '<main' in text:
        marker = text.find('<main')
        prefix = text[:marker]
        suffix = text[marker:]
        if '<body>' in prefix:
            prefix = prefix.split('<body>', 1)[0] + '<body>\n\n    <header class="site-header">\n        <nav class="site-nav" id="site-nav"></nav>\n    </header>\n\n'
        else:
            prefix = prefix + '<body>\n\n    <header class="site-header">\n        <nav class="site-nav" id="site-nav"></nav>\n    </header>\n\n'
        text = prefix + suffix
    else:
        text = text.replace('<body>', '<body>\n\n    <header class="site-header">\n        <nav class="site-nav" id="site-nav"></nav>\n    </header>\n\n', 1)

    text = re.sub(r'<body>.*?<main', '<body>\n\n    <header class="site-header">\n        <nav class="site-nav" id="site-nav"></nav>\n    </header>\n\n    <main', text, count=1, flags=re.S)
    if '<script src="nav.js"></script>' not in text and '<script src="../nav.js"></script>' not in text:
        footer = '../nav.js' if rel.startswith('research/') else 'nav.js'
        text = text.replace('</body>', f'    <script src="{footer}"></script>\n</body>', 1)
    path.write_text(text, encoding='utf-8')

# Ensure Projects page exists with consistent content
(root / 'Projects.html').write_text('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Oscar Salgado Flores | Projects</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header class="site-header">
        <nav class="site-nav" id="site-nav"></nav>
    </header>

    <main class="page-content">
        <section class="content-card">
            <h1>Projects</h1>
            <p>Selected work spanning applied AI, machine learning, software engineering, and educational technology.</p>
        </section>

        <section class="projects-grid">
            <article class="project-card">
                <h3>Diabetes Risk Prediction</h3>
                <p>Machine learning web application for structured risk prediction with deployment-oriented implementation.</p>
                <div class="project-actions">
                    <a class="button secondary" href="StockMarketPricePrediction.html">View Project</a>
                </div>
            </article>
            <article class="project-card">
                <h3>Adaptive Learning System</h3>
                <p>Decision-support and recommendation-oriented work for educational applications.</p>
                <div class="project-actions">
                    <a class="button secondary" href="SelfAssessedQuestionnaires.html">View Project</a>
                </div>
            </article>
            <article class="project-card">
                <h3>Learning Management System</h3>
                <p>Software engineering work covering backend development, SQL, deployment, and platform support.</p>
                <div class="project-actions">
                    <a class="button secondary" href="GoogleSheetTemplate.html">View Project</a>
                </div>
            </article>
        </section>
    </main>
    <script src="nav.js"></script>
</body>
</html>
''', encoding='utf-8')

research_dir = root / 'research'
research_dir.mkdir(exist_ok=True)
(research_dir / 'index.html').write_text('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Oscar Salgado Flores | Research</title>
    <link rel="stylesheet" href="../styles.css">
</head>
<body>
    <header class="site-header">
        <nav class="site-nav" id="site-nav"></nav>
    </header>

    <main class="page-content">
        <section class="content-card">
            <h1>Research</h1>
            <p>Selected publications and research work associated with Oscar Salgado Flores.</p>
        </section>

        <section class="publications-grid">
            <article class="publication-card">
                <h3>Replicación de principios neurobiológicos en la inteligencia artificial: Aproximación al estado del arte</h3>
                <p><strong>Journal:</strong> Diversidad Académica</p>
                <p><strong>Year:</strong> 2026</p>
                <a class="button secondary" href="publication-1.html">View Publication</a>
            </article>
            <article class="publication-card">
                <h3>Publication requiring verification</h3>
                <p><strong>Journal:</strong> Diversidad Académica</p>
                <p><strong>Year:</strong> Pending verification</p>
                <a class="button secondary" href="publication-2.html">View Publication</a>
            </article>
            <article class="publication-card">
                <h3>Publication requiring verification</h3>
                <p><strong>Journal:</strong> Diversidad Académica</p>
                <p><strong>Year:</strong> Pending verification</p>
                <a class="button secondary" href="publication-3.html">View Publication</a>
            </article>
            <article class="publication-card">
                <h3>Publication requiring verification</h3>
                <p><strong>Journal:</strong> Diversidad Académica</p>
                <p><strong>Year:</strong> Pending verification</p>
                <a class="button secondary" href="publication-4.html">View Publication</a>
            </article>
            <article class="publication-card">
                <h3>Publication requiring verification</h3>
                <p><strong>Journal:</strong> Diversidad Académica</p>
                <p><strong>Year:</strong> Pending verification</p>
                <a class="button secondary" href="publication-5.html">View Publication</a>
            </article>
        </section>
    </main>
    <script src="../nav.js"></script>
</body>
</html>
''', encoding='utf-8')

for idx in range(1, 6):
    title = 'Replicación de principios neurobiológicos en la inteligencia artificial: Aproximación al estado del arte' if idx == 1 else 'Publication requiring verification'
    authors = 'Aidee Alejandra Velázquez Favela, Paola Monserrath Velázquez Favela, Oscar Salgado Flores' if idx == 1 else 'Verification required'
    year = '2026' if idx == 1 else 'Pending verification'
    abstract = 'Verified abstract information is available from the journal page for this article. The full text and additional metadata remain under review for the remaining publications.' if idx == 1 else 'The complete publication metadata for this item could not be verified from the journal source at this time. The remaining details require manual verification.'
    (research_dir / f'publication-{idx}.html').write_text(f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Oscar Salgado Flores | Research Publication</title>
    <link rel="stylesheet" href="../styles.css">
</head>
<body>
    <header class="site-header">
        <nav class="site-nav" id="site-nav"></nav>
    </header>

    <main class="page-content">
        <section class="content-card">
            <h1>{title}</h1>
            <p><strong>Journal:</strong> Diversidad Académica</p>
            <p><strong>Authors:</strong> {authors}</p>
            <p><strong>Publication year:</strong> {year}</p>
            <h2>Abstract</h2>
            <p>{abstract}</p>
        </section>
    </main>
    <script src="../nav.js"></script>
</body>
</html>
''', encoding='utf-8')

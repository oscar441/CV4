(function () {
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

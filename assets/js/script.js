function showSection(id) {
  const sections = document.querySelectorAll('.section');
  const menuItems = document.querySelectorAll('.sidebar ul li');

  // Hide all sections and deactivate all links
  sections.forEach(sec => sec.classList.remove('active'));
  menuItems.forEach(item => item.classList.remove('active'));

  // Show selected section and activate the link
  document.getElementById(id).classList.add('active');
  event.target.classList.add('active');
}


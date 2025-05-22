function createCalendar(year, month) {
  const calendarDiv = document.getElementById('calendar');
  calendarDiv.innerHTML = ''; // Réinitialiser le contenu

  const daysOfWeek = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche'];
  const table = document.createElement('table');
  const caption = document.createElement('caption');
  const monthNames = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin',
                      'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre'];
  caption.textContent = `${monthNames[month - 1]} ${year}`;
  table.appendChild(caption);

  // En-têtes des jours
  const headerRow = document.createElement('tr');
  for (const day of daysOfWeek) {
    const th = document.createElement('th');
    th.textContent = day;
    headerRow.appendChild(th);
  }
  table.appendChild(headerRow);

  // Première date du mois
  const date = new Date(year, month - 1, 1);
  const firstDay = (date.getDay() + 6) % 7; // Lundi = 0

  const daysInMonth = new Date(year, month, 0).getDate();
  let row = document.createElement('tr');

  // Jours vides avant le 1er
  for (let i = 0; i < firstDay; i++) {
    row.appendChild(document.createElement('td'));
  }

  for (let day = 1; day <= daysInMonth; day++) {
    const cell = document.createElement('td');
    cell.textContent = day;
    row.appendChild(cell);

    if ((firstDay + day) % 7 === 0 || day === daysInMonth) {
      table.appendChild(row);
      row = document.createElement('tr');
    }
  }

  calendarDiv.appendChild(table);
}

// Exemple : Mai 2025
createCalendar(2025, 5);

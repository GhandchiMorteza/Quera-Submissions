function removeDuplicateStudents(students) {
  const answer = {};
  students.forEach((element) => {
    const id = `${element.grade}${element.name}${element.lastName}${element.birthDate}`;

    element.id = id;
    if (!answer[id] || answer[id].level < element.level) {
      answer[id] = element;
    }
  });
  return Object.values(answer);
}

module.exports = removeDuplicateStudents;

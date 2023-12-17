function submitForm() {
    const name = document.getElementById('name').value;
    const position = document.getElementById('position').value;

    // Send data to the server using AJAX/Fetch
    fetch('/add_employee', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ name, position }),
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert('Employee details submitted successfully!');
            document.getElementById('employeeForm').reset();
        } else {
            alert('Error submitting employee details.');
        }
    })
    .catch(error => console.error('Error:', error));
}

function displayEmployeeDetails() {
    // Fetch and display employee details from the server
    fetch('/get_employees')
    .then(response => response.json())
    .then(data => {
        const employeeList = document.getElementById('employeeList');
        employeeList.innerHTML = '';

        data.forEach(employee => {
            const listItem = document.createElement('li');
            listItem.textContent = `Name: ${employee.name}, Position: ${employee.position}`;
            employeeList.appendChild(listItem);
        });
    })
    .catch(error => console.error('Error:', error));
}

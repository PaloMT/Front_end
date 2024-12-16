document.getElementById("testConnection").addEventListener("click", () => {
    fetch("http://127.0.0.1:5001/test")
        .then(response => response.json())
        .then(data => {
            alert(data.success ? `Conexión exitosa: Base de datos ${data.database}` : `Error: ${data.error}`);
        })
        .catch(error => {
            alert(`Error: ${error}`);
        });
});

document.getElementById("addStudentForm").addEventListener("submit", (event) => {
    event.preventDefault();
    const id = document.getElementById("id").value;
    const nombre = document.getElementById("nombre").value;
    const clase = document.getElementById("clase").value;

    fetch("http://127.0.0.1:5001/add", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ id, nombre_alumno: nombre, clase })
    })
        .then(response => response.json())
        .then(data => {
            alert(data.success ? "Alumno agregado correctamente" : `Error: ${data.error}`);
        })
        .catch(error => {
            alert(`Error: ${error}`);
        });
});

document.getElementById("getStudents").addEventListener("click", () => {
    fetch("http://127.0.0.1:5001/students")
        .then(response => response.json())
        .then(data => {
            if (Array.isArray(data)) {
                const alumnos = data.map(alumno => `${alumno.id} - ${alumno.nombre_alumno} - ${alumno.clase}`).join("\n");
                alert(`Alumnos:\n${alumnos}`);
            } else {
                alert(`Error: ${data.error}`);
            }
        })
        .catch(error => {
            alert(`Error: ${error}`);
        });
});

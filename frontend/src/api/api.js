const API_URL = 'http://localhost:8000/api'; 

export const fetchSalas = async () => {
    const response = await fetch(`${API_URL}/salas/`);
    return response.json();
};

export const fetchReuniones = async (reunionData) => {
    const response = await fetch(`${API_URL}/asignar-reuniones`, {
        method: 'POST', 
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(reunionData), 
    });
    return response.json();
};

export const crearReunion = async (reunionData) => {
    const response = await fetch(`${API_URL}/reuniones/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(reunionData),
    });
    return response.json();
};


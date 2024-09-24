import React, { useState } from 'react';
import { TextField, Button, Typography } from '@mui/material';
import { crearReunion } from '../api/api';

// defino el componente
const ReunionForm = ({ salaId, onReunionCreada }) => { 
    // inicializo con una cadena vacia
    const [descripcion, setDescripcion] = useState('');
    // inicializo estado en 0 para su uso 
    const [cantidadAsistentes, setCantidadAsistentes] = useState(0);
    // inicializo para guardar la hora deseada de reunion
    const [horarioDeseado, setHorarioDeseado] = useState('');
    // defino funcion para ejecutar el formulario
    const handleSubmit = async (e) => {
        // llamo a preventDefault para evitar comportamiento erroneo del formulario 
        e.preventDefault();
        // creo un objeto con la siguiente informacion 
        const reunionData = {
            descripcion,
            cantidad_asistentes: cantidadAsistentes,
            horario_deseado: new Date(horarioDeseado).toISOString(),
            duracion: '01:00:00'
        };
        // llamo la funcion crearReunion y reunionData y espero el resultado con response
        const response = await crearReunion(reunionData);
        // valido si se creo la reunion
        if (response) {
            // si se crea con exito llamo a onReunionCreada()
            onReunionCreada(); 
            // actualizo el estado en una cadena vacia
            setDescripcion('');
            // reestablezco el estado en 0  
            setCantidadAsistentes(0);
            // reestablezco el estado en cuna cadena vacia para la hora
            setHorarioDeseado('');
        }
    };

    return (
        <div style={{ padding: '10px' }}>
            <Typography variant="h6" align="left">Crear Reunión</Typography>
            <form onSubmit={handleSubmit}>
                <TextField 
                    label="Descripción" 
                    variant="outlined" 
                    fullWidth 
                    margin="normal" 
                    value={descripcion} 
                    onChange={(e) => setDescripcion(e.target.value)} 
                    required 
                    size="small"
                />
                <TextField 
                    type="number" 
                    label="Cantidad de Asistentes" 
                    variant="outlined" 
                    fullWidth 
                    margin="normal" 
                    value={cantidadAsistentes} 
                    onChange={(e) => setCantidadAsistentes(e.target.value)} 
                    required 
                    size="small"
                />
                <TextField 
                    type="datetime-local" 
                    variant="outlined" 
                    fullWidth 
                    margin="normal" 
                    value={horarioDeseado} 
                    onChange={(e) => setHorarioDeseado(e.target.value)} 
                    required 
                    size="small"
                />
                <Button type="submit" variant="contained" color="primary" fullWidth>
                    Crear Reunión
                </Button>
            </form>
        </div>
    );
};

export default ReunionForm;
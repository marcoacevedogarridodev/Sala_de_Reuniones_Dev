import React, { useEffect, useState } from 'react';
import { fetchReuniones } from '../api/api';
import { List, ListItem, ListItemText, Typography, Divider, Box } from '@mui/material';

// defino el componente que recibe dos propiedades: salaId y refresh. salaId
const Calendario = ({ salaId, refresh }) => {
    // inicializo estado calendario y uso setcalendario para actualizar 
    const [calendario, setCalendario] = useState([]);
    // hook para cuando salaId o refresh cambien
    useEffect(() => {
        const getCalendario = async () => {
            const reunionData = {}; 
            // llamo a fetchReuniones con los datos de la api
            const data = await fetchReuniones(reunionData);
            // imprimo para ver la data 
            console.log('Fetched data:', data); 
            // filtro para traer solo los datos de sala_id que coincidan con salaId si no asigno un array vacio
            const filteredData = Array.isArray(data.asignaciones) 
                ? data.asignaciones.filter(asignacion => asignacion.sala_id === salaId) 
                : [];
            // ordeno la data de manera ascendente y convierto las fechas de las asignaciones a objetos de fecha para que puedan compararse.
            const sortedData = filteredData.sort((a, b) => new Date(a.fecha) - new Date(b.fecha));
            // imprimo para ver que salaId se esta utilizando
            console.log('salaId:', salaId); 
            //filtro su contenido para ver la data 
            console.log('Filtered and sorted data:', sortedData); 
            // actualizo con los datos ordenados
            setCalendario(sortedData);
        };
        // llamo a getCalendario para ejecutar y obtener datos
        getCalendario();
    }, [salaId, refresh]);

    return (
        <Box sx={{ padding: '20px', margin: '20px 0', border: '1px solid #ccc', borderRadius: '8px' }}>
            <Typography variant="h6" align="center" gutterBottom>
                Calendario de Salas
            </Typography>
            <List>
                {calendario.length > 0 ? (
                    calendario.map(asignacion => (
                        <div key={`${asignacion.id}-${asignacion.fecha}`}>
                            <ListItem>
                                <ListItemText 
                                    primary={asignacion.descripcion} 
                                    secondary={new Date(asignacion.fecha).toLocaleString()} 
                                />
                            </ListItem>
                            <Divider />
                        </div>
                    ))
                ) : (
                    <Typography variant="body2" color="textSecondary" align="center">
                        No hay reuniones programadas.
                    </Typography>
                )}
            </List>
        </Box>
    );
};

export default Calendario;

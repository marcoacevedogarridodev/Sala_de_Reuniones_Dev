import React, { useEffect, useState } from 'react';
import { Container, CssBaseline, Box, Typography } from '@mui/material';
import ReunionForm from './components/ReunionForm';
import Calendario from './components/Calendario';
import { fetchSalas } from './api/api';

const App = () => {
    const [salas, setSalas] = useState([]);
    const [refresh, setRefresh] = useState(false);

    useEffect(() => {
        const getSalas = async () => {
            const data = await fetchSalas();
            setSalas(data);
        };
        getSalas();
    }, []);

    const handleReunionCreada = () => {
        setRefresh(prev => !prev); 
    };

    return (
        <Container component="main" maxWidth="md">
            <CssBaseline />
            {salas.map(sala => (
                <Box key={sala.id} mt={2} p={2} border={1} borderColor="grey.300" borderRadius={2}>
                    <Typography variant="h7">{sala.nombre} - Capacidad: {sala.capacidad_maxima}</Typography>
                    <ReunionForm salaId={sala.id} onReunionCreada={handleReunionCreada} />
                    <Calendario salaId={sala.id} refresh={refresh} />
                </Box>
            ))}
        </Container>
    );
};

export default App;
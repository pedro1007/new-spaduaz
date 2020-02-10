Característica: Ver informacion del docente
    Como usuario del sistema Area Operativo de Atencion a Personal docente
    Quiero ver la informacion de un docente de la UAZ
    Para revisar un tramite solicitado por un docente

    Escenario: Extraccion correcta de los datos para un docente
        Dado que ingreso a la lista de docentes para buscar los datos de un docente
        Cuando escribo la curp "MUVA971209HZSRRN00" en el campo de busqueda
        Y presiono el acciones
        Y el apartado Perfil Completo
        Entonces puedo ver el perfil completo del Docente "José Andres Muro Vargas"
        Y sus datos personales "9 de Diciembre de 1997"
        Y sus datos laboraless "010167"

    Escenario: El docente no esta registrado
        Dado que ingreso a la lista de docentes para buscar los datos de un docente
        Cuando escribo la curp "DSDSDSSDSDSDSSDDSDD" en el campo de busqueda
        Entonces la tabla está vacía y me dice el mensaje "No matching records found"

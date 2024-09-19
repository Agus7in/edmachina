### Documentación Funcional para proyecto EdMachina

Este proyecto utiliza el framework de python FastAPI para construir una RESTful API para manejar inscripciones a materias de leads en un sistema educativo.

**Endpoints**

**Inscripciones**

- **POST de inscripción**: Crea una nueva inscripción para un lead en una
  materia. El cuerpo de la solicitud debe contener los siguientes
  parámetros:

  - `lead_id`: El ID del lead que se está inscribiendo.
  - `materia_id`: El ID de la materia a la que se está inscribiendo.
  - `carrera_id`: El Id de la carrera a la que pertenece la materia.
  - `anio_inscripcion`: El año en el que se cursará la materia.
  - `nro_veces_cursada`: La cantidad de veces que el lead curso la materia.
  - `tiempo_cursado`: La duracion de la materia, puede ser un semestre, un año, etc.

  **Endpoint**:

  _/inscripciones_

  **Response**:

  - `HTTP Status Code`: 201 Created
  - `Response Body`: Objeto JSON que contiene la inscripcion creada con los parámetros:

    - _lead_id:_ integer
    - _materia_id_: integer
    - _carrera_id_: integer
    - _anio_inscripcion_: integer
    - _nro_veces_cursada_: integer
    - _tiempo_cursado_: string

- **GET de inscripciones**: Obtiene todas las inscripciones que fueron registradas

  **Endpoint**:

  _/inscripciones_

  **Response**:

  - `HTTP Status Code`: 200 Ok
  - `Response Body`: Objeto JSON que contiene las inscripciones registradas con los parámetros:

    - _id_inscripcion:_ integer
    - _lead_id:_ integer
    - _materia_id_: integer
    - _carrera_id_: integer
    - _anio_inscripcion_: integer
    - _nro_veces_cursada_: integer
    - _tiempo_cursado_: string

- **GET de inscripción por id**: Obtiene, si es que existe, la inscripcion que coincide con el id proporcionado.

  **Endpoint**:

  _/inscripciones/{id}_

  **Parameters**:

  _id: integer, required_

  **Response**:

  - `HTTP Status Code`: 200 Ok
  - `Response Body`: Objeto JSON que contiene la inscripción registrada que conincide con el id proporcionado, con los parámetros:

    - _id_inscripcion:_ integer
    - _lead_id:_ integer
    - _materia_id_: integer
    - _carrera_id_: integer
    - _anio_inscripcion_: integer
    - _nro_veces_cursada_: integer
    - _tiempo_cursado_: string

**Leads**

- **POST de lead**: Registra un nuevo lead. El cuerpo de la solicitud debe contener los siguientes parámetros:

  - `nombre_completo`: Nombre completo del lead.
  - `direccion`: Dirección del lead.
  - `telefono`: Teléfono del lead.
  - `email`: Email del lead.

  **Endpoint**:

  _/leads_

  **Response**:

  - `HTTP Status Code`: 201 Created
  - `Response Body`: Objeto JSON que contiene el lead creado con los parámetros:

    - _id_lead_: integer
    - _nombre_completo_: string
    - _direccion_: string
    - _telefono_: string
    - _email_: string

- **GET de leads**: Obtiene todos los leads registrados, con la estructura:

  - `nombre_completo`: Nombre completo del lead.
  - `direccion`: Dirección del lead.
  - `telefono`: Teléfono del lead.
  - `email`: Email del lead.

  **Endpoint**:

  _/leads_

  **Response**:

  - `HTTP Status Code`: 200 Ok
  - `Response Body`: Objeto JSON que contiene todos los leads creados con los parámetros:

    - _id_lead_: integer
    - _nombre_completo_: string
    - _direccion_: string
    - _telefono_: string
    - _email_: string

- **GET de lead por id**: Obtiene, si es que existe, el lead que coincide con el id proporcionado.

  - `nombre_completo`: Nombre completo del lead.
  - `direccion`: Dirección del lead.
  - `telefono`: Teléfono del lead.
  - `email`: Email del lead.

  **Endpoint**:

  _/leads/{id}_

  **Parameters**:

  _id: integer, required_

  **Response**:

  - `HTTP Status Code`: 200 Ok
  - `Response Body`: Objeto JSON que contiene todos los leads creados con los parámetros:

    - _id_lead_: integer
    - _nombre_completo_: string
    - _direccion_: string
    - _telefono_: string
    - _email_: string

**Carreras**

- **GET de carreras**: Obtiene todas las carreras disponibles.

  `id_carrera`: Identificador de la carrera.
  `nombre_carrera`: Nombre de la carrera.

  **Endpoint**:

  \_/carreras

  **Response**:

  - `HTTP Status Code`: 200 Ok
  - `Response Body`: Objeto JSON que contiene todas las carreras registradas con los parámetros:

    - _id_carrera_: integer
    - _nombre_carrera_: string

**Materias**

- **GET de materias**: Obtiene todas las materias disponibles.

  `id_materia`: Identificador de la materia.
  `nombre_materia`: Nombre de la materia.

  **Endpoint**:

  \_/materias

  **Response**:

  - `HTTP Status Code`: 200 Ok
  - `Response Body`: Objeto JSON que contiene todas las materias registradas con los parámetros:

    - _id_materia_: integer
    - _nombre_materia_: string

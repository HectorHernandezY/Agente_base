PASOS SI TA TIENES GCLOUD CONFIGURADO Y POETRY INSTALADO

Paso 1: Clonar repositorio

git clone https://github.com/HectorHernandezY/Agente_base.git


Paso 2: Entorno Virtual con Poetry y dependencias
 
    poetry config virtualenvs.in-project true
    poetry install
   

Paso 3: Crear .env
    
    FIRESTORE_PROJECT_ID="tu-gcp-project-id"
    DATABASE_ID="(default)" # O el ID de tu base de datos Firestore
    GCS_RAG_BUCKET="tu-bucket-de-staging"
    GOOGLE_CLOUD_LOCATION="us-central1" # O tu región
    GOOGLE_GENAI_USE_VERTEXAI=TRUE
    ```

Paso 4: Activar el Entorno Virtual (por si no lo hiciste)

comando que te dira la ruta exacta y el comando que debes ejecutar
    poetry env actívate 
	Te saldra algo como: & "C:\Users\USUARIO\Documents\lab-agent-hdu\.venv\Scripts\activate.ps1"

ejemplo de activacion
    PS C:\Users\USUARIO\Documents\lab-agent-hdu> & "C:\Users\USUARIO\Documents\lab-agent-hdu\.venv\Scripts\activate.ps1"

Paso 5: Probar el agente

	poetry run adk web

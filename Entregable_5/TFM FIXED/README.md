# TFM – Predicción de Conversión (Bank Marketing)

Este repositorio contiene el código y recursos del Trabajo Final de Máster orientado a **modelos de predicción de conversión** (Logistic Regression vs. Árboles / Random Forest) sobre el dataset de *bank marketing*.

## 📦 Estructura
```
.
├── TFM_Final_FIXED.ipynb   # Notebook ejecutable con bloque CONFIG idempotente
├── bank-additional_bank-additional-full.csv              # Dataset (colócalo en la raíz)
├── requirements.txt        # Librerías y versiones validadas
└── README.md               # Este archivo
```

## 🧩 Entorno (VSCode)
1. **Python 3.10+ recomendado** (o el que usaste en el TFM).
2. Crear entorno:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   pip install --upgrade pip
   pip install -r requirements.txt
   ```
3. En VSCode, seleccionar el intérprete de `.venv` (Cmd/Ctrl+Shift+P → *Python: Select Interpreter*).

## ▶️ Ejecución
1. Coloca `bank-additional_bank-additional-full.csv` en la misma carpeta que el notebook.
2. Abre `TFM_Final_FIXED.ipynb` y ejecuta **Run All**.
3. El primer bloque **CONFIG**:
   - Fija una semilla (`SEED=42`) *sin modificar hiperparámetros existentes*.
   - Expone la ruta `DATASET_PATH` para lecturas del CSV.
   - Muestra versiones instaladas.

> **Nota:** Si el notebook tiene rutas absolutas o nombres de archivo distintos, cámbialos por `DATASET_PATH` o `"bank-additional_bank-additional-full.csv"` para reproducibilidad.

## 🧪 Comprobación de datos
- El bloque de chequeo confirma la presencia del CSV.
- Recomendación: añadir validaciones (nulos, tipos, cardinalidades) antes del preprocesado.

## 🧹 Estándares de código
- **Imports usados y mínimos** (ver `requirements.txt`). Elimina importaciones no utilizadas.
- **Naming**: usar *snake_case* en inglés (e.g., `train_data`, `fit_model`). Reservar castellano solo para términos de negocio.
- **Documentación**: cada sección con markdown breve (objetivo, entradas, salidas).

## 🔁 Reproducibilidad
- Fijar `random_state` en modelos, divisiones y procesos estocásticos.
- Registrar versiones (bloque CONFIG).

## 📜 Licencia
Uso académico.

---

> Generado automáticamente el 2025-10-23.

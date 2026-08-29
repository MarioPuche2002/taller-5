# Taller Semana 5 — El pipeline que nunca se escribió 🤖

**Empieza leyendo [`ENUNCIADO_TALLER.md`](ENUNCIADO_TALLER.md).**

## Qué hay aquí
```
pipeline-ci-ml/
├── ENUNCIADO_TALLER.md   <- LÉEME PRIMERO
├── src/inventario.py     <- el código (funciona)
├── tests/test_inventario.py  <- 5 pruebas (pasan)
├── requirements.txt
└── .gitignore
```

Falta lo más importante, y es tu trabajo: **`.github/workflows/ci.yml`**.

## Arranque
```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
ruff check .                     # All checks passed!
pytest                           # 5 passed
```

## Tu trabajo (resumen — el detalle está en el ENUNCIADO)
1. Corre el proyecto local y confirma que pasa.
2. Escribe `.github/workflows/ci.yml` (push/PR, ubuntu, checkout, python, install, ruff, pytest).
3. Súbelo a GitHub y velo ponerse verde en la pestaña Actions.
4. Rómpelo a propósito (un test y un lint) para ver el rojo, y arréglalo.
5. Documenta con capturas y trabaja con ≥5 commits.

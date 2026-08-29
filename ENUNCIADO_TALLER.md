# Taller Semana 5 — "El pipeline que nunca se escribió" 🤖

## El contexto

Trabajas en el equipo de datos de **una cadena nacional de tiendas con más de mil
sucursales**. El analista junior (sí, el mismo de siempre) dejó un módulo que calcula la
reposición de inventario: cuántos días dura el stock de cada tienda y cuáles necesitan
pedido urgente. El código funciona, y hasta escribió pruebas para él.

Pero hay un problema: **no hay ninguna automatización.** Cada vez que alguien del equipo
sube un cambio, tiene que acordarse de correr las pruebas a mano… y casi nunca lo hace.
La semana pasada alguien subió un cambio que rompió el cálculo de reposición, nadie corrió
los tests, y tres tiendas se quedaron sin producto porque el sistema decía que tenían stock
para rato. Nadie se dio cuenta hasta el reclamo.

Tu misión: **escribir el pipeline de CI** para que, de ahora en adelante, GitHub revise el
código automáticamente en cada push — y nadie pueda mezclar código roto o sucio otra vez.

## La escala real

En producción, este módulo alimenta el sistema de reposición de más de mil tiendas. Un bug
que pase sin ser detectado no es un número equivocado en una pantalla: son góndolas vacías,
ventas perdidas y clientes molestos en decenas de sucursales a la vez. Por eso el pipeline
que vas a escribir no es un lujo — es lo que separa "lo atrapamos en el push" de "lo
descubrimos por el reclamo".

## Lo que recibes

```
pipeline-ci-ml/
├── src/
│   └── inventario.py        # el código (funciona)
├── tests/
│   └── test_inventario.py   # 5 pruebas (pasan)
├── requirements.txt         # pytest y ruff ya listados
└── .gitignore
```

Lo que NO recibes — y es tu trabajo crear: **la carpeta `.github/workflows/` con el
archivo `ci.yml`.**

## Misión

**Fase 1 — Correrlo local.**
Antes de automatizar nada, comprueba que en tu máquina todo pasa:
```bash
pip install -r requirements.txt
ruff check .     # debe decir: All checks passed!
pytest           # debe decir: 5 passed
```
Si pasa local, tu meta es que pase igual en GitHub, automáticamente.

**Fase 2 — Escribir el workflow.**
Crea el archivo `.github/workflows/ci.yml`. Debe:
- Dispararse en cada `push` y cada `pull_request`.
- Correr en `ubuntu-latest`.
- Tener los pasos, en orden: traer el código (checkout), instalar Python, instalar
  dependencias, correr el linter (ruff), correr las pruebas (pytest).

**Fase 3 — Subirlo y verlo verde.**
Sube el repo a GitHub, ve a la pestaña **Actions**, y observa tu workflow correr. Tu meta:
el pipeline en **verde**, con los 5 tests pasando y el lint limpio.

**Fase 4 — Romperlo y verlo rojo (la prueba de que sirve).**
Haz que el pipeline falle a propósito, de DOS formas distintas, y captura cada una:
- **Un test rojo:** cambia el código para introducir un bug (ej. una fórmula mal) y
  confirma que pytest lo atrapa en Actions.
- **Un lint rojo:** ensucia el código (ej. un import sin usar) y confirma que ruff lo
  atrapa en Actions.
Luego arréglalo y déjalo verde de nuevo. Documenta con capturas en tu README.

## Entregable

El repo `pipeline-ci-ml` en GitHub, con:
- Tu `.github/workflows/ci.yml` funcionando.
- El historial de Actions mostrando al menos un verde, un rojo por test, y un rojo por lint.
- Un `README.md` con: qué hace tu workflow (los 5 pasos explicados en tus palabras) y las
  capturas de las 3 corridas (verde, rojo-test, rojo-lint).
- **≥5 commits** que narren el proceso (incluyendo los que rompen y arreglan).

## Cómo se evalúa

| Criterio | Peso | Qué se evalúa |
|---|---|---|
| El workflow existe y corre | 30% | .github/workflows/ci.yml bien ubicado, se dispara en push/PR, corre en Actions |
| Los pasos correctos, en orden | 30% | checkout → setup-python → install → ruff → pytest. Sin checkout, nada funciona. |
| Verde y rojos demostrados | 25% | capturas del pipeline verde, un rojo por test y un rojo por lint |
| README + Git | 15% | workflow explicado en tus palabras, ≥5 commits que cuenten la historia |

## Pistas sin espóiler

- El archivo va EXACTAMENTE en `.github/workflows/ci.yml` — si la ruta está mal, GitHub
  ni lo ve. Ojo con el punto al inicio de `.github`.
- No inventes la sintaxis de las actions: la de checkout y setup-python las copias como en
  la demo (`actions/checkout@v4`, `actions/setup-python@v5`).
- `checkout` casi siempre va primero. Sin él, el runner está vacío y todo lo demás falla.
- Los comandos de `run` son los mismos que corres local: `pip install -r requirements.txt`,
  `ruff check .`, `pytest`.
- Para el rojo por lint, un `import os` que no uses es la forma más fácil de ensuciar.
- Prueba tu YAML mentalmente leyéndolo de arriba a abajo: ¿cuándo corre? ¿dónde? ¿qué pasos?

## La defensa (al cierre)

Prepárate para responder: *"si tu compañero sube un Pull Request con un test que falla,
¿qué pasa exactamente, y por qué eso protege el proyecto?"* — sobre cómo CI + PR evitan que
el código roto se mezcle.

{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [

    {
      "cell_type": "markdown",
      "metadata": { "id": "header_title" },
      "source": [
        "# **Manual de Uso — Loans_Nicker**\n",
        "### Gestor de Préstamos de Activos Personales\n",
        "\n",
        "**Autores:** Keiner Sebastián Rios · Nickolas Sarmiento Rojas · Maria Camila Osorio Tuberquia  \n",
        "**Institución:** Universidad de Antioquia — Ingeniería Industrial, Semestre 3 (2026-1)  \n",
        "**Repositorio:** [github.com/sebastiankrios/Loans_Nicker](https://github.com/sebastiankrios/Loans_Nicker)"
      ]
    },

    {
      "cell_type": "markdown",
      "metadata": { "id": "seccion_que_es" },
      "source": [
        "## ¿Qué es Loans_Nicker?\n",
        "\n",
        "¿Prestaste tus herramientas, un juego o ese electrodoméstico y no recuerdas a quién? Con **Loans_Nicker**, el caos se termina. Es un sistema de consola en Python para gestionar préstamos de objetos personales (herramientas, videojuegos, libros, electrodomésticos, etc.).\n",
        "\n",
        "Aplica el principio **OGR**: **O**rganiza, **G**estiona y **R**ecuepera tus activos.\n",
        "\n",
        "### Módulos disponibles\n",
        "\n",
        "| # | Módulo |\n",
        "|---|--------|\n",
        "| 1 | Registrar Usuario |\n",
        "| 2 | Registrar Ítem en almacén / Registrar Préstamo |\n",
        "| 3 | Registrar Devolución |\n",
        "| 4 | Consultar ítems con más de 30 días |\n",
        "| 5 | Consultar artículos prestados |\n",
        "| 6 | Panel Administrador |\n",
        "| 7 | Salir |"
      ]
    },

    {
      "cell_type": "markdown",
      "metadata": { "id": "seccion_instalacion" },
      "source": [
        "## Instalación y Arranque\n",
        "\n",
        "**Paso 1:** Clonar el repositorio desde GitHub\n",
        "\n",
        "```\n",
        "https://github.com/sebastiankrios/Loans_Nicker.git\n",
        "```\n",
        "\n",
        "**Paso 2:** Ingresar a la carpeta `src`, allí encontrarás los dos archivos principales:\n",
        "- `main.py` — menú principal y lógica de flujo\n",
        "- `funciones.py` — todas las funciones del sistema\n",
        "\n",
        "**Paso 3:** Ejecutar con Python. Se recomienda usar **Spyder** o cualquier terminal:\n",
        "```\n",
        "python main.py\n",
        "```\n",
        "> **Nota:** El programa usa `input()`, por lo que requiere ejecución en terminal o Spyder. En Colab se recomienda usar el terminal integrado."
      ]
    },

    {
      "cell_type": "markdown",
      "metadata": { "id": "seccion_modulo1" },
      "source": [
        "## Módulo 1 — Registrar Usuario\n",
        "**Opción del menú: `1`**\n",
        "\n",
        "El sistema pedirá los siguientes datos. Todas las validaciones son automáticas:\n",
        "\n",
        "| Campo | Regla de validación |\n",
        "|-------|--------------------|\n",
        "| Cédula | Solo números, entre **3 y 15 dígitos** |\n",
        "| Nombre | Mínimo **3 caracteres**, sin números |\n",
        "| Apellido | Mínimo **3 caracteres**, sin números |\n",
        "| Correo | Debe contener `@` y terminar en `.com` |\n",
        "| Días de préstamo | Solo se aceptan: **5 \\| 10 \\| 15 \\| 30** |\n",
        "\n",
        "A continuación se muestra un ejemplo de entrada válida:"
      ]
    },

    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": { "id": "code_modulo1" },
      "outputs": [],
      "source": [
        "# Ejemplo de usuario válido\n",
        "ejemplo_usuario = {\n",
        "    \"cedula\"        : \"1234567890\",\n",
        "    \"nombre\"        : \"Carlos\",\n",
        "    \"apellido\"      : \"Pérez\",\n",
        "    \"correo\"        : \"carlos.perez@gmail.com\",\n",
        "    \"dias_prestamo\" : 15   # Opciones válidas: 5, 10, 15 ó 30\n",
        "}\n",
        "\n",
        "print(\"Ejemplo de usuario válido:\")\n",
        "print(\"-\" * 40)\n",
        "for campo, valor in ejemplo_usuario.items():\n",
        "    print(f\"  {campo:<20}: {valor}\")"
      ]
    },

    {
      "cell_type": "markdown",
      "metadata": { "id": "seccion_modulo2a" },
      "source": [
        "## Módulo 2A — Registrar Ítem en el Almacén\n",
        "**Opción del menú: `2` → sub-opción `1`**\n",
        "\n",
        "Campos requeridos para registrar un artículo:\n",
        "\n",
        "- **Nombre del ítem:** mínimo 3 caracteres.\n",
        "- **Categoría:** debe ser EXACTAMENTE una de las siguientes:\n",
        "\n",
        "  `Videojuegos` · `Libros` · `Música y video` · `Herramientas` · `Dinero` · `Misceláneo y varios`\n",
        "\n",
        "- **Precio de compra:** número positivo (entero o decimal con punto).\n",
        "- **Calificación de estado (0 al 10):**\n",
        "\n",
        "| Puntaje | Estado |\n",
        "|---------|--------|\n",
        "| 9 – 10 | Excelente (Perfectas condiciones) |\n",
        "| 7 – 8  | Bueno (Tiene detalles menores) |\n",
        "| 4 – 6  | Regular (Desgaste notable pero funcional) |\n",
        "| 1 – 3  | Malo (Necesita reparación urgente) |\n",
        "| 0      | Inservible (Artículo para renovar) |\n",
        "\n",
        "El sistema genera automáticamente un **ID único** con el formato:  \n",
        "`<3 primeras letras de la categoría en MAYÚSCULAS>-<consecutivo>`  \n",
        "**Ejemplo:** `VID-0`, `LIB-1`, `HER-2`"
      ]
    },

    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": { "id": "code_modulo2a" },
      "outputs": [],
      "source": [
        "# Ejemplo de ítem válido y simulación de ID automático\n",
        "ejemplo_item = {\n",
        "    \"nombre\"       : \"FIFA 25\",\n",
        "    \"categoria\"    : \"Videojuegos\",\n",
        "    \"precio\"       : \"150000\",\n",
        "    \"calificacion\" : \"8\"   # → estado: \"Bueno (Tiene detalles menores)\"\n",
        "}\n",
        "\n",
        "print(\"Ejemplo de ítem válido:\")\n",
        "print(\"-\" * 40)\n",
        "for campo, valor in ejemplo_item.items():\n",
        "    print(f\"  {campo:<15}: {valor}\")\n",
        "\n",
        "# Simulación de generación de ID (igual a como lo hace funciones.py)\n",
        "def CrearIdItem(categoria, consecutivo):\n",
        "    prefijo = categoria[:3].upper()\n",
        "    return f\"{prefijo}-{consecutivo}\"\n",
        "\n",
        "id_generado = CrearIdItem(ejemplo_item[\"categoria\"], 0)\n",
        "print(f\"\\n  ID generado automáticamente: {id_generado}\")"
      ]
    },

    {
      "cell_type": "markdown",
      "metadata": { "id": "seccion_modulo2b" },
      "source": [
        "## Módulo 2B — Registrar Préstamo\n",
        "**Opción del menú: `2` → sub-opción `2`**\n",
        "\n",
        "**Pasos:**\n",
        "1. Ingresar la cédula del usuario *(debe estar registrado previamente en el módulo 1)*.\n",
        "2. El sistema muestra todos los ítems disponibles en el inventario con su ID y estado.\n",
        "3. Ingresar el ID del ítem que se desea prestar.\n",
        "\n",
        "**Restricciones del sistema:**\n",
        "- El usuario debe existir en el sistema.\n",
        "- El ítem **no puede estar ya prestado** a otro usuario.\n",
        "- El tiempo máximo autorizado se toma del perfil del usuario (5 / 10 / 15 / 30 días).\n",
        "\n",
        "El sistema confirmará el préstamo mostrando el nombre del usuario y los días autorizados."
      ]
    },

    {
      "cell_type": "markdown",
      "metadata": { "id": "seccion_modulo3" },
      "source": [
        "## Módulo 3 — Registrar Devolución\n",
        "**Opción del menú: `3`**\n",
        "\n",
        "**Pasos:**\n",
        "1. Ingresar la cédula del usuario que devuelve.\n",
        "2. El sistema lista sus ítems prestados actualmente.\n",
        "3. Seleccionar el número del ítem a devolver.\n",
        "4. Ingresar cuántos días han pasado desde el préstamo.\n",
        "\n",
        "**Resultado según los días transcurridos:**\n",
        "\n",
        "| Situación | Resultado | Archivo generado |\n",
        "|-----------|-----------|------------------|\n",
        "| ✔ Dentro del plazo (≤ 30 días) | Certificado de devolución | `certificado_<cedula>_<id>.txt` |\n",
        "| ✖ Fuera del plazo (> 30 días) | Factura de venta forzosa con **impuesto del 23%** | `factura_<cedula>_<id>.txt` |\n",
        "\n",
        "A continuación se muestra cómo se calcula la factura forzosa:"
      ]
    },

    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": { "id": "code_modulo3" },
      "outputs": [],
      "source": [
        "# Ejemplo de cálculo de factura forzosa por préstamo vencido\n",
        "precio_compra = 150_000\n",
        "impuesto      = precio_compra * 0.23   # Impuesto por conchudez\n",
        "total_factura = precio_compra + impuesto\n",
        "\n",
        "print(\"=\" * 45)\n",
        "print(\"  FACTURA DE VENTA — PRÉSTAMO FORZOSO\")\n",
        "print(\"=\" * 45)\n",
        "print(f\"  Precio de compra del ítem : ${precio_compra:,.0f}\")\n",
        "print(f\"  Impuesto por conchudez 23%: ${impuesto:,.0f}\")\n",
        "print(f\"  TOTAL A PAGAR             : ${total_factura:,.0f}\")\n",
        "print(\"=\" * 45)"
      ]
    },

    {
      "cell_type": "markdown",
      "metadata": { "id": "seccion_modulo4" },
      "source": [
        "## Módulo 4 — Consultar Ítems con más de 30 días\n",
        "**Opción del menú: `4`**\n",
        "\n",
        "El sistema recorre **todos los préstamos activos** y pregunta, para cada ítem, cuántos días han pasado desde el préstamo.\n",
        "\n",
        "Si supera 30 días, el ítem aparece en el reporte con la siguiente información:\n",
        "- Nombre y ID del artículo\n",
        "- Usuario responsable\n",
        "- Días permitidos vs. días transcurridos\n",
        "- Precio de compra\n",
        "- ⚠️ Advertencia: artículo sujeto a **venta obligatoria + impuesto del 23%**\n",
        "\n",
        "> **Recomendación:** Usa la opción `3` (Registrar Devolución) para proceder con la facturación."
      ]
    },

    {
      "cell_type": "markdown",
      "metadata": { "id": "seccion_modulo5" },
      "source": [
        "## Módulo 5 — Consultar Artículos Prestados\n",
        "**Opción del menú: `5`**\n",
        "\n",
        "Genera un archivo de texto plano con todos los préstamos activos del sistema:\n",
        "\n",
        "**Archivo:** `registro_prestamos.txt`  \n",
        "**Formato de cada línea:**\n",
        "```\n",
        "<cedula>,<id_item>,<nombre_item>,<dias_autorizados>\n",
        "```\n",
        "\n",
        "Luego muestra en consola un resumen con:\n",
        "- Cédula del prestatario\n",
        "- Nombre del artículo\n",
        "- ID del artículo\n",
        "- Días autorizados de préstamo\n",
        "\n",
        "> Si no hay préstamos activos, el sistema lo informa sin generar el archivo."
      ]
    },

    {
      "cell_type": "markdown",
      "metadata": { "id": "seccion_modulo6" },
      "source": [
        "## Módulo 6 — Panel Administrador\n",
        "**Opción del menú: `6`**\n",
        "\n",
        "Acceso restringido con **usuario y contraseña** (definidos internamente en `funciones.ValidarCredencialesAdmin`).\n",
        "\n",
        "Al ingresar correctamente se despliega el reporte ejecutivo con:\n",
        "\n",
        "📊 **Estadísticas financieras**\n",
        "- Total de ventas forzosas realizadas\n",
        "- Monto total acumulado en pagos (con impuesto 23%)\n",
        "\n",
        "📋 **Detalle de ventas**\n",
        "- Por cada venta: usuario, ítem, precio, impuesto y total\n",
        "\n",
        "👥 **Lista de usuarios registrados**\n",
        "- Cédula, nombre y apellido de cada usuario\n",
        "\n",
        "🏆 **Récords de préstamos**\n",
        "- Usuario con **mayor** cantidad de ítems prestados\n",
        "- Usuario con **menor** cantidad de ítems prestados"
      ]
    },

    {
      "cell_type": "markdown",
      "metadata": { "id": "seccion_validaciones" },
      "source": [
        "## Tabla de Validaciones\n",
        "\n",
        "Resumen de todas las reglas que aplica el sistema automáticamente:"
      ]
    },

    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": { "id": "code_validaciones" },
      "outputs": [],
      "source": [
        "# Tabla resumen de validaciones del sistema\n",
        "reglas = {\n",
        "    \"Cédula\"            : \"Solo números | 3 a 15 dígitos\",\n",
        "    \"Nombre / Apellido\" : \"Sin números | mínimo 3 caracteres\",\n",
        "    \"Correo\"            : \"Debe tener '@' y terminar en '.com'\",\n",
        "    \"Días de préstamo\"  : \"Solo: 5, 10, 15 ó 30\",\n",
        "    \"Nombre del ítem\"   : \"Mínimo 3 caracteres\",\n",
        "    \"Categoría\"         : \"Videojuegos | Libros | Música y video | Herramientas | Dinero | Misceláneo y varios\",\n",
        "    \"Precio\"            : \"Número positivo, puede tener punto decimal\",\n",
        "    \"Calificación\"      : \"Entero entre 0 y 10\",\n",
        "}\n",
        "\n",
        "print(\"=\" * 75)\n",
        "print(\"  TABLA DE VALIDACIONES — LOANS_NICKER\")\n",
        "print(\"=\" * 75)\n",
        "for campo, regla in reglas.items():\n",
        "    print(f\"  {campo:<22}: {regla}\")\n",
        "print(\"=\" * 75)"
      ]
    },

    {
      "cell_type": "markdown",
      "metadata": { "id": "seccion_flujo" },
      "source": [
        "## Flujo de Uso Recomendado\n",
        "\n",
        "Para sacarle el máximo provecho al sistema, sigue este orden:\n",
        "\n",
        "```\n",
        "[1] Registrar usuarios          →  Opción 1\n",
        "[2] Agregar ítems al almacén    →  Opción 2 → sub-opción 1\n",
        "[3] Prestar un ítem             →  Opción 2 → sub-opción 2\n",
        "[4] Ver qué está prestado       →  Opción 5\n",
        "[5] Revisar mora (> 30 días)    →  Opción 4\n",
        "[6] Registrar una devolución    →  Opción 3\n",
        "[7] Revisar reportes globales   →  Opción 6 (admin)\n",
        "[8] Salir del sistema           →  Opción 7\n",
        "```"
      ]
    },

    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": { "id": "code_cierre" },
      "outputs": [],
      "source": [
        "print(\"=\"*55)\n",
        "print(\"  ¡Ya tienes todo lo que necesitas para usar\")\n",
        "print(\"  Loans_Nicker!  No más excusas, ¡entra ya! 🚀\")\n",
        "print(\"=\"*55)"
      ]
    }

  ]
}

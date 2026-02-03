### 🧰 Botiquín de Emergencias Técnicas (VS Code + Quarto)
**1\. Síntoma: "Error: No module named 'yaml'", "Jupyter not found" o Python no arranca.**
* **Diagnóstico:** VS Code "olvidó" que debe usar Anaconda. Pasa al abrir una terminal nueva.
* **La Cura (Opción A - Rápida):** Escribe en la terminal: Bash  conda activate libro-aca
*    
* **La Cura (Opción B - Definitiva):** Si lo anterior no funciona, presiona Cmd + Shift + P $\to$ Escribe Python: Select Interpreter $\to$ Elige la opción que dice libro-aca. Luego abre una terminal nueva (papelera 🗑️ y menú Terminal > New Terminal).

⠀**2. Síntoma: Hice cambios en _quarto.yml (menús, búsqueda, diseño) y no aparecen.**
* **Diagnóstico:** El servidor de vista previa (preview) es muy bueno detectando cambios de texto, pero "lento" detectando cambios de configuración profunda.
* **La Cura:**
  1. Ve a la terminal.
  2. Presiona Ctrl + C (para apagar el servidor).
  3. Escribe quarto preview (para encenderlo desde cero).

⠀**3. Síntoma: Error "ScannerError" o líneas rojas en el archivo _quarto.yml.**
* **Diagnóstico:** Problema de indentación (sangría). YAML es muy estricto: requiere **espacios** (generalmente 2), nunca tabuladores.
* **La Cura:** Revisa que las propiedades "hijas" estén exactamente 2 espacios a la derecha de sus "padres". *Incorrecto:* YAML  book:
* title: "Mi Libro"  (Misma línea)
*     *Correcto:* YAML  book:
* title: "Mi Libro" (2 espacios adentro)
*    

⠀**4. Síntoma: Creé un capítulo nuevo, pero no aparece en la página web o da "Page not found".**
* **Diagnóstico:** El archivo existe, pero no está registrado en el mapa del libro.
* **La Cura:** Abre _quarto.yml y asegúrate de añadir el nombre del archivo bajo la sección chapters:.

⠀
### 📚 Dónde aprender más (Sin volverse loco)
Para resolver dudas puntuales sin tener que leer manuales gigantes, te recomiendo estas 3 fuentes oficiales y limpias:
1. **Guía Oficial de Libros en Quarto (En inglés):** Es la biblia. Si quieres saber qué más puedes poner en el _quarto.yml, mira aquí.
   * ~[https://quarto.org/docs/books/](https://quarto.org/docs/books/)~
2. **Referencia de Markdown (Para escribir):** Si olvidas cómo poner una imagen, una tabla o una nota al pie.
   * ~[https://quarto.org/docs/authoring/markdown-basics.html](https://quarto.org/docs/authoring/markdown-basics.html)~
3. **Truco Pro:** Cuando tengas un error raro en la terminal, cópialo y pégalo en Google o aquí en el chat. Pero si quieres buscarlo tú mismo, añade siempre la palabra **"Quarto"** antes del error. (Ej: *"Quarto search bar not showing"*).

#libronotasACA/notas/adaptabilidad
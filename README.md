# apk-permission-auditor-web

Versión web de [apk-permission-auditor](https://github.com/juanpablocode-sudo/apk-permission-auditor):
misma lógica de análisis, pero con interfaz visual en el navegador
en vez de línea de comandos.

Subís un APK, la app extrae los permisos declarados en el
`AndroidManifest.xml` y muestra cuáles son considerados
"peligrosos" según la clasificación oficial de Android.

## Demo

🔗 [Link a la demo en vivo](#) 

## Uso local

\`\`\`bash
git clone https://github.com/juanpablocode-sudo/apk-permission-auditor-web.git
cd apk-permission-auditor-web
pip install -r requirements.txt
python app.py
\`\`\`

Abrir `http://localhost:5000` en el navegador.

## Qué revisa

- Lista todos los permisos declarados en el APK
- Separa visualmente los permisos "dangerous" de Android del resto
- Alerta si una app declara una cantidad excesiva de permisos
  peligrosos para lo que parece necesitar

## Stack

- **Backend**: Flask + [androguard](https://github.com/androguard/androguard)
  para el parseo del APK
- **Frontend**: HTML/CSS/JS vanilla, sin frameworks

Los APKs subidos se analizan en memoria y se borran del servidor
inmediatamente después del análisis — no se almacena ningún archivo.

## Motivación

Muchas apps piden más permisos de los que realmente necesitan para
funcionar. Esta herramienta ayuda a detectar sobre-solicitud de
permisos, un problema común de privacidad y seguridad, con una
interfaz accesible para cualquiera sin necesidad de usar la terminal.

## Proyecto relacionado

Este proyecto nació como una interfaz web para
[apk-permission-auditor](https://github.com/juanpablocode-sudo/apk-permission-auditor),
la herramienta original en formato CLI.

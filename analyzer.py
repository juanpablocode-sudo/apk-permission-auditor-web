"""
analyzer.py
Lógica de análisis de permisos de un APK.
Adaptado de apk-permission-auditor (CLI) para devolver los datos
como diccionario en vez de imprimirlos, así lo puede consumir
tanto una web app como cualquier otra interfaz.
"""

from androguard.core.apk import APK

# Permisos que Android clasifica como "dangerous"
# (requieren aprobación explícita del usuario en runtime)
DANGEROUS_PERMISSIONS = {
    "android.permission.READ_CONTACTS",
    "android.permission.WRITE_CONTACTS",
    "android.permission.CAMERA",
    "android.permission.RECORD_AUDIO",
    "android.permission.ACCESS_FINE_LOCATION",
    "android.permission.ACCESS_COARSE_LOCATION",
    "android.permission.READ_SMS",
    "android.permission.SEND_SMS",
    "android.permission.READ_CALL_LOG",
    "android.permission.CALL_PHONE",
    "android.permission.READ_EXTERNAL_STORAGE",
    "android.permission.WRITE_EXTERNAL_STORAGE",
    "android.permission.BODY_SENSORS",
    "android.permission.READ_CALENDAR",
    "android.permission.WRITE_CALENDAR",
}


def analyze(apk_path: str) -> dict:
    """
    Analiza un APK y devuelve un diccionario con los resultados.
    No imprime nada ni depende de consola - la capa de presentación
    (CLI, web, lo que sea) decide qué hacer con estos datos.
    """
    apk = APK(apk_path)

    permissions = apk.get_permissions() or []
    dangerous = sorted(p for p in permissions if p in DANGEROUS_PERMISSIONS)
    normal = sorted(p for p in permissions if p not in DANGEROUS_PERMISSIONS)

    return {
        "package": apk.get_package(),
        "app_name": apk.get_app_name(),
        "version": apk.get_androidversion_name(),
        "total_permissions": len(permissions),
        "dangerous_permissions": dangerous,
        "normal_permissions": normal,
        "dangerous_count": len(dangerous),
        "high_risk_warning": len(dangerous) > 5,
    }





















































































































































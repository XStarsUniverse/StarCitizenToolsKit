from __future__ import annotations

import json
from pathlib import Path

DEFAULT_CONFIG = {
    "starcitizen_install_dir": r"C:\Program Files\Roberts Space Industries\StarCitizen",
    "versions": ["LIVE", "PTU", "HOTFIX"],
}


def write_or_recreate(path: Path, content: str) -> None:
    """
    Supprime le fichier s'il existe puis le recrée.
    (Utile pour mettre à jour les .bat générés après un git pull)
    """
    path.parent.mkdir(parents=True, exist_ok=True)

    if path.exists():
        path.unlink()

    # Force CRLF for .bat comfort on Windows
    content = content.replace("\r\n", "\n").replace("\n", "\r\n")
    path.write_text(content, encoding="utf-8")


def load_or_create_config(config_path: Path) -> dict:
    if not config_path.exists():
        write_or_recreate(config_path, json.dumps(DEFAULT_CONFIG, indent=2))
        return DEFAULT_CONFIG.copy()

    with config_path.open("r", encoding="utf-8") as f:
        cfg = json.load(f)

    merged = DEFAULT_CONFIG.copy()
    merged.update(cfg or {})
    if "versions" not in merged or not isinstance(merged["versions"], list) or not merged["versions"]:
        merged["versions"] = DEFAULT_CONFIG["versions"]
    return merged


# ---------------- ScDataDumper-master ----------------

def bat_scdatadumper_start() -> str:
    return r"""@echo off
cd /d "%~dp0"
docker compose up -d --build
docker compose exec scdatadumper php cli.php generate:cache import
docker compose exec scdatadumper php cli.php load:data --scUnpackedFormat import export
"""


def bat_clean(dest_subfolder: str) -> str:
    # ROOT = ScDataDumper-master\
    # On veut écrire dans la racine du repo (StarCitizenToolsKit\VERSION)
    # Donc : ScDataDumper-master\ -> ..\ToolsKit\ -> ..\StarCitizenToolsKit\
    # => ..\..\{VERSION}
    return rf"""@echo off
REM =========================================
REM  Script Import / Export sans supprimer export
REM =========================================

REM Dossier où se trouve le script
set "ROOT=%~dp0"

REM Dossier import & export
set "IMPORT_DIR=%ROOT%import"
set "EXPORT_DIR=%ROOT%export"

REM Dossier de destination (racine du repo)
set "DEST_DIR=%ROOT%..\..\{dest_subfolder}"

echo --- Nettoyage du dossier "import" ---
if exist "%IMPORT_DIR%" (
    pushd "%IMPORT_DIR%"
    del /Q *.* 2>nul
    for /D %%D in (*) do rd /S /Q "%%D"
    popd
)

echo --- Deplacement du contenu de "export" vers "%DEST_DIR%" ---

REM Création du dossier de destination s'il n'existe pas
if not exist "%DEST_DIR%" mkdir "%DEST_DIR%"

REM Déplacement du contenu (fichiers + dossiers)
robocopy "%EXPORT_DIR%" "%DEST_DIR%" /E /MOVE /R:3 /W:1 >nul

REM Si robocopy a supprimé le dossier export, on le recrée
if not exist "%EXPORT_DIR%" mkdir "%EXPORT_DIR%"

echo --- Terminé ---
"""


# ---------------- unp4k ----------------

def bat_unp4k_start(version: str, sc_install_dir: str) -> str:
    data_p4k = rf"{sc_install_dir}\{version}\Data.p4k"
    return rf"""@echo off
cd /d "%~dp0"
unp4k.exe "{data_p4k}" *.xml
unp4k.exe "{data_p4k}" *.ini
unforge.exe .
"""


def bat_unp4k_start_full(version: str, sc_install_dir: str) -> str:
    data_p4k = rf"{sc_install_dir}\{version}\Data.p4k"
    return rf"""@echo off
cd /d "%~dp0"
unp4k.exe "{data_p4k}"
unforge.exe .
"""


def bat_scmove() -> str:
    return r"""@echo off
REM =========================================
REM  Script déplacement Data & Engine
REM =========================================

REM Paths (portables, relatifs au repo)
set "SRC=%~dp0"
set "DST=%~dp0..\ScDataDumper-master\import"

echo --- Déplacement des dossiers Data et Engine ---

REM Vérifie si le dossier de destination existe, sinon le créer
if not exist "%DST%" (
    echo Création du dossier cible : "%DST%"
    mkdir "%DST%"
)

REM Déplacement de Data
if exist "%SRC%\Data" (
    echo Déplacement de Data...
    robocopy "%SRC%\Data" "%DST%\Data" /E /MOVE >nul
) else (
    echo Le dossier Data n'existe pas dans la source.
)

REM Déplacement de Engine
if exist "%SRC%\Engine" (
    echo Déplacement de Engine...
    robocopy "%SRC%\Engine" "%DST%\Engine" /E /MOVE >nul
) else (
    echo Le dossier Engine n'existe pas dans la source.
)

echo --- Terminé ---
"""


def main() -> None:
    toolskit_root = Path(__file__).resolve().parent
    scdatadumper_dir = toolskit_root / "ScDataDumper-master"
    unp4k_dir = toolskit_root / "unp4k"
    config_path = toolskit_root / "config.json"

    cfg = load_or_create_config(config_path)
    sc_install_dir = cfg["starcitizen_install_dir"]
    versions = [str(v).upper() for v in cfg.get("versions", [])]

    # --- ScDataDumper-master ---
    write_or_recreate(scdatadumper_dir / "START.bat", bat_scdatadumper_start())

    for v in versions:
        write_or_recreate(scdatadumper_dir / f"Clean4{v}.bat", bat_clean(dest_subfolder=v))

    # --- unp4k ---
    for v in versions:
        write_or_recreate(unp4k_dir / f"START_{v}.bat", bat_unp4k_start(v, sc_install_dir))
        write_or_recreate(unp4k_dir / f"START_FULL_{v}.bat", bat_unp4k_start_full(v, sc_install_dir))

    write_or_recreate(unp4k_dir / "ScMOVE.bat", bat_scmove())

    print("OK: .bat générés (suppression/recréation) dans ScDataDumper-master/ et unp4k/")
    print(f"Config: {config_path}")


if __name__ == "__main__":
    main()

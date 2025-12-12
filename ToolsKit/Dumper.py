import subprocess
import os
import sys
import time
import json
from datetime import datetime
from pathlib import Path

DEFAULT_DOCKER_DESKTOP_PATH = r"C:\Program Files\Docker\Docker\Docker Desktop.exe"

VERSIONS = {
    "1": "LIVE",
    "2": "PTU",
    "3": "HOTFIX",
}


# --------------------------------------------------
# Utils
# --------------------------------------------------

def log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {message}")


def load_config(repo_root: Path) -> dict:
    cfg_path = repo_root / "config.json"
    if cfg_path.exists():
        try:
            return json.loads(cfg_path.read_text(encoding="utf-8"))
        except Exception as e:
            log(f"[ERREUR] config.json invalide : {e}")
    return {}


def run_bat(bat_path: Path, cwd: Path) -> bool:
    if not bat_path.exists():
        log(f"[ERREUR] Fichier introuvable : {bat_path}")
        return False

    log(f"=== DÉBUT script : {bat_path.name} ===")
    log(f"Dossier de travail : {cwd}")

    result = subprocess.run(
        ["cmd", "/c", str(bat_path)],
        cwd=str(cwd)
    )

    if result.returncode == 0:
        log(f"[OK] FIN script : {bat_path.name}")
        return True
    else:
        log(f"[ERREUR] Code retour {result.returncode} : {bat_path.name}")
        return False


# --------------------------------------------------
# Docker helpers
# --------------------------------------------------

def is_docker_desktop_running():
    try:
        result = subprocess.run(
            ["tasklist", "/FI", "IMAGENAME eq Docker Desktop.exe"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return "Docker Desktop.exe" in result.stdout
    except Exception:
        return False


def wait_for_docker_engine_ready(timeout=300, interval=5):
    log("Vérification du moteur Docker (docker info)...")
    start = time.time()

    while time.time() - start < timeout:
        try:
            if subprocess.run(
                ["docker", "info"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            ).returncode == 0:
                log("Moteur Docker prêt.")
                return True
        except Exception:
            pass

        log("Docker pas encore prêt, attente...")
        time.sleep(interval)

    log("[ERREUR] Docker n'est pas prêt après le délai imparti.")
    return False


def ensure_docker_desktop_running(docker_desktop_path: str):
    if not is_docker_desktop_running():
        if not os.path.exists(docker_desktop_path):
            log(f"[ERREUR] Docker Desktop introuvable : {docker_desktop_path}")
            return False

        log("Lancement de Docker Desktop...")
        subprocess.Popen(
            [docker_desktop_path],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

    return wait_for_docker_engine_ready()


# --------------------------------------------------
# Main
# --------------------------------------------------

def ask_version() -> str:
    print("\nQuelle version veux-tu dumper ?\n")
    print("1. LIVE")
    print("2. PTU")
    print("3. HOTFIX")

    while True:
        choice = input("\nChoix (1/2/3) : ").strip()
        if choice in VERSIONS:
            return VERSIONS[choice]
        print("Choix invalide, réessaie.")


def main():
    repo_root = Path(__file__).resolve().parent  # ToolsKit/
    cfg = load_config(repo_root)

    docker_desktop_path = cfg.get(
        "docker_desktop_path",
        DEFAULT_DOCKER_DESKTOP_PATH
    )

    version = ask_version()
    log(f"=== Démarrage du Dumper [{version}] ===")

    unp4k_dir = repo_root / "unp4k"
    scdump_dir = repo_root / "ScDataDumper-master"

    # 1) START_<VERSION>.bat
    if not run_bat(unp4k_dir / f"START_{version}.bat", unp4k_dir):
        sys.exit(1)

    # 2) ScMOVE.bat
    if not run_bat(unp4k_dir / "ScMOVE.bat", unp4k_dir):
        sys.exit(1)

    # 3) Docker prêt
    log("--- Vérification Docker Desktop ---")
    if not ensure_docker_desktop_running(docker_desktop_path):
        sys.exit(1)

    # 4) START.bat (ScDataDumper)
    if not run_bat(scdump_dir / "START.bat", scdump_dir):
        sys.exit(1)

    # 5) Clean4<VERSION>.bat
    if not run_bat(scdump_dir / f"Clean4{version}.bat", scdump_dir):
        sys.exit(1)

    log(f"=== Dump {version} terminé avec succès ===")


if __name__ == "__main__":
    main()

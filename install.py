import subprocess

def install_dependencies():
    try:
        import colorama
    except ImportError:
        print("Instalowanie bibliotek...")
        subprocess.call(['pip', 'install', 'colorama'])
        print("Biblioteki zostały pomyślnie zainstalowane.")
    else:
        print("Wszystkie potrzebne biblioteki są już zainstalowane.")

if __name__ == "__main__":
    install_dependencies()
    

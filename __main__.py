import sys, os, subproccess, cmd, string

class CLIbase(cmd.Cmd):
    intro = 'Bienvenue dans l\'outil d\'analyse réseau. Tapez help ou ? pour voir les commandes disponibles.'
    prompt = '(AnalyseReseau) '

    def do_exit(self, arg):
        """Quitte l'application."""
        print("Au revoir!")
        return True

    def do_analyse(self, arg):
        """Démarre l'analyse réseau selon les choix de l'utilisateur."""
        os_choice = input("Choisissez l'OS (Linux/Windows): ").lower()
        analysis_type = input("Choisissez le type d'analyse (statique/dynamique): ").lower()

        if os_choice == "linux":
            if analysis_type == "statique":
                self.startStaticLinux()
            elif analysis_type == "dynamique":
                self.startDynamicLinux()
            else:
                print("Type d'analyse non reconnu.")
        elif os_choice == "windows":
            if analysis_type == "statique":
                self.startStaticWindows()
            elif analysis_type == "dynamique":
                self.startDynamicWindows()
            else:
                print("Type d'analyse non reconnu.")
        else:
            print("OS non reconnu.")

    # Définition des méthodes pour les analyses Linux
    def startStaticLinux(self):
        print("Démarrage de l'analyse statique pour Linux...")
        subprocess.run(["./linux/StaticIpCheck.sh"], shell=True)

    def startDynamicLinux(self):
        print("Démarrage de l'analyse dynamique pour Linux...")
        subprocess.run(["./linux/DynamicIpCheck.sh"], shell=True)

    # Définition des méthodes pour les analyses Windows (à compléter)
    def startStaticWindows(self):
        print("Démarrage de l'analyse statique pour Windows...")
        # Exemple avec PowerShell
        subprocess.run(["powershell", "./windows/StaticIpCheck.ps1"])

    def startDynamicWindows(self):
        print("Démarrage de l'analyse dynamique pour Windows...")
        # Exemple avec PowerShell
        subprocess.run(["powershell", "./windows/DynamicIpCheck.ps1"])

if __name__ == '__main__':
    CLIbase().cmdloop()

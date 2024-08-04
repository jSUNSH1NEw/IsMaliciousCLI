import sys, os, subprocess, cmd, string

class CLIbase(cmd.Cmd):
    intro = (
        Fore.MAGENTA + Back.WHITE + """
            ________  ______                                                                             
           /_______/\/_____/\                                                                            
    _______\__.::._\/\::::_\/_     _______                                                               
   /______/\  \::\ \  \:\/___/\   /______/\                                                              
   \__::::\/  _\::\ \__\_::._\:\  \__::::\/                                                              
             /__\::\__/\ /____\:\                                                                        
             \________\/ \_____\/                                                                        
                                                                                                         
 ___ __ __   ________   __        ________  ______    ________  ______   __  __   ______       ______    
/__//_//_/\ /_______/\ /_/\      /_______/\/_____/\  /_______/\/_____/\ /_/\/_/\ /_____/\     /_____/\   
\::\| \| \ \\::: _  \ \\:\ \     \__.::._\/\:::__\/  \__.::._\/\:::_ \ \\:\ \:\ \\::::_\/_    \__:::\ \  
 \:.      \ \\::(_)  \ \\:\ \       \::\ \  \:\ \  __   \::\ \  \:\ \ \ \\:\ \:\ \\:\/___/\      /::/ /  
  \:.\-/\  \ \\:: __  \ \\:\ \____  _\::\ \__\:\ \/_/\  _\::\ \__\:\ \ \ \\:\ \:\ \\_::._\:\     \::\/_  
   \. \  \  \ \\:.\ \  \ \\:\/___/\/__\::\__/\\:\_\ \ \/__\::\__/\\:\_\ \ \\:\_\:\ \ /____\:\      /__/\ 
    \__\/ \__\/ \__\/\__\/ \_____\/\________\/ \_____\/\________\/ \_____\/ \_____\/ \_____\/      \__\/
"""
    ).replace(Fore.MAGENTA, '\033[35m').replace(Back.WHITE, '\033[47m')
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
        print("\033[35m" + "Démarrage de l'analyse statique pour Linux..." + "\033[0m")

    def startDynamicLinux(self):
        print("\033[35m" + "Démarrage de l'analyse dynamique pour Linux..." + "\033[0m")

    # Définition des méthodes pour les analyses Windows (à compléter)
    def startStaticWindows(self):
        print("\033[35m" + "Démarrage de l'analyse statique pour Windows..." + "\033[0m")

    def startDynamicWindows(self):
        print("\033[35m" + "Démarrage de l'analyse dynamique pour Windows..." + "\033[0m")

if __name__ == '__main__':
    CLIbase().cmdloop()


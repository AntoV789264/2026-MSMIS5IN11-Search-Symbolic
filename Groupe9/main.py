import time
from src.generator import generate_rdf_database
from src.shacl_engine import run_shacl_validation

def main():
   
    db_path = "data/patients_db.ttl"
    shapes_path = "data/shapes.ttl"
    num_patients = 1000
    
    # 1. Génération de la base de données
    errors_injected = generate_rdf_database(db_path, num_patients=num_patients, error_rate=0.05)
    print(f"    -> Terminé. {errors_injected} aberrations ont été volontairement cachées.\n")
    
    # 2. Validation par SHACL
    start_shacl = time.time()
    
    shacl_conforms, shacl_report = run_shacl_validation(db_path, shapes_path)
    
    end_shacl = time.time()
    time_shacl = end_shacl - start_shacl
    
    # 3. Résultats
    print("\n" + "="*50)
    if not shacl_conforms:
        print(f" Le moteur SHACL a intercepté les dossiers corrompus !")
        # On affiche juste les 500 premiers caractères du rapport pour ne pas inonder le terminal
        print(f"\nAperçu du rapport SHACL :\n{shacl_report[:500]}...\n[Rapport tronqué pour la lisibilité]")
    else:
        print(" Aucun problème détecté.")
        
    print(f"\n Temps d'exécution SHACL pour {num_patients} patients : {time_shacl:.4f} secondes")

if __name__ == "__main__":
    main()
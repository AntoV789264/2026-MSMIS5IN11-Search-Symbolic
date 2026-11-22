import time
from src.shacl_engine import run_shacl_validation
from src.naive_engine import run_naive_validation

def main():
    print(" DÉMARRAGE DU VÉRIFICATEUR CLINIQUE FHIR\n" + "="*40)
    
    # 1. Test de l'approche symbolique (SHACL)
    print("\n[1] Lancement du moteur SHACL (IA Symbolique)...")
    start_shacl = time.time()
    
    shacl_conforms, shacl_report = run_shacl_validation("data/patient_invalide.ttl", "data/shapes.ttl")
    
    end_shacl = time.time()
    time_shacl = end_shacl - start_shacl
    
    if not shacl_conforms:
        print(" Aberration clinique détectée par SHACL.")
    print(f" Temps d'exécution SHACL : {time_shacl:.4f} secondes")


    # 2. Test de l'approche classique (Script en dur)
    print("\n[2] Lancement de l'approche naïve (Comparatif)...")
    patient_mock = {
        "resourceType": "Patient",
        "birthDate": "1990-01-01",
        "deceasedDateTime": "1985-05-15"
    }
    
    start_naive = time.time()
    naive_conforms, naive_report = run_naive_validation(patient_mock)
    end_naive = time.time()
    time_naive = end_naive - start_naive
    
    if not naive_conforms:
        print(" Aberration clinique détectée par script naïf.")
    print(f" Temps d'exécution Naïf : {time_naive:.4f} secondes")
    
    
    # 3. Bilan des performances
    print("\n" + "="*40)
    print(" BILAN DES PERFORMANCES")
    print(f"Le script naïf est {time_shacl/time_naive:.1f}x plus rapide sur 1 patient.")
    print("Cependant, le moteur SHACL est générique : il n'a besoin d'aucune modification de code pour valider 500 règles supplémentaires, contrairement à l'approche naïve.")

if __name__ == "__main__":
    main()
import os
import pandas as pd

# Étape 1 : Initialisation classique
def main():
    print("Hello, World! Script démarré avec succès.")

    # Étape 2 : Création du dossier /dataset et du fichier CSV
    dataset_dir = "./dataset"
    os.makedirs(dataset_dir, exist_ok=True)  # Crée le dossier s'il n'existe pas

    dataset_path = os.path.join(dataset_dir, "tweets.csv")
    if not os.path.exists(dataset_path):
        # Données fictives
        data = [
            {"tweet_content": "This is a sample tweet.", "score": 50},
            {"tweet_content": "Another example of a tweet.", "score": 70},
        ]
        df = pd.DataFrame(data)
        df.to_csv(dataset_path, index=False)
        print(f"Fichier CSV créé : {dataset_path}")
    else:
        print(f"Fichier CSV déjà existant : {dataset_path}")

    # Étape 3 : Lecture et prétraitement des données
    df = pd.read_csv(dataset_path)
    print("Données lues depuis le fichier CSV :")
    print(df)

    # Exemple de prétraitement simple : convertir le texte en minuscules
    df["tweet_content"] = df["tweet_content"].str.lower()
    print("Données après prétraitement :")
    print(df)

if __name__ == "__main__":
    main()